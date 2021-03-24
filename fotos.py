'''
Este Script inserta imagenes de la manzana selecionada.
si quiere insertar todo un bloque cambiar .selectFeatures() por .getFeatures()
'''
fotos = 'D:/CATASTRO_SICUANI/fotos_fachadas/tupac_amaru/mzna_c'
atributo_foto = 'foto'
atributo = 'id_lote'
# layer 0
mapcanvas = iface.mapCanvas()
layers = mapcanvas.layers()
layer  = layers[0]

import os
#lista de path de fotos
path = []
for i in os.listdir(fotos):
    ruta = fotos + '/' + i
    path.append(ruta)
#lista de cod_lote attributos
idlote = []
for j in layer.selectedFeatures():
    idlote.append(j[atributo])

#unir
lista = []
for i in path:
    for j in idlote:
        if i[-18:-4] == j:
            lista.append(j)
            lista.append(i)
#print(lista)
# diccionario
def dicc(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct
key_fotos = dicc(lista)
#print(key_fotos)

# llenar con el path

layer.startEditing()
feature = layer.selectedFeatures()
ids = []
for i in feature:
    ids.append(i.id())
i = 0
for j in idlote:
    layer.changeAttributeValue(ids[i], layer.fields().lookupField(atributo_foto), key_fotos[j]) #id, campo, rellenar
    i+=1
layer.commitChanges()

iface.messageBar().pushMessage("qgis", "Se inserto fotos fachadas con exito!!!", level=Qgis.Info, duration=2)
