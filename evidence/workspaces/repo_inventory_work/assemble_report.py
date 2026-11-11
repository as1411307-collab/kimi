from pathlib import Path
import re
base=Path('/mnt/agents/output/repo_inventory_work')
out=Path('/mnt/agents/output')
report=out/'تقرير_جرد_المستودعات_الأربعة.md'
intro=report.read_text()
intro=intro.replace('`REAL`: multi-agent orchestration وhandoffs/workflows','`REAL`: multi-agent orchestration وA2A وworkflows')
intro=intro.replace('مكتبة أمثلة ومشاريع مستقلة ومهارات ودروس للوكلاء وRAG والصوت والذاكرة وMCP وUI','144 مشروعاً/مثالاً مستقلاً + 8 مهارات + 21 درساً للوكلاء وRAG والصوت والذاكرة وMCP وUI')

def clean(name):
    s=(base/name).read_text()
    s=s.replace('\n---\n','\n')
    # Remove methodology blockquotes that mention local working files; the report introduction covers method.
    lines=s.splitlines()
    lines=[l for l in lines if not any(x in l for x in ['open-design.tree.json','awesome-llm-apps.tree.json','awesome-llm-apps.branches.json','langflow.tree.json','langflow.branches.json','langflow.head.txt','ollama.tree.json','ollama.branches.json'])]
    s='\n'.join(lines)
    if name.startswith('langflow'):
        s=s.replace('**الثغرات/الاعتبارات**','**ملاحظات تقنية/حوكمة — ليست ثغرات مثبتة**')
        s=s.replace('**لا معالجة فيديو/صوت أصلية** — تعتمد كلياً على مزودين خارجيين (TwelveLabs, AssemblyAI...).','**لا معالجة فيديو أصلية** — الفيديو عبر مزودين خارجيين؛ أما Voice Mode فواجهته وتنسيقه مدمجان، بينما يعتمد التعرف/التوليد على مزودين مثل AssemblyAI وfunasr.')
        s=s.replace('**113 ملف مكوّن** عبر 28 حزمة مورّد.','**نحو 113 ملف مكوّن** عبر 28 حزمة مورّد، بحسب تصنيف ملفات المكونات في هذا الجرد.')
    return s.strip()+'\n'

def demote(s,section,title,slug):
    lines=s.splitlines()
    # Drop source H1; every remaining heading goes down two levels.
    rest=[]
    for l in lines[1:]:
        m=re.match(r'^(#{1,6})\s',l)
        if m: l='##' + l
        rest.append(l)
    return f'### {section} {title}\n\n**المصدر الرسمي:** [{slug}@main](https://github.com/{slug}/tree/main).\n\n'+'\n'.join(rest).lstrip()+'\n'

od=demote(clean('open-design.analysis.md'),'6.1','Open Design — الجرد التفصيلي','nexu-io/open-design')
aw=demote(clean('awesome-llm-apps.final.md'),'6.2','Awesome LLM Apps — الجرد التفصيلي','Shubhamsaboo/awesome-llm-apps')
lf=demote(clean('langflow.analysis.md'),'6.3','Langflow — الجرد التفصيلي','langflow-ai/langflow')
ol=demote(clean('ollama.final.md'),'6.4','Ollama — الجرد التفصيلي','ollama/ollama')
branches=(base/'branches.section.md').read_text()
recs=(base/'recommendations.section.md').read_text()
appendix='''\n## 9. دليل الملفات المرفقة\n\n- **هذا التقرير:** الخريطة المختصرة + الجرد التفصيلي + الفروع + حزم التوسع المرمزة.\n- **`الفهرس_الكامل_لمسارات_المستودعات.txt`:** كل الـ35,381 مدخلاً في أشجار `main`، مع النوع والحجم والمسار وSHA لكل لقطة. استخدمه للبحث عن أي ملف لا يظهر في العناوين المختصرة.\n- **`السجل_الكامل_للفروع.txt`:** كل الـ6,020 فرعاً مع SHA وحالة الحماية المتاحة. لا يعني السجل أن محتوى كل فرع تمت قراءته.\n- **`ملخص_جرد_المستودعات_الأربعة.png`:** خريطة بصرية من صفحة واحدة للمشاركة والمراجعة السريعة.\n- **`جرد_المستودعات.kanva.pptd`:** النسخة القابلة للتحرير من الخريطة البصرية.\n\n**الحد النهائي للمرحلة:** لم أستخرج الأكواد ولم أشغّل المشاريع. المرحلة التالية تبدأ فقط بالرموز التي تختارها أنت من القسم 8.\n'''
report.write_text(intro.rstrip()+'\n\n'+od+'\n'+aw+'\n'+lf+'\n'+ol+'\n'+branches+'\n'+recs+'\n'+appendix)
print('report bytes',report.stat().st_size,'lines',len(report.read_text().splitlines()))
for bad in ['repo_inventory_work','.tree.json','.branches.json','langflow.head.txt']:
    assert bad not in report.read_text(), bad
