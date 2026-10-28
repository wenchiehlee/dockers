# Docker-Deck

**A clear starting point for discovering and using Docker images published by `wenchiehlee1020`.**

Docker-Deck is a user-facing catalog for the Docker images maintained in the [wenchiehlee1020 Docker Hub account](https://hub.docker.com/u/wenchiehlee1020). It brings the information people need to evaluate an image and get started with it into one place: what it does, which version to choose, how to run it, when it was updated, how large it is, and what is known about its security vulnerabilities.

## What users should be able to do

- Browse and understand the available images.
- Compare tags and versions, including update time and image size.
- Copy a practical command-line example to pull and run an image.
- Review vulnerability information and understand when and how it was checked.
- Follow links to the image's source, documentation, and Docker Hub page.

## Image information

Each image page should present the following information where it is available:

| Information | What it tells the user |
| --- | --- |
| Name and summary | The image's purpose and intended audience. |
| Usage instructions | Prerequisites, configuration, volumes, ports, and a working example. |
| Tags and versions | Available releases and the tag recommended for common use. |
| Updated time | When the image or tag was most recently published. |
| Image size | The size of the selected image/tag. |
| Pull and run commands | Copyable commands using the fully qualified image name and selected tag. |
| Vulnerability status | Scanner or data source, scan time, severity counts, and a link to findings when available. |
| References | Links to Docker Hub, source code, release notes, and project documentation. |

Information should be shown with its source and timestamp where practical. If a value is unavailable or has not been checked, say so plainly rather than implying that the image is current, small, or vulnerability-free. Vulnerability results are point-in-time findings and should include the scanner/source and last scan time; they are not a guarantee that an image is free of risk.

## Example image page

The following is a content template, not a claim about any specific image:

### `<image-name>`

`<One-sentence description of what this image does and who it is for.>`

- **Latest update:** `<date and time>`
- **Recommended tag:** `<tag>`
- **Image size:** `<size>`
- **Vulnerability check:** `<status and last checked time>`
- **Docker Hub:** `<link>`
- **Source and documentation:** `<links>`

```sh
docker pull wenchiehlee1020/<image-name>:<tag>
docker run --rm wenchiehlee1020/<image-name>:<tag>
```

Add the image's actual required options, such as ports, environment variables, and volume mounts, to the run example and explain them alongside the command.

## Project relationship

Docker-Deck is part of the `.Deck` family of sites:

- **UX-Deck** ([Portal](https://wenchiehlee-ux.github.io/UX-Deck/) · [Repo](https://github.com/wenchiehlee-ux/UX-Deck)) — UX resources and presentation.
- **Skill-Deck** ([Portal](https://wenchiehlee.github.io/skills/) · [Repo](https://github.com/wenchiehlee/skills)) — skills and related resources.
- **Analytics-Deck** ([Portal](https://wenchiehlee.github.io/Analytics-Deck/) · [Repo](https://github.com/wenchiehlee/Analytics-Deck)) — telemetry and analytics observability hub across ecosystem endpoints.
- **Docker-Deck** ([Portal](https://wenchiehlee-ux.github.io/UX-Deck/showcases.html#docker-deck) · [Repo](https://github.com/wenchiehlee/dockers)) — this repository, focused on Docker image discovery and usage.

## Draft direction

The portal should make the first-use path easy: understand the image, choose a tag, check its freshness and security information, then copy a command and get started. This README is the initial content and product brief; image-specific facts and implementation details should be added as the catalog is built.
