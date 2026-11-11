
## 3.5) خريطة الوحدات التي تهم بناء الوكلاء

### أ) API والخادم والسياق

- `api/types.go` و`api/client.go`: عقود Generate وChat وEmbed وShow وPull/Push وCreate وList وPS وVersion وأنواع Tool/ToolCall، مع أمثلة في `api/examples/`.
- `server/routes.go` و`server/sched.go`: نقاط API وجدولة تحميل/تفريغ النماذج والتوازي.
- `openai/openai.go`: توافق Chat Completions؛ `openai/responses*.go`: توافق Responses API والأدوات والأخطاء.
- `openai/responses_compact.go` و`server/responses_compact.go`: ضغط/تلخيص سياق المحادثة لـResponses API؛ مفيد لإدارة السياق، لكنه ليس ذاكرة معرفية طويلة الأمد.
- `anthropic/`: توافق Anthropic Messages API مع thinking، و`middleware/` يربط التوافق والمقاييس والبحث وthinking.

### ب) الصوت والكلام

- `cmd/speech.go`: واجهة CLI للصوت.
- `server/speech.go` و`server/transcription.go`: مسارا speech وtranscription في الخادم.
- `llm/speech.go` و`llm/llama_server_speech.go`: ربط الصوت بمحرك الاستدلال.
- `mlxrunner/speech.go` و`mlxrunner/client_speech.go` و`mlxrunner/model/audio/`: دعم الصوت داخل runner ومعالجة النماذج.
- `model/renderers/audio.go` و`model/renderers/speech.go` و`model/parsers/lfm3audio.go`: rendering/parsing للوسائط الصوتية.
- `docs/capabilities/speech.mdx` و`integration/audio_test.go`: التوثيق واختبار التكامل. لم أشغّل الاختبار.

### ج) المحادثة والذاكرة والتخزين

- `app/store/database.go` و`app/store/schema.sql`: SQLite محلي لتطبيق سطح المكتب، ومنه تخزين محادثات/إعدادات التطبيق.
- `readline/history.go`: تاريخ إدخال الطرفية.
- `mlxrunner/prefix_cache.go` و`mlxrunner/cache/`: KV/prefix cache لإعادة استخدام بادئات المحادثة؛ ذاكرة تشغيلية قصيرة، لا ذاكرة مستخدم دلالية.
- `server/sched.go`: slots وجلسات الاستدلال، لا ملف تعريف مستخدم طويل الأمد.
- الخلاصة: توجد لبنات سياق وتخزين محلي، لكن **لا يوجد نظام ذاكرة وكيل طويلة المدى أو ذاكرة متجهية مدمج**.

### د) البحث والقراءة والجلب

- `middleware/web_search.go`: بحث ويب كأداة ضمن مسار Responses.
- `app/tools/web_search.go` و`app/tools/browser_websearch.go`: أدوات بحث للتطبيق.
- `app/tools/browser.go` و`app/tools/browser_crawl.go` و`app/tools/web_fetch.go`: تصفح وزحف وجلب URL.
- `app/tools/url_policy.go` و`app/tools/cloud_policy.go`: سياسات URL والسحابة حول هذه الأدوات.
- `docs/capabilities/web-search.mdx` و`middleware/responses_web_search_test.go`: التوثيق والاختبار.
- الحد: لا يوجد فهرس بحث محلي/متجهي أو محلل PDF مدمج؛ هذه أدوات وصول وبحث، لا نظام RAG كامل.

### هـ) الوكلاء والتكاملات

- `cmd/launch/`: مشغّلات Claude Code وClaude Desktop وCodex وCodex App وCopilot وCline وDeepSeek Harness وDroid وHermes وKimi وMuse وOpenClaw وOpenCode وPi وPoolside وQwen وVS Code وغيرها، مع `registry.go` و`context_window.go` و`model_inventory.go`.
- `internal/proxy/`: بروكسيات Claude Desktop وCodex Desktop؛ `server/codex_proxy.go` و`server/cloud_proxy.go` للتمرير والسحابة.
- `tools/` و`model/parsers/` و`docs/capabilities/tool-calling.mdx`: Function/Tool Calling وتحليل مخرجاته، وليس تنسيق فرق وكلاء.
- `docs/integrations/`: أدلة التكاملات الخارجية، بما فيها n8n وOnyx وMarimo وGoose وRoo Code وJetBrains وXcode وZed وغيرها.
- الخلاصة: الوكلاء المذكورون **برامج خارجية** يشغّلها Ollama أو يمرّر لها الطلبات؛ ليست أقساماً داخل المستودع.

### و) parsers وrenderers وStructured Outputs

- `model/parsers/`: محللات عائلات النماذج وtool calls وthinking؛ تظهر عائلات qwen3 وqwen3.5 وqwen3coder وdeepseek3 وgemma4 وglm46/47 وcohere وlfm2/3 وministral وnemotron وolmo3 وغيرها.
- `model/renderers/`: قوالب تلك العائلات مع JSON وimage/audio/speech/thinking.
- `thinking/parser.go` و`harmony/harmonyparser.go`: فصل قنوات التفكير وتنسيق Harmony.
- `llm/gbnf.go` و`mlxrunner/grammar.go` و`mlxrunner/xgrammar/` و`model/renderers/json.go`: الإخراج المقيد وStructured Outputs.
- `parser/`: محلل Modelfile، و`template/`: قوالب المحادثات القديمة والحالية لمختلف العائلات.

### ز) runtime منخفض المستوى — مفيد عند الحاجة المتخصصة

- `llm/` و`llama/`: تشغيل ومراقبة llama-server وإدارة المنصات وتوزيع الأوزان.
- `mlxrunner/`: runner بمعمارية Go+MLX، وفيه batch وKV cache وprefix cache وtokenizer وsample وspeculative generation وxgrammar وتنفيذات معماريات نماذج متعددة.
- `discover/`: اكتشاف CUDA وROCm وVulkan وMetal وCPU واختيار runner.
- `create/` و`compatmigrate/` و`fs/gguf/` و`fs/safetensors/`: تحويل الأوزان وتكميمها وترحيل التوافق.
- هذه الوحدات قوية لتحسين الأداء أو تعديل runtime، لكنها ليست نقطة البداية المثلى لبناء منسّق أقسام.

### ح) التوثيق والاختبارات

- `docs/api/`: OpenAI/Anthropic compatibility وauthentication وerrors وstreaming وusage وcloud usage وbalance.
- `docs/capabilities/`: tool-calling وthinking وvision وspeech وembeddings وstructured-outputs وstreaming وweb-search وdecision.
- `integration/`: اختبارات vision وaudio وtools وembed وconcurrency وcontext وquantization وmigration وstructured output وthinking.
- `.github/workflows/`: test وrelease وtest-install وtest-tokenizer وtest-xgrammar وغيرها. وجودها دليل بنية CI، لا نتيجة نجاح مثبتة في هذا الجرد.
