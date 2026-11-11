
## 7. قراءة الفروع — ما الذي يعنيه عددها الكبير؟

الفروع ليست «إصدارات منتج» ولا ميزات مضمونة. أغلبها تطوير وإصلاح وتجارب وPRs. لذلك لم أدمج أي ادعاء من اسم فرع داخل قائمة إمكانات `main`. السجل النصي المرفق يحفظ الأسماء وSHA كاملة.

| المستودع | العدد | أكثر البادئات ظهوراً | فروع محمية/ملاحظة |
|---|---:|---|---|
| Open Design | 2852 | `fix=758 · codex=652 · feat=395 · [root]=168 · agent=145 · looper=119` | 50 محمياً؛ منها main وخطوط release/v* |
| Awesome LLM Apps | 15 | `[root]=9 · claude=3 · feat=2 · fix=1` | لا يظهر فرع محمي في السجل المسترجع |
| Langflow | 2660 | `[root]=1218 · cz=265 · test=250 · feat=182 · codeflash=176 · fix=158` | 19 محمياً؛ منها main وdev وrelease-* |
| Ollama | 493 | `[root]=102 · jmorganca=79 · hoyyeva=55 · brucemacd=53 · mxyng=46 · parth=46` | main محمي؛ بقية الأسماء غالباً تجارب مطورين |

### فروع Awesome LLM Apps الخمسة عشر كاملة

هذا هو المستودع الوحيد ذو العدد الصغير الذي يسمح بإدراج القائمة هنا بوضوح؛ البقية في سجل الفروع المرفق.

| الفرع | SHA المختصر |
|---|---|
| `add-vorflux-sponsor` | `b2bdfa591006` |
| `advisor-cover-image` | `2e6877e83a4b` |
| `advisor-skill-cover-and-readme` | `cfc6779f8bdb` |
| `claude/zealous-heisenberg-6y0cil` | `8abf46a4e707` |
| `claude/zealous-heisenberg-v4xhow` | `927b0bb7d743` |
| `claude/zealous-heisenberg-x1x0jp` | `1dd9f2ab105a` |
| `feat/excaliflow` | `1bb58b544f7b` |
| `feat/excaliflow-agent-collab` | `d83499be1877` |
| `fix/insurance-live-demo-reliability` | `233dcbcd3aef` |
| `insurance-claim-gemini-3-8-live` | `062954d888be` |
| `main` | `c46144eb61c1` |
| `swap-advisor-cover-dark` | `cfc6779f8bdb` |
| `thinking-out-loud-skill` | `17ea03824590` |
| `update-advisor-worker-gemini-3-7-flash` | `2d52ca9214f8` |
| `update-agent-skills` | `da0490fb5ac0` |

### أسماء فروع تستحق الفحص الاختياري لاحقاً — ليست إمكانات مؤكدة في main

- **Ollama:** `parth/agent-skills`، `parth/agents`، `royh/whisper`، `codex/phonon-tts`، `nicole/websearch_local`، `parth/add-websearch-client`، `research-codex-web-search-proxy`. هذه أسماء فقط؛ يلزم diff وقراءة الكود قبل الحكم.
- **Awesome LLM Apps:** `update-agent-skills`، `thinking-out-loud-skill`، `feat/excaliflow-agent-collab`، `fix/insurance-live-demo-reliability`.
- **Open Design:** خطوط `release/v*` و`feat/workspace-team` مفيدة لتتبع الاستقرار والتعاون، لا لافتراض ميزات إضافية.
- **Langflow:** `dev` وخطوط `release-*` مفيدة للمقارنة واكتشاف ما تغيّر، لكن تقرير هذه المرحلة ثابت على `main`.
