numeros = []
pares = []
impares = []

while True:
	numeros.append(int(input('Digite um valor: ')));
	
	continuar = input('Quer continuar? [S/N] ');
	if(continuar in 'Nn'):
		break;

for num in numeros:
	if num % 2 == 0 :
		pares.append(num);
	else:
		impares.append(num);

print('-=' * 30);
print(f'A lista completa é {numeros}');
print(f'A lista de pares é {pares}');
print(f'A lista de impares é {impares}');