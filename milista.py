# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 10:36:56 2021

@author: Diego
"""

fname = 'e:/repos/listanegocio/TEXTO.TXT'

fname = 'e:/repos/listanegocio/mypage.html'
with open(fname, 'r', encoding="utf-8") as f:
    miwebpage  = f.read()
print(miwebpage  )



#%%
fname = 'e:/repos/listanegocio/TEXTO.TXT'
list_ = open(fname).read().split('\n')


fecha = list_[1][25:].strip()

import re
L=[]
for line in list_:    
    if re.match("^\d", line): # si empieza con un dígito
        l={}
        l['line'] = line
        l['cod'] = line[:11].strip()
        l['desc'] = line[11:52].strip()
        l['desc'] = re.sub('[\.]{3,}','',l['desc'])
        l['unidad'] = line[52:55].strip()
        unit = line[59:].strip().replace(',','')
        if len(unit.strip())==0:
            l['unit'] = ''
            l['iva'] = ''
        else:
            l['unit'] = ('%.2f')  % (float(unit))
            l['iva'] = ('%.2f')  % (round(float(l['unit'])*1.21,2))
        # print(line)
        # print(l)
        if len(l['desc'])==0: #si la descripción está vacía salteo
            continue
        if l['unit']=='': #si el precio está vacía salteo
            continue
        
        L.append(l)
print(L)
# 80.702008  FIESTA 8mm ............................. UNI   _  259.050
# 80.705020  VICTORIAN 20mm ......................... Pza   _  245.320
# 80.710000  Raso 0 FLUO x50m ....................... Pza   _  392.430
# 80.723000  galon Pampa ............................ Pza   _  882.050

tabla = ''
for item in L:
   itemlista = [item['cod'],item['desc'],item['unidad'],item['unit'],item['iva']]
   tabla += '<tr>\n<td>'  + '</td>\n<td>'.join(itemlista) + '</td>\n<tr>'
   

out = miwebpage.replace('%TABLA%', tabla)
out = out.replace('%FECHA%', fecha)
    
fname = 'out.html'
with open(fname, 'w', encoding="utf-8") as f:
    f.write(out)



#    <tr>
  #   <td>Koniglich Essen</td>
  #   <td>Germany</td>
  #   <td>Alfreds Futterkiste</td>
  #   <td>Germany</td>
  # </tr>
  # nii_t1_1mm_filename = '/'.join(st_t1.split('/')[-5:]).replace('T1', 'T1_1mm')


    