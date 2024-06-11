import pandas as pd
import os
import colorama
from colorama import Fore, Style
import json
import cx_Oracle 
import base64
import warnings
# Inicializar colorama
colorama.init()
warnings.filterwarnings('ignore')
def printRed(text):
    print(f"{Fore.RED}{text}{Style.RESET_ALL}")
def printGreen(text):
    print(f"{Fore.GREEN}{text}{Style.RESET_ALL}")
with open('config.json','r') as configuracion:
    datos=json.load(configuracion)

#credenciales base de datos
username = datos['username']
password = datos['password']
dns = datos['dns']
port = datos['port']
encoding = datos['encoding']

#Configuracion de rutas
#resultados
results=datos['rutaResultados']
#queries
queries=datos['rutaQueries']

# Funcion para Crear conexion
def conectar_a_oracle():
    try:
        connection = cx_Oracle.connect(
            base64.b64decode(username).decode("utf-8"),
            base64.b64decode(password).decode("utf-8"),
            dns,
            encoding=encoding
        )
        # Imprime en caso de ser exitosa la conexion
        printGreen(f"Conexión exitosa a Oracle")
        return connection
    except cx_Oracle.Error as error:
        printRed(f"Error de conexión: {error}")
        exit()
# Funcion para Crear consulta y exportar como Excel
def ejecutar_consulta(connection, sql_query, QueryName):
    try:
        # Crear la carpeta "reporte_mensual" si no existe
        output_dir = results
        os.makedirs(output_dir, exist_ok=True)
        print(f"*******{QueryName}*******")
        # Definir la ruta completa del archivo
        excel_file = os.path.join(output_dir, f"{QueryName}.xlsx")
        
        # Carga de informacion proveniente de la consulta en un dataframe
        # Formateamos el Query eliminando espacios en blanco al finak y el ; de cierre si este lo posee
        sql_query=sql_query.rstrip('\n')
        sql_query=sql_query.rstrip(' ')
        sql_query=sql_query.rstrip(';')
        
        df = pd.read_sql(sql_query, connection)
        print("Datos cargados en DataFrame")


        # Eliminar el archivo si ya existe
        if os.path.exists(excel_file):
            os.remove(excel_file)
            print(f"Archivo {excel_file} eliminado")

        # Guardar el DataFrame en el archivo Excel
        df.to_excel(excel_file)
        printGreen(f"Datos guardados en {excel_file}")

    except pd.errors.DatabaseError as db_error:
        printRed(f"Error al cargar datos en DataFrame: {db_error}")
# solo se ejecuta cuando es iniciacio y no cuando es importado como un modulo
if __name__ == "__main__":
    # Seleccion de directorio donde se encontraran los archivos .sql
    sql_directory = queries

    # Listar todos los archivos .sql en el directorio
    sql_files = [f for f in os.listdir(sql_directory) if f.endswith('.sql')]
    connection = conectar_a_oracle()
    # Iteramos cada archivo .sql encontrado en el directorio
    for sql_file in sql_files:
        #Conectamos a oracleDB

        sql_path = os.path.join(sql_directory, sql_file)  # Construir la ruta completa al archivo .sql
        with open(sql_path, "r") as file:
            #leemos la consulta Sql para luego ser ejecutada. la consulta no debe finalizar con punto y coma (;)
            consulta_sql = file.read()
        # Del archivo .sql, obtenemos el nombre para agregarlo al archivo .xlsx que será posteriormente creado
        query_name = os.path.splitext(os.path.basename(sql_file))[0]
        
        ejecutar_consulta(connection, consulta_sql, query_name)
    if connection:
       connection.close()
    input()

