import json,re,sys
from pathlib import Path
base=Path('/mnt/agents/output/repo_inventory_work')
r=Path('/mnt/agents/output/تقرير_جرد_المستودعات_الأربعة.md').read_text()
errors=[]
sections={'open-design':r.split('### 6.1')[1].split('### 6.2')[0],'awesome-llm-apps':r.split('### 6.2')[1].split('### 6.3')[0],'langflow':r.split('### 6.3')[1].split('### 6.4')[0],'ollama':r.split('### 6.4')[1].split('## 7.')[0]}
def children(repo,root,typ='tree'):
    x=json.loads((base/f'{repo}.tree.json').read_text())['tree']; p=root+'/'
    return sorted({e['path'][len(p):].split('/')[0] for e in x if e['type']==typ and e['path'].startswith(p) and len(e['path'])>len(p)})
checks=[]
for root in ['skills','design-templates','design-systems']:
    for n in children('open-design',root): checks.append(('open-design',f'{root}/{n}',n))
for cat in children('open-design','plugins/_official'):
    for n in children('open-design',f'plugins/_official/{cat}'): checks.append(('open-design',f'plugin {cat}/{n}',n))
for root in ['agent_skills','always_on_agents','generative_ui_agents','mcp_ai_agents','rag_tutorials','starter_ai_agents','voice_ai_agents','advanced_llm_apps']:
    for n in children('awesome-llm-apps',root): checks.append(('awesome-llm-apps',f'{root}/{n}',n))
for root in ['autonomous_game_playing_agent_apps','single_agent_apps','multi_agent_apps']:
    for n in children('awesome-llm-apps',f'advanced_ai_agents/{root}'): checks.append(('awesome-llm-apps',f'{root}/{n}',n))
for n in children('awesome-llm-apps','advanced_ai_agents/multi_agent_apps/agent_teams'): checks.append(('awesome-llm-apps',f'team/{n}',n))
for root in ['chat_with_X_tutorials','cursor_ai_experiments','llm_apps_with_memory_tutorials','llm_finetuning_tutorials','llm_optimization_tools']:
    for n in children('awesome-llm-apps',f'advanced_llm_apps/{root}'): checks.append(('awesome-llm-apps',f'{root}/{n}',n))
for course in children('awesome-llm-apps','ai_agent_framework_crash_course'):
    checks.append(('awesome-llm-apps',f'course/{course}',course))
    for n in children('awesome-llm-apps',f'ai_agent_framework_crash_course/{course}'): checks.append(('awesome-llm-apps',f'course {course}/{n}',n))
for n in children('langflow','src/backend/base/langflow/initial_setup/starter_projects','blob'):
    if n.endswith('.json'): checks.append(('langflow',f'starter/{n}',n[:-5]))
for repo,where,n in checks:
    if n not in sections[repo]: errors.append(f'{repo}: missing catalog item {where} => {n}')
root_total=0
for repo,s in sections.items():
    x=json.loads((base/f'{repo}.tree.json').read_text())['tree']; roots=sorted({e['path'].split('/')[0] for e in x})
    for n in roots:
        root_total+=1
        if n not in s: errors.append(f'{repo}: missing root entry {n}')
for needle in ['### 6.1 Open Design','### 6.2 Awesome LLM Apps','### 6.3 Langflow','### 6.4 Ollama','## 7. قراءة الفروع','## 8. القوائم المرشحة','## 9. دليل الملفات']:
    if needle not in r: errors.append('missing section '+needle)
for bad in ['repo_inventory_work','.tree.json','.branches.json','langflow.head.txt','9 Agent Skills','6 أمثلة مخصصة للذاكرة']:
    if bad in r: errors.append('forbidden/superseded text '+bad)
print(f'Catalog names checked: {len(checks)}; root entries checked: {root_total}')
print(f'RESULT: {len(errors)} issues')
for e in errors[:100]: print(e)
if errors: sys.exit(1)
