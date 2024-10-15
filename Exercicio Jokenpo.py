import random

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while x < min or x > max:
        print(f"Escolha inválida! Digite um número entre {min} e {max}.")
        x = int(input(pergunta))
    return x

def vencedor(jogador1, jogador2):
    global v1, v2, empate
    if jogador1 == 1:  # Pedra
        if jogador2 == 1:  # Pedra
            empate += 1
        elif jogador2 == 2:  # Papel
            v2 += 1
        elif jogador2 == 3:  # Tesoura
            v1 += 1
    elif jogador1 == 2:  # Papel
        if jogador2 == 1:  # Pedra
            v1 += 1
        elif jogador2 == 2:  # Papel
            empate += 1
        elif jogador2 == 3:  # Tesoura
            v2 += 1
    elif jogador1 == 3:  # Tesoura
        if jogador2 == 1:  # Pedra
            v2 += 1
        elif jogador2 == 2:  # Papel
            v1 += 1
        elif jogador2 == 3:  # Tesoura
            empate += 1

# PROGRAMA PRINCIPAL
print('JOKENPO')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

jogadas = []
v1 = 0
v2 = 0
empate = 0

while True:
    j1 = valida_int('Escolha sua jogada (0 para sair): ', 0, 3)
    if j1 == 0:  # Condição para sair do loop
        break
    j2 = random.randint(1, 3)
    jogadas.append([j1, j2])
    vencedor(j1, j2)

# Exibindo as jogadas e os resultados
for jogada in jogadas:
    print(f'Jogador 1: {jogada[0]} | Jogador 2: {jogada[1]}')

print(f'Número de vitórias do jogador 1: {v1}')
print(f'Número de vitórias do jogador 2: {v2}')
print(f'Número de empates: {empate}')
