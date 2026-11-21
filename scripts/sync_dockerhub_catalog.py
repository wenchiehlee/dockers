#!/usr/bin/env python3
"""Refresh the Docker Hub metadata in the Docker-Deck README."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from datetime import datetime
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


NAMESPACE = "wenchiehlee1020"
README = Path(__file__).resolve().parents[1] / "README.md"
HUB_API = "https://hub.docker.com/v2"
REPOSITORIES = (
    "synology-photo-tagger",
    "llm-cli-api-server",
    "chromium",
)
VERSION_RE = re.compile(r"^v?(\d+(?:\.\d+)*)(?:-([0-9A-Za-z.-]+))?(?:\+[0-9A-Za-z.-]+)?$")


def get_json(url: str) -> dict:
    request = Request(url, headers={"User-Agent": "Docker-Deck catalog sync"})
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def list_tags(repository: str) -> list[dict]:
    url = f"{HUB_API}/repositories/{NAMESPACE}/{repository}/tags/?{urlencode({'page_size': 100, 'ordering': 'last_updated'})}"
    tags = []
    while url:
        payload = get_json(url)
        tags.extend(payload.get("results", []))
        url = payload.get("next")
    return [tag for tag in tags if tag.get("tag_status") == "active"]


def semver_key(tag: dict) -> tuple | None:
    match = VERSION_RE.fullmatch(tag.get("name", ""))
    if not match:
        return None
    # Stable releases are preferred; prereleases remain available as a fallback.
    parts = tuple(int(part) for part in match.group(1).split("."))
    parts = (parts + (0, 0, 0, 0))[:4]
    prerelease = match.group(2)
    return (*parts, 0 if prerelease is None else -1, tag.get("last_updated", ""))


def choose_tag(tags: list[dict]) -> dict:
    stable = [tag for tag in tags if (key := semver_key(tag)) and key[-2] == 0]
    if stable:
        return max(stable, key=semver_key)

    latest = next((tag for tag in tags if tag.get("name") == "latest"), None)
    if latest:
        return latest
    if tags:
        return max(tags, key=lambda tag: tag.get("last_updated", ""))
    raise ValueError("Docker Hub returned no active tags")


def format_size(size: int) -> str:
    if size >= 1_000_000_000:
        return f"~{size / 1_000_000_000:.2f} GB"
    return f"~{size / 1_000_000:.0f} MB"


def tag_metadata(tag: dict, repo_info: dict) -> dict:
    images = tag.get("images", [])
    architectures = sorted(
        {image["architecture"] for image in images if image.get("architecture")},
        key=lambda architecture: (architecture != "amd64", architecture != "arm64", architecture),
    )
    size = max(
        [image.get("size", 0) for image in images]
        + [tag.get("full_size", 0)]
    )
    updated = tag.get("last_updated") or tag.get("tag_last_pushed") or ""
    if not updated:
        raise ValueError(f"Docker Hub did not return an update time for tag {tag.get('name', '<unknown>')}")
    try:
        update_date = datetime.fromisoformat(updated.replace("Z", "+00:00")).date().isoformat()
    except ValueError as error:
        raise ValueError(f"Unexpected update time for {repository}:{tag['name']}: {updated}") from error

    return {
        "tag": tag["name"],
        "size": format_size(size),
        "architectures": architectures,
        "pulls": f"{repo_info.get('pull_count', 0):,}+",
        "updated": update_date,
    }


def replace_table_row(lines: list[str], repository: str, metadata: dict) -> None:
    for index, line in enumerate(lines):
        if not line.startswith(f"| **`{repository}`** |"):
            continue
        cells = line.split("|")
        if len(cells) != 10:
            raise ValueError(f"Unexpected catalog row format for {repository}")
        cells[3] = f" [`{metadata['tag']}`](#{repository}) "
        cells[4] = f" {metadata['size']} "
        cells[5] = " " + ", ".join(f"`{arch}`" for arch in metadata["architectures"]) + " "
        cells[6] = f" {metadata['pulls']} "
        cells[7] = f" {metadata['updated']} "
        lines[index] = "|".join(cells)
        return
    raise ValueError(f"No catalog table row found for {repository}")


def replace_detail(lines: list[str], repository: str, metadata: dict) -> None:
    heading = f"### `{repository}`"
    start = next((i for i, line in enumerate(lines) if line == heading), None)
    if start is None:
        raise ValueError(f"No image detail section found for {repository}")
    end = next(
        (i for i in range(start + 1, len(lines)) if lines[i].startswith("### `")),
        len(lines),
    )
    section = lines[start:end]
    latest_suffix = " (or `latest`)" if metadata["has_latest"] and metadata["tag"] != "latest" else ""
    fields = {
        "Recommended tag": f"`{metadata['tag']}`{latest_suffix}",
        "Image size": f"{metadata['size']} (Compressed download)",
        "Supported architectures": ", ".join(f"`linux/{arch}`" for arch in metadata["architectures"]),
        "Total pulls": metadata["pulls"],
        "Latest update": metadata["updated"],
    }
    for field, value in fields.items():
        prefix = f"- **{field}:**"
        for index, line in enumerate(section):
            if line.startswith(prefix):
                section[index] = f"{prefix} {value}"
                break
        else:
            raise ValueError(f"No '{field}' field found for {repository}")

    # Keep every example command aligned with the selected tag.
    image_prefix = f"{NAMESPACE}/{repository}:"
    for index, line in enumerate(section):
        section[index] = re.sub(
            re.escape(image_prefix) + r"[^\s`]+",
            image_prefix + metadata["tag"],
            line,
        )
    lines[start:end] = section


def main() -> int:
    try:
        listing = get_json(f"{HUB_API}/repositories/{NAMESPACE}/?page_size=100")
        repository_info = {item["name"]: item for item in listing.get("results", [])}
        lines = README.read_text(encoding="utf-8").splitlines()

        for repository in REPOSITORIES:
            if repository not in repository_info:
                raise ValueError(f"{NAMESPACE}/{repository} was not found in Docker Hub")
            tags = list_tags(repository)
            selected = choose_tag(tags)
            metadata = tag_metadata(selected, repository_info[repository])
            metadata["has_latest"] = any(item.get("name") == "latest" for item in tags)
            replace_table_row(lines, repository, metadata)
            replace_detail(lines, repository, metadata)

        README.write_text("\n".join(lines) + "\n", encoding="utf-8")
    except (HTTPError, URLError, TimeoutError, OSError, ValueError, KeyError) as error:
        print(f"Docker Hub catalog sync failed: {error}", file=sys.stderr)
        return 1

    print("Docker Hub catalog metadata synchronized.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
