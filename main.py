# EXERCICIO 1
nomes = ['Emanuel', 'Nicholas', 'Stephany', 'Giovanna', 'Mariah']
print(f'Primeiro nome: {nomes[0]}')
print(f'Último nome: {nomes[-1]}')

# EXERCICIO 2
valores = [7, 4, 9, 6, 3]
valores.append(8)
valores.remove(4)
print(f'Lista final: {valores} [{len(valores)} números]')

# EXERCICIO 3
notas = [8, 3, 7, 5, 2, 9, 4]
for nota in notas:
    if nota < 5:
        print(f'Nota: {nota}')
    else:
        print('---')

# EXERCICIO 4
pares = []
impares = [] 
for num in range(20):
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f'{len(pares)} Pares: {pares}')
print(f'{len(impares)} Impares {impares}')