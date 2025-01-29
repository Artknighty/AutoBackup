from operations import backup_sql, compress_file

# Executa função para backup do SQL_Server
backup_source = backup_sql()
backup_output = backup_source.replace('.bak', '.zip')
compress_file(backup_source, backup_output)

# Aguarda o usuario finalizar o programa
input("Pressione enter para sair...")
