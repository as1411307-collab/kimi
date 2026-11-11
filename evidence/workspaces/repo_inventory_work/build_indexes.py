import json, collections
from pathlib import Path
base=Path('/mnt/agents/output/repo_inventory_work')
repos=['open-design','awesome-llm-apps','langflow','ollama']
stats={}
for name in repos:
    data=json.loads((base/f'{name}.tree.json').read_text())
    entries=data['tree']
    blobs=[x for x in entries if x['type']=='blob']; dirs=[x for x in entries if x['type']=='tree']; commits=[x for x in entries if x['type']=='commit']
    with (base/f'{name}.paths.txt').open('w') as f:
        f.write(f'# {name} — main — complete recursive Git tree\n')
        f.write(f'# entries={len(entries)} files={len(blobs)} directories={len(dirs)} submodules={len(commits)} truncated={data.get("truncated")}\n')
        for x in sorted(entries,key=lambda z:z['path']):
            f.write(f"{x['type']}\t{x.get('size','')}\t{x['path']}\n")
    ext=collections.Counter()
    for x in blobs:
        p=x['path']; fn=p.rsplit('/',1)[-1]
        suffix='.'+fn.split('.',1)[1] if '.' in fn else '[no extension]'
        if len(suffix)>35: suffix=Path(fn).suffix or '[no extension]'
        ext[suffix]+=1
    roots=collections.Counter(x['path'].split('/')[0] for x in entries)
    bfile=base/f'{name}.branches.json'
    branches=json.loads(bfile.read_text()) if bfile.exists() else []
    prefixes=collections.Counter((b['name'].split('/')[0] if '/' in b['name'] else '[root]') for b in branches)
    stats[name]={
        'tree_sha':data.get('sha'),'truncated':data.get('truncated'),'entries':len(entries),'files':len(blobs),'directories':len(dirs),'submodules':len(commits),
        'blob_bytes':sum(x.get('size',0) for x in blobs),'top_extensions':ext.most_common(20),'root_entry_counts':dict(sorted(roots.items())),
        'branches':len(branches),'main_commit':next((b['commit']['sha'] for b in branches if b['name']=='main'),None),
        'branch_prefixes':prefixes.most_common(25)
    }
(base/'inventory_stats.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2))
for name,s in stats.items():
    print('\n===',name,'===')
    print({k:s[k] for k in ['entries','files','directories','submodules','truncated','branches','main_commit']})
    print('Top extensions:',s['top_extensions'][:10])
    print('Branch prefixes:',s['branch_prefixes'][:10])
