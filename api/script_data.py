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

        connection = psycopg2.connect(user="postgres",
                                      password="admin",
                                      host="127.18.0.1",
                                      port="5432",
                                      database="VEOX_2020_DEV")
        obj_depatamento = data[0]
        departamentos = obj_depatamento['Departamento']
        for dato in departamentos:
            cursor = connection.cursor()
            sql_insert_query = """ INSERT INTO GN.GN_REGION (in_id_pais, vc_nombre, vc_descripcion, vc_ubigeo, bo_estado, vc_id_usuario_creacion, vc_id_usuario_modificacion, ts_fecha_creacion, ts_fecha_modificacion) 
                            VALUES ('1',%s,%s,'','1','VEOX','VEOX','NOW()','NOW()') """
            records = [ (dato['name'], dato['descripcion']) ]

            # executemany() to insert multiple rows rows
            result = cursor.executemany(sql_insert_query, records)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into mobile table")
        
        obj_provincia = data[1]
        provincias = obj_provincia['Provincia']
        for dato in provincias:
            cursor = connection.cursor()
            sql_insert_query = """ INSERT INTO GN.GN_PROVINCIA (in_id_region, vc_nombre, vc_descripcion, vc_ubigeo, bo_estado, vc_id_usuario_creacion, vc_id_usuario_modificacion, ts_fecha_creacion, ts_fecha_modificacion) 
                            VALUES (%s,%s,%s,'','1','VEOX','VEOX','NOW()','NOW()') """
            records = [ (dato['departamento'],dato['name'], dato['descripcion']) ]

            # executemany() to insert multiple rows rows
            result = cursor.executemany(sql_insert_query, records)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into mobile table")
        obj_distrito = data[2]
        distritos = obj_distrito['Distrito']
        for dato in distritos:
            cursor = connection.cursor()
            sql_insert_query = """ INSERT INTO GN.GN_DISTRITO (in_id_provincia, vc_nombre, vc_descripcion, vc_ubigeo, bo_estado, vc_id_usuario_creacion, vc_id_usuario_modificacion, ts_fecha_creacion, ts_fecha_modificacion) 
                            VALUES (%s,%s,%s,'','1','VEOX','VEOX','NOW()','NOW()') """
            records = [ (dato['provincia'],dato['name'], dato['descripcion']) ]

            # executemany() to insert multiple rows rows
            result = cursor.executemany(sql_insert_query, records)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into mobile table")
