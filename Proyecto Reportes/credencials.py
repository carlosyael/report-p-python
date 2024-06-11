
import base64
import json
usuario=input("increse usuario: ")
password=input("increse contraseña: ")
# Codificar la contraseña
encoded_user = base64.b64encode(usuario.encode("utf-8")).decode("utf-8")
encoded_password = base64.b64encode(password.encode("utf-8")).decode("utf-8")
# Datos a escribir
with open('config.json','r') as configuracion:
    datos=json.load(configuracion)

datos_nuevos = {
    "username": encoded_user,
    "password": encoded_password,
    "dns": datos['dns'],
    "port": datos['port'],
    "encoding":datos['encoding'] ,
    "rutaResultados":datos['rutaResultados'],
    "rutaQueries":datos['rutaQueries']
}
# Escribir en el archivo JSON
with open('config.json', 'w') as archivo:
    json.dump(datos_nuevos, archivo, indent=4)

print("Datos escritos en config.json")
input()