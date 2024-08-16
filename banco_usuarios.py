import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='081298',
    database='bdusuarios',
)
cursor = conexao.cursor()

def adicionar_usuarios(nome, idade):
    comando = f'INSERT INTO usuarios (nome, idade) VALUES ("{nome}", {idade})'
    cursor.execute(comando)
    conexao.commit()
    conexao.close()

def listar_usuarios():
    comando = f'SELECT * FROM usuarios'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)
    

def atualizar_usuarios(idusuarios, nome, idade):
    comando = f'UPDATE usuarios SET nome = "{nome}", idade = {idade} WHERE idusuarios = {idusuarios}'
    cursor.execute(comando)
    conexao.commit()
    conexao.close()
    
    
def deletar_usuarios(idusuarios):
    comando = f'DELETE FROM usuarios WHERE idusuarios = {idusuarios}'
    cursor.execute(comando)
    conexao.commit()
    conexao.close()
    

def menu():
    print("\n[1]. Adicionar usuário")
    print("[2]. Listar usuários")
    print("[3]. Atualizar usuário")
    print("[4]. Deletar usuário")
    print("[5]. Sair.")

while True:
    menu()
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        nome = input("Digite o nome do usuário: ")
        idade = int(input("Digite a idade do usuário: "))
        adicionar_usuarios(nome, idade)
        print("Usuário adicionado com sucesso!")
    elif escolha == '2':
        print('\nTodos os usuários:')
        listar_usuarios()
    elif escolha == '3':
        idusuarios = int(input("Digite o ID do usuario a ser atualizado: "))
        nome = input("Digite o novo nome do usuário: ")
        idade = int(input("Digite a nova idade do usuário: "))
        atualizar_usuarios(idusuarios, nome, idade)
        print("Usuario atualizado com sucesso!")
    elif escolha == '4':
        idusuarios = int(input("Digite o ID do usuário a ser deletado: "))
        deletar_usuarios(idusuarios)
        print("Usuário Deletado com sucesso! ")
    elif escolha == '5':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        
cursor.close()