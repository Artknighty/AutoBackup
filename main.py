from connection import connection_sql
from time import sleep
from configparser import ConfigParser
from datetime import date

# Obtendo a data atual
data_atual = date.today()

# Formatando a data
data_formatada = data_atual.strftime('%d_%m_%Y')

# Criando o objeto configparser
config = ConfigParser()

# Lendo o arquivo config.ini com o caminho completo
config.read('Config.ini', encoding='utf-8')

# Obtendo os valores
sHost = config['Database']['sHost']
sDatabaseName = config['Database']['sDatabaseName']
sUser = config['Session']['sUser']
sPassWord = config['Session']['sPassWord']

# Conexão SQL
con = connection_sql(server=f'{sHost}', database=f'{sDatabaseName}', username=f'{sUser}', password=f'{sPassWord}')

# Caminho e database onde o backup será salvo
database = f'{sDatabaseName}'
backup_path = f'C:\\CSSistemas\\CSBackup\\{sDatabaseName}_{data_formatada}.bak'

try:
    # Configurando a conexão para autocommit
    con.autocommit = True

    # Criando o cursor para executar comandos no SQL Server
    cursor = con.cursor()

    # Comando SQL para realizar o backup
    backup_command = f"BACKUP DATABASE {database} TO DISK = '{backup_path}' WITH INIT"

    # Executa o comando
    print("Realizando backup SQL...")
    cursor.execute(backup_command)
    print(f"Backup do banco de dados '{database}' concluído com sucesso!")

except Exception as e:
     print(f"Erro ao realizar o backup: {e}")

finally:
    # Fechando a conexão
    if con:
        sleep(3)
        con.close()
    print("Conexão fechada.")

input("Pressione enter para sair...")
