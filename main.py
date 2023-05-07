import getpass

def verifica_senha(senha):
    if len(senha) < 8:
        return False
    if senha.isnumeric():
        return False
    if senha.isalpha():
        return False
    return True

while True:
    senha = getpass.getpass("Digite a senha para verificar sua validade (ou 'sair' para encerrar): ")
    if senha.lower() == 'sair':
        break
    if verifica_senha(senha):
        print("Senha válida!")
    else:
        print("Senha inválida!")
    resposta = input("Deseja verificar outra senha? (s/n): ")
    if resposta.lower() == 'n':
        break
