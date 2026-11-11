# إثراء الجمع من Hermes وComposio وإضافاتها

**الهدف:** استخراج ما يغني الملفات السابقة ويضيف قدرات إلى معمارية `Langflow + Ollama + Open Design` دون فقدان نتائجها.

**المنهج:** جرد المصدر والمسارات والتراخيص ونسخ انتقائي. **لم تُنفّذ اختبارات تشغيل أو قبول**؛ لذلك كل تصنيف هنا يخص ما هو موجود في المصدر، وليس إثبات نجاح تشغيل أو إنتاج.

## 1. اللقطات المثبتة

| المستودع | الفرع | Commit | الترخيص الظاهر |
|---|---|---|---|
| `NousResearch/hermes-agent` | `main` | `b7db40d82568ea68ce321ac1ead3bfea354c7f56` | MIT |
| `ComposioHQ/composio` | `next` | `e7c4aac1e3b1fd05019d17a6e1010891c0917e6e` | MIT |
| `ComposioHQ/trustclaw` | `main` | `9a60c563711ee17687d0a60d34901417162ad531` | MIT |
| `ComposioHQ/helm-charts` | `release-stable` | `c6ea94c82fc0fd6eca73cab7b9ce5c0ef04f7a8c` | MIT |
| `ComposioHQ/awesome-claude-skills` | `master` | `be2a406907dbc61b73e6827ded415c96139d13a2` | راجع ملف `LICENSE.txt` داخل كل مهارة |
| `NousResearch/hermes-agent-self-evolution` | `main` | `0a929e3aa20e15cf04dc7c28492a7d41a5139125` | **لا يوجد LICENSE في الجذر — وثائق فقط** |

## 2. ما الذي يضيف فعلاً إلى الجمع؟

| الإضافة | دورها المحتمل | مكانها في المعمارية الحالية | حدودها |
|---|---|---|---|
| **Hermes** | الذاكرة والمهارات والتعلم من الخبرة والتنفيذ والبحث والقنوات والجدولة | مصدر أنماط ومكونات اختيارية أو runtime مستقل عند الحاجة؛ لا يستبدل Langflow تلقائياً | يحتاج نموذجاً وضبطاً أمنياً وتشغيلاً منفصلاً؛ ليست كل أدواته محلية |
| **Composio** | OAuth وإدارة الاتصالات والحسابات وtool discovery وMCP وtool execution | بوابة أدوات خارجية خلف Policy Gateway، مع user scoping وموافقة وعزل أسرار | يعتمد خدمة Composio المدارة وOAuth والحسابات الخارجية؛ ليس طبقة محلية مجانية بالكامل |
| **TrustClaw** | مرجع لتطبيق وكيل شخصي: ذاكرة pgvector وقنوات وcron وrate limits وaudit وOAuth | أنماط تُنقل إلى Langflow/Open Design، لا حاجة لتشغيله كمنصة ثانية | يعتمد Vercel AI Gateway وComposio وخدمات أخرى؛ ليس Offline |
| **Helm Charts** | نشر Composio على Kubernetes مع secrets وRBAC وobservability وخدماته | قوالب نشر انتقائية للحاويات والصلاحيات ومراقبة المنظومة | معقد وقد يتطلب Enterprise/مكونات خارجية؛ ليس مساراً مبسطاً للتطبيق كله |
| **Awesome Claude Skills** | مهارات جاهزة للبحث والبناء والتدقيق والمستندات وMCP/Rube | مكتبة محتوى مهارات تُراجع وتُثبت انتقائياً في Hermes/Open Design أو agents أخرى | ليست كل مهارة آمنة أو محلية؛ يجب فحص LICENSE والمصدر والتعليمات والأدوات |
| **Self-Evolution** | نمط تقييم وتحسين المهارات والبرومبتات والكود عبر DSPy + GEPA | وثائق مرجعية لبناء evals وتحسين المهارات، لا كود منسوخ | لا يوجد LICENSE في الجذر؛ يمنع إعادة استخدام الكود حتى يتضح الترخيص |

## 3. قاعدة الجمع المحفوظة

تبقى القاعدة كما هي:

1. **Ollama:** model runtime محلي.
2. **Langflow:** orchestration وworkflows وRAG وRBAC وMCP وHITL.
3. **Open Design:** التصميم والمهارات وHyperFrames ومساحة العمل، مع OpenCode + Ollama للمسار المحلي.
4. **Awesome LLM Apps:** أنماط مستقلة تُنقل انتقائياً بعد الإصلاح، لا تشغيل 144 مشروعاً.
5. **Open Design ↔ Langflow:** لا تكامل أصيل مثبت؛ يلزم اختبار OpenAI Responses أو MCP.

**النواة المحفوظة:** `Ollama + Langflow + Open Design + Awesome patterns`.
**الربطان المثبتان:** `Langflow + Ollama` رسمي، و`Open Design + Ollama + OpenCode` عبر BYOK. لا تغيّر الإضافات الجديدة هذين المسارين.

الإضافات الجديدة اختيارية ولا تغيّر هذه القاعدة: **Hermes للتعلم والمهارات، Composio للأدوات وOAuth، TrustClaw للأنماط التشغيلية، Helm للنشر، Skills كمحتوى، Self-Evolution كوثائق تقييم فقط.**

## 4. الجرد التفصيلي والملفات المختارة للنسخ

### 4.1 Composio — ما يمكن نقله وما هو SaaS

**النتيجة الرئيسية:** المستودع SDK وCLI ووثائق ومحوّلات، وليس خادماً محلياً لـTool Router أو تخزين التوكنات أو sandbox. وظائف `backend.composio.dev` ليست قابلة للاستضافة من هذا المستودع.

| الحالة | المكونات | كيف تفيد الجمع؟ |
|---|---|---|
| **REAL — كود عميل قابل للنسخ / DEMO — نضج تجريبي** | `Sessions.ts`, `ToolRouter*`, `SessionContext`, `BaseProvider`, `typesafe`, `langchain`, `OpenAIProvider`, modifiers، local custom tools، CLI keyring، `experimental/src/workbench` | عقود جلسة ومحوّلات وتعديل سلوك وعزل مفاتيح وworkbench تجريبي. يمكن استخدامها داخل تطبيقاتنا مع بقاء التنفيذ الخارجي عند استخدام Composio |
| **REAL — حماية واستئناف** | `toolRouterMcp.ts`, approvals و`requestState` و`inputResponses`, tool hints, token-custody docs, rate-limit docs | منع تسريب ترويسات MCP إلى origin مختلف، عدم اتباع redirects، وموافقة المستخدم قبل الأفعال الحساسة مع حالة استئناف معتمة |
| **EXTERNAL — خادم Composio** | Tool Router sessions، OAuth/token custody، semantic tool search، meta tools execution، hosted MCP، remote sandbox، triggers/firewall/Instant | تُستخدم كخدمة اختيارية خلف Policy Gateway، لا كمكون محلي. تحتاج API key وإدارة تكلفة ومصدر بيانات وصلاحيات |
| **DEMO/تجريبي** | `examples-manifest.json` | أمثلة وواجهات اختبار، لا ضمان إنتاج |

**أفضل ما نُسخ من Composio:**

- `ts/packages/core/src/models/{Sessions,ToolRouter,ToolRouterSession,SessionConfigs,SessionContext}` — نمط جلسة مرتبطة بمستخدم وأدوات وحالة.
- `ts/packages/core/src/lib/toolRouterMcp.ts` — حارسة وجهة MCP والترويسات ومنع redirect.
- `BaseProvider` و`typesafe` و`langchain` — محوّلات لـOllama/OpenAI-compatible وLangflow/LangChain وOpen Design/custom provider.
- `experimental/src/workbench` — نمط workbench ذاتي الاستضافة، مع بقاء أدوات Composio خارجية.
- `python/composio/core/models/_modifiers.py` و`modifiers.types.ts` — قبل/بعد تعديل schema والمدخلات والمخرجات في العميل.
- `docs/security/token-custody.mdx`, `governance/approvals.mdx`, `docs/reference/v3/rate-limits.mdx`, `meta-tools/*`, `custom-providers/*`.

**قواعد الربط الآمن:**

1. `user_id` يُشتق من جلسة backend موثقة، لا من نص واجهة أو نموذج. حسابات toolkit المتعددة تبقى تحت نفس `user_id` ولا تستخدم `default` في الإنتاج.
2. `tool search → get schemas → approval/HITL → multi_execute` مع snapshot للسكيمة والموافقة؛ لا تثبيت ثابت لأن schemas تتغير.
3. `openai` أو `typesafe` لـOllama، و`langchain` أو hosted MCP لـLangflow، و`custom provider` لـOpen Design. هذه واجهات ربط وليست ضمان توافق جاهز.
4. Composio خيار خارجي فقط. البديل المحلي للأدوات الحساسة يبقى داخل Langflow/OpenCode مع allowlist وأسرار محلية.
5. راجع `Retry-After` و`X-RateLimit*` ولا تخلط حدود Composio مع حدود Google أو المزودين الآخرين.

**الترخيص:** الجذر MIT، لكن حزم TypeScript تعلن ISC وحزمة Python تعلن Apache-2.0. نُسخ `core-package.json`, `typesafe-package.json`, `langchain-package.json`, `python-pyproject.toml` لضمان الإسناد الصحيح لكل ملف.

### 4.2 Awesome Claude Skills — انتقاء بدلاً من النسخ بالجملة

- المستودع يضم **32 مهارة مستقلة + 832 مهارة Rube/Composio مولّدة**. لم تُنسخ الـ832؛ اختيرت تطبيقات قليلة ذات صلة فقط.
- **Apache-2.0 موثق:** نُسخت كاملة مع السكربتات والقوالب: `webapp-testing`, `artifacts-builder`, `internal-comms`, `theme-factory`, `brand-guidelines`, `canvas-design`, `slack-gif-creator`، إضافة إلى `mcp-builder` و`skill-creator` ومراجعهما.
- **ترخيص غير مؤكد:** نُسخ نص `SKILL.md` فقط كمرجع: `content-research-writer`, `invoice-organizer`, `video-downloader`, `changelog-generator`, `langsmith-fetch`, `developer-growth-analysis`, `file-organizer`, `meeting-insights-analyzer`.
- **Rube/Composio:** اختيرت `tavily`, `firecrawl`, `algolia`, `virustotal`, `quickbooks`, `xero`, `alpha-vantage`, `heygen`, `elevenlabs`. هذه خارجية وليست أدوات محلية، ولا يوجد لها ملف ترخيص خاص في الحزمة.
- **مستبعد:** `document-skills/docx/pdf/pptx/xlsx` لأنها شروط تجارية لـAnthropic وليست مفتوحة المصدر. كما أن قسم Security & Systems في README روابط خارجية لا كود محلي، ولا توجد مهارة RAG صريحة أو vector DB في `composio-skills`.

### 4.3 Hermes Agent Self-Evolution — وثائق تقييم فقط

- `pyproject.toml` يعلن MIT لكن **لا يوجد ملف LICENSE في الجذر**. لذلك لم يُنسخ كود من `evolution/`؛ نُسخت `README.md`, `PLAN.md`, `pyproject.toml`, `phase1-demo-report.pdf` فقط كمراجع.
- النمط المفيد: `SKILL.md` كمعامل تحسين في `dspy.Module`، و`GEPA` مع تراجع إلى `MIPROv2`، وبيانات synthetic/sessiondb/golden بتقسيم 50/25/25، وفلتر أسرار للجلسات، وروبرك وصفي بدل expected text حرفي، ولياقة correctness/procedure/conciseness مع غرامة طول.
- البنشماركات **بوابات نشر** لا مجرد fitness: اختبارات وسلامة frontmatter وحدود حجم ودلالة وprompt-caching ومراجعة بشرية عبر PR.
- نتيجة Phase 1 (+20.7% على مثالي holdout) **DEMO** ولا تعمم؛ لا تستخدم كدليل جاهزية أو تحسين إنتاجي.

### 4.4 Hermes Agent — الذاكرة والمهارات والتنفيذ والحدود الأمنية

**المعمارية:** Hermes يقدّم وكيلاً شخصياً واحداً عبر CLI وTUI وElectron وقنوات مراسلة. التوسعة تكون عبر **plugins وskills** لا بتضخيم النواة، مع facade ووحدات موضوعية مستقلة (`run_agent.py`, `agent/turn_*.py`, `hermes_state*`, `model_tools.py`, `gateway/`, `cron/`).

**الأرقام المفيدة من الشجرة:** 44 مهارة في `skills/`، و141 في `optional-skills/`، و66 كتالوج في `optional-mcps/`، و19 مجلد plugin، و39 مجلد evals. هذه أرقام محتوى وليست ضمان جودة أو تشغيل.

| المحور | ما يمكن الاستفادة منه | الملفات المنسوخة |
|---|---|---|
| الذاكرة والمهارات | memory providers، إنشاء المهارات، optional skills، progressive disclosure، تفويض subagents | `website/docs/developer-guide/{memory-provider-plugin,creating-skills}.md`, `website/docs/user-guide/features/{memory,skills}.md`, `optional-skills-catalog.md`, `skills-catalog.md` |
| السياق والتكلفة | prompt caching كقيد تصميم، compression عند الحاجة فقط، منع تبديل toolsets/الذاكرة أثناء المحادثة | `website/docs/developer-guide/context-compression-and-caching.md`, `AGENTS.md` |
| التنفيذ والعزل | terminal backend للأوامر، لكن **Whole-process wrapping مطلوب للمدخلات غير الموثوقة** لأن plugins/skills/code execution/MCP قد تتجاوز shell sandbox | `SECURITY.md`, `website/docs/developer-guide/terminal-environment-plugin.md` |
| النموذج المحلي | custom OpenAI-compatible endpoint بلا مفتاح مع Ollama | `website/docs/integrations/providers.md` |
| مهارات متخصصة | Chroma/FAISS للذاكرة المتجهية، evaluation وDSPy، DCF/comps/3-statement للمال، MCP OAuth gateway، container supervision، adversarial UX، HyperFrames، OpenCode | `hermes/المهارات-المختارة/` |

**كود Hermes المنسوخ أيضاً:** `hermes/النواة-المزودة/` (مزود Ollama ومعايرة السياق)، `hermes/الذاكرة-والسياق/` (الذاكرة والضغط)، `hermes/الأدوات-والتنفيذ/` (السجل والبيئة والموافقات والمنصة)، `hermes/الموافقة-والتفويض/` (subagents)، `hermes/الجدولة-والبحث/` (cron وFTS5)، و`hermes/acp_adapter/` (ربط Agent Client Protocol للمحررات). كلها تحت رخصة MIT مع إشعارها. مسار ACP مسموح لأنه واجهة محرر مفتوحة؛ استُبعدت واجهات Electron/TUI/Desktop وقنوات messaging الـ26 فقط.

**ضبط Ollama لـHermes:** الوثائق تشترط `context_length ≥ 64,000` للجلسة النشطة. تُضبط القيمة على خادم Ollama (`OLLAMA_CONTEXT_LENGTH`) أو في Modelfile، **لا عبر OpenAI-compatible API**. وضع parallel slots يقسم الذاكرة؛ ارفعها بحيث لا تنخفض الجلسة النشطة عن الحد المطلوب.

**حدود الحماية:** سياسة Hermes تقول إن **العزل الحقيقي على مستوى OS**، وليس approval gate أو redaction أو tool allowlist. plugins وskills المحملة داخل العملية لها صلاحيات الوكيل نفسه، لذلك يجب مراجعة Python/scripts لا قراءة `SKILL.md` فقط. وكل سطح شبكة يحتاج caller allowlist؛ session ID ليس تصريح وصول. وكذلك Hermes **single-tenant** ولا يقدم per-caller capabilities؛ استخدم نسخاً منفصلة عند الحاجة للفصل.

### 4.5 TrustClaw وHelm — الذاكرة والتشغيل والنشر

**TrustClaw** مرجع لتطبيق وكيل شخصي حقيقي: Next.js/tRPC/Better Auth/Prisma+Postgres+pgvector/Redis/Vercel AI SDK/Composio. لكنه **ليس Offline**: يحتاج Composio وVercel AI Gateway وقاعدة البيانات، والتنفيذ في remote sandbox.

**أنماط تفيد Langflow/Open Design:**

- `memory-search.ts` و`memory-save.ts`: حفظ واسترجاع الذاكرة.
- `context-pruning.ts`, `context-window.ts`, `build-context.ts`, `token-estimation.ts`: إدارة السياق والرموز.
- `memory-flush.ts` و`run-compaction.ts`: ثلاثية pruning → memory flush → summarization compaction.
- `rate-limit.ts`: حدود per-user لـchat/cron/Telegram مع fail-mode واضح و`REDIS_URL`.
- `glen.ts`: نمط ذاكرة فريق اختيارية لكل مستخدم، مرتبطة بمفاتيحه ومنظمة مستقلة، لا ذاكرة مشتركة مفتوحة.
- `cron-execute-route.ts`, `schema.prisma`, `env.example`, `vercel.json`: الجدولة والنشر والإعداد.
- `setup.ts`, `system-prompt.ts`: إعداد الوكيل وحدود system prompt.

**حدود TrustClaw:** يحتاج Composio وVercel AI Gateway وPostgres+pgvector. خطة Vercel Hobby تقيد cron يومياً ومدة function إلى 300 ثانية؛ لذلك لا تعتبره مسار Offline أو إنتاج مجاني دائم. مكانه في الجمع **أنماط مرجعية، لا منصة ثانية**.

**Helm Charts** يضيف قوالب نشر Composio على Kubernetes: `Chart.yaml`, `values-DEVELOPMENT-NOT-PRODUCTION.yaml`, `example-values.yaml`, `_helpers.tpl`, `secrets.md`. ركّز على secrets وRBAC وhealth/status informers وvalues للخدمات `apollo/thermos/mercury/frontend/database` لا على نسخ كل dependencies التاريخية. Commit الحالي يتضمن تقييد صلاحيات Replicated SDK لقراءة الأسرار، وهو مرجع أفضل من إعداد عام قديم.

**حدود Helm:** النشر معقد وقد يتطلب Enterprise ومكونات خارجية. لا تعتبره حزمة «تشغيل كله بلا خادم» ولا تنقل values بأسرار أو سياسات غير مدقوقة. **Knative ClusterRole بصلاحيات `*` على `default` لم يُنسخ، و`TEST_DEBUG=true` وWeaviate anonymous ليسا إعداد إنتاج.** ملف `postgres-init-job.yaml` يحتاج `IF NOT EXISTS` قبل الاستخدام.

**حدود أخرى موثقة:** `prisma/migrations` غير موجود في لقطة TrustClaw؛ المتوفر `schema.prisma` و`prisma.config.ts`. تكامل `glen-UNKNOWN.ts` مصنّف UNKNOWN ونسخ كمرجع فقط. لا يوجد audit immutable مستقل؛ المطلوب جدول `AuditEvent` مستقل مع actor/user/session/tool/action/input-hash/result-status/timestamp بدلاً من الاعتماد على `Message.content` فقط.

## 5. ما تم نسخه فعلياً والتحقق منه

تم نسخ **395 ملفاً** في حزمة `حزمة_إثراء_الجمع` مع manifest يثبت المستودع والـcommit والترخيص والحجم وSHA-256 لكل ملف:

- **Hermes:** مزود Ollama المخصص، معايرة `num_ctx`، ضغط السياق والمسارات، FTS5/session recall، الذاكرة وعزل scope، delegation، execution/approval، cron، ACP، ومهارات Chroma/FAISS/evaluation/DSPy/finance/MCP-OAuth/devops/adversarial UX/HyperFrames/OpenCode.
- **Composio:** Sessions وToolRouter وProviders وModifiers وMCP origin guard وworkbench التجريبي، ووثائق custody/approvals/rate limits/meta tools/custom providers، وملفات إثبات تراخيص الحزم المختلفة.
- **TrustClaw:** مخطط Prisma وmemory/context/compaction وrate limiting وcron وBetter Auth/tRPC/Better Auth route وNext config وstream store وTelegram وملفات env.
- **Helm:** قوالب OTel/PDB/Ingress/Deployment/ServiceAccounts/values-managed-vpc، مع استبعاد Knative والصور الخاصة والأنماط غير الآمنة.
- **Skills:** مهارات Apache-2.0 كاملة، ومهارات نصية أخرى تحت `ترخيص-غير-مؤكد` و`composio-rube` بدلاً من نسخ 832 مهارة بالجملة.
- **Self-Evolution:** وثائق `README`, `PLAN`, `pyproject`, `phase1_validation_report.pdf` فقط، بلا كود `evolution/`.

### التحقق المنجز دون اختبارات

1. تطابق كل ملف منسوخ مع SHA-256 المسجل في manifest.
2. لا ملفات Knative أو document-skills التجارية أو كود Self-Evolution غير المرخص.
3. لا علامات على أسرار حقيقية في الحزمة النصية.
4. `values-DEVELOPMENT-NOT-PRODUCTION.yaml` موسوم بوضوح كإعداد غير إنتاجي، مع ملف استبعادات أمنية وترخيصية مستقل.
5. `prisma/migrations` لم يوجد في اللقطة، ولم يُدّعَ وجوده.
6. الحزمة النصية الكاملة تحتوي 395 سجلاً لملفات المصدر ومحتواها وSHA-256، مع الدليل والاستبعادات والفهرس.

### الملفات النهائية

- `دليل_إثراء_الجمع.md`: هذا الدليل.
- `حزمة_إثراء_الجمع_الكاملة.txt`: الحزمة النصية الكاملة مع محتوى الملفات ومصدرها.
- `manifest-إثراء-الجمع.json` و`manifest-إثراء-الجمع.txt`: الفهرس الآلي والنصي للهاش.
- `حزمة_إثراء_الجمع/`: الملفات المنسوخة مصنفة مع التراخيص والاستبعادات.
- `ملخص_إثراء_الجمع.png`: خريطة مرئية للإضافات.
- `إثراء_الجمع.kanva.pptd`: النسخة القابلة للتحرير من الخريطة.

**النتيجة:** إضافات Hermes وComposio وTrustClaw وHelm وSkills أصبحت مواد قابلة للتكييف مع الجمع الحالي، مع فصل واضح بين ما هو كود عميل وما هو SaaS وما هو DEMO وما هو غير مؤكد الترخيص. لا يوجد ادعاء تشغيل أو إنتاج.
