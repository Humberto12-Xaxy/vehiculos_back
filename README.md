
# Vehiculos

En este proyecto se puede obtener, crear, actualizar y eliminar vehiculos, además de la creación y autenticación de usuarios.


## Instalación

Instalar las siguientes dependencias:

```bash
  pip install django djangorestframework django-cors-headers
```

## migraciones

verificamos si hay migraciones por hacer

```bash
  python manage.py makemigrations
```

Hacer migracion para la creacion de la base de datos en sqlite3

```bash
  python manage.py migrate
```


## Ejecución

Levantar el servidor de forma local:

```bash
  python manage.py runserver
```

## Ejemplos CURL

Petición GET:

Se le pasa el id del usuario para que nos arroge los vehiculos a su disposición
```bash
  curl http://127.0.0.1:8000/api/vehiculos/1/
```

Petición POST:

```bash
curl  -X POST \
  'http://127.0.0.1:8000/api/vehiculos/' \
  --header 'Accept: */*' \
  --header 'Authorization: Token 6597d286dbef2d8979b4757175f363b304e9895b' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "placas" : "awqe",
  "latitud" : -93.784353,
  "longitud" : 15.934945,
  "user_id" : 1
}'
```
Petición PUT:

```bash
  curl  -X PUT \
  'http://127.0.0.1:8000/api/vehiculos/6/' \
  --header 'Accept: */*' \
  --header 'Authorization: Token 6597d286dbef2d8979b4757175f363b304e9895b' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "placas" : "aasdf",
  "latitud" : -93.784380,
  "longitud" : 15.9349123,
  "user_id" : 1
}'
```

Petición DELETE:

```bash
  curl -X DELETE http://127.0.0.1:8000/api/vehiculos/{id}/
```
