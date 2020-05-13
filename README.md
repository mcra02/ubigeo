<h1 align="center">Bienvenido Proyecto hecho en Django 👋</h1>
<p>
</p>

> Proyecto de practica hecho con Django, API Rest que permite realizar todas las operaciones como (create, delete, update, partial_update,list, retrieve) utilizando REST FRAMEWORK y mapeo de datos de un archivo xlsx o excel utilizando la biblioteca de software PANDAS.

### 🏠 [Inicio](manage.py)

## Uso

##### 1. Instalar requerimientos

```sh
pip install -r requirements.txt
```

##### 2. Generar archivos de migracion

```sh
python manage.py makemigrations
```

##### 3. Migracion de tablas

```sh
python manage.py migrate
```

##### 4. Iniciar servicio

```sh
python manage.py runserver
```

##### 5. Request

```sh
http://localhost:800/api/file/
```

key: 'Ubigeo'
encabezado: 'Ubigeo,Distrtito,Provincia,Departamento'
file: file.xlsx

## Autor

👤 **Maicol C Rodrigo**

- Website: maicolrodrigo.com
- Github: [@mcra02](https://github.com/mcra02)

---

_This README was generated with ❤️ by [mcra02](https://github.com/mcra02)_
