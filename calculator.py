def welcome():
    print('''
Bem vindo a matematica comigo!!
''')

def calculate():
    operation = input('''
        qual vai ser a operacao meu mano?:
        + adicao
        - subtracao
        * multiplicacao
        / divisao
        ** potenciacao
        % porcentagem
    ''')
    number_1 = int(input('Primeiro numero:'))
    number_2 = int(input('Segundo numero:'))

    if operation == '+':
        # adicao
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        # subtracao
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        # multiplicacao
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        # divisao
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    elif operation == '**':
        # potenciacao
        print('{} ** {} = '.format(number_1, number_2))
        print(number_1 ** number_2)

    elif operation == '%':
        # porcentagem
        print('{} % {} = '.format(number_1, number_2))
        print(number_1 % number_2)

    else:
        print('isso dai nn e uma operacao jhow')

    dnv()

def dnv():
    calc_dnv = input('bora denovo? S / N')
    
    if calc_dnv.upper() == 'S':
        calculate()
    
    elif calc_dnv.upper() == 'N':
        print('falou meu mano')

    else:
        calculate()

welcome()
calculate()
