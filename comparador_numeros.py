# Comparador de Números
num1 = int(input('\033[1;34mPrimeiro número:\033[m '))
num2 = int(input('\033[1;36mSegundo número:\033[m '))
maior = num1
if num2 > num1:
    maior = num2
    print('O maior número é o \033[1;35m{}\033[m'.format(maior))
if num1 == num2:
    print('\033[1;33mOs dois números são iguais!!\033[m')