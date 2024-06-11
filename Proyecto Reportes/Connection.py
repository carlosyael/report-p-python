import config  #Archivo configuracion credenciales DB
import cx_Oracle 
import colorama
from colorama import Fore, Style
import base64
import warnings
warnings.filterwarnings('ignore')
# Inicializar colorama
colorama.init()
# Funcion para Crear conexion   
def conectar_a_oracle():
    try:
        connection = cx_Oracle.connect(
            base64.b64decode(config.username).decode("utf-8"),
            base64.b64decode(config.password).decode("utf-8"),
            config.dsn,
            encoding=config.encoding
        )
        # Imprime en caso de ser exitosa la conexion
        print(f"{Fore.GREEN}Conexión exitosa a Oracle{Style.RESET_ALL}")
        return connection
    except cx_Oracle.Error as error:
        print(f"{Fore.RED}Error de conexión: {error} {Style.RESET_ALL}")
        exit()

if __name__ == "__main__":
    connection = conectar_a_oracle()
    if connection:
            connection.close()
    input()
