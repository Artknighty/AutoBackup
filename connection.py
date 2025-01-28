from pyodbc import connect

def connection_sql(server, database, username, password):
    try:
        # Conectando ao SQL Server
        connection = connect(
            f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        )
        msg = "Conexão com o SQL Server bem-sucedida!"
        print(msg)
        return connection
    except Exception as e:
        msg = f"Erro ao conectar ao SQL Server: {e}"
        print(msg)
        return None
