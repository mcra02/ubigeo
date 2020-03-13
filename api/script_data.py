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
