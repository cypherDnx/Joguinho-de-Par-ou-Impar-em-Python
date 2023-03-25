from random import randint
jogador = 0
cont = 0
while True:
    aleatorio = randint(0,10)
    print('-='*15)
    print('Vamos jogar par ou ímpar')
    print('-='*15)
    jogador = int(input('Digite um valor: '))
    esc = str(input('Par ou Ímpar? [P/I] ')).upper().strip() [0]
    soma = jogador + aleatorio
    if esc == 'P':
        if soma % 2 == 0:
            print('-='*20)
            print(f'O jogador digitou {jogador} e o computador digitou {aleatorio}. Deu PAR!')
            print('-='*20)
            print('Você GANHOU!')
            print('Vamos jogar novamente...')
            cont += 1
        else:
            print('-='*20)
            print(f'O jogador digitou {jogador} e o computador digitou {aleatorio}. Deu ÍMPAR!')
            print('-='*20)
            print(f'Você PERDEU! Conseguiu me vencer {cont} vezes')
            break
    if esc == 'I':
        if soma % 2 != 0:
            print('-='*20)
            print(f'O jogador digitou {jogador} e o computador digitou {aleatorio}. Deu ÍMPAR!')
            print('-='*20)
            print(f'Você GANHOU!')
            print('Vamos jogar novamente...')
            cont += 1
        else:
            print('-='*20)
            print(f'O jogador digitou {jogador} e o computador digitou {aleatorio}. Deu PAR!')
            print('-='*20)
            print(f'Você PERDEU! Conseguiu me vencer {cont} vezes')
            break
