import sys, pprint, importlib.util
def load(path):
    spec=importlib.util.spec_from_file_location('m',path); m=importlib.util.module_from_spec(spec); sys.path.insert(0,'/home/claude/g6build'); spec.loader.exec_module(m); return m
def save(path, L):
    s=open(path).read(); i=s.index('LESSON = {'); j=s.index('\nTEACHER = {')
    open(path,'w').write(s[:i]+'LESSON = '+pprint.pformat(L,width=200,sort_dicts=False)+'\n'+s[j:])
def items(L):
    for sec in ('reconnect',):
        for q in L[sec]['items']: yield q
    for l in L['learn']:
        for q in l.get('checks',[]): yield q
    for q in L['handson']['record']: yield q
    for q in L['think']['items']: yield q
    for q in L.get('exit',[]): yield q
    for pt in L.get('checkpoint',{}).get('parts',[]):
        for q in pt['items']: yield q
def find(L, text):
    r=[q for q in items(L) if text in q['q']]; assert len(r)==1,(text,len(r)); return r[0]
def replace_item(L, text, new):
    for lst in [L['reconnect']['items'], L['handson']['record'], L['think']['items'], L.get('exit',[])]+[l.get('checks',[]) for l in L['learn']]+[pt['items'] for pt in L.get('checkpoint',{}).get('parts',[])]:
        for k,q in enumerate(lst):
            if text in q['q']: lst[k]=new; return
    raise KeyError(text)
def sub(L, a, b):
    import json
    s=json.dumps(L,ensure_ascii=False); A=json.dumps(a,ensure_ascii=False)[1:-1]; B=json.dumps(b,ensure_ascii=False)[1:-1]
    assert A in s, a[:80]; return json.loads(s.replace(A,B))
