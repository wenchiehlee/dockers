# Docker-Deck

**A clear starting point for discovering and using Docker images published by `wenchiehlee1020`.**

Docker-Deck is a user-facing catalog for the Docker images maintained in the [wenchiehlee1020 Docker Hub account](https://hub.docker.com/u/wenchiehlee1020). It brings the information people need to evaluate an image and get started with it into one place: what it does, which version to choose, how to run it, when it was updated, how large it is, and what is known about its security vulnerabilities.

---

## Published Images Catalog

Overview of currently published images on [Docker Hub (`wenchiehlee1020`)](https://hub.docker.com/repositories/wenchiehlee1020):

| Image | Category | Recommended Tag | Size | Architecture | Pulls | Last Updated | Links |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`synology-photo-tagger`** | Machine learning & AI | [`v0.3.12`](#synology-photo-tagger) | ~114 MB | `amd64`, `arm64` | 2,960+ | 2026-10-26 | [Docker Hub](https://hub.docker.com/r/wenchiehlee1020/synology-photo-tagger) · [GitHub](https://github.com/ZhongZheng782/Synology-Photo-Tagger) · [Docs](https://zhongzheng782.github.io/Synology-Photo-Tagger/) |
| **`llm-cli-api-server`** | Machine learning & AI | [`v1.3.2`](#llm-cli-api-server) | ~1.29 GB | `amd64` | 560+ | 2026-10-26 | [Docker Hub](https://hub.docker.com/r/wenchiehlee1020/llm-cli-api-server) |
| **`chromium`** | Networking & Browser | [`v1.0.0`](#chromium) | ~1.18 GB | `amd64` | 170+ | 2026-10-11 | [Docker Hub](https://hub.docker.com/r/wenchiehlee1020/chromium) |

---

## Image Details & Usage

### `synology-photo-tagger`

**Synology Photos with private MLX analysis and per-user tag vocabulary.**

A lightweight web app for browsing Synology Photos libraries and inspecting photo metadata with private AI-assisted descriptions and tag suggestions.

- **Recommended tag:** `v0.3.12` (or `latest`)
- **Image size:** ~114 MB (Compressed download)
- **Supported architectures:** `linux/amd64`, `linux/arm64`
- **Total pulls:** 2,960+
- **Latest update:** 2026-10-26
- **Docker Hub:** [wenchiehlee1020/synology-photo-tagger](https://hub.docker.com/r/wenchiehlee1020/synology-photo-tagger)
- **Source code:** [ZhongZheng782/Synology-Photo-Tagger](https://github.com/ZhongZheng782/Synology-Photo-Tagger)
- **Documentation:** [Synology Photo Tagger Portal](https://zhongzheng782.github.io/Synology-Photo-Tagger/)

#### Quickstart

```sh
docker pull wenchiehlee1020/synology-photo-tagger:v0.3.12
```

Using Docker Compose:

```yaml
version: "3"
services:
  photo-tagger:
    image: wenchiehlee1020/synology-photo-tagger:v0.3.12
    container_name: synology-photo-tagger
    ports:
      - "5056:5056"
    env_file:
      - .env
    restart: unless-stopped
```

---

### `llm-cli-api-server`

**LLM CLI & MCP Bridge Server on Synology NAS (Codex CLI, Antigravity CLI, OpenAI Tunnel).**

Automated bridge server enabling execution and proxying of LLM CLI tooling (`codex-cli`, `agy` Antigravity CLI, OpenAI Secure MCP Tunnel) on Synology NAS Container Manager with token persistence and smart routing.

- **Recommended tag:** `v1.3.2`
- **Image size:** ~1.29 GB (Compressed download)
- **Supported architectures:** `linux/amd64`
- **Total pulls:** 560+
- **Latest update:** 2026-10-26
- **Docker Hub:** [wenchiehlee1020/llm-cli-api-server](https://hub.docker.com/r/wenchiehlee1020/llm-cli-api-server)

#### Quickstart

```sh
docker pull wenchiehlee1020/llm-cli-api-server:v1.3.2
```

Running the container:

```sh
docker run -d \
  --name llm-cli-api-server \
  -p 8443:8443 \
  -v ./codex-auth:/app/codex-auth \
  -v ./gemini-auth:/app/gemini-auth \
  -e CODEX_API_KEY="your-api-key" \
  wenchiehlee1020/llm-cli-api-server:v1.3.2
```

---

### `chromium`

**Chromium with pre-installed Chinese fonts, KasmVNC web GUI, and supervised CDP proxy on Synology NAS.**

A production-ready headless/desktop Chromium container optimized for scraping, automation, and remote browser testing. Pre-bundles Noto CJK, WenQuanYi, and Arphic Chinese fonts, and includes an s6-overlay supervised remote Chrome DevTools Protocol (CDP) proxy on port 9222.

- **Recommended tag:** `v1.0.0` (or `latest`)
- **Image size:** ~1.18 GB (Compressed download)
- **Supported architectures:** `linux/amd64`
- **Total pulls:** 170+
- **Latest update:** 2026-10-11
- **Docker Hub:** [wenchiehlee1020/chromium](https://hub.docker.com/r/wenchiehlee1020/chromium)

#### Quickstart

```sh
docker run -d \
  --name chromium \
  -p 3020:3000 \
  -p 3021:3001 \
  -p 9222:9222 \
  -e TITLE="Chromium Desktop" \
  -e CUSTOM_USER="myuser" \
  -e PASSWORD="mysecurepassword" \
  -e TZ=Asia/Taipei \
  -e CHROME_CLI="--remote-debugging-port=9222 --remote-allow-origins=* --disable-features=FontationsFontBackend https://about:blank" \
  -e LC_ALL=zh_TW.UTF-8 \
  --shm-size="1gb" \
  --security-opt seccomp:unconfined \
  -v ./config:/config \
  wenchiehlee1020/chromium:v1.0.0
```

- **Web GUI:** `http://<HOST_IP>:3020` (HTTP) or `https://<HOST_IP>:3021` (HTTPS)
- **Remote CDP Debugging:** `http://<HOST_IP>:9222`

---

## Project relationship

Docker-Deck is part of the `-Deck Family` of sites:

- **UX-Deck** ([Portal](https://wenchiehlee-ux.github.io/UX-Deck/) · [Repo](https://github.com/wenchiehlee-ux/UX-Deck)) — UX resources and presentation.
- **Skill-Deck** ([Portal](https://wenchiehlee.github.io/skills/) · [Repo](https://github.com/wenchiehlee/skills)) — skills and related resources.
- **Analytics-Deck** ([Portal](https://wenchiehlee.github.io/Analytics-Deck/) · [Repo](https://github.com/wenchiehlee/Analytics-Deck)) — telemetry and analytics observability hub across ecosystem endpoints.
- **Pipeline-Deck** ([Portal](https://wenchiehlee.github.io/Pipeline-Deck/) · [Repo](https://github.com/wenchiehlee/Pipeline-Deck)) — pipeline workflows and automation resources.
- **Docker-Deck** ([Portal](https://wenchiehlee.github.io/dockers/) · [Repo](https://github.com/wenchiehlee/dockers)) — this repository, focused on Docker image discovery and usage.
