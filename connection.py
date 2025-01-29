from pyodbc import connect
from configparser import ConfigParser

def connection_sql():
    try:
        # Conectando ao SQL Server
        connection = connect(
            f'DRIVER={{SQL Server}};SERVER={sHost};DATABASE={sDatabaseName};UID={sUser};PWD={sPassWord}'
        )
        msg = "Conexão com o SQL Server bem-sucedida!"
        print(msg)
        return connection
    except Exception as e:
        msg = f"Erro ao conectar ao SQL Server: {e}"
        print(msg)
        return None

# Criando o objeto configparser
config = ConfigParser()

# Lendo o arquivo config.ini com o caminho completo
config.read('Config.ini', encoding='utf-8')

# Obtendo os valores
sHost = config['Database']['sHost']
sDatabaseName = config['Database']['sDatabaseName']
sUser = config['Session']['sUser']
sPassWord = config['Session']['sPassWord']
