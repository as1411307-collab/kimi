# تحليل مستودع `nexu-io/open-design` — المرحلة الأولى (جرد شامل، دون استخراج أكواد)

> **المنهجية وحدودها:** اعتمد هذا الجرد على ملف شجرة Git الكامل غير المبتور (`open-design.tree.json`، 16,766 مدخلاً، `truncated: false`) لفرع `main` فقط، وعلى ملف الفروع (`open-design.branches.json`)، إضافة إلى قراءة `README.md` الرسمي و`LICENSE` من `raw.githubusercontent.com`. لم تُقرأ أسطر الأكواد ولم يُنفَّذ أي بناء أو تعديل على المستودع. كل ما يلي **موثق من الشجرة أو الوثائق المذكورة** ما لم يُوسم صراحة بأنه (استنتاج).

---

## 1) التعريف والترخيص واللغة والتقنيات

- **التعريف (من README):** «OpenDesign: أول مساحة عمل تعاونية لوكيل تصميم ذكاء اصطناعي» — يبدأ بموجز (brief)، ثم يستخدم وكيل برمجة موجوداً لدى المستخدم (Claude Code / Codex / Cursor / …) أو OpenDesign Cloud لتوليد نماذج أولية (prototypes) وشرائح وصور وفيديو تتبع نظام تصميم (`DESIGN.md`)، مع سير عمل قابل للتوسعة عبر أربع طبقات: **Plugins** (سير عمل) + **Skills** (سلوك وكيل) + **Design Templates** (مخططات عرض) + **Design Systems** (الهوية).
- **الترخيص:** Apache-2.0 (ملف `LICENSE` في الجذر، تم التحقق من نصه). استثناءات موثقة في README: حزم مدمجة تحتفظ برخصها الخاصة MIT — `design-templates/guizang-ppt/` و`design-templates/html-ppt/` و`skills/web-clone/`.
- **commit فرع main (من سجل الفروع):** `07a86b1041531bfa0bec1006d9c0993985fee560` — ويتطابق مع `sha` الشجرة المفحوصة. عدد الفروع الكلي في الملف: **2852 فرعاً**.
- **اللغة والتقنيات (موثق):** مونوريبو pnpm (`pnpm-workspace.yaml`) بلغة TypeScript؛ الواجهة **Next.js 16 App Router + React 18**؛ الدايمون **Node 24 + Express + SSE + better-sqlite3**؛ سطح المكتب **Electron** مع sidecar IPC؛ البناء esbuild؛ الاختبارات **Vitest + Playwright**؛ النشر **Docker / AWS SAM / Azure Bicep / Sealos**؛ فيديو عبر **HyperFrames** (HTML+CSS+GSAP → MP4 عبر headless Chrome + FFmpeg)؛ بروتوكول **MCP** (stdio server) للتكامل مع وكلاء البرمجة.
- **الإصدارات (من CHANGELOG الموجود في الشجرة):** `docs/CHANGELOG/` يحوي ملفات إصدارات حتى v0.24.0 على الأقل، وملف جذر `RELEASE-NOTES-0.10.0.md`.

---

## 2) مجلدات وملفات الجذر (52 عنصراً) وشرح كل واحد

**مجلدات تشغيلية/منتج:**
- `apps/` — التطبيقات الخمسة (انظر القسم 3).
- `packages/` — 17 حزمة مشتركة (انظر القسم 3).
- `skills/` — 169 مهارة وظيفية بصيغة `SKILL.md` (مواثيق Agent Skills).
- `design-templates/` — 115 قالب عرض/تصميم قابل للتوليد.
- `design-systems/` — 152 حزمة نظام تصميم + مجلد `_schema`.
- `plugins/` — البلجنات: `_official/` (رسمية)، `community/` (10 إدخالات مجتمعية)، `registry/` (سجلّا official/community)، `spec/` (مواصفة البلجن SPEC.md + أدلة)، `open-design/` (إعداد `.mcp.json` و`.claude-plugin`).
- `prompt-templates/` — قوالب برومبت صور وفيديو (JSON + معاينات).
- `docs/` — الوثائق (انظر القسم 3).
- `deploy/` — النشر: Dockerfile وdocker-compose وAWS SAM وAzure Bicep وسكربتات تثبيت/تحقق واختبارات.
- `e2e/` — اختبارات طرف-لطرف (Playwright/Vitest).

**مجلدات داعمة:**
- `assets/` — أصول ثابتة: `community-pets/`، `frames/` (إطارات أجهزة)، `prompt-templates/`.
- `charts/` — Helm chart (`open-design`) لنشر Kubernetes (استنتاج من الاسم والهيكل؛ لم يُفتح محتواه).
- `clipper/` — إضافة متصفح (manifest.json + content/background/popup) لالتقاط محتوى الويب إلى OpenDesign («brand-capture»).
- `craft/` — أدلة حِرفة تصميمية نصية (typography, color, anti-ai-slop, laws-of-ux, accessibility-baseline, rtl-and-bidi…).
- `data/` — بيانات: `contributors.json`, `events.jsonl`, `cards/`, `plugin-previews/`.
- `figma-plugin/` — بلجن Figma مستقل (`code.js`, `manifest.json`, `ui.html`, `IR.md`).
- `mocks/` — وكيل وهمي (`mock-agent.mjs`) وتسجيلات ذهبية للاختبار.
- `scripts/` — 47+ سكربت صيانة/تحقق/مزامنة (sync-design-systems, check-*…).
- `shells/` — `terminal/` (غلاف طرفية) + AGENTS.md.
- `specs/` — مواصفات ميزات (`current/`, `change/`, `od-clipper.md`, `2026-04-29-live-artifacts/`).
- `story/` — `STORY.md` قصة/سردية المشروع (إنجليزي + صيني).
- `templates/` — قوالب HTML داخلية: `deck-framework.html`, `kami-deck.html`, `live-artifacts/`.
- `tools/` — أدوات المستودع: `dev`, `pack`, `release`, `serve` (نقطة الدخول `pnpm tools-dev`).
- `ui-audit/` — تدقيق UI (`goal66/`).
- `.github/` — CI/workflows وسكربتات وكلاء (agent-pr-explore…). `.claude/` و`.claude-plugin/` — إعدادات Claude. `.vaunt/` و`.looper-attachments/` — ملحقات أدوات خارجية (استنتاج).
- ملفات جذر وثائقية: `AGENTS.md` (عقد إلزامي للوكلاء، يتضمن «Daemon data directory contract»)، `CLAUDE.md`، `CONTEXT.md`، `CONTRIBUTING.md`، `MAINTAINERS.md`، `PRIVACY.md`، `QUICKSTART.md`، `CHANGELOG.md`، `TRANSLATIONS.md`، `design-browser-task-handoff.md`.
- ملفات إعداد: `package.json`, `pnpm-lock.yaml`, `mise.toml`, `vercel.json`, `.node-version`, `.gitignore/.gitattributes/.dockerignore/.ignore`.

---

## 3) الجرد الكامل للأسماء في المجلدات المطلوبة

### 3.1 `apps/` — 5 تطبيقات
| التطبيق | الدور |
|---|---|
| `apps/daemon` | الدايمون المحلي (Node/Express/SSE/SQLite) — العملية المميّزة الوحيدة؛ تعريفات الـruntimes في `src/runtimes/defs/` |
| `apps/web` | تطبيق الويب Next.js 16 (App Router) + sidecar |
| `apps/desktop` | غلاف Electron لسطح المكتب (macOS/Windows) |
| `apps/packaged` | نسخة التغليف القابلة للتوزيع (esbuild) — له README خاص |
| `apps/closure` | حزمة/إغلاق (closure) بإعداد esbuild خاص (الدور الدقيق لم يُقرأ — استنتاج من الاسم) |

### 3.2 `packages/` — 17 حزمة
`agui-adapter` (محوّل بروتوكول AG-UI — استنتاج من الاسم) · `components` · `contracts` · `diagnostics` · `download` · `dsh-runtime` (runtime لـ DeepSeek Harness عبر `dsh` CLI؛ يحوي `cordis.patch.yml`) · `host` · `launcher` · `launcher-proto` · `metatool` · `platform` · `plugin-runtime` · `registry-protocol` · `release` · `sidecar` · `sidecar-proto` · `standalone`
(لكل حزمة `src/` و`tests/` و`package.json`؛ الأدوار التفصيلية لم تُقرأ في هذه المرحلة.)

### 3.3 `docs/` — 59 عنصراً بالمستوى الأول

**ملفات:** `MOCKS-CONTRACT-CHECK.md` · `agent-adapters.md` · `ai-native-observability-trace-analysis.md` · `architecture.md` · `atoms.md` · `code-review-guidelines.md` · `codex-pets.md` · `critique-theater.md` · `deepseek-harness-one-click-install.zh-CN.md` · `design-system-tracking-spec.md` · `design-systems.md` · `external-media-orchestration.md` · `headless-byok.md` · `install-guide.md` · `media-stock-telemetry.md` · `modes.md` · `motion-template-sources.md` · `new-agent-runtime-acp.md` · `notebooklm.md` · `orchestrator-workspaces.md` · `plugins-spec.md` · `plugins-spec.zh-CN.md` · `prompt-composition.md` · `publishing-a-plugin.md` · `publishing-a-plugin.zh-CN.md` · `references.md` · `roadmap.md` · `seats-journey-analytics.md` · `self-hosting-a-registry.md` · `skills-contributing.md` · `skills-protocol.md` · `spec.md` · `typescript-7.md` · `v0.8.0-announcement.md` · `v0.8.0-announcement.zh-CN.md` · `whats-new.json` · `whats-new.md` · `windows-troubleshooting.md` · `wsl-setup.md`

**مجلدات:**
- `adr/` — قرار معماري واحد: `0001-centralize-daemon-startup.md`
- `CHANGELOG/` — 15 مدخلاً (v0.14.1 … v0.24.0+)
- `assets/` · `images/` · `screenshots/` — أصول وصور الوثائق وجولة المنتج
- `ci/` — `version-bump-policy.md`، `workload-products.md`
- `deployment/` — `docker.md`، `cloud/`، `workspace-team-rollout.md`
- `design/` — `chat-mirror/`، `run-errors/`
- `evidence/` — أدلة تشغيلية (`od-next-profile-access`, `pi-rpc-close-grace`)
- `examples/` — `DESIGN.sample.md`، `saas-landing-skill/`
- `handoffs/` — `slides-project-experience-handoff.md`
- `i18n/` — 35 ملف ترجمة (README/CONTRIBUTING/MAINTAINERS بـ 8+ لغات منها العربية)
- `observability/` — `update-lifecycle.md` + `drafts/`
- `plans/` — خطط: sandbox-orchestration-hardening، plugins-implementation، plugin-registry، manual-edit-mode، amr-vela-cli-ci
- `qa/` — تقارير QA ولقطات
- `rfc-drafts/` — `agent-ready.md`، `agent-ready-cross-project.md`، `dev-server-auto-detect.md`
- `schemas/` — `open-design.plugin.v1.json`، `open-design.marketplace.v1.json`
- `superpowers/` — `plans/` و`specs/` (منهجية عمل داخلية — استنتاج من الاسم)
- `telemetry/` — crash-and-exit، preview-and-navigation، responsiveness، stability-metrics، update-lifecycle
- `testing/` — 22 مدخلاً (عقود اختبار AMR، تغطية e2e، codex-patch-streaming…)

### 3.4 `skills/` — 169 مهارة (الأسماء الكاملة من الشجرة)


`8-bit-orbit-video-template` · `ad-creative` · `after-hours-editorial-template` · `agent-browser` · `ai-music-album` · `algorithmic-art` · `animate` · `apple-hig` · `article-magazine` · `artifacts-builder` · `brainstorming` · `brand-extract` · `brand-guidelines` · `brandkit` · `brutalist-skill` · `canvas-design` · `card-twitter` · `card-xiaohongshu` · `chat-motion-overlay` · `color-expert` · `competitive-ads-extractor` · `copywriting` · `creative-director` · `d3-visualization` · `data-report` · `deck-guizang-editorial` · `deck-open-slide-canvas` · `deck-swiss-international` · `design-brief` · `design-consultation` · `design-md` · `design-review` · `digits-fintech-swiss-template` · `doc` · `doc-kami-parchment` · `docx` · `domain-name-brainstormer` · `ecommerce-image-workflow` · `editorial-burgundy-principles-template` · `emil-design-eng` · `emilkowalski-motion` · `enhance-prompt` · `export-download-debugging` · `fal-3d` · `fal-generate` · `fal-image-edit` · `fal-kling-o3` · `fal-lip-sync` · `fal-realtime` · `fal-restore` · `fal-train` · `fal-tryon` · `fal-upscale` · `fal-video-edit` · `fal-vision` · `faq-page` · `field-notes-editorial-template` · `figma-code-connect-components` · `figma-create-design-system-rules` · `figma-create-new-file` · `figma-generate-design` · `figma-generate-library` · `figma-implement-design` · `figma-use` · `flutter-animating-apps` · `frame-data-chart-nyt` · `frame-flowchart-sticky` · `frame-glitch-title` · `frame-light-leak-cinema` · `frame-liquid-bg-hero` · `frame-logo-outro` · `frame-macos-notification` · `frontend-design` · `frontend-dev` · `frontend-skill` · `frontend-slides` · `full-page-screenshot` · `gif-sticker-maker` · `gpt-tasteskill` · `gsap-core` · `gsap-frameworks` · `gsap-performance` · `gsap-plugins` · `gsap-react` · `gsap-scrolltrigger` · `gsap-timeline` · `gsap-utils` · `hand-drawn-diagrams` · `hatch-pet` · `html-ppt-retro-quarterly-review` · `huashu-art-motion` · `image-enhancer` · `image-to-code-skill` · `imagegen` · `imagegen-frontend-mobile` · `imagegen-frontend-web` · `imagen` · `impeccable-design-polish` · `library-curator` · `login-flow` · `marketing-psychology` · `minimalist-skill` · `minimax-docx` · `minimax-pdf` · `mockup-device-3d` · `motion-design` · `motion-lab` · `nanobanana-ppt` · `od-next-media-inputs` · `oil-motion` · `output-skill` · `paywall-upgrade-cro` · `pdf` · `pixelbin-media` · `plan-design-review` · `platform-design` · `poster-hero` · `ppt-keynote` · `pptx` · `pptx-generator` · `pptx-html-fidelity-audit` · `pr-feedback-quality-gate` · `redesign-skill` · `reference-design-contract` · `release-notes-one-pager` · `remotion` · `replicate` · `research-decision-room` · `resume-modern` · `review-animations` · `screenshot` · `screenshots-marketing` · `shadcn-ui` · `shader-dev` · `slack-gif-creator` · `slides` · `social-reddit-card` · `social-spotify-card` · `social-x-post-card` · `soft-skill` · `sora` · `speech` · `stitch-loop` · `stitch-skill` · `swiftui-design` · `swiss-creative-mode-template` · `swiss-user-research-video-template` · `taste-skill` · `taste-skill-v1` · `theme-factory` · `threejs` · `ui-animation` · `ui-skills` · `ui-ux-pro-max` · `venice-audio-music` · `venice-audio-speech` · `venice-image-edit` · `venice-image-generate` · `venice-video` · `vfx-text-cursor` · `video-downloader` · `video-hyperframes` · `web-artifacts-builder` · `web-clone` · `web-design-guidelines` · `weread-year-in-review-video-template` · `wpds` · `writing-guidelines` · `youtube-clipper`


(منها عائلات واضحة: تكاملات Figma السبع `figma-*`، عائلة Fal للوسائط `fal-*` (توليد/تعديل/ترقية صور وفيديو وlip-sync وتدريب ورؤية)، عائلة GSAP الثمانية للحركة، عائلة Venice للوسائط، مهارات مستندات `doc/docx/pdf/pptx/pptx-*`، مهارات صوت `speech`/`venice-audio-*`، مهارات فيديو `sora`/`video-*`/`remotion`، ومهارات هندسية `frontend-*`/`shadcn-ui`/`threejs`/`shader-dev`/`gsap-*`.)

### 3.5 `design-templates/` — 115 قالباً (الأسماء الكاملة من الشجرة)


`aster-atelier` · `audio-jingle` · `blog-post` · `clinical-case-report` · `contact-widget` · `critique` · `dashboard` · `dating-web` · `dcf-valuation` · `digital-eguide` · `docs-page` · `email-marketing` · `eng-runbook` · `finance-report` · `flowai-live-dashboard-template` · `gamified-app` · `github-dashboard` · `guizang-ppt` · `hr-onboarding` · `html-ppt` · `html-ppt-course-module` · `html-ppt-graphify-dark-graph` · `html-ppt-hermes-cyber-terminal` · `html-ppt-knowledge-arch-blueprint` · `html-ppt-obsidian-claude-gradient` · `html-ppt-pitch-deck` · `html-ppt-presenter-mode-reveal` · `html-ppt-product-launch` · `html-ppt-taste-brutalist` · `html-ppt-taste-editorial` · `html-ppt-tech-sharing` · `html-ppt-testing-safety-alert` · `html-ppt-weekly-report` · `html-ppt-xhs-pastel-card` · `html-ppt-xhs-white-editorial` · `html-ppt-zhangzara-8-bit-orbit` · `html-ppt-zhangzara-biennale-yellow` · `html-ppt-zhangzara-block-frame` · `html-ppt-zhangzara-blue-professional` · `html-ppt-zhangzara-bold-poster` · `html-ppt-zhangzara-broadside` · `html-ppt-zhangzara-capsule` · `html-ppt-zhangzara-cartesian` · `html-ppt-zhangzara-cobalt-grid` · `html-ppt-zhangzara-coral` · `html-ppt-zhangzara-creative-mode` · `html-ppt-zhangzara-daisy-days` · `html-ppt-zhangzara-editorial-tri-tone` · `html-ppt-zhangzara-grove` · `html-ppt-zhangzara-long-table` · `html-ppt-zhangzara-mat` · `html-ppt-zhangzara-monochrome` · `html-ppt-zhangzara-neo-grid-bold` · `html-ppt-zhangzara-peoples-platform` · `html-ppt-zhangzara-pin-and-paper` · `html-ppt-zhangzara-pink-script` · `html-ppt-zhangzara-playful` · `html-ppt-zhangzara-raw-grid` · `html-ppt-zhangzara-retro-windows` · `html-ppt-zhangzara-retro-zine` · `html-ppt-zhangzara-sakura-chroma` · `html-ppt-zhangzara-scatterbrain` · `html-ppt-zhangzara-signal` · `html-ppt-zhangzara-soft-editorial` · `html-ppt-zhangzara-stencil-tablet` · `html-ppt-zhangzara-studio` · `html-ppt-zhangzara-vellum` · `hyperframes` · `ib-pitch-book` · `image-poster` · `invoice` · `kami-deck` · `kami-landing` · `kanban-board` · `last30days` · `live-artifact` · `live-dashboard` · `magazine-poster` · `meeting-notes` · `mobile-app` · `mobile-onboarding` · `motion-frames` · `open-design-landing` · `open-design-landing-deck` · `orbit-general` · `orbit-github` · `orbit-gmail` · `orbit-linear` · `orbit-notion` · `pm-spec` · `pricing-page` · `replit-deck` · `saas-landing` · `simple-deck` · `social-carousel` · `social-media-dashboard` · `social-media-matrix-tracker-template` · `sprite-animation` · `team-okrs` · `trading-analysis-dashboard-template` · `tweaks` · `video-shortform` · `waitlist-page` · `web-prototype` · `web-prototype-taste-brutalist` · `web-prototype-taste-editorial` · `web-prototype-taste-soft` · `webgl-experience` · `weekly-update` · `wireframe-annotated` · `wireframe-greybox` · `wireframe-mobile-flow` · `wireframe-sketch` · `worker-visualizer` · `x-research`


(عائلة `html-ppt-*` وحدها ≈40 قالب شرائح، منها سلسلة `html-ppt-zhangzara-*`؛ وقوالب مالية: `dcf-valuation`, `finance-report`, `ib-pitch-book`, `invoice`, `trading-analysis-dashboard-template`؛ وقوالب بحث: `x-research`, `last30days`؛ وفيديو: `video-shortform`, `hyperframes`؛ وصوت: `audio-jingle`.)

### 3.6 `design-systems/` — 152 حزمة + `_schema` (مجمّعة في فئات؛ التصنيف مأخوذ من README وطُبّق على أسماء الشجرة الموثقة)


- **أنظمة شركات AI/LLM** (13): `claude` · `cohere` · `mistral-ai` · `minimax` · `together-ai` · `replicate` · `runwayml` · `elevenlabs` · `ollama` · `x-ai` · `openai` · `huggingface` · `perplexity`
- **أدوات مطوّرين** (23): `cursor` · `vercel` · `linear-app` · `expo` · `clickhouse` · `mongodb` · `supabase` · `hashicorp` · `posthog` · `sentry` · `warp` · `sanity` · `mintlify` · `composio` · `opencode-ai` · `voltagent` · `github` · `figma` · `framer` · `webflow` · `raycast` · `shadcn` · `resend`
- **إنتاجية وتواصل** (13): `notion` · `miro` · `airtable` · `superhuman` · `intercom` · `zapier` · `cal` · `clay` · `slack` · `discord` · `loom` · `webex` · `wechat`
- **تقنية مالية Fintech** (8): `stripe` · `coinbase` · `binance` · `kraken` · `mastercard` · `revolut` · `wise` · `trading-terminal`
- **تجارة واستهلاك** (7): `shopify` · `airbnb` · `uber` · `nike` · `starbucks` · `pinterest` · `duolingo`
- **إعلام ومنصات** (6): `spotify` · `playstation` · `wired` · `theverge` · `meta` · `xiaohongshu`
- **سيارات** (7): `tesla` · `bmw` · `bmw-m` · `ferrari` · `lamborghini` · `bugatti` · `renault`
- **شركات تقنية أخرى** (7): `apple` · `ibm` · `nvidia` · `vodafone` · `spacex` · `cisco` · `cloudflare-kumo`
- **أنماط بصرية/عامة وحزم ابتدائية** (68): `agentic` · `ant` · `application` · `arc` · `artistic` · `atelier-zero` · `bento` · `bold` · `brutalism` · `cafe` · `canva` · `claymorphism` · `clean` · `colorful` · `contemporary` · `corporate` · `cosmic` · `creative` · `dashboard` · `default` · `dithered` · `doodle` · `dramatic` · `editorial` · `elegant` · `energetic` · `enterprise` · `expressive` · `fantasy` · `flat` · `friendly` · `futuristic` · `glassmorphism` · `gradient` · `hud` · `kami` · `levels` · `lingo` · `lovable` · `luxury` · `material` · `minimal` · `mission-control` · `modern` · `mono` · `neobrutalism` · `neon` · `neumorphism` · `pacman` · `paper` · `perspective` · `premium` · `professional` · `publication` · `refined` · `retro` · `simple` · `skeumorphism` · `sleek` · `spacious` · `storytelling` · `tetris` · `tom-modern` · `totality-festival` · `urdu` · `vibrant` · `vintage` · `warm-editorial`


(كل حزمة حديثة تحوي `DESIGN.md` كعقد هوية + `manifest.json` + `tokens.css` + `design-tokens.json` + `components.html` + `components.manifest.json` + `tailwind-v4.css` + `USAGE.md` + `preview/` + `source/` + `system/` — موثق من الشجرة في عيّنات مفحوصة مثل `wechat` و`trading-terminal` و`agentic`.)

### 3.7 `plugins/_official/` — 6 فئات، 479 مجلد بلجن فعلياً

**`atoms/` (13):** `build-test` · `code-import` · `critique-theater` · `design-extract` · `diff-review` · `direction-picker` · `discovery-question-form` · `figma-extract` · `handoff` · `patch-edit` · `rewrite-plan` · `todo-write` · `token-map`

**`scenarios/` (14):** `od-code-migration` · `od-default` · `od-design-refine` · `od-figma-migration` · `od-media-generation` · `od-new-generation` · `od-next-strategy` · `od-nextjs-export` · `od-plugin-authoring` · `od-react-export` · `od-share-to-community` · `od-tune-collab` · `od-vue-export` · `od-web-effect-extractor`

**`image-templates/` (45):** `3d-stone-staircase-evolution-infographic` · `anime-martial-arts-battle-illustration` · `e-commerce-live-stream-ui-mockup` · `game-screenshot-anime-fighting-game-captain-ryuuga-vs-kaze-renshin` · `game-screenshot-three-kingdoms-guanyu-slaying-yanliang` · `game-screenshot-three-kingdoms-lyubu-yuanmen-archery` · `game-screenshot-three-kingdoms-zhaoyun-cradle-escape` · `game-ui-ancient-china-open-world-mmo-hud` · `illustrated-city-food-map` · `illustration-crayon-kid-drawing-rework` · `infographic-otaku-dance-choreography-breakdown-gokurakujodo-16-panels` · `momotaro-explainer-slide-in-hybrid-style` · `notion-team-dashboard-live-artifact` · `profile-avatar-anime-girl-to-cinematic-photo` · `profile-avatar-casual-fashion-grid-photoshoot` · `profile-avatar-cinematic-south-asian-male-portrait-with-vultures` · `profile-avatar-cyberpunk-anime-portrait-with-neon-face-text` · `profile-avatar-elegant-fantasy-girl-in-violet-garden` · `profile-avatar-ethereal-blue-haired-fantasy-portrait` · `profile-avatar-glamorous-woman-in-black-portrait` · `profile-avatar-hyper-realistic-selfie-texture-prompts` · `profile-avatar-lavender-fantasy-mage-portrait` · `profile-avatar-monochrome-studio-portrait` · `profile-avatar-old-photo-restoration-to-dslr-portrait` · `profile-avatar-poetic-woman-in-garden-portrait` · `profile-avatar-professional-identity-portrait-wallpaper` · `profile-avatar-realistically-imperfect-ai-selfie` · `profile-avatar-signed-marker-portrait-on-shikishi` · `profile-avatar-snow-rabbit-empress-portrait` · `profile-avatar-snow-rabbit-mask-hanfu-portrait` · `profile-avatar-snowy-rabbit-hanfu-portrait` · `profile-avatar-snowy-rabbit-spirit-portrait` · `profile-avatar-song-dynasty-hanfu-portrait` · `social-media-post-anime-pokemon-shop-outfit-teaser-poster` · `social-media-post-cinematic-elevator-scene` · `social-media-post-confused-elf-girl-at-pastel-desk` · `social-media-post-editorial-fashion-photography` · `social-media-post-fashion-editorial-collage` · `social-media-post-psg-transfer-announcement-poster` · `social-media-post-sensational-girl-dance-storyboard-8-shots` · `social-media-post-showa-day-retro-culture-magazine-cover` · `social-media-post-social-media-fashion-outfit-generation` · `social-media-post-travel-snapshot-collage-prompt` · `social-media-post-vintage-sign-painter-sketch` · `vr-headset-exploded-view-poster`

**`video-templates/` (63):** `3d-animated-boy-building-lego` · `a-decade-of-refinement-glow-up` · `ancient-guardian-dragon-rescue` · `ancient-indian-kingdom-fpv-video` · `animation-transfer-and-camera-tracking-prompt` · `beat-synced-outfit-transformation-dance` · `character-intro-motion-graphics-sequence` · `cinematic-birthday-celebration-sequence` · `cinematic-dragon-interaction-flight` · `cinematic-east-asian-woman-hand-dance` · `cinematic-emotional-face-close-up` · `cinematic-marine-biologist-exploration` · `cinematic-music-podcast-and-guitar-technique` · `cinematic-route-navigation-guide` · `cinematic-street-racing-sequence-for-seedance-2` · `cinematic-vampire-alley-fight-sequence` · `crimson-horizon-sci-fi-cinematic-sequence` · `cyberpunk-game-trailer-script` · `forbidden-city-cat-satire` · `frame-bold-poster` · `frame-bold-signal` · `frame-build-minimal` · `frame-creative-voltage` · `frame-data-chart-nyt` · `frame-data-rollup` · `frame-decision-tree` · `frame-electric-studio` · `frame-glitch-title` · `frame-kinetic-type` · `frame-light-leak-cinema` · `frame-liquid-bg-hero` · `frame-logo-outro` · `frame-nyt-graph` · `frame-pentagram-stat` · `frame-play-mode` · `frame-product-promo` · `frame-product-promo-30s` · `frame-swiss-grid` · `frame-takram-organic` · `frame-vignelli` · `frame-warm-grain` · `hollywood-haute-couture-fantasy-video-prompt` · `hunched-character-animation` · `live-action-anime-adaptation-water-vs-thunder-breathing-duel` · `luxury-supercar-cinematic-narrative` · `magical-academy-storyboard-sequence` · `modern-rural-aesthetics-healing-short-film-video-prompt` · `nightclub-flyer-atmospheric-animation` · `retro-hk-wuxia-film-aesthetic` · `seedance-2-0-15-second-cinematic-japanese-romance-short-film` · `seedance-2-0-80-year-old-rapper-mv` · `sequence-and-movement-instruction-for-martial-arts-video` · `soul-switching-mirror-magic-sequence` · `toaster-rocket-jumpscare` · `traditional-dance-performance` · `vfx-text-cursor` · `video-seedance-desk-hologram-ar-realdesk` · `video-seedance-three-kingdoms-guanyu-slaying-yanliang` · `video-seedance-three-kingdoms-lyubu-yuanmen-archery` · `video-seedance-three-kingdoms-zhaoyun-cradle-escape` · `vintage-disney-style-pirate-crocodile-animation` · `viral-k-pop-dance-choreography` · `wasteland-factory-chase`

**`design-systems/` (143):** نفس أسماء أنظمة التصميم مغلّفة كبلجنات (مجموعة شبه مطابقة لمحتوى `design-systems/`؛ أولها: `agentic` · `airbnb` · `airtable` · `ant` · `apple` · `application` · `arc` · `artistic` · `atelier-zero` · `bento` …).

**`examples/` (201):** `article-magazine` · `audio-jingle` · `blog-post` · `card-twitter` · `card-xiaohongshu` · `clinical-case-report` · `codex-interactive-capability-map` · `critique` · `dashboard` · `data-report` · `dating-web` · `dcf-valuation` · `deck-guizang-editorial` · `deck-open-slide-canvas` · `deck-swiss-international` · `design-brief` · `digital-eguide` · `doc-kami-parchment` · `docs-page` · `email-marketing` · `eng-runbook` · `finance-report` · `flowai-live-dashboard-template` · `frame-data-chart-nyt` · `frame-flowchart-sticky` · `frame-glitch-title` · `frame-light-leak-cinema` · `frame-liquid-bg-hero` · `frame-logo-outro` · `frame-macos-notification` · `frontend-slides` · `fs-creative-voltage` · `fs-editorial-forest` · `fs-electric-studio` · `fs-emerald-editorial` · `fs-notebook-tabs` · `gamified-app` · `github-dashboard` · `guizang-ppt` · `hatch-pet` · `hps-academic-paper` · `hps-bauhaus` · `hps-memphis-pop` · `hps-retro-tv` · `hps-true-blueprint` · `hps-y2k-chrome` · `hr-onboarding` · `html-ppt` · `html-ppt-course-module` · `html-ppt-graphify-dark-graph` · `html-ppt-hermes-cyber-terminal` · `html-ppt-knowledge-arch-blueprint` · `html-ppt-obsidian-claude-gradient` · `html-ppt-pitch-deck` · `html-ppt-presenter-mode-reveal` · `html-ppt-product-launch` · `html-ppt-taste-brutalist` · `html-ppt-taste-editorial` · `html-ppt-tech-sharing` · `html-ppt-testing-safety-alert` · `html-ppt-weekly-report` · `html-ppt-xhs-pastel-card` · `html-ppt-xhs-white-editorial` · `html-ppt-zhangzara-8-bit-orbit` · `html-ppt-zhangzara-biennale-yellow` · `html-ppt-zhangzara-block-frame` · `html-ppt-zhangzara-blue-professional` · `html-ppt-zhangzara-bold-poster` · `html-ppt-zhangzara-broadside` · `html-ppt-zhangzara-capsule` · `html-ppt-zhangzara-cartesian` · `html-ppt-zhangzara-cobalt-grid` · `html-ppt-zhangzara-coral` · `html-ppt-zhangzara-creative-mode` · `html-ppt-zhangzara-daisy-days` · `html-ppt-zhangzara-editorial-tri-tone` · `html-ppt-zhangzara-grove` · `html-ppt-zhangzara-long-table` · `html-ppt-zhangzara-mat` · `html-ppt-zhangzara-monochrome` · `html-ppt-zhangzara-neo-grid-bold` · `html-ppt-zhangzara-peoples-platform` · `html-ppt-zhangzara-pin-and-paper` · `html-ppt-zhangzara-pink-script` · `html-ppt-zhangzara-playful` · `html-ppt-zhangzara-raw-grid` · `html-ppt-zhangzara-retro-windows` · `html-ppt-zhangzara-retro-zine` · `html-ppt-zhangzara-sakura-chroma` · `html-ppt-zhangzara-scatterbrain` · `html-ppt-zhangzara-signal` · `html-ppt-zhangzara-soft-editorial` · `html-ppt-zhangzara-stencil-tablet` · `html-ppt-zhangzara-studio` · `html-ppt-zhangzara-vellum` · `huashu-annual-letter` · `huashu-bento-insight` · `huashu-golden-circle` · `huashu-keynote-black` · `huashu-luxe-whitespace` · `huashu-pentagram-grid` · `huashu-slides` · `huashu-sparkline-arc` · `huashu-takram-soft-tech` · `hyperframes` · `ib-pitch-book` · `image-poster` · `invoice` · `kami-deck` · `kami-landing` · `kanban-board` · `last30days` · `live-artifact` · `live-dashboard` · `magazine-poster` · `meeting-notes` · `mobile-app` · `mobile-onboarding` · `mockup-device-3d` · `motion-claude-agent-lab` · `motion-claude-design-team` · `motion-distilbook-explainer` · `motion-flowdrive-motion-reel` · `motion-frames` · `motion-future` · `motion-kinetic-motion-designer` · `motion-mind-clarity-journey` · `motion-opus-design-lab` · `motion-product-promo` · `motion-prompt-motion-gallery` · `motion-semantic-color-stripes` · `motion-showreel` · `motion-sky-water-tessellation` · `motion-superx-audience-growth` · `motion-tixfox-ticket-promo` · `motion-ui-morph` · `motion-visual-lesson` · `motion-windows-studio-launch` · `od-plugin-contribute-open-design` · `od-plugin-publish-github` · `open-design-homepage` · `open-design-landing` · `open-design-landing-deck` · `orbit-general` · `orbit-github` · `orbit-gmail` · `orbit-linear` · `orbit-notion` · `pm-spec` · `poster-hero` · `ppt-keynote` · `pptx-html-fidelity-audit` · `pricing-page` · `replit-deck` · `resume-modern` · `saas-landing` · `simple-deck` · `social-carousel` · `social-media-dashboard` · `social-media-matrix-tracker-template` · `social-reddit-card` · `social-spotify-card` · `social-x-post-card` · `sprite-animation` · `team-okrs` · `trading-analysis-dashboard-template` · `tweaks` · `ve-midnight-editorial` · `ve-terminal-mono` · `velar-luxury-real-estate` · `vfx-text-cursor` · `video-hyperframes` · `video-shortform` · `waitlist-page` · `web-clone` · `web-prototype` · `web-prototype-taste-brutalist` · `web-prototype-taste-editorial` · `web-prototype-taste-soft` · `webgl-aurora-veil` · `webgl-caustic-pool` · `webgl-depth-gallery` · `webgl-distortion-grain` · `webgl-experience` · `webgl-halftone-drift` · `webgl-holographic-foil` · `webgl-horizontal-parallax` · `webgl-liquid-iridescence` · `webgl-liquid-metal` · `webgl-neon-grid` · `webgl-particle-galaxy` · `webgl-pixel-reveal-gallery` · `webgl-raymarched-hero` · `webgl-voronoi-cells` · `weekly-update` · `wireframe-annotated` · `wireframe-greybox` · `wireframe-mobile-flow` · `wireframe-sketch` · `worker-visualizer` · `x-research`

### 3.8 `prompt-templates/`
- `image/` — **48 قالب JSON** (+ معاينة PNG واحدة على الأقل)، أسماء تمثل: إنفوغرافيك، لقطات ألعاب، بورتريهات سينمائية، خرائط طعام مرسومة…
- `video/` — **58 قالب JSON**: مشاهد سينمائية، HyperFrames (saas-promo، karaoke talking-head، logo-outro، bar-chart-race، flight-map…)، برومبتات Seedance.

### 3.9 `deploy/`
`Dockerfile` + `Dockerfile.local` + `docker-compose.yml` + `docker-compose.linux.yml` + `.env.example` · `aws/` (SAM `template.yaml`) · `azure/` (Bicep: `aci`, `app-service`, `container-instance` + `azure-pipelines.yml` + سكربت) · `scripts/` (install/uninstall/update/publish-images/verify-image…) · `tests/` (اختبارات Bicep والتثبيت) · `README.md`.

### 3.10 `e2e/`
- `playwright.config.ts` + `playwright.visual.config.ts` + `vitest.config.ts`
- `specs/` — مواصفات Playwright للمنصات (`mac.spec.ts`, `win.spec.ts`, `linux.spec.ts`) + مجلدات `dialog/namespace/orbit/pet/web-clone` (≈13 ملف spec)
- `tests/` — ≈150 مسار اختبار (vitest): amr، antigravity، collab، artifact-lint، docker-image…
- `ui/` — **126 ملف اختبار UI** (أكبر مجموعة: سيناريوهات sandbox، wallet، settings، chat، memory routines…)
- `lib/` — مساعدات (fake-agents، playwright، desktop…) · `resources/` — تسجيلات وفريمات · `scripts/` — أدوات تشغيل.

---

## 4) العدّ الفعلي من الشجرة مقابل أرقام README

| العنصر | رقم README | العدد الفعلي من الشجرة | ملاحظة |
|---|---|---|---|
| أنظمة التصميم | 151 | **152 حزمة** (+ مجلد `_schema`) | README متأخر بمقدار 1 على الأقل |
| المهارات الوظيفية | «100+» | **169 مجلداً** في `skills/` | متوافق تقريبياً (README متحفظ) |
| البلجنات الرسمية | 277 + 183 مثالاً | **278 + 201 = 479** (atoms 13 + scenarios 14 + image 45 + video 63 + design-systems 143 + examples 201) | فروق: scenarios 14 لا 13 (وجود `od-next-strategy`)، examples 201 لا 183 |
| قوالب البرومبت | 93 («11 HyperFrames + 39 Seedance») | **48 صورة + 58 فيديو = 106 JSON** | README أقدم من المحتوى |
| قوالب الشرائح html-ppt | «15 قالباً × 36 ثيماً» | ≈40 مجلداً باسم `html-ppt*` | README يعدّ «القوالب» لا المجلدات |
| تعريفات الـruntimes | 27 تعريفاً / 26 CLI | لم يُعدَّ في هذه المرحلة (يتطلب قراءة `apps/daemon/src/runtimes/`) | مؤجل للمرحلة الثانية |
| اختبارات e2e/ui | — | **126 ملفاً** | — |

---

## 5) ماذا يفيد المستودع في المواضيع المطلوبة (بمسارات دقيقة)

- **الذاكرة:** محدود لكنه موجود — اختبار `e2e/ui/settings-memory-routines.test.ts`، ومواصفة `specs/current/creative-memory-integration-shape.md`، وإشارة README إلى تراكم «screenshots/fonts/palettes/artifacts» كافتراضيات للجلسات. لا يوجد نظام ذاكرة عام مستقل (vector store…). (موثق شجرة + README)
- **المحادثة:** جوهرية — محادثات ورسائل مخزنة في SQLite (README roadmap)، بث عبر `/api/chat (SSE)`، اختبارات `e2e/ui/chat-*.test.ts`، توثيق `docs/design/chat-mirror/`، مهارة `skills/chat-motion-overlay/`. (موثق)
- **الصوت:** توليد فقط (TTS/موسيقى)، لا معالجة/تعرّف — مهارات `skills/speech/`, `skills/venice-audio-speech/`, `skills/venice-audio-music/`, `skills/ai-music-album/`, `skills/fal-lip-sync/`، قالب `design-templates/audio-jingle/`، موفر `senseaudio` ضمن BYOK proxy (README). (موثق)
- **المعماريات:** غنية — `docs/architecture.md`, `docs/adr/0001-centralize-daemon-startup.md`, `docs/spec.md`, `docs/plugins-spec.md`, `docs/skills-protocol.md`, `docs/agent-adapters.md`, `docs/new-agent-runtime-acp.md`, `docs/orchestrator-workspaces.md`, `docs/prompt-composition.md`, `packages/contracts`, `packages/registry-protocol`, `docs/schemas/open-design.plugin.v1.json`. (موثق)
- **الوكلاء:** جوهر المنتج — `apps/daemon/src/runtimes/defs/` (تعريفات 26+ وكيل CLI)، `docs/agent-adapters.md` (عقد المحوّل)، MCP stdio server، `packages/agui-adapter`, `packages/dsh-runtime`, ملفات `AGENTS.md` في كل مجلد رئيسي، سيناريوهات `plugins/_official/scenarios/od-*`. (موثق)
- **التصميم:** كتلة المستودع الأكبر — `design-systems/` (152)، `design-templates/` (115)، `skills/` (169 أغلبها تصميمي)، `craft/` (أدلة جودة)، `docs/design-system-tracking-spec.md`, `docs/atoms.md`, `docs/modes.md`. (موثق)
- **الحماية:** وقائية معمارية لا هجومية — حماية SSRF في BYOK proxy (README)، ربط loopback افتراضي + `OD_BIND_HOST`/`OD_ALLOWED_ORIGINS`، `OD_ALLOWED_INTERNAL_HOSTS`، `OD_API_TOKEN` + Basic Auth في Docker، sandboxed iframe للمعاينة، Electron sandboxed renderer، `docs/plans/2026-06-01-sandbox-orchestration-hardening-architecture.md`، اختبارات `e2e/ui/*sandbox*.test.ts` و`api-security-view016.test.ts`، `PRIVACY.md` (telemetry بموافقة). (موثق)
- **المهارات:** بروتوكول كامل — `docs/skills-protocol.md`, `docs/skills-contributing.md`, `skills/README.md`, `skills/AGENTS.md`. (موثق)
- **الأنظمة (design systems):** `design-systems/README.md`, `_schema/`, `scripts/sync-design-systems.ts`, اختبارات سلامة الحزم في `scripts/check-design-system-*.ts`. (موثق)
- **البحث والقراءة:** بحث محلي في الكتالوجات (صفحة Plugins ببحث حسب README)؛ لا يوجد RAG/فيكتور. قوالب بحث: `skills/research-decision-room/`, `design-templates/x-research/`, `design-templates/last30days/`، وأداة التقاط ويب `clipper/` + `specs/od-clipper.md`. (موثق + استنتاج لغياب RAG من غياب أي مسارات vector/embedding في الشجرة)
- **الفيديو:** قوي — HyperFrames (`design-templates/hyperframes/`, `docs/external-media-orchestration.md`, `docs/motion-template-sources.md`)، مهارات `sora`, `remotion`, `fal-kling-o3`, `fal-video-edit`, `video-downloader`, `youtube-clipper`, `video-hyperframes`, `venice-video`, `chat-motion-overlay`، و58 برومبت فيديو + 63 بلجن فيديو. (موثق)
- **التحليل المالي:** قوالب عرض مالية فقط، لا محرك حسابات — `design-templates/dcf-valuation/` (به `references/`)، `finance-report/`, `ib-pitch-book/`, `invoice/`, `trading-analysis-dashboard-template/`, نظام `design-systems/trading-terminal/`. (موثق)
- **البحث الاستدلالي:** لا يوجد مكوّن مخصص؛ أقرب شيء: `skills/research-decision-room/`, `skills/brainstorming/`, بلجن مجتمعي `plugins/community/deep-think-maximum-cognitive-effort-protocol-*`، وتكامل مع وكلاء خارجيين يملكون الاستدلال. (موثق للأسماء؛ الحكم استنتاج)
- **فك الشفرات/الثغرات:** **لا يوجد** أي مكوّن لهذا الغرض (لا أسماء ولا مسارات تتعلق بـ CTF/exploit/decrypt في الشجرة). (موثق بالسلب)

---

## 6) ما لا يوجد صراحة / خارج نطاق المستودع (بلا مبالغة)

1. **لا يوجد نموذج/وكيل ذكاء اصطناعي خاص** — المستودع «model-agnostic» ويعتمد كلياً على CLIs خارجية أو BYOK (README صريح: "We don't ship an agent").
2. **لا ذاكرة دلالية/متجهة (RAG، embeddings، vector DB)** — لا مسارات ولا حزم بهذا المعنى؛ «الذاكرة» الحالية تفضيلات وتراكم أصول.
3. **لا معالجة صوتية** (تعرّف على الكلام/تحويل صوت-نص محلي) — التوليد فقط عبر مزودين خارجيين.
4. **لا أدوات فك شفرات أو اختبار اختراق أو CTF** إطلاقاً؛ «الحماية» كلها دفاعية لتأمين الدايمون المحلي.
5. **لا محرك تحليل مالي حسابي** (بيانات سوق حية، backtesting) — قوالب عرض HTML فقط.
6. **لا دعم Linux مبنياً مسبقاً** لسطح المكتب (README: من المصدر فقط، متابعة في issue #4368).
7. **لا تكامل استدلالي مدمج** (deep-research/multi-hop) كمكوّن — يُفوَّض للوكيل الخارجي.
8. ميزات معلنة لكنها **غير مكتملة** حسب roadmap: tweaks panel، comment-mode surgical edits، `npx od init`، Plugin SDK CLI، وبلجنات ترحيل Figma→React (alpha).

---

## 7) مرشحون للتوسع في مرحلة لاحقة (مع السبب)

1. **`apps/daemon/src/runtimes/defs/` + `docs/agent-adapters.md`** — عقد تكامل 26+ وكيل CLI؛ الأعلى قيمة لفهم طبقة «الوكلاء».
2. **`plugins/_official/scenarios/od-*` (14 سيناريو)** — سير عمل كامل جاهز (ترحيل كود/Figma، توليد وسائط، تصدير React/Next/Vue).
3. **`docs/skills-protocol.md` + `plugins/spec/SPEC.md` + `docs/schemas/*.json`** — المواصفات الرسمية القابلة لإعادة الاستخدام في أنظمة بلجن أخرى.
4. **`design-systems/_schema/` + `scripts/sync-design-systems.ts`** — آلية تحويل هوية علامة إلى حزمة `DESIGN.md` قابلة للنقل.
5. **`design-templates/hyperframes/` + `docs/external-media-orchestration.md`** — خط أنابيب HTML→MP4 (فيديو) الوحيد الموثق تفصيلياً.
6. **`packages/contracts` و`registry-protocol` و`plugin-runtime`** — عقود البنية الداخلية قبل أي استخراج كود.
7. **`deploy/` (Docker/AWS/Azure) + عقد بيانات الدايمون في `AGENTS.md`** — لمسار الاستضافة الذاتية.
8. **`e2e/` (≈290 اختباراً)** — خريطة سلوك فعلية للمنتج مفيدة للتحقق من أي فهم لاحق.
9. **`clipper/` + `specs/od-clipper.md`** — التقاط هوية بصرية من الويب (مدخل «البحث والقراءة» الوحيد تقريباً).
10. **`docs/plans/2026-06-01-sandbox-orchestration-hardening-architecture.md`** — أعمق وثيقة حماية في المستودع.
