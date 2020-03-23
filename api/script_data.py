import pandas as pd
import pickle
import json

from api.serializers import (
    DepartamentoSerializer,
    ProvinciaSerializer,
    DistritoSerializer
)
import psycopg2

class ScriptExcel:

    def extractData(self, file, key, encabezado):
        pickle_in = open(file,"rb")
        example_dict = pickle.load(pickle_in)
        archivo = pd.read_excel(example_dict)
        values = archivo[key].values
        columnas = encabezado
        df_seleccionados = archivo[columnas]
        data = df_seleccionados.to_json(orient='records')
        return data

    def mapData(self, data):
        first_element = data[0]
        arguments = [*first_element]
        indice = len(arguments)
        elements = []
        elm_index = -1
        for item in reversed(arguments):
            items = []
            if item != arguments[0]:
                for element in data:
                    if item != arguments[len(arguments)-1]:
                        obj_position = {"name": element[arguments[indice]], "descripcion": arguments[indice] + " de " + element[arguments[indice]]}
                        if elm_index > 0:
                            obj_position_child = {"name": element[arguments[indice+1]], "descripcion": arguments[indice+1] + " de " + element[arguments[indice+1]]}
                            ant_elemnt_child = elements[elm_index-1]
                            position_child = ant_elemnt_child[arguments[indice+1]].index(obj_position_child) + 1
                            obj_position = {"name": element[arguments[indice]], "descripcion": arguments[indice] + " de " + element[arguments[indice]],arguments[indice+1].lower(): position_child }
                        ant_elemnt = elements[elm_index]
                        position = ant_elemnt[arguments[indice]].index(obj_position) + 1
                        obj = {"name": element[item], "descripcion": item + " de " + element[item], arguments[indice].lower(): position}
                    else:
                        obj = {"name": element[item], "descripcion": item + " de " + element[item]}
                    if obj not in items:
                        items.append(obj)
                elements.append({item: items})
                elm_index += 1            
            indice -= 1
        return elements

    def inserData(self, data):

        #preparanmos el Serializar con los elementos:
        #  si ubie se uno elemento  data =(a:"",b:"")
        # si fueran varios data = {(a:"",b:""),(a:"",b:""),...,(a:"",b:"")}  many= True
        serializerDepartamento = DepartamentoSerializer(data=data[0]["Departamento"],many=True)
        
        
        #print(serializerProvincia.is_valid(raise_exception=True))
        #validamos los campos
        # raise_exception= True es para que envie automaticamente el error por http
        if serializerDepartamento.is_valid(raise_exception=True):
            #si son correctos guardamos
            serializerDepartamento.save()
        
        """else:
            print(serializerDepartamento.errors)"""

        #repetimos
        serializerProvincia = ProvinciaSerializer(data=data[1]["Provincia"],many=True)

        if serializerProvincia.is_valid():
            serializerProvincia.save()
        

        serializerDistrito = DistritoSerializer(data=data[2]["Distrito"],many=True)

        if serializerDistrito.is_valid():
            serializerDistrito.save()
        

        """print(data[0])"""