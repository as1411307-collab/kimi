# تحليل جرد مستودع Shubhamsaboo/awesome-llm-apps — المرحلة الأولى (جرد فقط)

> نطاق هذه المرحلة: **جرد بنيوي فقط** اعتماداً على شجرة Git الكاملة لفرع `main`
> (الملف `awesome-llm-apps.tree.json`، 2547 مدخلاً، غير مبتورة `truncated=false`)
> وملف الفروع `awesome-llm-apps.branches.json` وملف README الرسمي.
> **لم يتم استخراج أي كود، ولم يتم تشغيل أو اختبار أي مشروع، ولم يتم تعديل المصدر.**

## 1) تعريف وترخيص وتقنيات وcommit الفرع main

- **التعريف**: مجموعة مفتوحة المصدر تضم «100+» تطبيق وكيل ذكاء اصطناعي ومهارات وكلاء (Agent Skills) وتطبيقات RAG، وفق وصف README الرسمي: "Hand-built, tested end-to-end". المستودع **ليس منظومة واحدة** بل فهرس مشاريع/أمثلة مستقلة، كل مشروع في مجلده الخاص مع README واعتمادياته الخاصة. ملاحظة: عبارة "tested end-to-end" ادعاء من صاحب المستودع؛ **نحن لم نختبر أي عنصر**.
- **الترخيص**: Apache-2.0 (ملف `LICENSE` في الجذر، ويؤكده تذييل README: "Apache-2.0 · Fork it, ship it, sell it").
- **commit الفرع main**: `c46144eb61c18cd1a495445c79ec47145722053e` (مطابق لجذر الشجرة المحفوظة). عدد الفروع في ملف الفروع: 15 فرعاً؛ التحليل هنا يخص `main` فقط.
- **التقنيات** (مستنتجة من الشجرة وREADME، لا من فحص الأكواد):
  - اللغات: Python غالباً (`.py`, requirements, Streamlit)، وTypeScript/React/Next.js في مشاريع الواجهات التوليدية والإضافات (`.ts/.tsx`، package-lock)، إضافة إلى Prisma وSQL وDocker/Nixpacks في بعض المشاريع.
  - أطر الوكلاء المذكورة رسمياً: OpenAI Agents SDK، Google ADK، CrewAI، AG2 (AutoGen)، LangGraph، Pydantic AI، Agno، EvoAgentX، MCP (Model Context Protocol)، browser-use.
  - النماذج المذكورة: Claude، GPT (OpenAI)، Gemini، DeepSeek R1، Llama 3.x، Qwen، Grok (xAI)، Gemma/EmbeddingGemma، Cohere Command R7B.
  - بنى تحتية متكررة: Qdrant ومتاجر متجهات، Firecrawl، Unsloth (LoRA)، واجهات Streamlit، بوابات CI في `.github/workflows` (منها `skill-evals.yml` كبوابة تقييم/أمان لمهارات الوكلاء).

## 2) شرح مجلدات الجذر (16 مدخلاً)

| المسار | النوع | الشرح |
|---|---|---|
| `.gitattributes` | ملف | إعدادات Git. |
| `.github/` | مجلد | workflows للتكامل المستمر: `claude.yml` و`skill-evals.yml` (بوابة CI لتقييم وأمان المهارات). |
| `.gitignore` | ملف | استثناءات Git. |
| `LICENSE` | ملف | ترخيص Apache-2.0. |
| `README.md` | ملف | الفهرس الرئيسي الرسمي لكل القوالب. |
| `advanced_ai_agents/` | مجلد | وكلاء متقدمون: ألعاب مستقلة، تطبيقات وكيل مفرد، تطبيقات متعددة الوكلاء وفرق وكلاء. |
| `advanced_llm_apps/` | مجلد | تطبيقات LLM متقدمة: محادثة مع مصادر (Chat with X)، ذاكرة، ضبط دقيق، تحسين تكلفة، أدوات/إضافات مستقلة. |
| `agent_skills/` | مجلد | «مهارات وكلاء» قابلة للتثبيت بأمر واحد لوكلاء البرمجة (Claude Code/Codex/Cursor...) مع مجلد `evals/` للتقييمات. |
| `ai_agent_framework_crash_course/` | مجلد | دورتان تعليميتان متدرجتان: Google ADK وOpenAI Agents SDK. |
| `always_on_agents/` | مجلد | وكلاء يعملون باستمرار/بجدولة (مراقبة وإيجازات استباقية). |
| `docs/` | مجلد | أصول توثيقية فقط: `banner/sponsors/` و`gallery/` (صور المعرض)، لا كود. |
| `generative_ui_agents/` | مجلد | وكلاء يولّدون واجهات تفاعلية (مكونات، لوحات، تطبيقات MCP) لا نصوصاً فقط. |
| `mcp_ai_agents/` | مجلد | وكلاء يتصلون بأدوات خارجية عبر بروتوكول MCP. |
| `rag_tutorials/` | مجلد | خطوط استرجاع معزز (RAG): من السلسلة البسيطة إلى RAG وكيل/هجين/متعدد الوسائط/رسوم معرفية. |
| `starter_ai_agents/` | مجلد | وكلاء مبتدئون أحاديو الملف غالباً، يعملون بمفتاح API واحد. |
| `voice_ai_agents/` | مجلد | وكلاء صوت-إلى-صوت بواجهات Realtime. |

## 3) القائمة الكاملة للمشاريع/الأمثلة (محسوبة من الشجرة)

### 3.1 `advanced_ai_agents/` — 38 مجلد مشروع أولي، **54 مشروعاً طرفياً**
- `autonomous_game_playing_agent_apps/` — **3** مشاريع لعب ذاتي:
  - `ai_3dpygame_r1` (DeepSeek R1 يكتب PyGame ووكلاء متصفح يشغّلونه)
  - `ai_chess_agent` (وكيل أبيض ضد وكيل أسود بحركات متحققة)
  - `ai_tic_tac_toe_agent` (نموذجان يتنافسان نقلة-نقلة)
- `single_agent_apps/` — **18** وكيلاً مفرداً:
  `ai_agent_governance`، `ai_consultant_agent`، `ai_customer_support_agent`، `ai_deep_research_agent`، `ai_email_gtm_reachout_agent`، `ai_fraud_investigation_agent`، `ai_health_fitness_agent`، `ai_investment_agent`، `ai_journalist_agent`، `ai_meeting_agent`، `ai_movie_production_agent`، `ai_personal_finance_agent`، `ai_recipe_meal_planning_agent`، `ai_startup_insight_fire1_agent`، `ai_system_architect_r1`، `earnings_call_analyst_agent`، `research_agent_gemini_interaction_api`، `windows_use_autonomous_agent`.
- `multi_agent_apps/` — **17** مدخلاً = 16 تطبيقاً مستقلاً + مجلد `agent_teams/` الذي يضم **17** فريقاً:
  - التطبيقات الستة عشر: `ai_aqi_analysis_agent`، `ai_codebase_migration_agent`، `ai_domain_deep_research_agent`، `ai_email_gtm_outreach_agent`، `ai_financial_coach_agent`، `ai_home_renovation_agent`، `ai_mental_wellbeing_agent`، `ai_negotiation_battle_simulator`، `ai_news_and_podcast_agents`، `ai_self_evolving_agent`، `ai_speech_trainer_agent`، `devpulse_ai`، `multi_agent_researcher`، `multi_agent_trust_layer`، `product_launch_intelligence_agent`، `trust_gated_agent_team`.
  - فرق `agent_teams/` (17): `ag2_adaptive_research_team`، `ai_competitor_intelligence_agent_team`، `ai_finance_agent_team`، `ai_game_design_agent_team`، `ai_legal_agent_team`، `ai_real_estate_agent_team`، `ai_recruitment_agent_team`، `ai_sales_intelligence_agent_team`، `ai_seo_audit_team`، `ai_services_agency`، `ai_teaching_agent_team`، `ai_travel_planner_agent_team`، `ai_vc_due_diligence_agent_team`، `llm_panel_agent_team`، `multimodal_coding_agent_team`، `multimodal_design_agent_team`، `multimodal_uiux_feedback_agent_team`.

### 3.2 `advanced_llm_apps/` — 13 مجلداً أولياً، **28 مشروعاً طرفياً**
- `chat-with-tarots/` — مشروع واحد (دردشة تاروت؛ بنية data/helpers/images).
- `chat_with_X_tutorials/` — **7**: `chat_with_github`، `chat_with_gmail`، `chat_with_pdf`، `chat_with_research_papers`، `chat_with_substack`، `chat_with_youtube_videos`، `streaming_ai_chatbot`.
- `cursor_ai_experiments/` — **2**: `llm_router_app`، `local_chatgpt_clone`.
- `excaliflow/` — مشروع واحد (لوحة رسم Excalidraw بأسهم متحركة وتصدير فيديو).
- `gpt_oss_critique_improvement_loop/` — مشروع واحد (حلقة نقد وتحسين ذاتي بنماذج GPT المفتوحة).
- `llm_apps_with_memory_tutorials/` — **7**: `adk_career_coach_agent_memory`، `ai_arxiv_agent_memory`، `ai_travel_agent_memory`، `llama3_stateful_chat`، `llm_app_personalized_memory`، `local_chatgpt_with_memory`، `multi_llm_memory`.
- `llm_finetuning_tutorials/` — **2**: `gemma3_finetuning`، `llama3.2_finetuning`.
- `llm_optimization_tools/` — **2**: `headroom_context_optimization`، `toonify_token_optimization`.
- `multimodal_video_moment_finder/` — مشروع واحد (backend+frontend لإيجاد لقطات في الفيديو).
- `needle/` — مشروع واحد (إضافة Chrome للبحث الدلالي داخل الصفحات؛ api/extension/server/src/tests).
- `resume_job_matcher/` — مشروع واحد (مطابقة السير الذاتية مع الوظائف).
- `ripple/` — مشروع واحد (إضافة تكشف التناقضات أثناء تحرير Google Doc).
- `thinkpath_chatbot_app/` — مشروع واحد.

### 3.3 `agent_skills/` — **8 مهارات** + مجلد تقييمات
- المهارات الثماني: `advisor-orchestrator-worker` (حلقة ميتا: مستشار/منسّق/عامل)، `commit-archaeologist` (إعادة بناء سبب وجود الكود من تاريخ الالتزامات)، `dependency-doctor` (فحص ملفات الاعتماديات)، `first-reader` (محاكاة قرّاء حقيقيين للمسودات)، `project-graveyard` (تشريح المشاريع الجانبية المهجورة)، `scope-creep-detector` (كشف تضخم نطاق الـdiff)، `self-improving-agent-skills` (تحسين المهارات ذاتياً عبر Gemini وADK)، `thinking-out-loud` (تحويل الثرثرة الصوتية إلى موجز قابل للمسح).
- `evals/` — ليست مهارة بل **بنية تقييم**: 7 مجلدات تقييم مماثلة للمهارات + مجلد `tools/`، وتدعمها بوابة CI `skill-evals.yml`.

### 3.4 `ai_agent_framework_crash_course/` — دورتان، **21 درساً**
- `google_adk_crash_course/` — **10**: `1_starter_agent`، `2_model_agnostic_agent`، `3_structured_output_agent`، `4_tool_using_agent`، `5_memory_agent`، `6_callbacks`، `7_plugins`، `8_simple_multi_agent`، `9_multi_agent_patterns`، `adk_yaml_examples`.
- `openai_sdk_crash_course/` — **11**: `1_starter_agent`، `2_structured_output_agent`، `3_tool_using_agent`، `4_running_agents`، `5_context_management`، `6_guardrails_validation`، `7_sessions`، `8_handoffs_delegation`، `9_multi_agent_orchestration`، `10_tracing_observability`، `11_voice`.

### 3.5 `always_on_agents/` — **2**
`always_on_hn_briefing_agent` (إيجاز Hacker News مجدول إلى Slack/بريد)، `release_radar_agent` (مراقبة إصدارات الاعتماديات وتصنيف الكاسر/الأمني/الرئيسي).

### 3.6 `generative_ui_agents/` — **8**
`ai-dashboard-canvas-agent`، `ai-deep-research-agent`، `ai-financial-coach-agent`، `ai-knowledge-explorer`، `ai-mcp-app-builder`، `ai-shadcn-component-generator`، `generative-ui-starter-project`، `mcp-apps-generative-ui-showcase`.

### 3.7 `mcp_ai_agents/` — **7**
`ai_travel_planner_mcp_agent_team`، `browser_mcp_agent`، `github_mcp_agent`، `multi_mcp_agent`، `multi_mcp_agent_router`، `notion_mcp_agent`، `openai_remote_mcp_bridge`.

### 3.8 `rag_tutorials/` — **24**
`agentic_rag_embedding_gemma`، `agentic_rag_gpt5`، `agentic_rag_math_agent` (بنية كاملة: app/benchmark/config/data/logs/rag)، `agentic_rag_with_reasoning`، `agentic_typed_rag_pydanticai`، `ai_blog_search`، `autonomous_rag`، `contextualai_rag_agent`، `corrective_rag`، `deepseek_local_rag_agent`، `gemini_agentic_rag`، `hybrid_search_rag`، `knowledge_graph_rag_citations`، `llama3.1_local_rag`، `local_hybrid_search_rag`، `local_rag_agent`، `multimodal_agentic_rag` (backend+frontend)، `qwen_local_rag`، `rag-as-a-service`، `rag_agent_cohere`، `rag_chain`، `rag_database_routing`، `rag_failure_diagnostics_clinic`، `vision_rag`.

### 3.9 `starter_ai_agents/` — **17**
`ai_blog_to_podcast_agent`، `ai_breakup_recovery_agent`، `ai_data_analysis_agent`، `ai_data_visualisation_agent`، `ai_life_insurance_advisor_agent`، `ai_medical_imaging_agent`، `ai_meme_generator_agent_browseruse`، `ai_music_generator_agent`، `ai_reasoning_agent`، `ai_startup_trend_analysis_agent`، `ai_travel_agent`، `ai_x402_paying_agent`، `mixture_of_agents`، `multimodal_ai_agent`، `openai_research_agent`، `web_scraping_ai_agent`، `xai_finance_agent`.

### 3.10 `voice_ai_agents/` — **4**
`ai_audio_tour_agent`، `customer_support_voice_agent`، `insurance_claim_live_agent_team` (استقبال مطالبات صوتي حي مع رؤية عبر الكاميرا)، `voice_rag_openaisdk`.

### 3.11 `docs/` — **0 مشاريع** (محتوى توثيقي فقط)
`docs/banner/sponsors/` و`docs/gallery/` (صور PNG للمعرض المستخدمة في README).

### إجمالي الحساب
مشاريع/أمثلة طرفية قابلة للتشغيل نظرياً: 3 (ألعاب) + 18 (مفرد) + 33 (متعدد الوكلاء والفرق) + 28 (advanced_llm_apps) + 17 (starter) + 4 (voice) + 2 (always-on) + 8 (generative UI) + 7 (MCP) + 24 (RAG) = **144 مشروعاً**، إضافة إلى **8 مهارات وكلاء** و**21 درساً** في الدورتين. README يقول "100+" وهو متسق مع هذا العدد. **تنبيه جوهري: هذه أمثلة مستقلة متفاوتة النضج، وليست منظومة واحدة متكاملة.**

## 4) فهرس الفائدة (مسارات دقيقة من الشجرة)

- **الذاكرة (Memory)**:
  - `advanced_llm_apps/llm_apps_with_memory_tutorials/` — 7 أمثلة: `ai_arxiv_agent_memory`، `ai_travel_agent_memory`، `adk_career_coach_agent_memory`، `llama3_stateful_chat`، `llm_app_personalized_memory`، `local_chatgpt_with_memory`، `multi_llm_memory` (ذاكرة مشتركة بين نماذج مختلفة).
  - `ai_agent_framework_crash_course/google_adk_crash_course/5_memory_agent`، `openai_sdk_crash_course/5_context_management` و`7_sessions`.
- **المحادثة (Chat/Conversational)**:
  - `advanced_llm_apps/chat_with_X_tutorials/` (GitHub/Gmail/PDF/أوراق بحثية/Substack/YouTube + `streaming_ai_chatbot`).
  - `advanced_llm_apps/cursor_ai_experiments/local_chatgpt_clone`، `advanced_llm_apps/thinkpath_chatbot_app`.
- **الصوت (Voice/Audio)**:
  - `voice_ai_agents/` الأربعة كلها؛ `ai_agent_framework_crash_course/openai_sdk_crash_course/11_voice`؛ `starter_ai_agents/ai_blog_to_podcast_agent`؛ `agent_skills/thinking-out-loud`؛ `advanced_ai_agents/multi_agent_apps/ai_speech_trainer_agent` و`ai_news_and_podcast_agents` (توليد بودكاست).
- **المعماريات (System Architecture)**:
  - `advanced_ai_agents/single_agent_apps/ai_system_architect_r1` (مراجعة معمارية باستدلال DeepSeek R1 + Claude).
  - `advanced_llm_apps/excaliflow/` (رسم معماريات بتدفقات متحركة).
- **الوكلاء (Agents عموماً)**:
  - `starter_ai_agents/` (17 للمبتدئين)، `advanced_ai_agents/single_agent_apps/` (18)، `advanced_ai_agents/multi_agent_apps/` (16+17 فريقاً)، `ai_agent_framework_crash_course/` (دروس التدرج من وكيل مفرد إلى تعدد وكلاء وتفويض Handoffs).
- **التصميم والواجهات التوليدية (Design/Generative UI)**:
  - `generative_ui_agents/` الثمانية كلها (خاصة `ai-shadcn-component-generator` و`ai-dashboard-canvas-agent` و`generative-ui-starter-project` و`mcp-apps-generative-ui-showcase`).
  - `advanced_ai_agents/multi_agent_apps/agent_teams/multimodal_design_agent_team` و`multimodal_uiux_feedback_agent_team` و`multimodal_coding_agent_team`.
  - `advanced_ai_agents/multi_agent_apps/ai_home_renovation_agent` (تصميم داخلي فوتورياليستي).
- **الحماية والثقة والحوكمة (Security/Trust/Guardrails)**:
  - `advanced_ai_agents/multi_agent_apps/multi_agent_trust_layer`، `trust_gated_agent_team` (سجل تدقيق مربوط بالتجزئة)، `advanced_ai_agents/single_agent_apps/ai_agent_governance`.
  - `ai_agent_framework_crash_course/openai_sdk_crash_course/6_guardrails_validation`.
  - `agent_skills/dependency-doctor` (إصدارات مسحوبة/غير مثبتة)، `agent_skills/scope-creep-detector`، `always_on_agents/release_radar_agent` (تنبيهات أمنية للاعتماديات).
  - بوابة CI: `.github/workflows/skill-evals.yml`.
- **المهارات (Agent Skills)**: `agent_skills/` الثمانية (انظر 3.3) — قابلة للتثبيت عبر `npx skills add` وتعمل مع Claude Code/Codex/Cursor.
- **البحث والتقصي (Research/Search)**:
  - `advanced_ai_agents/single_agent_apps/ai_deep_research_agent`، `generative_ui_agents/ai-deep-research-agent`، `advanced_ai_agents/multi_agent_apps/ai_domain_deep_research_agent` و`multi_agent_researcher`، `starter_ai_agents/openai_research_agent`، `advanced_ai_agents/multi_agent_apps/agent_teams/ag2_adaptive_research_team`، `advanced_ai_agents/single_agent_apps/research_agent_gemini_interaction_api`، `rag_tutorials/ai_blog_search`، `advanced_llm_apps/needle/` (بحث دلالي داخل صفحات الويب).
- **القراءة والمحادثة مع المستندات (Reading/Docs)**:
  - `advanced_llm_apps/chat_with_X_tutorials/chat_with_pdf` و`chat_with_research_papers` و`chat_with_substack` و`chat_with_gmail`؛ `voice_ai_agents/voice_rag_openaisdk`؛ `rag_tutorials/knowledge_graph_rag_citations` (استشهادات متعددة القفزات) و`vision_rag` و`corrective_rag` و`rag_failure_diagnostics_clinic` (تشخيص أعطال RAG).
- **الفيديو (Video)**:
  - `advanced_llm_apps/chat_with_X_tutorials/chat_with_youtube_videos`، `advanced_llm_apps/multimodal_video_moment_finder/`، `starter_ai_agents/multimodal_ai_agent`، `advanced_ai_agents/single_agent_apps/earnings_call_analyst_agent` (مزامنة تحليل مع تشغيل مكالمات الأرباح).
- **التحليل المالي (Finance)**:
  - `advanced_ai_agents/multi_agent_apps/agent_teams/ai_finance_agent_team` و`ai_vc_due_diligence_agent_team`؛ `advanced_ai_agents/single_agent_apps/ai_investment_agent` و`ai_personal_finance_agent` و`earnings_call_analyst_agent`؛ `advanced_ai_agents/multi_agent_apps/ai_financial_coach_agent` و`generative_ui_agents/ai-financial-coach-agent`؛ `starter_ai_agents/xai_finance_agent`؛ `starter_ai_agents/ai_x402_paying_agent` (مدفوعات وكيل لكل استدعاء).
- **الاستدلال (Reasoning)**:
  - `starter_ai_agents/ai_reasoning_agent`، `rag_tutorials/agentic_rag_with_reasoning`، `rag_tutorials/deepseek_local_rag_agent`، `advanced_ai_agents/single_agent_apps/ai_system_architect_r1`، `advanced_ai_agents/autonomous_game_playing_agent_apps/ai_3dpygame_r1`، `rag_tutorials/gemini_agentic_rag` (إعادة صياغة الاستعلام)، `advanced_llm_apps/gpt_oss_critique_improvement_loop` (نقد وتحسين ذاتي).
- **فك الشفرات/الثغرات (Security probing)**:
  - **لا يوجد مشروع مخصص لكسر التشفير أو اختبار الاختراق الهجومي.** الأقرب دفاعياً: `advanced_ai_agents/single_agent_apps/ai_fraud_investigation_agent` (تحقيق احتيال من السجلات العامة)، `agent_skills/commit-archaeologist` (تنقيب تاريخ الكود)، `agent_skills/dependency-doctor` و`always_on_agents/release_radar_agent` (مخاطر سلسلة الإمداد)، و`multi_agent_trust_layer`/`trust_gated_agent_team` (تدقيق وثقة).

## 5) ما لا يوجد / ما ليس نظاماً جاهزاً

- **ليس منتجاً واحداً**: لا يوجد تطبيق موحّد أو نقطة دخول مشتركة؛ كل مجلد مشروع مستقل باعتمادياته، وكثير منها أمثلة تعليمية (Crash courses, tutorials) لا أنظمة إنتاجية.
- **لا اختبارات شاملة قابلة للتحقق**: مجلدات `tests/` موجودة فقط في 9 مواقع من أصل ~144 مشروعاً (`needle`، `ripple`، `always_on_hn_briefing_agent`، `release_radar_agent`، `insurance_claim_live_agent_team`، `earnings_call_analyst_agent`، `ai_news_and_podcast_agents/beifong`، `generative_ui_agents/ai-deep-research-agent/agent`، `generative_ui_agents/ai-knowledge-explorer/agent`). عبارة README "tested end-to-end" لم نتحقق منها ولم نشغّل شيئاً.
- **لا أدوات هجومية/تشفيرية**: لا كسر تشفير، لا فحص ثغرات، لا CTF.
- **لا نماذج مدرّبة داخلياً**: المستودع يستهلك نماذج خارجية (سحابية أو محلية عبر Ollama-style) ولا يحتوي أوزاناً.
- **لا بيانات حقيقية حساسة**: أمثلة مثل التأمين والطب (`ai_medical_imaging_agent`، `ai_life_insurance_advisor_agent`) أمثلة تعليمية وليست أنظمة معتمدة طبياً/تأمينياً.
- **`docs/` ليست وثائق تقنية**: مجرد صور لافتات ومعرض؛ الوثائق الفعلية موزعة كـ README داخل كل مشروع.
- بعض عناصر README **روابط خارجية** لا توجد في الشجرة (مثل Openwork وWispr Flow clone) — ليست جزءاً من المستودع.

## 6) المرشحون للتوسع (مرحلة لاحقة) ولماذا

1. **`advanced_llm_apps/llm_apps_with_memory_tutorials/` (7 مشاريع)** — تغطية الذاكرة الأوسع والأنظف تنظيماً؛ مباشرة الصلة بأي منظومة محادثة طويلة الأمد.
2. **`ai_agent_framework_crash_course/` (21 درساً)** — أساس تعليمي متدرج لبناء الوكلاء (ADK + OpenAI SDK) يصلح كنواة معرفية قبل أي توسع.
3. **`rag_tutorials/` (24 مشروعاً)** — أغنى قسم؛ يشمل RAG محلياً بالكامل (`local_rag_agent`، `llama3.1_local_rag`، `qwen_local_rag`، `deepseek_local_rag_agent`) وRAG تشخيصياً (`rag_failure_diagnostics_clinic`) وبالاستشهادات (`knowledge_graph_rag_citations`) — قيمة عملية عالية وقابلية دمج.
4. **`agent_skills/` (8 مهارات + evals)** — وحدات صغيرة محكمة الحدود مع بوابة CI فعلية (`skill-evals.yml`)؛ أسهل ما يمكن تبنيه والتحقق منه.
5. **`mcp_ai_agents/` (7)** — طبقة تكامل موحدة عبر MCP (GitHub/Notion/متصفح) قابلة لإعادة الاستخدام كموصّلات.
6. **`generative_ui_agents/` (8)** — الوحيد الذي يغطي الواجهات التفاعلية التوليدية؛ مرشح قوي إن كان الهدف منتجاً بوجهة مستخدم.
7. **`voice_ai_agents/` (4)** — صغير ومتماسك؛ `voice_rag_openaisdk` يجمع الصوت+القراءة معاً.
8. **`always_on_agents/` (2)** — نمط الجدولة/المراقبة الاستباقية نادر في المستودع وقابل للتعميم (منهجان فقط لكن باختبارات موجودة).

