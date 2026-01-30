# Verificador de Maioridade
idade = int(input('Qual é a sua idade? '))
if idade < 18:
    print('\033[1;31mVocê é menor de idade!\033[m')
else:
    print('\033[1;32mVocê já é maior de idade!\033[m')