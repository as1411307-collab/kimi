import json, re, time
from pathlib import Path
import requests
base=Path('/mnt/agents/output/repo_inventory_work')
repos={'open-design':'nexu-io/open-design','awesome-llm-apps':'Shubhamsaboo/awesome-llm-apps','langflow':'langflow-ai/langflow','ollama':'ollama/ollama'}
s=requests.Session(); s.headers['Accept']='application/vnd.github+json'; s.headers['User-Agent']='repo-inventory'

def get(url):
    for attempt in range(3):
        try:
            r=s.get(url,timeout=60)
            if r.status_code==200: return r
            print('HTTP',r.status_code,url,r.text[:160])
            if r.status_code in (403,429): raise RuntimeError('Rate limit or forbidden')
        except requests.RequestException as e:
            print('retry',attempt+1,url,str(e)[:120])
        time.sleep(2)
    raise RuntimeError('failed '+url)

for name,repo in repos.items():
    first=f'https://api.github.com/repos/{repo}/branches?per_page=100&page=1'
    r=get(first); items=r.json(); links=r.headers.get('Link','')
    m=re.search(r'[?&]page=(\d+)>; rel="last"',links)
    last=int(m.group(1)) if m else 1
    for p in range(2,last+1):
        items.extend(get(f'https://api.github.com/repos/{repo}/branches?per_page=100&page={p}').json())
    (base/f'{name}.branches.json').write_text(json.dumps(items,ensure_ascii=False,indent=2))
    (base/f'{name}.branches.txt').write_text('\n'.join(f"{x['name']}\t{x['commit']['sha']}" for x in items)+'\n')
    print(name,'branches=',len(items),'pages=',last,'main=',next((x['commit']['sha'] for x in items if x['name']=='main'),'not-on-listed-pages'))
print('remaining',get('https://api.github.com/rate_limit').json()['resources']['core']['remaining'])
