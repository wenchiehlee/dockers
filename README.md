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

## Deck Family

- **UX-Deck** ([Portal](https://wenchiehlee-ux.github.io/UX-Deck/) · [Repo](https://github.com/wenchiehlee-ux/UX-Deck)) — UX resources and presentation.
- **Skill-Deck** ([Portal](https://wenchiehlee.github.io/skills/) · [Repo](https://github.com/wenchiehlee/skills)) — skills and related resources.
- **Analytics-Deck** ([Portal](https://wenchiehlee.github.io/Analytics-Deck/) · [Repo](https://github.com/wenchiehlee/Analytics-Deck)) — telemetry and analytics observability hub across ecosystem endpoints.
- **Pipeline-Deck** ([Portal](https://wenchiehlee.github.io/Pipeline-Deck/) · [Repo](https://github.com/wenchiehlee/Pipeline-Deck)) — pipeline workflows and automation resources.
- **Data-Deck** ([Portal](https://wenchiehlee-money.github.io/biztrends.TW/) · [Repo](https://github.com/wenchiehlee-money/biztrends.TW)) — Taiwan industry cycles, market trends, and data resources.
- **Llm-Deck** ([Portal](https://wenchiehlee.github.io/llm/) · [Repo](https://github.com/wenchiehlee/llm)) — unified LLM client library, multi-provider fallback & smart routing.
- **Docker-Deck** ([Portal](https://wenchiehlee.github.io/dockers/) · [Repo](https://github.com/wenchiehlee/dockers)) — Docker image discovery and usage.

<style>
*, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: #f8fafc;
      color: #0f172a;
      padding: 40px 16px;
      line-height: 1.4;
    }

    .preview-canvas {
      max-width: 1440px;
      margin: 0 auto;
    }

    .preview-header {
      margin-bottom: 24px;
      text-align: center;
    }

    .preview-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 3px 10px;
      background: #e2e8f0;
      color: #334155;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      border-radius: 9999px;
      margin-bottom: 8px;
    }

    .preview-badge::before {
      content: "";
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #10b981;
    }

    .preview-header h1 {
      font-size: 20px;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: #0f172a;
    }

    .preview-header p {
      font-size: 12.5px;
      color: #64748b;
      margin-top: 4px;
    }

    /* =========================================================
       STRICT ONE ROW 7 CARDS FOOTER
       ========================================================= */
    .deck-family-footer {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      padding: 8px;
      box-shadow: 0 2px 10px -2px rgba(15, 23, 42, 0.04);
      width: 100%;
      overflow-x: auto;
    }

    /* STRICT ONE ROW (7 CARDS EQUAL WIDTH, NO WRAPPING) */
    .deck-cards-row {
      display: grid;
      grid-template-columns: repeat(7, minmax(130px, 1fr));
      gap: 6px;
      width: 100%;
    }

    /* ULTRA COMPACT CARD (~90px height) */
    .deck-card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 7px 8px 6px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 5px;
      transition: all 0.16s ease;
      min-width: 0;
    }

    .deck-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 14px -3px rgba(15, 23, 42, 0.08);
      border-color: var(--deck-accent, #3b82f6);
    }

    /* Card Head: Avatar + Title + Tag */
    .deck-card-head {
      display: flex;
      align-items: center;
      gap: 5px;
      min-width: 0;
    }

    .deck-avatar {
      font-size: 13px;
      line-height: 1;
      width: 20px;
      height: 20px;
      border-radius: 4px;
      background: var(--deck-bg, #f1f5f9);
      border: 1px solid var(--deck-border, #e2e8f0);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }

    .deck-card-title {
      font-size: 11px;
      font-weight: 700;
      color: #0f172a;
      letter-spacing: -0.01em;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .deck-tag {
      font-size: 8px;
      font-weight: 700;
      text-transform: uppercase;
      padding: 1px 3px;
      border-radius: 3px;
      background: var(--deck-bg, #f1f5f9);
      color: var(--deck-accent, #475569);
      margin-left: auto;
      border: 1px solid var(--deck-border, #e2e8f0);
      white-space: nowrap;
      flex-shrink: 0;
    }

    /* Compact Key Numbers Tray */
    .deck-numbers-compact {
      background: #f8fafc;
      border: 1px solid #edf2f7;
      border-radius: 4px;
      padding: 3px 5px;
      display: flex;
      flex-direction: column;
      gap: 2px;
    }

    .stat-line {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 8.5px;
      line-height: 1.2;
      white-space: nowrap;
      gap: 4px;
    }

    .stat-lbl {
      color: #64748b;
      font-weight: 500;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .stat-val {
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      color: var(--deck-accent, #0f172a);
      font-size: 9px;
      flex-shrink: 0;
    }

    /* Compact Dual Action Buttons */
    .deck-actions-compact {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 4px;
    }

    .deck-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 2px;
      padding: 3px 0;
      font-size: 9px;
      font-weight: 600;
      text-decoration: none;
      border-radius: 4px;
      line-height: 1;
      transition: all 0.12s ease;
      white-space: nowrap;
    }

    .deck-btn-portal {
      background: var(--deck-accent, #0f172a);
      color: #ffffff;
      border: 1px solid var(--deck-accent, #0f172a);
    }

    .deck-btn-portal:hover {
      opacity: 0.9;
    }

    .deck-btn-repo {
      background: #ffffff;
      color: #334155;
      border: 1px solid #cbd5e1;
    }

    .deck-btn-repo:hover {
      background: #f8fafc;
      border-color: #94a3b8;
      color: #0f172a;
    }

    .deck-btn svg {
      width: 8px;
      height: 8px;
      stroke-width: 2.2;
    }

    /* THEME ACCENTS */
    .theme-ux {
      --deck-accent: #0d9488;
      --deck-bg: #f0fdfa;
      --deck-border: #ccfbf1;
    }
    .theme-skill {
      --deck-accent: #059669;
      --deck-bg: #ecfdf5;
      --deck-border: #a7f3d0;
    }
    .theme-analytics {
      --deck-accent: #2563eb;
      --deck-bg: #eff6ff;
      --deck-border: #bfdbfe;
    }
    .theme-pipeline {
      --deck-accent: #7c3aed;
      --deck-bg: #f5f3ff;
      --deck-border: #ddd6fe;
    }
    .theme-data {
      --deck-accent: #d97706;
      --deck-bg: #fffbeb;
      --deck-border: #fde68a;
    }
    .theme-llm {
      --deck-accent: #4f46e5;
      --deck-bg: #eef2ff;
      --deck-border: #c7d2fe;
    }
    .theme-docker {
      --deck-accent: #0284c7;
      --deck-bg: #f0f9ff;
      --deck-border: #bae6fd;
    }
</style>
<footer class="deck-family-footer">
      
      <!-- STRICT 7 CARDS IN ONE ROW -->
      <div class="deck-cards-row">

        <!-- 1. UX-Deck -->
        <article class="deck-card theme-ux">
          <div class="deck-card-head">
            <span class="deck-avatar">🦌</span>
            <span class="deck-card-title">UX-Deck</span>
            <span class="deck-tag">Design</span>
          </div>
          <div class="deck-numbers-compact">
            <div class="stat-line">
              <span class="stat-lbl">幾何吉祥物</span>
              <span class="stat-val">13 Mascots</span>
            </div>
            <div class="stat-line">
              <span class="stat-lbl">涵蓋端點</span>
              <span class="stat-val">9+ Hubs · AA</span>
            </div>
          </div>
          <div class="deck-actions-compact">
            <a href="https://wenchiehlee-ux.github.io/UX-Deck/" target="_blank" rel="noopener noreferrer" class="deck-btn deck-btn-portal">
              <span>Portal</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M7 17L17 7M17 7H7M17 7V17"/></svg>
            </a>
            <a href="https://github.com/wenchiehlee-ux/UX-Deck" target="_blank" rel="noopener noreferrer" class="deck-btn deck-btn-repo">
              <span>Repo</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
            </a>
          </div>
        </article>

        <!-- 2. Skill-Deck -->
        <article class="deck-card theme-skill">
          <div class="deck-card-head">
            <span class="deck-avatar">🐇</span>
            <span class="deck-card-title">Skill-Deck</span>
            <span class="deck-tag">Registry</span>
          </div>
          <div class="deck-numbers-compact">
            <div class="stat-line">
              <span class="stat-lbl">收錄技能</span>
              <span class="stat-val">60+ Skills</span>
            </div>
            <div class="stat-line">
              <span class="stat-lbl">分類 / 下游</span>
              <span class="stat-val">8 Cats · 8+</span>
            </div>
          </div>
          <div class="deck-actions-compact">
            <a href="https://wenchiehlee.github.io/skills/" target="_blank" rel="noopener noreferrer" class="deck-btn deck-btn-portal">
              <span>Portal</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M7 17L17 7M17 7H7M17 7V17"/></svg>
            </a>
            <a href="https://github.com/wenchiehlee/skills" target="_blank" rel="noopener noreferrer" class="deck-btn deck-btn-repo">
              <span>Repo</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
            </a>
          </div>
        </article>

        <!-- 3. Analytics-Deck -->
        <article class="deck-card theme-analytics">
          <div class="deck-card-head">
            <span class="deck-avatar">📊</span>
            <span class="deck-card-title">Analytics-Deck</span>
            <span class="deck-tag">Telemetry</span>
          </div>
          <div class="deck-numbers-compact">
            <div class="stat-line">
              <span class="stat-lbl">全站累積</span>
              <span class="stat-val">20.5k Views</span>
            </div>
            <div class="stat-line">
              <span class="stat-lbl">觀測 / 頻率</span>
              <span class="stat-val">13 Pods · 4x/D</span>
            </div>
          </div>
          <div class="deck-actions-compact">
            <a href="https://wenchiehlee.github.io/Analytics-Deck/" target="_blank" rel="noopener noreferrer" class="deck-btn deck-btn-portal">
              <span>Portal</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M7 17L17 7M17 7H7M17 7V17"/></svg>
            </a>
            <a href="https://github.com/wenchiehlee/Analytics-Deck" target="_blank" rel="noopener noreferrer" class="deck-btn deck-btn-repo">
              <span>Repo</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
            </a>
          </div>
        </article>

        <!-- 4. Pipeline-Deck -->
        <article class="deck-card theme-pipeline">
          <div class="deck-card-head">
            <span class="deck-avatar">⚙️</span>
            <span class="deck-card-title">Pipeline-Deck</span>
            <span class="deck-tag">Workflow</span>
          </div>
          <div class="deck-numbers-compact">
            <div class="stat-line">
              <span class="stat-lbl">自動化架構</span>
              <span class="stat-val">CI/CD Engine</span>
            </div>
            <div class="stat-line">
              <span class="stat-lbl">排程調度</span>
              <span class="stat-val">GitOps · Actions</span>
            </div>
          </div>
          <div class="deck-actions-compact">
            <a href="https://wenchiehlee.github.io/Pipeline-Deck/" target="_blank" rel="noopener noreferrer" class="deck-btn deck-btn-portal">
              <span>Portal</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M7 17L17 7M17 7H7M17 7V17"/></svg>
            </a>
            <a href="https://github.com/wenchiehlee/Pipeline-Deck" target="_blank" rel="noopener noreferrer" class="deck-btn deck-btn-repo">
              <span>Repo</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
            </a>
          </div>
        </article>

        <!-- 5. Data-Deck -->
        <article class="deck-card theme-data">
          <div class="deck-card-head">
            <span class="deck-avatar">📈</span>
            <span class="deck-card-title">Data-Deck</span>
            <span class="deck-tag">Finance</span>
          </div>
          <div class="deck-numbers-compact">
            <div class="stat-line">
              <span class="stat-lbl">核心管線</span>
              <span class="stat-val">89 Pipelines</span>
            </div>
            <div class="stat-line">
              <span class="stat-lbl">個股 / 來源</span>
              <span class="stat-val">1,735 · 16 Src</span>
            </div>
          </div>
          <div class="deck-actions-compact">
            <a href="https://wenchiehlee-money.github.io/biztrends.TW/" target="_blank" rel="noopener noreferrer" class="deck-btn deck-btn-portal">
              <span>Portal</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M7 17L17 7M17 7H7M17 7V17"/></svg>
            </a>
            <a href="https://github.com/wenchiehlee-money/biztrends.TW" target="_blank" rel="noopener noreferrer" class="deck-btn deck-btn-repo">
              <span>Repo</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
            </a>
          </div>
        </article>

        <!-- 6. Llm-Deck -->
        <article class="deck-card theme-llm">
          <div class="deck-card-head">
            <span class="deck-avatar">🧠</span>
            <span class="deck-card-title">Llm-Deck</span>
            <span class="deck-tag">Inference</span>
          </div>
          <div class="deck-numbers-compact">
            <div class="stat-line">
              <span class="stat-lbl">總調用量</span>
              <span class="stat-val">25k+ Calls</span>
            </div>
            <div class="stat-line">
              <span class="stat-lbl">路由 / 提供</span>
              <span class="stat-val">3 Provider · AI</span>
            </div>
          </div>
          <div class="deck-actions-compact">
            <a href="https://wenchiehlee.github.io/llm/" target="_blank" rel="noopener noreferrer" class="deck-btn deck-btn-portal">
              <span>Portal</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M7 17L17 7M17 7H7M17 7V17"/></svg>
            </a>
            <a href="https://github.com/wenchiehlee/llm" target="_blank" rel="noopener noreferrer" class="deck-btn deck-btn-repo">
              <span>Repo</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
            </a>
          </div>
        </article>

        <!-- 7. Docker-Deck -->
        <article class="deck-card theme-docker">
          <div class="deck-card-head">
            <span class="deck-avatar">🐳</span>
            <span class="deck-card-title">Docker-Deck</span>
            <span class="deck-tag">Catalog</span>
          </div>
          <div class="deck-numbers-compact">
            <div class="stat-line">
              <span class="stat-lbl">正式映像</span>
              <span class="stat-val">3 Images</span>
            </div>
            <div class="stat-line">
              <span class="stat-lbl">累計拉取</span>
              <span class="stat-val">3,600+ Pulls</span>
            </div>
          </div>
          <div class="deck-actions-compact">
            <a href="https://wenchiehlee.github.io/dockers/" target="_blank" rel="noopener noreferrer" class="deck-btn deck-btn-portal">
              <span>Portal</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M7 17L17 7M17 7H7M17 7V17"/></svg>
            </a>
            <a href="https://github.com/wenchiehlee/dockers" target="_blank" rel="noopener noreferrer" class="deck-btn deck-btn-repo">
              <span>Repo</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
            </a>
          </div>
        </article>

      </div>

    </footer>
