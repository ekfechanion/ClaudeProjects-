import json
p=json.load(open('part1.json'))
L1=('<ul>'
 '<li><a href="https://ekfechanion.eu/files/Books/lab_activities_lyk_book.pdf">Οδηγός εργαστηριακών δραστηριοτήτων Φυσικής</a>: Ιδέες και προτάσεις για εφαρμογή στο εργαστήριο αλλά και την τάξη (<em>Ν.Αναστασάκης, 2017</em>)</li>'
 '<li><a href="https://drive.google.com/file/d/0ByluOFI8PPiiMV9CcDN0WGZhalE/view?usp=drive_link&amp;resourcekey=0-PDvof9cigcMxhVDcIWEIhg">Εργαστηριακές ασκήσεις στην ύλη της Χημείας Α’ Λυκείου</a> <em>(Δ.Μαρκογιαννάκης, Κ.Παπαθανασίου, 2015)</em></li>'
 '<li><a href="https://ekfechanion.eu/wp-content/uploads/2024/10/Xhmikes-ousies-Asymvatothta.pdf">Ασυμβατότητα Χημικών Ουσιών</a></li>'
 '<li><a href="https://ekfechanion.eu/files/chemsefe-final.html">Χημικές Ουσίες</a>: Κατάλογος, ιδιότητες, ταυτοποίηση, προφυλάξεις</li>'
 '</ul>')
L2=('<ul>'
 '<li><a href="https://ekfechanion.eu/2023/11/08/fyllo-ergasias-anafora/" target="_blank">Φύλλα εργασίας και εργαστηριακή αναφορά</a>: Υποδείγματα εφαρμογής της διερευνητικής προσέγγισης.</li>'
 '<li><a href="https://prezi.com/c0l2qaiz3nwg/metriseis-k-sfalmata/" target="_blank">Μετρήσεις – σφάλματα</a>: Μια παρουσίαση από το ΕΚΦΕ Ρεθύμνου</li>'
 '<li><a href="https://ekfechanion.eu/2024/10/02/asfaleia-sto-ergastirio-f-e/">Ασφάλεια στο εργαστήριο</a></li>'
 '<li><a href="https://ekfechanion.eu/2023/09/20/promitheftes-exoplismoy/">Προμηθευτές</a></li>'
 '</ul>')
xml2=('<e-flexbox configuration-id="res"><e-svg configuration-id="res-icon"></e-svg>'
 '<e-flexbox configuration-id="res-row"><e-paragraph configuration-id="res-l1"></e-paragraph><e-paragraph configuration-id="res-l2"></e-paragraph></e-flexbox></e-flexbox>'
 '<e-flexbox configuration-id="div-row"><e-divider configuration-id="div"></e-divider></e-flexbox>'
 '<e-flexbox configuration-id="btns"><e-button configuration-id="btn1"></e-button><e-button configuration-id="btn2"></e-button><e-button configuration-id="btn3"></e-button></e-flexbox>')
cfg=p['cfg'];cls=p['cls'];st={};inter=p['inter']
cfg['res']={"tag":"section"}; cfg['subjects']={"tag":"section"}
cfg['res-icon']={"svg":{"value":"far fa-check-circle","library":"fa-regular"}}
cfg['res-l1']={"paragraph":L1,"tag":"span"}; cfg['res-l2']={"paragraph":L2,"tag":"span"}
cfg['btn1']={"text":"Εργαστηριακοί Οδηγοί","link":{"destination":"https://ekfechanion.eu/2023/09/18/ergastiriakoi-odigoi/"}}
cfg['btn2']={"text":"Οδηγίες Διδασκαλίας","link":{"destination":"https://ekfechanion.eu/2023/10/13/odigies-didaskalias-fe/"}}
cfg['btn3']={"text":"Νέα Προγράμματα Σπουδών","link":{"destination":"https://iep.edu.gr/el/nea-ps-provoli","isTargetBlank":True}}
cls['res-icon']=['ekfe-resources-icon']; cls['res-l1']=['ekfe-link-list']; cls['res-l2']=['ekfe-link-list']
cls['res-row']=['ekfe-section']; cls['div-row']=['ekfe-section']; cls['btns']=['ekfe-section']
for b in ('btn1','btn2','btn3'): cls[b]=['ekfe-btn-main']
st['subjects']='padding-top: 40px; padding-bottom: 30px;'
st['res']='display: flex; flex-direction: column; align-items: center; gap: 20px; padding: 10px 10px 40px 10px;'
st['res-row']='gap: 100px; @media (--tablet) { gap: 10px; }'
st['res-l1']='display: block;'; st['res-l2']='display: block;'
st['div-row']='padding-top: 0px; padding-bottom: 30px;'
st['div']='flex: 1 1 auto; width: 100%; max-width: 100%; height: 1px; background-color: #000000;'
st['btns']='justify-content: center; align-items: center; gap: 85px; padding-top: 50px; padding-bottom: 50px; @media (--tablet) { align-items: center; } @media (--mobile) { gap: 30px; flex-direction: column; align-items: center; }'
inter['res-icon']=inter['fiz-icon']
args={"post_id":22627,"parent_id":"document","mode":"replace_children","xml_structure":p['xml']+xml2,"element_config":cfg,"classes":cls,"style":st,"interactions":inter}
json.dump(args,open('build.json','w'),ensure_ascii=False)
a=dict(args);a['dry_run']=True;json.dump(a,open('build_dry.json','w'),ensure_ascii=False)
