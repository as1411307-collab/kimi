# دليل استخدام مرجع بناء تطبيق آيفون والوكيل

## القرار الحالي

- واجهة التطبيق: **Swift 6 أصيل + SwiftUI** عبر Xcode Cloud وحساب Apple Developer.
- الـ Core المرجعي: TypeScript/Fastify + SQLite WAL + `node:sqlite` في Node 22.
- التطبيق إدخال وعرض فقط. الحالة والقرار والصلاحيات والتنفيذ تبقى في Core.
- لا نقل لـ Expo ولا n8n ولا Docker ولا أسرار من هذه اللقطة.

## ما الموجود فعلاً؟

`reference/ahmed-v01/` يحتوي Core وعقوداً واختبارات قديمة مفيدة:

- `POST /v1/messages`: رسالة نصية أو ملف مع `request_id` و`conversation_id`.
- `GET /v1/tasks/:taskId`: استرجاع حالة المهمة.
- `POST /v1/tasks/:taskId/actions/:actionId/decision`: قرار الموافقة أو الرفض.
- `GET /v1/conversations/:conversationId`: استعادة الرسائل والمهام.

العقد يمنع التكرار بـ`request_id`، ويحجز التنفيذ مرة واحدة بـ`idempotency_key`، وتنتهي صلاحية الموافقة خلال 15 دقيقة.

## حالات المهمة

`RECEIVED → PROCESSING → COMPLETED` للقراءة.

`RECEIVED → PROCESSING → WAITING_FOR_APPROVAL → APPROVED → EXECUTING → VERIFYING → COMPLETED أو FAILED` للكتابة، مع إمكانية `REJECTED`.

إعادة التشغيل لا تعيد التنفيذ؛ تتحقق من الواقع والحالة المحفوظة في SQLite.

## ما ليس موجوداً

- لا كود SwiftUI ولا بناء Xcode Cloud ولا إثبات تشغيل على iPhone فعلي.
- لا أسرار أو مفاتيح API ولا Production جاهز.
- لا أحدث نسخة من المستودع الأصلي المحذوف؛ هذه لقطة قديمة موثقة بـ`eb3c224`.
- لا `/v1/health` و`/v1/chat` في هذه اللقطة؛ لا تفترض وجودها دون مراجعة المصدر.
- لا إثبات Secure Enclave أو Tailscale أو LLM حقيقي أو نشر خارجي.

## التحقق الذي تم

- **11/11** اختباراً ناجحاً.
- `typecheck` ناجح للعقد والنواة.
- **0 ثغرات** في فحص الاعتماديات بعد التصحيح.

## طريقة الاستفادة

1. اقرأ `reference/ahmed-v01/PROVENANCE.md` قبل استخدام الكود.
2. حافظ على `packages/contract` و`V0_CONTRACT.md` كمصدر حقيقة للعقد القديم عند الحاجة.
3. انقل العقود والاختبارات الصالحة، لا الافتراضات والواجهات القديمة.
4. ابدأ بأول REAL: iPhone ← Core ← LLM ← رد محفوظ ← حالة المهمة ← Restart.
5. لا تضف أدوات خارجية أو موافقات آلية أو نشراً قبل إثبات هذا المسار والنسخة الاحتياطية والاستعادة.

## حالة الصدق

الكود مفيد كمرجع تنفيذي واختباري، **وليس تطبيق وكيل مكتمل ولا إثبات أن المسار الحالي جاهز للإنتاج**.
