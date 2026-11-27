current_users = ['caio', 'joao', 'juliana', 'josefa', 'lucia', 'atanilson']
current_users_upper = []

for user in current_users:
    current_users_upper.append(user.upper())

new_users = ['maria', 'Caio', 'klara', 'any', 'bento', 'ATANILSON']

for new_user in new_users:
    if new_user.upper() in current_users_upper:
        print(f"O nome '{new_user}' já está em uso. Escolha outro nome.")
    else:
        print(f"Nome '{new_user}' disponível.")