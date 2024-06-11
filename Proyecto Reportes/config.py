import json
with open('config.json','r') as configuracion:
    datos=json.load(configuracion)

#credenciales base de datos
username = datos['username']
password = datos['password']
dsn = datos['dns']
port = datos['port']
encoding = datos['encoding']

#Configuracion de rutas
#resultados
results=datos['rutaResultados']
#queries
queries=datos['rutaQueries']