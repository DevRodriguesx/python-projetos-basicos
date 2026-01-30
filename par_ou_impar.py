# Par ou Ímpar
num = int(input('Digite um número para verificar se ele é PAR ou ÍMPAR: '))
if num % 2 == 0:
    print('O número {} é \033[1;36mPAR\033[m'.format(num))
else:
    print('O número {} é \033[1;35mÍMPAR\033[m'.format(num))