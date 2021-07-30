# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 10:36:56 2021

@author: Diego
"""
#%% Cargo página template

fname = 'mypagetemplate.html'
with open(fname, 'r', encoding="utf-8") as f:
    miwebpage  = f.read()
print('Template cargado')

#%% Cargo lista de precios
fname = 'TEXTO.TXT'
list_ = open(fname).read().split('\n')

fecha = list_[1][25:].strip()
miwebpage = miwebpage.replace('%FECHA%', fecha)

import re
L=[]
resto = []
for line in list_:    
	try:
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
			# if l['unit']=='': #si el precio está vacía salteo
				# continue
			
			L.append(l)
		else:
			resto.append(line)
	except:
		print("Hubo un error al manipular la linea: " + line)
print('Lista cargada')
# 80.702008  FIESTA 8mm ............................. UNI   _  259.050
# 80.705020  VICTORIAN 20mm ......................... Pza   _  245.320
# 80.710000  Raso 0 FLUO x50m ....................... Pza   _  392.430
# 80.723000  galon Pampa ............................ Pza   _  882.050


#%% Convierto lista a string y reemplazo en el template
tabla = ''
for item in L:
    if len(item['unit'])==0:
        # itemlista = ["",'<b>'+item['desc']+'</b>',"","",""]
        # tabla += '<tr>\n<td>'  + '</td>\n<td>'.join(itemlista) + '</td>\n<tr>'        
        stritem = '<tr>\n<td>%s</td>\n<td>%s</td>\n<td>%s</td>\n<td>%s</td>\n<td>%s</td>\n<tr>' % ("",'<b>'+item['desc']+'</b>',"","","")
        tabla += stritem 
    else:
        # itemlista = [item['cod'],item['desc'],item['unidad'],item['unit'],item['iva']]
        # tabla += '<tr>\n<td>'  + '</td>\n<td>'.join(itemlista) + '</td>\n<tr>'
        stritem = '<tr>\n<td>%s</td>\n<td>%s</td>\n<td>%s</td>\n<td style="text-align:right">%s</td>\n<td style="text-align:right">%s</td>\n<tr>' % (item['cod'],item['desc'],item['unidad'],item['unit'],item['iva'])
        tabla += stritem  
miwebpage = miwebpage.replace('%TABLA%', tabla)
    
fname = 'docs/index.html'
with open(fname, 'w', encoding="utf-8") as f:
    f.write(miwebpage)
print('Salida guardada')





    