import json,re,html
d=json.load(open('acc.json'))
subjects=[('fiz','Φυσική','fas fa-atom'),('xim','Χημεία','fas fa-flask'),('bio','Βιολογία','fas fa-leaf')]
xml=['<e-flexbox configuration-id="subjects">']
cfg={};cls={};inter={}
cls['subjects']=['ekfe-section']
fade=[{"trigger":"scrollIn","animation":{"effect":"fade","type":"in","direction":"","timing_config":{"duration":{"unit":"ms","size":600},"delay":{"unit":"ms","size":0}}}}]
def clean(p):
    p=re.sub(r'^<p>|</p>$','',p.strip()); p=html.unescape(p).replace('\xa0',' ')
    return re.sub(r'\s+',' ',p).strip()
for (k,name,icon),items in zip(subjects,d):
    xml.append(f'<e-flexbox configuration-id="{k}-col"><e-svg configuration-id="{k}-icon"></e-svg><e-heading configuration-id="{k}-title"></e-heading><e-accordion configuration-id="{k}-acc">')
    cls[f'{k}-col']=['ekfe-subject-col']; cls[f'{k}-icon']=['ekfe-subject-icon']; cls[f'{k}-title']=['ekfe-subject-title']; cls[f'{k}-acc']=['ekfe-accordion']
    cfg[f'{k}-icon']={"svg":{"value":icon,"library":"fa-solid"}}
    cfg[f'{k}-title']={"title":name,"tag":"h3"}
    cfg[f'{k}-acc']={"default_state":"all_collapsed","max_expanded":"one","show_icon":True}
    inter[f'{k}-icon']=fade
    for n,it in enumerate(items,1):
        p=f'{k}{n}'
        btn=it['buttons'][0] if it['buttons'] else None
        xml.append(f'<e-accordion-item configuration-id="{p}"><e-accordion-item-header configuration-id="{p}-h"><e-accordion-item-icon configuration-id="{p}-i"><e-svg configuration-id="{p}-is"></e-svg></e-accordion-item-icon><e-accordion-item-title configuration-id="{p}-t"><e-paragraph configuration-id="{p}-tp"></e-paragraph></e-accordion-item-title></e-accordion-item-header><e-accordion-item-content configuration-id="{p}-c"><e-paragraph configuration-id="{p}-txt"></e-paragraph>'+(f'<e-button configuration-id="{p}-b"></e-button>' if btn else '')+'</e-accordion-item-content></e-accordion-item>')
        cls[f'{p}-h']=['ekfe-acc-header'];cls[f'{p}-i']=['ekfe-acc-icon'];cls[f'{p}-is']=['ekfe-acc-svg'];cls[f'{p}-tp']=['ekfe-acc-title'];cls[f'{p}-c']=['ekfe-acc-content'];cls[f'{p}-txt']=['ekfe-acc-text']
        cfg[f'{p}-is']={"svg":{"value":"fas fa-caret-down","library":"fa-solid"}}
        cfg[f'{p}-tp']={"paragraph":it['title'],"tag":"span"}
        cfg[f'{p}-txt']={"paragraph":clean(' '.join(it['text']))}
        if btn:
            cls[f'{p}-b']=['ekfe-btn-small']
            cfg[f'{p}-b']={"text":btn[1],"link":{"destination":html.unescape(btn[0])}}
    xml.append('</e-accordion></e-flexbox>')
xml.append('</e-flexbox>')
json.dump({"xml":''.join(xml),"cfg":cfg,"cls":cls,"inter":inter},open('part1.json','w'),ensure_ascii=False)
print(len(''.join(xml)), len(json.dumps(cfg,ensure_ascii=False)))
