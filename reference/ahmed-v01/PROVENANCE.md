# مصدر وحدود نسخة ahmed-v01

## المصدر

- المستودع: `yjtjcfc5cm-boop/ahemed--agent-v01`.
- الـ commit الأصلي: `eb3c224542686ee4d8b3203be867de71fd0d2ce9`.
- هذه **لقطة قديمة** وليست أحدث حالة للمستودع الأصلي `as1411307-collab/ahemed--agent-v01` الذي لم يعد متاحاً.

## ما نُقل انتقائيًا

- `apps/core`: Fastify + TypeScript + حالة وعقود وأدوات واختبارات.
- `packages/contract`: أنواع العقد المشترك.
- `V0_CONTRACT.md`: عقد الرسائل والمهام والموافقات والاسترجاع.
- `docs/BUILD_PROMPT.md` و`docs/VISION.md`: تعليمات ومرجع تصميم قديمان.
- ملفات npm workspaces وTypeScript وpackage-lock.

لم ننقل واجهة Expo ولا n8n ولا أسراراً ولا ادعاء أن هذه أحدث نسخة إنتاجية.

## التعديلات المطبقة قبل الإضافة

1. استبدال `better-sqlite3` بـ `node:sqlite` المدمج في Node 22، مع غلاف transaction يحافظ على ACID.
2. تحديث أنواع نتائج `node:sqlite` لتتوافق مع TypeScript.
3. إزالة Expo من npm workspaces ومن الاعتماديات غير المطلوبة للـ Core.
4. إزالة `better-sqlite3` و`@types/better-sqlite3` من الاعتماديات وتحديث `package-lock.json`.
5. تصحيح مسار حالة الاختبار ليمر بالحالات الصحيحة، وإضافة اختبار رفع الملف وتلخيصه.
6. تطبيق `npm audit fix` على التبعيات.

## التحقق المنفذ

- `npm test`: **11/11 اختباراً ناجحاً** على ملفين (`slice.test.ts` و`unit.test.ts`).
- `npm run typecheck`: نجاح لكل من `contract` و`core`.
- `npm audit --omit=dev`: **0 ثغرات** بعد التصحيح.
- التحقق يتطلب Node 22 وتفعيل `NODE_OPTIONS=--experimental-sqlite`.

## الحالة والحدود

- الكود **مرجع قابل للاستخدام والتطوير**، وليس تطبيق وكيل مكتمل أو إثبات Production.
- العقد هنا v0.1 ولا يمثل تلقائياً أحدث عقود مسارات `/v1/health` و`/v1/chat` اللاحقة غير الموجودة في هذه اللقطة.
- لا يوجد تطبيق SwiftUI في هذه النسخة، ولا إثبات Secure Enclave أو Xcode Cloud أو نشر على جهاز فعلي.
- `docs/BUILD_PROMPT.md` و`docs/VISION.md` تاريخيان وقد يتعارضان مع القرار الحالي Swift 6 الأصيل؛ عند التعارض، القرار الحالي يتقدم.
- قبل أي استخدام إنتاجي، يلزم اختبار من iPhone فعلي ← Core ← LLM ← رد محفوظ ← Restart، مع نسخة احتياطية مختبرة الاستعادة.
