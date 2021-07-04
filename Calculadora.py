"""""
Calculadora
"""""
print()
print()
print('CALCULADORA BÁSICA.')
print()
print()

calculo = input('Deseja realizar um Cálculo? [S]im ou [N]ão: ').lower()
print()

while calculo != 'n' and calculo != 's':
    calculo = input('Digite [S] para sim ou [N] para não: ').lower()
    print()
else:
    while calculo == 's':
        try:
            x = float(input('Digite o primeiro número: '))
            print()

            print('Operadores Disponíveis:')
            print('Adicão: [+]')
            print('Subtração: [-]')
            print('Multiplicação: [*]')
            print('Divisão: [/]')
            print()

            operador = input('Qual o tipo de operação deseja realizar? ')
            print()

            while (operador != '+') and (operador != '-') and (operador != '*') and (operador != '/'):
                print('Operação invalida!')
                operador = input('Escolha uma operação válida: ')

            y = float(input('Digite outro número: '))
            print()

            adicao = x + y
            subtracao = x - y
            multiplicacao = x * y
            divisao = x / y

            print('Resultado:')

            if operador == '+':
                print(f'{x}{operador}{y} = {adicao}')
                print()
            elif operador == '-':
                print(f'{x}{operador}{y} = {subtracao}')
                print()
            elif operador == '*':
                print(f'{x}{operador}{y} = {multiplicacao}')
                print()
            elif operador == '/':
                print(f'{x}{operador}{y} = {divisao}')
                print()

            calculo = input('Deseja fazer outro cálculo? ')
            print()

            while calculo != 's' and calculo != 'n':
                calculo = input('Digite [S] para sim ou [N] para não: ').lower()
                print()

        except:
            print('Algo deu errado... Tente novamente!')
            print()
            print('Apenas números!')

    else:
        print('Até mais')
