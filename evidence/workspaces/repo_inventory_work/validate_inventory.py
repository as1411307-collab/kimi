import json,re,sys
from pathlib import Path
from PIL import Image
base=Path('/mnt/agents/output/repo_inventory_work')
out=Path('/mnt/agents/output')
repos={'open-design':('nexu-io/open-design',16766,14266,2500,2852),'awesome-llm-apps':('Shubhamsaboo/awesome-llm-apps',2547,1989,558,15),'langflow':('langflow-ai/langflow',14234,11878,2356,2660),'ollama':('ollama/ollama',1834,1632,202,493)}
errors=[]; notes=[]
def check(ok,msg):
    (notes if ok else errors).append(('PASS ' if ok else 'FAIL ')+msg)
for name,(slug,entries_n,files_n,dirs_n,branches_n) in repos.items():
    tree=json.loads((base/f'{name}.tree.json').read_text()); entries=tree['tree']
    files=sum(x['type']=='blob' for x in entries); dirs=sum(x['type']=='tree' for x in entries)
    check(tree.get('truncated') is False,f'{name}: tree not truncated')
    check((len(entries),files,dirs)==(entries_n,files_n,dirs_n),f'{name}: tree counts {len(entries)}/{files}/{dirs}')
    branches=json.loads((base/f'{name}.branches.json').read_text())
    names=[x['name'] for x in branches]
    check(len(branches)==branches_n and len(set(names))==branches_n,f'{name}: {branches_n} unique branches')
    main=next((x['commit']['sha'] for x in branches if x['name']=='main'),None)
    check(main==tree['sha'],f'{name}: main SHA matches tree snapshot')

report=(out/'تقرير_جرد_المستودعات_الأربعة.md').read_text()
check('35,381' in report and '29,765' in report and '6,020' in report,'report totals present')
check('7 أمثلة مخصصة للذاكرة' in report,'Awesome memory count corrected to 7')
check('8 مهارات في `agent_skills`' in report,'Awesome skill count corrected to 8')
check('/mnt/agents/output/repo_inventory_work' not in report,'no scratch path in report')
check('6 أمثلة مخصصة للذاكرة' not in report and '9 مجلدات في `agent_skills`' not in report,'no superseded counts in report')

# Branch register must contain one SHA-bearing line per branch.
branch_lines=[l for l in (out/'السجل_الكامل_للفروع.txt').read_text().splitlines() if re.search(r'\t[0-9a-f]{40}\t',l)]
check(len(branch_lines)==6020,f'branch register contains 6020 records (found {len(branch_lines)})')
# Path index: data lines carry blob/tree/commit.
path_lines=[l for l in (out/'الفهرس_الكامل_لمسارات_المستودعات.txt').read_text().splitlines() if re.match(r'^(blob|tree|commit)\t',l)]
check(len(path_lines)==35381,f'path index contains 35381 records (found {len(path_lines)})')

# Validate key catalog counts from Open Design directly.
od=json.loads((base/'open-design.tree.json').read_text())['tree']; paths={x['path'] for x in od}; dirs={x['path'] for x in od if x['type']=='tree'}
def children(root):
    p=root+'/'
    return sorted({q[len(p):].split('/')[0] for q in dirs if q.startswith(p) and len(q)>len(p)})
for root,marker,n in [('skills','SKILL.md',169),('design-templates','SKILL.md',115),('design-systems','DESIGN.md',152)]:
    got=sum(f'{root}/{c}/{marker}' in paths for c in children(root))
    check(got==n,f'Open Design {root}: {got} marked packages')
manifests=[p for p in paths if p.startswith('plugins/_official/') and p.endswith('/open-design.json')]
check(len(manifests)==479,f'Open Design official plugin manifests: {len(manifests)}')

# All these deep-dive paths must exist as file or directory.
required={
'open-design':['docs/architecture.md','docs/agent-adapters.md','apps/daemon/src/runtimes','docs/skills-protocol.md','plugins/spec/SPEC.md','plugins/spec/AGENT-DEVELOPMENT.md','packages/plugin-runtime','apps/daemon/src/media','design-templates/hyperframes','skills/video-hyperframes','skills/speech','prompt-templates/video','apps/daemon/src/api-token-auth.ts','apps/daemon/tests','packages/contracts/src/api/artifact-lint.ts','e2e'],
'awesome-llm-apps':['advanced_llm_apps/llm_apps_with_memory_tutorials','advanced_llm_apps/chat_with_X_tutorials','ai_agent_framework_crash_course','rag_tutorials','mcp_ai_agents','agent_skills','advanced_ai_agents/multi_agent_apps/multi_agent_trust_layer','advanced_ai_agents/multi_agent_apps/trust_gated_agent_team','advanced_ai_agents/single_agent_apps/ai_agent_governance','voice_ai_agents','generative_ui_agents','advanced_llm_apps/multimodal_video_moment_finder','always_on_agents','advanced_llm_apps/llm_optimization_tools','advanced_llm_apps/llm_finetuning_tutorials'],
'langflow':['docs/docs/Agents','src/backend/base/langflow/api','src/lfx/src/lfx/components','docs/docs/Develop/memory.mdx','docs/docs/Develop/memory-bases.mdx','docs/docs/Components','src/backend/base/langflow/base/memory','src/backend/base/langflow/api/v1/voice_mode.py','src/backend/base/langflow/utils/voice_utils.py','src/frontend','docs/docs/Develop/concepts-voice-mode.mdx','SECURITY.md','docs/docs/Develop/authentication-overview.mdx','docs/docs/Develop/api-keys-and-authentication.mdx','docs/docs/Develop/authorization.mdx','src/backend/tests','docker','deploy','DEVELOPMENT.md','DESIGN.md','BUNDLE_API.md','regressions','src/lfx/src/lfx/components/tools/yahoo_finance.py','src/backend/base/langflow/initial_setup/starter_projects/Financial Report Parser.json','src/bundles/lfx-bundles/src/lfx_bundles/twelvelabs','src/bundles/lfx-bundles/src/lfx_bundles/youtube'],
'ollama':['api','server','openai','anthropic','docs/openapi.yaml','cmd/speech.go','server/speech.go','server/transcription.go','llm/speech.go','docs/capabilities/speech.mdx','integration/audio_test.go','model/parsers','model/renderers','thinking','tools','llm/gbnf.go','mlxrunner/xgrammar','openai/responses_compact.go','server/responses_compact.go','app/store','middleware/web_search.go','app/tools','cmd/launch','internal/proxy','docs/integrations','llm','llama','mlxrunner','discover','create','compatmigrate','integration']}
for name,reqs in required.items():
    tree=json.loads((base/f'{name}.tree.json').read_text())['tree']; ps={x['path'] for x in tree}
    for p in reqs: check(p in ps,f'{name}: required path exists: {p}')

im=Image.open(out/'ملخص_جرد_المستودعات_الأربعة.png')
check(im.size in [(1080,1720),(2160,3440)],f'infographic dimensions {im.size} (1x or 2x of 1080x1720)')
for line in notes:
    if 'required path' not in line: print(line)
print(f'Path existence assertions: {sum("required path" in x for x in notes)} passed')
print(f'\nRESULT: {len(notes)} passed; {len(errors)} failed')
for e in errors: print(e)
if errors: sys.exit(1)
