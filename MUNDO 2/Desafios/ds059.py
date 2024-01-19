num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

menu = 0 

while menu <= 5:
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    menu = int(input('Digite qual opção deseja: '))

    if menu == 1:
        soma = num1 + num2
        print(f'Soma: {soma}')

    if menu == 2:
        multi = num1 * num2
        print(f'Multiplicação: {multi}')

    if menu == 3:
        if num1 > num2:
            print(f'{num1} é o maior número')
        if num2 > num1:
            print(f'{num2} é o maior número')
    
    if menu == 4:
        print('Digite novos números')

        num1 = int(input('Digite um novo número: '))
        num2 = int(input('Digite outro número novo: '))
        while menu <= 5:
            print('[1] somar')
            print('[2] multiplicar')
            print('[3] maior')
            print('[4] novos números')
            print('[5] sair do programa')
            menu = int(input('Digite qual opção deseja: '))

            if menu == 1:
                soma = num1 + num2
                print(f'Soma: {soma}')

            if menu == 2:
                multi = num1 * num2
                print(f'Multiplicação: {multi}')

            if menu == 3:
                if num1 > num2:
                    print(f'{num1} é o maior número')
                if num2 > num1:
                    print(f'{num2} é o maior número')
            
            if menu == 4:
                print('Digite novos números')

                num1 = int(input('Digite um novo número: '))
                num2 = int(input('Digite outro número novo: '))

            if menu == 5:
                print('Você saiu do programa!')

    if menu == 5:
        print('Você saiu do programa!')
