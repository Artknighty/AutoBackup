from time import sleep
from connection import connection_sql
from datetime import date
from zipfile import ZipFile, ZIP_DEFLATED

# Backup SQL
def backup_sql():
    # Obtendo a data atual
    data_atual = date.today()

    # Formatando a data
    data_formatada = data_atual.strftime('%d_%m_%Y')

    # Caminho e database onde o backup será salvo
    backup_path = f'C:\\CSSistemas\\CSBackup\\DADOS_{data_formatada}.bak'

    try:
        # Cria um objeto de conexão
        con = connection_sql()

        # Configurando a conexão para autocommit
        con.autocommit = True

        # Criando o cursor para executar comandos no SQL Server
        cursor = con.cursor()

        # Comando SQL para realizar o backup
        backup_command = f"BACKUP DATABASE DADOS TO DISK = '{backup_path}' WITH INIT"

        # Executa o comando
        print("Realizando backup SQL...")
        cursor.execute(backup_command)
        print(f"Backup do banco de dados 'DADOS' concluído com sucesso!")

    except Exception as e:
        print(f"Erro ao realizar o backup: {e}")

    finally:
        # Fechando a conexão
        if con:
            sleep(3)
            con.close()
        print("Conexão fechada.")

    return backup_path

# Compacador de backup
def compress_file(backup_source, backup_output):
    try:
        print('Compactando arquivo...')
        with ZipFile(f'{backup_output}', 'w', ZIP_DEFLATED) as file:
            file.write(f'{backup_source}')
            print(f'Arquivo compactado com sucesso!')
    except Exception as e:
        print(f'Erro ao tentar compactar o arquivo \n', f'Motivo: {e}')
