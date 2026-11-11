# تحليل جرد مستودع langflow-ai/langflow — فرع main

> **نطاق العمل**: مرحلة جرد (Inventory) فقط — لا استخراج كود، لا تشغيل، لا اختبار.
> **منهجية التحقق**: قراءة برمجية لشجرة Git الكاملة غير المبتورة (`langflow.tree.json`, 14,234 عنصراً، `truncated: false`) + ملف الفروع (`langflow.branches.json`) + الوثائق الرئيسية المجلوبة من الالتزام المثبَّت (README.md، DEVELOPMENT.md، DESIGN.md، SECURITY.md، LICENSE، CONTRIBUTING.md).
> **تنبيه**: كل ما ورد أدناه مستنتج من أسماء المسارات والملفات والوثائق، ولم يتم تشغيل أي جزء من المشروع أو اختباره.

---

## 1. التعريف والترخيص والتقنيات

### التعريف
- **الاسم**: Langflow — منظومة مفتوحة المصدر لبناء ونشر وكلاء الذكاء الاصطناعي وسير العمل (AI agents & workflows).
- **التعريف الرسمي (README)**: «منصة قوية لبناء ونشر الوكلاء وسير العمل المدعومة بالذكاء الاصطناعي، مع مُنشئ مرئي (Visual builder) وخوادم API وMCP مدمجة تحوّل كل سير عمل إلى أداة قابلة للتكامل».
- **المالك/المنظمة**: `langflow-ai` (الإبلاغ الأمني عبر HackerOne التابع لـ IBM — مؤشر على علاقة IBM بالمشروع).
- **الموقع**: langflow.org — التوثيق: docs.langflow.org.

### الترخيص
- **MIT License** — `LICENSE` (Copyright (c) 2024 Langflow). ترخيص متساهل يسمح بالاستخدام التجاري والتعديل وإعادة التوزيع.

### معرّف الفرع الرئيسي
- **main HEAD commit**: `60999cc9a7350e44dde3ef641baae864e10861f0` (من `langflow.head.txt` و`langflow.branches.json`؛ الفرع **محمي/protected**).
- إجمالي الفروع في المستودع: **2660 فرعاً** (منها فروع إصدارات مرقّمة مثل 1.9.x–1.13.x).

### التقنيات (من DEVELOPMENT.md وملفات الإعداد في الشجرة)
| الطبقة | التقنية | الدليل |
|---|---|---|
| لغة الخلفية | Python 3.10–3.14 | README + `pyproject.toml` + `uv.lock` |
| مدير الحزم | uv (≥0.4) من Astral | DEVELOPMENT.md |
| إطار الخلفية | FastAPI + SQLAlchemy + Alembic | `src/backend/base/langflow/api/`، `alembic/`، مراجع `.agents/skills/backend-code-review/references/sqlalchemy-rule.md` |
| الواجهة | React + TypeScript + Vite + Tailwind CSS | `src/frontend/` (vite.config.mts, tailwind.config.mjs, tsconfig.json) |
| جودة الواجهة | Biome, ESLint, Jest, Playwright, Storybook, Husky | ملفات الإعداد في `src/frontend/` |
| Node.js | v22.12 LTS / npm v10.9 | DEVELOPMENT.md |
| بناء/تشغيل | Makefile + Makefile.frontend | الجذر |
| CI/CD | GitHub Actions — **52 سير عمل** | `.github/workflows/` |
| التوثيق | Docusaurus (مع i18n ونسخ versioned) | `docs/docusaurus.config.js`، `docs/versioned_docs/` |
| الحاويات | Docker / docker-compose / Render / GCP | `docker/`، `deploy/`، `render.yaml`، `scripts/gcp/` |
| الترجمة | 8 لغات (en, de, es, fr, ja, ko, pt, zh-Hans) | `src/frontend/src/locales/`، `src/backend/base/langflow/locales/` |

### حجم الشجرة
- **11,878 ملفاً** و**2,356 مجلداً**؛ صفحات التوثيق الحالية (docs/docs): **276 صفحة** mdx/md.

---

## 2. كل مجلدات وملفات الجذر

### مجلدات الجذر (11)
| المجلد | الوصف المستنتج |
|---|---|
| `.agents/skills/` | مهارات وكلاء الترميز لمراجعة الكود (11 مهارة: backend-code-review, component-refactoring, e2e-testing, frontend-code-review, frontend-i18n, frontend-query-mutation, frontend-testing, ibm-a11y-level1-audit, ibm-a11y-pr-remediation, ibm-a11y-route-scan, ibm-a11y-testing-guide) — كل مهارة بملف SKILL.md ومراجع |
| `.cursor/` | إعدادات محرر Cursor |
| `.devcontainer/` | حاوية تطوير جاهزة (موصى بها لويندوز) |
| `.github/` | 52 workflow + قوالب issues + dependabot + codeql + ملاحظات mend-scan |
| `.release-artifacts/` | قطع الإصدارات |
| `.vscode/` | إعدادات VS Code |
| `deploy/` | نشر إنتاجي: docker-compose + prometheus + observability (grafana-loki) + listeners (k8s deployment) |
| `design/` | موارد تصميم: `dedicated-integrations/` و`dedicated-integrations-triggers/` |
| `docker/` | 6+ Dockerfiles (build_and_push, backend, ep, cdk, dev, render) + compose للتطوير |
| `docker_example/` | مثال نشر مبسّط (Dockerfile + compose + pre) |
| `docs/` | موقع Docusaurus الكامل للتوثيق (276 صفحة + نسخ مؤرشفة 1.9–1.13) |
| `regressions/` | ملفات YAML لاختبارات الانحدار لكل إصدار: 1.9.x إلى 1.13.x + README |
| `scripts/` | سكربتات تشغيلية (تفصيل أدناه) |
| `src/` | الكود المصدري (تفصيل أدناه) |

### أهم ملفات الجذر
- الوثائق: `README.md`, `DEVELOPMENT.md`, `DESIGN.md` (نظام تصميم كامل بالألوان/الطباعة/المكونات), `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `RELEASE.md`, `AGENTS.md`, `AGENTS-example.md`, `CLAUDE.md`, `BUNDLE_API.md`, `ci-skip-analysis.md`
- البناء: `Makefile`, `Makefile.frontend`, `pyproject.toml`, `uv.lock`, `package.json`, `package-lock.json`
- الإعداد/الأمان: `.env.example`, `.dockerignore`, `.pre-commit-config.yaml`, `.secrets.baseline`, `.whitesource`, `.coderabbit.yaml`, `.composio.lock`, `codecov.yml`, `render.yaml`, `wss-generated.config`

---

## 3. خريطة src و deploy و docker و docs و scripts و tests/regressions

### 3.1 خريطة `src/` (6 وحدات رئيسية)
```
src/
├── backend/            # تطبيق FastAPI الرئيسي
│   ├── base/langflow/  # الحزمة الأساسية (api, services, graph, agentic, alembic...)
│   ├── langflow/       # نسخة التوزيع (version فقط)
│   └── tests/          # unit (1162 ملف اختبار) + integration (52) + locust + performance + stress + test_migrations
├── frontend/           # React/TS/Vite — src/{components, CustomNodes, CustomEdges, pages, modals, stores, controllers, hooks, contexts, locales...} + tests (295 ملفاً)
├── lfx/                # نواة المكونات الجديدة (حزمة مستقلة): src/lfx/{components, base, mcp, memory, workflow, execution, services...} + tests (593 ملفاً)
├── bundles/            # حزم تكامل منفصلة قابلة للتثبيت (28 حزمة مورّد + lfx-bundles الداخلية)
├── sdk/                # SDK مستقل (src + tests + langflow-environments.toml.example)
└── langflow-stepflow/  # محرك/حزمة stepflow (src/langflow_stepflow + tests)
```

#### الخلفية `src/backend/base/langflow/` — أبرز الوحدات
- `api/v1/`: **أكثر من 55 موجّه endpoint** منها: `flows`, `chat`, `voice_mode`, `mcp`, `mcp_projects`, `a2a`, `a2a_executor`, `knowledge_bases`, `memories`, `triggers`, `trigger_ingress`, `openai_responses`, `authz_*` (roles, teams, shares, capabilities, audit), `audits`, `monitor`, `store`, `files`, `projects*`, `deployments`, `model_provider_policy*`, `policy_bundle`, `data_subjects*`, `login`, `users`, `api_key`, `variable`, `flow_version`, `flow_conflict*`, `flow_events`
- `api/v2/`: `workflow*` (host/execution/background/validation/reconstruction/public), `hitl` (Human-in-the-loop), `mcp`, `files`, `registration`
- `agentic/`: `api`, `flows`, `mcp` (خادم MCP داخلي: `server.py`), `services`, `schema`
- `services/`: **40 خدمة** منها: `auth`, `authorization`, `audit`, `rate_limit`, `session`, `chat`, `cache`, `database`, `storage`, `store`, `telemetry`, `tracing`, `triggers`, `jobs`, `job_queue`, `task`, `variable`, `flow`, `state`, `transaction`, `checkpoint`, `knowledge_base_storage`, `memory_base`, `warm_registry`, `catalog_policy`, `deployment_artifacts`
- وحدات بنيوية: `graph/`, `processing/`, `schema/`, `serialization/`, `template/`, `custom/`, `load/`, `inputs/`, `io/`, `middleware.py`, `worker.py`, `main.py`, `server.py`, `memory.py`
- `initial_setup/starter_projects/`: **27 مشروعاً جاهزاً** (انظر §5)

#### نواة lfx `src/lfx/src/lfx/`
- `components/` (105 فئات فرعية/مجلدات)، `base/` (agents, chains, embeddings, memory, models, vectorstores, tools, triggers, mcp, composio, knowledge_bases...), `workflow/` (actions, host, router, agui_translator, end_user_identity), `mcp/`, `memory/` (flow_context, stubs), `execution/`, `integrations/` (capabilities), `services/`, `upgrade/`, `testing/`
- ملفات مرجعية: `LFX_MCP.md`, `PLUGGABLE_SERVICES.md`, `README.md`, `lfx.toml.example`

### 3.2 خريطة `deploy/`
- `docker-compose.yml` + `docker-compose.override.yml` + `.env.example` + `prometheus.yml`
- `observability/grafana-loki/` — مراقبة سجلات
- `listeners/` — `docker-compose.listeners.yml` + `kubernetes-deployment.yaml`

### 3.3 خريطة `docker/` و`docker_example/`
- صور: `build_and_push.Dockerfile`, `build_and_push_backend.Dockerfile`, `build_and_push_ep.Dockerfile`, `cdk.Dockerfile`, `dev.Dockerfile`, `render.Dockerfile`, `render.pre-release.Dockerfile`, `frontend/`
- أوضاع: `cdk-docker-compose.yml`, `dev.docker-compose.yml`, `install_hardened_npm.sh` (تصلّب أمني لـ npm)

### 3.4 خريطة `docs/`
- أقسام التوثيق: `Get-Started`, `Agents`, `Components`, `Flows`, `Develop`, `Deployment`, `API-Reference`, `Lfx`, `Tutorials`, `Contributing`, `Support`
- `versioned_docs/`: نسخ 1.9.0، 1.10.0، 1.11.0، 1.12.0، 1.13.0
- `openapi/`، `i18n/`، `agents/`، `features/`، `development/`

### 3.5 خريطة `scripts/`
- `ci/` (89 عنصراً: مصفوفة authz، مقاييس اختبارات، bundle profiles وقفلها، فحص المصادقة...)، `gcp/` (نشر GCP + spot)، `benchmark/`، `e2e_deployment_tests/watsonx_orchestrate`، `migrate/` (ترحيل الحزم)، `migration_rehearsal/`، `lint/`، `a11y/` (فحص الوصولية)، `windows/` (bat/ps1)، `i18n/`، `setup/`، `gp/`
- ملفات: `build_component_index.py`, `generate_migration.py`, `migrate_secret_key.py`, `update_legacy_storage_sources.py`, `release-lfx.sh`

### 3.6 الاختبارات والانحدارات
| الموقع | العدد المحسوب من الشجرة |
|---|---|
| `src/backend/tests/unit/` | 1,162 ملف Python |
| `src/backend/tests/integration/` | 52 ملفاً |
| `src/backend/tests/` إضافية | `locust/`، `performance/`، `stress/`، `test_migrations/` |
| `src/lfx/tests/` | 593 ملفاً |
| `src/frontend/tests/` | 295 ملفاً (Playwright/Jest) |
| `regressions/` | تعريفات YAML: 1.9.x، 1.10.x، 1.11.x، 1.12.x، 1.13.x |
| CI | workflows مخصصة: `backend-unit-tests.yml`, `cross-bundle-test.yml`, `cross-platform-test.yml`, `db-migration-validation.yml`, `a11y-scan.yml`, `codeql.yml`... |

---

## 4. فئات المكونات والحزم (عدّ محسوب من الشجرة)

### العدد الإجمالي
- **مكونات النواة lfx** (`src/lfx/src/lfx/components/`): **182 ملف مكوّن .py** موزعة على **~100 فئة/مزوّد**.
- **الحزم المنفصلة** (`src/bundles/*`): **113 ملف مكوّن** عبر 28 حزمة مورّد.
- **الحزم الداخلية المجمّعة** (`src/bundles/lfx-bundles/src/lfx_bundles/`): **200 وحدة .py** عبر 73 مجلد مورّد (منها ~70 مكوّن Composio).
- **الإجمالي التقريبي: ~495 ملف مكوّن** (182 + 113 + 200).

### 4.1 فئات مكونات lfx الأساسية (الأسماء الفعلية من الشجرة)
- **الوكلاء والنماذج** `models_and_agents/` (10): `agent.py`, `a2a_agent.py`, `language_model.py`, `embedding_model.py`, `mcp_component.py`, `memory.py`, `model_selection.py`, `prompt.py`, `policies_component.py` + مجلدات `agent_helpers`, `policies`, `structured_output`
- **الوكلاء التوليدية** `agentics/` (5): `agenerate_component.py`, `amap_component.py`, `areduce_component.py`
- **المدخلات/المخرجات** `input_output/` (6): `chat.py`, `chat_output.py`, `text.py`, `text_output.py`, `webhook.py`
- **المحفّزات** `triggers/` (3): `inbound_webhook_trigger.py`, `schedule_trigger.py`
- **مصادر البيانات** `data_source/` (10): `api_request.py`, `csv_to_data.py`, `json_to_data.py`, `sql_executor.py`, `url.py`, `web_search.py`, `news_search.py`, `rss.py`, `mock_data.py`
- **الملفات والمعرفة** `files_and_knowledge/` (12): `file.py`, `directory.py`, `filesystem.py`, `ingestion.py`, `retrieval.py`, `knowledge.py`, `memory_retrieval.py`, `save_file.py` + عزل نظام الملفات `_filesystem_isolation.py`, `_filesystem_namespace.py`
- **الأدوات** `tools/` (12): `calculator.py`, `python_repl.py`, `google_search_api.py`, `google_serper_api.py`, `serp_api.py`, `search_api.py`, `searxng.py`, `tavily_search_tool.py`, `wikipedia_api.py`, `wikidata_api.py`, `yahoo_finance.py`
- **عمليات LLM** `llm_operations/` (8): `structured_output.py`, `guardrails.py`, `guardrails_v2.py`, `llm_conditional_router.py`, `llm_selector.py`, `batch_run.py`, `lambda_filter.py`
- **التحكم بالتدفق** `flow_controls/` (11): `conditional_router.py`, `loop.py`, `sub_flow.py`, `run_flow.py`, `flow_tool.py`, `human_input.py`, `listen.py`, `notify.py`, `pass_message.py`
- **المعالجة** `processing/` (28): `parse_data.py`, `filter_data.py`, `merge_data.py`, `split_text.py`, `regex.py`, `data_operations.py`, `dataframe_operations.py`, `store_message.py`...
- **أدوات LangChain** `langchain_utilities/` (27)
- **معطّلة** `deactivated/` (23)
- فئات مفردة أخرى: `chains`, `embeddings`, `models`, `output_parsers`, `textsplitters`, `vectorstores`, `helpers`, `logic`, `link_extractors`, `documentloaders`, `knowledge_bases`, `custom_component`, `prototypes`, `utilities`, `toolkits`, `data`

### 4.2 مزودو LLM (فئات فعلية — 28 تقريباً)
openai, anthropic, azure, google/vertexai, amazon (Bedrock), ollama, mistral, groq, cohere, deepseek, xai, openrouter, litellm, lmstudio, huggingface, nvidia, sambanova, novita, perplexity, maritalk, baidu, cometapi, aiml, ibm (watsonx), cloudflare, vllm, openai-compatible

### 4.3 مخازن المتجهات وقواعد البيانات (21 تقريباً)
FAISS, chroma, qdrant, pinecone, weaviate, milvus, pgvector, redis, valkey, upstash, elastic, clickhouse, couchbase, mongodb, supabase, cassandra/datastax (AstraDB + HCD + Graph RAG), oracle (oraclevs), ibm (db2_vector), vectara, needle, nextplaid (multivector/vllm)

### 4.4 البحث والزحف واستخراج الويب
tavily, exa, serpapi, searchapi, serpingapi, serply, duckduckgo, bing, yahoosearch, wikipedia, wikidata, wolframalpha, arxiv + firecrawl (crawl/map/scrape/search), apify, spider, scrapegraph, unstructured, docling (4 مكونات), confluence, glean, mrscraper

### 4.5 حزم bundles المنفصلة (العدد الفعلي لكل حزمة)
google (20)، datastax (14)، microsoft (12)، slack (9)، ibm (8)، toolguard (6)، confluent (5: Kafka consumer/producer + tableflow + context engine)، amazon (4)، firecrawl (4)، docling (4)، oracle (4)، cohere (3)، nextplaid (3)، azure (2)، ollama (2)، openai (2)، valkey (2)، empiriolabs (2)، وملف واحد لكل من: anthropic, arxiv, duckduckgo, exa, paddle, serpingapi, serply
- **ملاحظة**: حزم google وmicrosoft وslack تتضمن **محفّزات** (gmail_trigger, calendar_trigger, drive_trigger, mail_trigger, file_trigger, slack_on_message, slack_on_reaction).

### 4.6 lfx-bundles (73 مورّداً داخلياً، أبرزها)
- **~70 مكوّن Composio** جاهز: github, gmail, slack, notion, jira, linear, asana, airtable, discord, dropbox, figma, canva, reddit, instagram, snowflake, supabase, googlesheets/docs/calendar/meet/tasks/bigquery/classroom, outlook, onedrive, calendly, todoist, wrike, miro, pandadoc, klaviyo, freshdesk, peopledatalabs, listennotes, timelinesai, elevenlabs, heygen, bolna, fireflies, brightdata, apollo, attio, coda, contentful, digicert, flexisign, finage, fixer, jotform, missive, mem0, exa, firecrawl, perplexityai, serpapi, tavily, youtube...
- وكلاء متخصصون: `crewai` (7 مكونات)، `altk/altk_agent.py`, `cuga/cuga_agent.py`, `codeagents/codeact_agent_smolagents.py`, `codeagents/open_ds_star_agent.py`
- صوت: `funasr/funasr_transcription.py`، `assemblyai/` (5: start/poll/list transcripts, lemur, subtitles)
- فيديو: `twelvelabs/` (9: pegasus index/model, video embeddings, split_video, text embeddings...)، `youtube/` (7: search, channel, playlist, comments, trending, transcripts, video_details)
- ذاكرة: `mem0/mem0_chat_memory.py`, `zep/zep.py`

---

## 5. الإمكانات التفصيلية مع المسارات

> كل ما يلي «موجود في الشجرة» — لم يُختبر تشغيلياً.

| الإمكانية | الحالة | المسارات الدالة |
|---|---|---|
| **الذاكرة** | مدمجة + خارجية | `src/lfx/src/lfx/memory/` (flow_context, stubs)؛ مكوّن `models_and_agents/memory.py`؛ `files_and_knowledge/memory_retrieval.py`؛ خارجية: `lfx_bundles/mem0/mem0_chat_memory.py`, `lfx_bundles/zep/zep.py`, `bundles/datastax/astradb_chatmemory.py`, redis/upstash/valkey؛ خدمات: `services/session`, `services/memory_base`, `backend/base/langflow/memory.py`؛ endpoint: `api/v1/memories.py` |
| **المحادثة** | مدمجة | مكوّنا `input_output/chat.py` و`chat_output.py`؛ `api/v1/chat.py`؛ `services/chat/`؛ مشروع «Memory Chatbot.json» الجاهز؛ Playground تفاعلي في الواجهة (`src/frontend/src/components/core/playgroundComponent/`) |
| **الصوت** | مدمج (Voice Mode) + خارجي | `api/v1/voice_mode.py` + `utils/voice_utils.py`؛ واجهة كاملة: `src/frontend/src/modals/IOModal/components/chatView/chatInput/components/voice-assistant/` (أزرار، إعدادات صوت/ميكروفون/لغة، audio-worklet)؛ توثيق `docs/docs/Develop/concepts-voice-mode.mdx`؛ خارجي: funasr (تفريغ)، AssemblyAI (5 مكونات)، ElevenLabs عبر Composio، plivo، bolna |
| **المعماريات** | متعددة | خادم FastAPI + workers (`worker.py`, `services/job_queue`, `services/jobs`, `services/task`)؛ محرك workflow مستقل (`lfx/workflow/`, `api/v2/workflow_*`)؛ محرك graph (`graph/`)؛ SDK مستقل (`src/sdk/`)؛ نواة lfx قابلة للتثبيت منفصلة؛ حزم opt-in (`docs`: _partial-opt-in-bundles)؛ خدمات قابلة للتبديل (`lfx/PLUGGABLE_SERVICES.md`) |
| **Multi-agent** | مدمج | مكوّن `agent.py` و`a2a_agent.py` (بروتوكول Agent-to-Agent مع `api/v1/a2a.py` + `a2a_executor.py` + `a2a_utils.py`)؛ CrewAI (7 مكونات)؛ وكلاء `altk`, `cuga`, `codeagents` (smolagents CodeAct, Open DS Star)؛ مشاريع جاهزة: «Multi Agent Flow.json», «Sequential Tasks Agents.json», «Travel Planning Agents.json»؛ README يذكر «Multi-agent orchestration» صراحة |
| **MCP** | عميل + خادم | خادم: `agentic/mcp/server.py`, `api/v1/mcp.py`, `mcp_projects.py`, `api/v2/mcp.py`؛ عميل: مكوّن `models_and_agents/mcp_component.py`؛ `lfx/mcp/`؛ توثيق: `docs/docs/Agents/mcp-server.mdx`, `mcp-client.mdx`, `Components/mcp-tools.mdx`؛ README: «Deploy as an MCP server» |
| **RAG** | مدمج | `files_and_knowledge/` (ingestion, retrieval, knowledge)؛ `knowledge_bases/` + `api/v1/knowledge_bases.py` + `services/knowledge_base_storage/`؛ 21 مخزن متجهات؛ مشاريع جاهزة: «Vector Store RAG.json», «Hybrid Search RAG.json», «Document Q&A.json», «Knowledge Retrieval.json»؛ `bundles/datastax/graph_rag.py` (GraphRAG)؛ مقسمات نصوص `textsplitters`؛ docling لتقسيم المستندات |
| **البحث** | مدمج + خارجي | مدمج: `data_source/web_search.py`, `news_search.py`؛ أدوات: tavily, serp, google_search, searxng, wikipedia, wikidata, yahoo_finance؛ خارجي: 13+ مزود بحث (§4.4) |
| **القراءة/جلب المستندات** | مدمج + خارجي | مدمج: `data_source/url.py`, `api_request.py`, `csv/json_to_data.py`, `file.py`, `directory.py`؛ خارجي: firecrawl, apify, spider, scrapegraph, unstructured, docling, confluence, google_drive_fetch, sharepoint_fetch, youtube_transcripts |
| **التصميم** | نظام تصميم موثّق | `DESIGN.md` (نظام ألوان/طباعة/مكونات كامل: Inter + JetBrains Mono + Chivo، شبكة 4px، 14 لوناً لأنواع البيانات، وضع فاتح/داكن)؛ مجلد `design/` للتكاملات المخصصة؛ Storybook (`.storybook/`) |
| **الحماية** | طبقات متعددة | مصادقة: `services/auth`, `api/v1/login.py`, `api_key.py`، auto-login يُعطَّل افتراضياً في الإصدارات الرسمية (README/DEVELOPMENT)؛ تخويل دقيق: `services/authorization` + 8 موجهات `authz_*` (roles, teams, shares, capabilities, audit)؛ تدقيق: `services/audit`, `api/v1/audits.py`, `flows_audits.py`؛ تحديد المعدل: `services/rate_limit`؛ عزل نظام الملفات: `_filesystem_isolation.py`؛ حماية SSRF: `bundles/datastax/_ssrf.py`؛ سياسات: `model_provider_policy*`, `catalog_policy`, `policy_bundle`, `custom_component_policy`؛ حِراسات: `llm_operations/guardrails.py` + `guardrails_v2.py` + حزمة `toolguard` (6 مكونات)؛ فحص: codeql.yml, .secrets.baseline, .whitesource (Mend)؛ الإبلاغ: SECURITY.md عبر HackerOne/IBM |
| **المهارات (Skills)** | مهارات وكلاء ترميز | `.agents/skills/` — 11 مهارة SKILL.md (مراجعة backend/frontend، إعادة هيكلة المكونات، e2e، i18n، 4 مهارات وصولية IBM a11y) — موجّهة لوكلاء التطوير لا لمكونات المنتج |
| **الفيديو** | خارجي فقط | `lfx_bundles/twelvelabs/` (9 مكونات: فهرسة Pegasus، تضمينات فيديو/نص، تقسيم)؛ `lfx_bundles/youtube/` (7 مكونات)؛ heygen عبر Composio؛ لا معالجة فيديو أصلية مدمجة |
| **المال/الأسواق** | أدوات محدودة | `tools/yahoo_finance.py` + اختباره؛ عبر Composio: `finage_composio.py`, `fixer_composio.py` (عملات)؛ مشاريع جاهزة ذات طابع مالي: «Financial Report Parser.json», «Price Deal Finder.json», «SaaS Pricing.json»؛ **لا** يوجد مدفوعات/فوترة (لا stripe/payment/billing في الشجرة) |
| **الاستدلال/التوجيه** | مدمج | `llm_operations/` (llm_conditional_router, llm_selector, structured_output, batch_run)؛ `flow_controls/conditional_router.py`, `data_conditional_router.py`؛ `logic/`؛ `output_parsers/`؛ `agentics/` (amap/areduce/agenerate)؛ حلقات `flow_controls/loop.py` |
| **Human-in-the-loop** | مدمج | `api/v2/hitl.py`؛ مكوّن `flow_controls/human_input.py`؛ `flow_controls/listen.py`, `notify.py` |
| **المحفّزات والجدولة** | مدمج + خارجي | `triggers/` (webhook وschedule)؛ `api/v1/triggers.py`, `trigger_ingress.py`؛ `services/triggers/`؛ محفّزات Gmail/Calendar/Drive/Outlook/Slack/OneDrive في الحزم |
| **المراقبة والتتبع** | مدمج + خارجي | `services/tracing` (LangSmith, LangFuse حسب README)، `services/telemetry`, `observability*.py` في lfx، `api/v1/monitor.py`, `traces.py`؛ deploy: prometheus + grafana-loki؛ خارجي: langwatch |
| **الثغرات/الاعتبارات** | ملاحظات جرد | (1) مجلد `deactivated/` فيه 23 مكوّناً معطّلاً (دين تقني مرئي)؛ (2) ملف متبقٍّ محرر: `src/frontend/src/.routes.tsx.swp`؛ (3) ازدواج بنيوي أثناء الترحيل: المكونات موزعة بين lfx وبين bundles (أرشيف انتقالي موثّق في BUNDLE_API.md وscripts/migrate)؛ (4) auto-login مفعّل في فروع التطوير افتراضياً (موثّق، مقصود، لكنه خطر إن أُسيء نشره)؛ (5) `.secrets.baseline` يشير لتاريخ فحص أسرار — لم تُفحص نتائجه؛ (6) ملفات `.composio.lock` و`.whitesource` تكشف اعتمادات خارجية تحتاج إدارة |

### المشاريع الجاهزة (27 في `initial_setup/starter_projects/`)
Basic Prompting, Blog Writer, Content Aggregator, Custom Component Generator, Deep Research Agent, Document Q&A, Financial Report Parser, Hybrid Search RAG, Image Sentiment Analysis, Instagram Copywriter, Knowledge Retrieval, Market Research, Meeting Summary, Memory Chatbot, Multi Agent Flow, Portfolio Website Code Generator, Price Deal Finder, Research Translation Loop, SEO Keyword Generator, SaaS Pricing, Sequential Tasks Agents, Simple Agent, Social Media Agent, Text Sentiment Analysis, Travel Planning Agents, Twitter Thread Generator, Vector Store RAG.

---

## 6. مدمج (Built-in) مقابل تكامل خارجي

| مدمج في النواة | تكامل خارجي (حزم/واجهات) |
|---|---|
| محرك graph + workflow + API + MCP server | كل مزودي LLM الخارجيين (OpenAI, Anthropic, Google...) |
| الذاكرة المحلية (session/flow_context) وذاكرة المحادثة | mem0, zep, AstraDB chat memory, Redis/Upstash/Valkey |
| RAG محلي (ingestion/retrieval/KB) + FAISS/Chroma | 19+ مخزن متجهات سحابي |
| Voice Mode (WebSocket + واجهة) | funasr, AssemblyAI, ElevenLabs, Bolna, Plivo |
| الوكلاء الأساسيون + A2A + أدوات Python REPL/حاسبة | CrewAI, smolagents, altk, cuga, Composio (~70 أداة SaaS) |
| الحِراسات الأساسية guardrails v1/v2 | IBM toolguard |
| بحث ويب أساسي (web_search/news_search) | tavily, exa, serpapi, duckduckgo... |
| المحفّزات (webhook/schedule) | محفّزات Gmail/Outlook/Slack/Drive |
| التتبع الداخلي + telemetry | LangSmith, LangFuse, LangWatch |
| المتجر المدمج (store) لمشاركة التدفقات | Langflow Store الخارجي |

---

## 7. ما لا يوجد / خارج النطاق
- **لا مدفوعات أو فوترة أو إدارة اشتراكات** (لا ملفات payment/billing/stripe) — المنتج أداة OSS بلا طبقة تجارية داخلية.
- **لا تطبيق موبايل** — الواجهة ويب فقط + Langflow Desktop (مستودع منفصل، يُوزَّع كثنائيات).
- **لا معالجة فيديو/صوت أصلية** — تعتمد كلياً على مزودين خارجيين (TwelveLabs, AssemblyAI...).
- **لا تدريب/ضبط دقيق (fine-tuning) للنماذج** داخل الشجرة — استدلال فقط.
- **لا خط أنابيب بيانات ضخم داخلي** — التكامل مع Kafka عبر حزمة confluent فقط.
- **خارج نطاق هذه المرحلة**: قراءة محتوى الأكواد، تشغيل الاختبارات (1,162 + 593 + 295 ملف اختبار موجودة لكنها لم تُشغَّل)، فحص ثغرات فعلي، تقييم جودة التنفيذ.

---

## 8. المرشحون للتوسّع ولماذا
1. **`src/lfx/` (النواة)** — مرشح أول: إنها الحزمة المستقلة التي تنتقل إليها المكونات (توثيق LFX_MCP.md وPLUGGABLE_SERVICES.md)، وفهمها يفتح فهم كل شيء آخر؛ بها 593 اختباراً جاهزاً كمرجع سلوك.
2. **`src/lfx/src/lfx/components/` (182 مكوّناً)** — لأي استخراج/إعادة استخدام للمكونات؛ البدء بـ `models_and_agents/` و`files_and_knowledge/` و`llm_operations/` لأنها قلب الوكلاء وRAG.
3. **`src/backend/base/langflow/api/` + `services/`** — لمن يريد بناء منتج فوق الخادم: طبقة authz/audit/rate-limit النادرة في مشاريع مشابهة تجعلها صالحة مؤسسياً.
4. **`src/bundles/` كنموذج توسعة** — آلية حزم opt-in موثّقة (BUNDLE_API.md, PORTING.md, NIGHTLY.md) تسمح بإضافة مزودين جدد دون لمس النواة — المسار الأنظف لأي توسيع.
5. **Voice Mode + A2A + HITL** — قدرات حديثة (voice_mode.py, a2a_*, v2/hitl.py) قليلة الانتشار في البدائل، ومرشحة لتمايز تنافسي أو اقتباس التصميم.
6. **starter_projects (27 تدفقاً جاهزاً)** — أسرع طريق لفهم أنماط الاستخدام الحقيقية (RAG، وكلاء متعددون، أبحاث عميقة) قبل أي توسع.
7. **مناطق حذرة للتوسع**: `deactivated/` (23 مكوّناً) وملف `.routes.tsx.swp` والازدواج أثناء ترحيل lfx/bundles — يجب التحقق من وضعها قبل البناء عليها.

---

*أُنجز هذا الجرد آلياً من شجرة Git الكاملة للفرع main عند الالتزام `60999cc9a7350e44dde3ef641baae864e10861f0` مع قراءة الوثائق الرئيسية. لم يتم تشغيل أو اختبار أي مكوّن. الأعداد محسوبة من الشجرة مباشرة.*
