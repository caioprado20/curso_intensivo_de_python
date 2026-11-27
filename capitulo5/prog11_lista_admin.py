usuarios = ['clara','caio', 'leticia','thais','admin']
if usuarios:
    for usuario in usuarios:
        if usuario == 'admin':
            print("Olá adminstrador, gostaria de ver o relatório de status?")
        else:
            print(f'Olá {usuario}, obrigado por fazer login novamente')   
else:
    print("É necessário encontrar novos usuários")             
