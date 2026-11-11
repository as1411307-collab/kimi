# تحليل جرد مستودع ollama/ollama — المرحلة الأولى (جرد فقط)

> نطاق هذه المرحلة: **جرد بنيوي فقط** اعتماداً على شجرة Git الكاملة لفرع `main`
> (الملف `ollama.tree.json`، 1834 مدخلاً، غير مبتورة `truncated=false`)
> وملف الفروع الموحّد `ollama.branches.json` (493 فرعاً) وREADME الرسمي.
> **لم يتم استخراج أي كود، ولم يتم تشغيل أو اختبار أي شيء، ولم يتم تعديل المصدر.**

## 1) تعريف وترخيص وتقنيات وcommit الفرع main

- **التعريف**: Ollama — منصة/أداة سطر أوامر وخادم محلي لتشغيل النماذج اللغوية المفتوحة محلياً أو سحابياً، مع REST API وتطبيق سطح مكتب. **بعكس awesome-llm-apps، هذا مشروع برمجي واحد متماسك** (منتج واحد ببنية Go موحّدة)، وليس فهرس أمثلة.
- **الترخيص**: MIT (ملف `LICENSE` في الجذر؛ الترخيص المعروف للمشروع — لم يُفتح محتوى الملف في هذه المرحلة).
- **commit الفرع main**: `1f23c7232e8e35b21d81bb03569a8afde2a6b0f9` (مطابق لجذر الشجرة المحفوظة).
- **الفروع**: 493 فرعاً في الملف الموحّد `ollama.branches.json` (الصفحات 1–4 عبر API مباشرة + الصفحة 5 بمسار بديل بسبب حد المعدل)؛ فرع واحد فقط محمي (protected)؛ أغلب الفروع أفرع مهام لفريق التطوير (bmizerany/*, brucemacd/*, drifkin/*, parth*, pdevine/*, royh/*) إضافة إلى أفرع إصدارات `release_v*`.
- **التقنيات** (محسوبة من الشجرة): Go هو الأساس الساحق (**1077 ملف .go**، منها **489 ملف `_test.go`** — تغطية اختبارات واسعة بنيوياً)، مع TypeScript/TSX (~108 ملفات) لتطبيق سطح المكتب `app/` (webview/wintray/darwin)، C/CMake للربط مع المحركات، وقوالب محادثة `.gotmpl`/`.jinja`، ووثائق Mintlify بصيغة `.mdx` (60 ملفاً). محركات التشغيل: llama.cpp (`llama/`، ملف الإصدار `LLAMA_CPP_VERSION`) وApple MLX (`mlx/`, `mlxrunner/`، ملفا `MLX_VERSION`/`MLX_C_VERSION`). وثائق مفتاحية في الجذر: `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `SECURITY.md`.

## 2) شرح مجلدات/عناصر الجذر (58 مدخلاً)

| المسار | الشرح |
|---|---|
| `main.go`, `cmd/` | نقطة دخول CLI؛ `cmd/` يضم `bench` (قياس أداء)، `config`، `launch` (تشغيل تكاملات مثل Claude Code/Codex)، `tui` (واجهة طرفية تفاعلية)، `internal`. |
| `server/` | خادم HTTP الرئيسي (75 ملفاً): إنشاء/سحب النماذج، المصادقة `auth.go`، بروكسيات `cloud_proxy*.go` و`codex_proxy.go`، اختبارات fuzz للإنشاء. |
| `api/` | تعريفات REST API وعميل Go (`client.go`, `types.go`) + `api/examples/`. |
| `app/` | تطبيق سطح المكتب (16 حزمة فرعية: `darwin`, `wintray`, `webview`, `ui`, `updater`, `auth`, `store`, `server`, `tools`, `assets`...) — واجهة Ollama الرسومية. |
| `llm/` | طبقة إدارة محرك الاستدلال: تشغيل ثنائيات llama.cpp (`llama_binary.go`, `llama_server*.go` بما فيه نسخة speech)، GBNF grammars. |
| `llama/` | تكامل llama.cpp (`compat`, `server`). |
| `mlx/`, `mlxrunner/` | محرك Apple MLX للتشغيل على أجهزة Apple Silicon (`generator`, `quant`, `compat`, اختبارات). |
| `ml/` | تجريدات الأجهزة (`device.go`) ومسارات المكتبات. |
| `discover/` | اكتشاف العتاد: GPU (CUDA/AMD/Metal عبر `gpu_darwin.*`), CPU لكل نظام. |
| `model/` | `model/parsers` و`model/renderers` — محللات ومصيّرات لكل عائلة نماذج. |
| `create/` | تحويل/إنشاء النماذج من الصيغ الخام (63 ملفاً: gguf, safetensors, quant مثل blockfp8, دعم عائلات: cohere2moe, gemma, gpt-oss, deepseek, glm...). |
| `fs/` | قراءة صيغ النماذج: `gguf`, `safetensors`. |
| `parser/` | محلل Modelfile. |
| `template/` | قوالب المحادثة الجاهزة (44 ملفاً: `.gotmpl` + بيانات اختبار `.json` لعائلات مثل chatml, alpaca, command-r, codellama...). |
| `tools/` | تحليل وتوليد استدعاءات الأدوات (tool calling) وقوالبها. |
| `thinking/` | محلل/قوالب مخرجات «التفكير» (reasoning traces). |
| `harmony/` | محلل صيغة Harmony (قناة/تنسيق gpt-oss). |
| `openai/` | طبقة توافق OpenAI API بما فيه **Responses API** (responses*.go). |
| `anthropic/` | طبقة توافق Anthropic Messages API مع دعم thinking. |
| `middleware/` | وسائط HTTP: openai/anthropic، مقاييس، thinking، بحث ويب/أدوات في Responses. |
| `decision/` | وحدة قرار/توجيه داخلية (17 ملفاً: `clef`, `d1`, `d3`, `kev`, `pplx`, `prompts` + اختبارات autotrust). |
| `auth/` | مفاتيح/مصادقة النماذج السحابية. |
| `transfer/` | تنزيل/رفع النماذج (resume، redirect، ملفات sparse على Windows). |
| `manifest/` | بيانات النماذج الوصفية (manifests/layers) واختبارات الترقية/التراجع. |
| `envconfig/`, `format/`, `logutil/`, `progress/`, `readline/`, `version/`, `types/` | حزم أدوات مساعدة (إعدادات بيئة، تنسيق، سجلات، أشرطة تقدم، طرفية، إصدار، أنواع مشتركة). |
| `internal/` | حزم داخلية: `cloud`, `proxy`, `onboarding`, `modelref`, `orderedmap`, `decisiontest`, `testutil`. |
| `compatmigrate/` | ترحيلات توافق لعائلات النماذج (34 ملفاً: gemma3/4, gptoss, glm, deepseek_ocr, laguna...). |
| `integration/` | اختبارات تكامل (`testdata`). |
| `docs/` | وثائق Mintlify فعلية: `api/` (بما فيه openai-compatibility وanthropic-compatibility وauthentication), `capabilities/` (tool-calling, vision, speech, thinking, embeddings, web-search, structured-outputs, decision), `integrations/`, `tools/`، إضافة إلى `cli.mdx`, `faq.mdx`, `gpu.mdx`, `docker.mdx`, `development.md`. |
| `scripts/` | سكربتات دعم. |
| `.github/` | قوالب Issues + workflows: `test.yaml`, `release.yaml`, `latest.yaml`, `test-install.yaml`, `test-llamacpp-update.yaml`, `test-tokenizer.yaml`, `test-xgrammar.yaml` — CI حقيقي شامل. |
| `Dockerfile`, `CMakeLists.txt`, `CMakePresets.json`, `.golangci.yaml` | بناء Docker/CMake وفحص Go (golangci-lint). |
| `go.mod`, `go.sum` | وحدة Go واعتمادياتها. |
| `LICENSE`, `README.md`, `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `SECURITY.md` | ترخيص ووثائق مفتاحية (بما فيها سياسة أمن وسياسات للوكلاء). |
| `LLAMA_CPP_VERSION`, `MLX_VERSION`, `MLX_C_VERSION` | تثبيت إصدارات المحركات المدمجة. |

## 3) ملاحظات بنيوية رئيسية (من الشجرة فقط)

1. **منتج واحد متماسك** بمعمارية حزم Go واضحة (server ← api/middleware ← llm ← llama/mlx)، وليس مجموعة أمثلة.
2. **اختبارات واسعة**: 489 ملف `_test.go` (نسبة ~45% من ملفات Go) شاملة fuzz tests — لكننا **لم نشغّلها**.
3. **واجهات توافق متعددة**: واجهة Ollama الأصلية + OpenAI (chat + Responses) + Anthropic، مع بروكسيات سحابية وCodex — أي أنه يعمل كطبقة تجريد/موجّه للنماذج محلياً وسحابياً.
4. **قدرات موثقة رسمياً**: tool calling، vision، speech، thinking، embeddings، web search، structured outputs (`docs/capabilities/*`).
5. **دعم عتاد واسع**: CUDA/AMD/Metal/CPU عبر `discover/`، ومحرك MLX مخصص لـApple Silicon.
6. **تطبيق سطح مكتب مدمج** (`app/` بنية TS/webview) إلى جانب CLI/TUI.
7. README يركّز على التكامل مع وكلاء البرمجة (Claude Code, Codex, Copilot CLI, OpenCode, OpenClaw) عبر `ollama launch`.

## 4) فهرس فائدة سريع (مسارات دقيقة)

- **تشغيل نماذج محلياً/خصوصية**: `server/`, `llm/`, `llama/`, `mlxrunner/`, `discover/`.
- **واجهة OpenAI/Anthropic متوافقة للتكامل مع الوكلاء**: `openai/`, `anthropic/`, `middleware/`.
- **استدعاء الأدوات Tool calling**: `tools/`, `docs/capabilities/tool-calling.mdx`.
- **الاستدلال/التفكير**: `thinking/`, `harmony/`.
- **تحويل واستيراد النماذج والكمّ**: `create/`, `fs/gguf`, `fs/safetensors`, `compatmigrate/`.
- **قوالب المحادثة**: `template/`.
- **الواجهات**: `cmd/tui` (طرفية), `app/` (سطح مكتب).
- **الوثائق الرسمية داخل المستودع**: `docs/` (60 ملف mdx).
- **الأمن**: `SECURITY.md`, `auth/`, `server/auth.go`, `decision/autotrust_decision_test.go`.

## 5) ما لا يوجد / حدود

- لا يحتوي أوزان نماذج؛ النماذج تُسحب من سجل Ollama أو تُستورد.
- لا يوجد إطار وكلاء متعدد داخل المستودع؛ Ollama بنية تحتية للتشغيل ويُتكامل مع أطر الوكلاء خارجياً.
- وحدة `decision/` غير موثقة بتفصيل في README؛ وظيفتها تُستنتج من أسماء الملفات فقط في هذه المرحلة.
- لم نتحقق من نجاح الاختبارات أو البناء؛ الاستنتاج عن CI من أسماء workflows فقط.

## 6) منهجية ومصادر التحقق

- الشجرة: `ollama.tree.json` (1834 مدخلاً، `truncated=false`) عند commit `main` = `1f23c7232e8e35b21d81bb03569a8afde2a6b0f9`.
- الفروع: `ollama.branches.json` الموحّد (493 فرعاً؛ الصفحة الأخيرة جُلبت بمسار بديل بعد استنفاد حد معدل GitHub API).
- README الرسمي لفرع `main`.
- حدود الثقة: كل التصنيفات أعلاه من أسماء/بنى الملفات وREADME؛ **لم يُقرأ كود ولم يُشغَّل شيء**.
