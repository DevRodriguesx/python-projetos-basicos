# Aprovado ou Reprovado a partir da Média
print('\033[1;34mPara ser aprovado sua média terá que ser superior ou igual a 6\033[m')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 6:
    print('Parabéns você está \033[1;32mAPROVADO\033[m, sua média foi {}!'.format(media))
else:
    print('Infelizmente você está \033[1;31mREPROVADO\033[m, sua média foi {}'.format(media))