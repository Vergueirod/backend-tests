import mysql.connector

config = {
    'host': '127.0.0.1',
    'user': 'vergueiro',
    'password': 'Htabbas13.',
    'database': 'learning',
    'port': 3306 
}

conexao = mysql.connector.connect(**config)

cursor = conexao.cursor()

# Fechar cursor e conexão
cursor.close()
conexao.close()