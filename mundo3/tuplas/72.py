numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')

c=-1;
while (c < 0 or c > 20):
	c = int(input('Digite um valor entre 0 e 20:'))

print(f'O número {c} por extenso é {numeros[c]}');