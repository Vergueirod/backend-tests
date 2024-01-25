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

# consulta teste:
consulta_selecionar = "SELECT * FROM usuarios"
cursor.execute(consulta_selecionar)

registros_users = cursor.fetchall()

active_users = []
desactive_users = []

def main():
    login = input(str('Digite seu login: '))
    senha = input(str('Digite seu Senha: ')) 
    separe_users(login, senha)


def separe_users(login, senha):
    for r in range(len(registros_users)):
        if registros_users[r][8] == 1:
            active_users.append(registros_users[r])  
        elif registros_users[r][8] == 0:
            desactive_users.append(registros_users[r])
    auth(login, senha, active_users)


def auth(login, senha, active_users):
    right = False
    for valid in range(len(active_users)):
        if active_users[valid][3] == login and active_users[valid][5] == senha:
            right = True
            break
        else:
            right  = False
    show_auth(right)
         
            
def show_auth(right):  
    if right:
        print('Login realizado.')
    else:
        print('Usuario não cadastrado ou dados digitados errados.')    
        
main()     

# Fechar cursor e conexão
cursor.close()
conexao.close()