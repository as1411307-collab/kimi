
## 8. القوائم المرشحة للتوسع — اخترها برمزها

هذه ليست أمراً بالتنفيذ؛ هي فهارس مرشحة فقط. عندما تختار رمزاً، تكون الخطوة التالية قراءة الملفات والأكواد داخل ذلك المسار، واستخراج الأنماط والعقود والاختبارات، ثم الحكم على قابلية النقل.

### 8.1 Open Design

| الرمز | القائمة المختارة | لماذا أرشحها؟ | الأولوية |
|---|---|---|---|
| `OD-01` | `docs/architecture.md` + `docs/agent-adapters.md` + `apps/daemon/src/runtimes/` | لفهم فصل الواجهة عن الـdaemon، واكتشاف coding agents، وتوحيد streaming/cancel/resume | عالية للمعمارية |
| `OD-02` | `docs/skills-protocol.md` + `plugins/spec/SPEC.md` + `plugins/spec/AGENT-DEVELOPMENT.md` + `packages/plugin-runtime/` | لبناء نظام Skills/Plugins قابل للتحقق والتوسعة بدلاً من مجلدات prompts مبعثرة | عالية للمهارات |
| `OD-03` | `apps/daemon/src/media/` + `design-templates/hyperframes/` + `skills/video-hyperframes/` + `skills/speech/` + `prompt-templates/video/` | أفضل مسار مباشر لتوليد الفيديو والصوت والصور وفهم rendering والتكاملات الخارجية | عالية للفيديو والصوت |
| `OD-04` | `apps/daemon/src/api-token-auth.ts` + اختبارات SSRF/auth في `apps/daemon/tests/` + `packages/contracts/src/api/artifact-lint.ts` + `e2e/` | أنماط حماية وحدود وصلاحيات وlint واختبارات قبل قبول المخرجات | عالية للحماية والتدقيق |
| `OD-05` | أسماء محددة من `skills/` و`design-templates/` و`design-systems/`، لا المكتبة كلها دفعة واحدة | 169 مهارة و115 قالباً و152 نظام تصميم؛ الاختيار الانتقائي أسرع وأنفع من النسخ الشامل | حسب قسم التصميم |

### 8.2 Awesome LLM Apps

| الرمز | القائمة المختارة | لماذا أرشحها؟ | الأولوية |
|---|---|---|---|
| `AW-01` | `advanced_llm_apps/llm_apps_with_memory_tutorials/` + `advanced_llm_apps/chat_with_X_tutorials/` + دروس memory/sessions في `ai_agent_framework_crash_course/` | 7 نماذج ذاكرة و7 تطبيقات Chat with X ودروس sessions؛ تغطي المحادثة والحالة والذاكرة المشتركة | عالية جداً |
| `AW-02` | `rag_tutorials/` + `ai_deep_research_agent` + `ai_domain_deep_research_agent` + `multi_agent_researcher` + `ag2_adaptive_research_team` | 24 مسار RAG مع بحث محلي وهجين وتصحيحي ومتعدد الوسائط وKnowledge Graph وتشخيص الأعطال | عالية جداً للبحث والقراءة |
| `AW-03` | `mcp_ai_agents/` + `agent_skills/` + `ai_agent_framework_crash_course/` + `multi_mcp_agent_router` | موصّلات MCP، و8 مهارات مع evals، و21 درساً في التنسيق والتفويض والحواجز والمراقبة | عالية جداً للمعمارية |
| `AW-04` | `multi_agent_trust_layer` + `trust_gated_agent_team` + `ai_agent_governance` + `agent_skills/dependency-doctor` + `always_on_agents/release_radar_agent` | أنماط الثقة والحوكمة وسلسلة الإمداد وسجل التدقيق؛ مفيدة للحماية الدفاعية لا للهجوم | عالية للحماية |
| `AW-05` | `voice_ai_agents/` + `ai_news_and_podcast_agents` + `ai_blog_to_podcast_agent` + `ai_speech_trainer_agent` + درس `11_voice` | أربعة وكلاء صوت ونماذج Podcast وتحويل الكلام إلى موجز؛ مسار صغير ومتماسك | عالية للصوت |
| `AW-06` | `ai_finance_agent_team` + `ai_financial_coach_agent` + `ai_investment_agent` + `ai_personal_finance_agent` + `ai_vc_due_diligence_agent_team` + `earnings_call_analyst_agent` + `ai_fraud_investigation_agent` | تغطي التحليل والاستثمار والميزانية وVC والأرباح والاحتيال؛ أمثلة بداية لا مصدر بيانات موثوق تلقائياً | عالية للمال |
| `AW-07` | `multimodal_coding_agent_team` + `ai_codebase_migration_agent` + `ai_seo_audit_team` + `llm_panel_agent_team` + `dependency-doctor` + `scope-creep-detector` + `commit-archaeologist` + `self-improving-agent-skills` | بناء وتدقيق ومراجعة جماعية وفحص اعتماديات وتاريخ الكود وتحسين المهارات | عالية للبرمجة والتدقيق |
| `AW-08` | `generative_ui_agents/` + `multimodal_design_agent_team` + `multimodal_uiux_feedback_agent_team` + `excaliflow/` | واجهات تفاعلية ولوحات وMCP Apps ونقد تصميم ورسم معماري متحرك | عالية للتصميم |
| `AW-09` | `advanced_llm_apps/multimodal_video_moment_finder/` + `chat_with_youtube_videos` + `multimodal_ai_agent` + `excaliflow/` | فهم الفيديو واستخراج اللحظات والمحادثة معه وتصدير رسم متحرك؛ ليس بديلاً عن HyperFrames | متخصصة للفيديو |
| `AW-10` | `always_on_agents/` + `llm_optimization_tools/` + `llm_finetuning_tutorials/` | جدولة ومراقبة استباقية، ثم خفض السياق والتكلفة، ثم fine-tuning عند الحاجة فقط | متوسطة/متخصصة |

### 8.3 Langflow

| الرمز | القائمة المختارة | لماذا أرشحها؟ | الأولوية |
|---|---|---|---|
| `LF-01` | `docs/docs/Agents/` + `src/backend/base/langflow/api/` + `src/lfx/src/lfx/components/` + ملفات MCP الحالية في `docs/docs/` | نواة agents/workflows وتحويلها إلى API وMCP وربط الأدوات والمكونات | عالية جداً للنواة |
| `LF-02` | `docs/docs/Develop/memory.mdx` + `memory-bases.mdx` + `docs/docs/Components/` + `src/backend/base/langflow/base/memory/` + مكونات retrieval/vector stores | الذاكرة والمعرفة وRAG ورسائل المحادثة وقواعد البيانات المتجهية | عالية جداً للذاكرة والبحث |
| `LF-03` | `src/backend/base/langflow/api/v1/voice_mode.py` + `src/backend/base/langflow/utils/voice_utils.py` + مكونات voice في `src/frontend/` + `docs/docs/Develop/concepts-voice-mode.mdx` | تنفيذ voice mode فعلياً مع واجهة واختبارات وصلاحيات، لا مجرد اسم تكامل | عالية للصوت |
| `LF-04` | `SECURITY.md` + `docs/docs/Develop/authentication-overview.mdx` + `api-keys-and-authentication.mdx` + `authorization.mdx` + `src/backend/tests/` | المصادقة والصلاحيات ونطاقات الجلسات والاختبارات؛ ضرورية قبل مشاركة الأقسام أو نشرها | عالية للحماية |
| `LF-05` | `docker/` + `deploy/` + `DEVELOPMENT.md` + `DESIGN.md` + `BUNDLE_API.md` + `src/frontend/` + `regressions/` | التشغيل والنشر والواجهة وحدود الحزم والانحدارات؛ يفيد قسم الأنظمة والبناء | عالية للأنظمة |
| `LF-06` | `src/lfx/src/lfx/components/tools/yahoo_finance.py` + `starter_projects/Financial Report Parser.json` + `src/bundles/lfx-bundles/src/lfx_bundles/twelvelabs/` + `youtube/` | مكونات مالية وفيديو جاهزة كتكاملات؛ تُراجع بعد الأساس لا قبله | متخصصة للمال والفيديو |

### 8.4 Ollama

| الرمز | القائمة المختارة | لماذا أرشحها؟ | الأولوية |
|---|---|---|---|
| `OL-01` | `api/` + `server/` + `openai/` + `anthropic/` + `docs/openapi.yaml` | عقود REST وOpenAI وAnthropic وإدارة النماذج والجدولة؛ هي نقطة ربط المنظومة بالنماذج | عالية جداً |
| `OL-02` | `cmd/speech.go` + `server/speech.go` + `server/transcription.go` + `llm/speech.go` + `docs/capabilities/speech.mdx` + `integration/audio_test.go` | مسار speech/transcription حقيقي مع اختبارات؛ لا حاجة لتخمين بنية الصوت | عالية للصوت |
| `OL-03` | `model/parsers/` + `model/renderers/` + `thinking/` + `tools/` + `llm/gbnf.go` + `mlxrunner/xgrammar/` | tool calling وthinking وStructured Outputs وقوالب عائلات النماذج؛ مهم لاستقرار الوكلاء | عالية جداً |
| `OL-04` | `openai/responses_compact.go` + `server/responses_compact.go` + `app/store/` + `middleware/web_search.go` + `app/tools/` | ضغط السياق وتخزين محادثات التطبيق والبحث والجلب والزحف؛ مكملات للذاكرة والبحث لا بديل عنهما | عالية للمحادثة والبحث |
| `OL-05` | `cmd/launch/` + `internal/proxy/` + `docs/integrations/` | أنماط ربط coding agents والتطبيقات الخارجية مع الحفاظ على حدود runtime | عالية للتكاملات |
| `OL-06` | `llm/` + `llama/` + `mlxrunner/` + `discover/` + `create/` + `compatmigrate/` + `integration/` | الأداء والعتاد والتحويل والتكميم والمحرك منخفض المستوى؛ لا تبدأ به إلا إذا كان هدفك تعديل runtime نفسه | متخصصة جداً |

### 8.5 ترتيبي المقترح عند اختيار أقل عدد يعطي أوسع تغطية

1. **النواة والعقود:** `LF-01` + `OL-01` + `OL-03`.
2. **الذاكرة والبحث والقراءة:** `AW-01` + `AW-02` + `LF-02` + `OL-04`.
3. **المهارات وتعدد الوكلاء والحماية:** `AW-03` + `AW-04` + `OD-01` + `OD-02` + `OD-04` + `LF-04`.
4. **الأقسام المتخصصة:** `AW-05` للصوت، `AW-06` للمال، `AW-07` للبرمجة والتدقيق، `AW-08` للتصميم، `OD-03` للفيديو.
5. **التشغيل والتكاملات:** `LF-05` + `OL-02` + `OL-05`.

### 8.6 ما لا أرشح البدء به

- `docs/versioned_docs/` في Langflow: نسخ تاريخية مكررة؛ ابدأ بـ`docs/docs/` الحالية، وارجع للتاريخ عند الحاجة فقط.
- كل الفروع الـ6,020 أو مقارنة كل الإصدارات: ابدأ بـ`main`، ثم اختر فرعاً محدداً لسبب واضح.
- جميع Design Systems والقوالب والأمثلة دفعة واحدة: اختر ما يخدم القسم المطلوب لتجنب مئات الملفات المتكررة.
- الصور والأصول الثابتة و`.github/screenshots/` و`docs/gallery/`: مفيدة للعرض لا لاستخراج معمارية الوكلاء.
- `mlxrunner/` و`llm/` و`create/` في Ollama قبل فهم API: قوية لكنها منخفضة المستوى، وتستهلك وقتاً بلا فائدة مباشرة لمنسّق الأقسام.
- الروابط الخارجية المذكورة في README ولا توجد داخل شجرة المستودع: ليست جزءاً من هذا الجرد وتحتاج جرداً مستقلاً إن اخترتها.
- أي مشروع طبي أو تأميني أو مالي بوصفه جاهزاً للاستخدام الحقيقي: هي أمثلة تحتاج مراجعة بيانات وحدود واختبارات ومسؤولية مهنية.

**طريقة الاختيار للمرحلة الثانية:** أرسل الرموز فقط، مثل: `AW-01 + AW-02 + LF-01 + OD-03 + OL-02`، وسأتوسع في تلك القوائم وحدها.
