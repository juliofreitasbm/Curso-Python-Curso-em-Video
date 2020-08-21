numeros = []
for c in range(0,5):
	numeros.append(int(input(f'Digite um valor para a Posição {c}: ')));

print('=-' * 40)
print(f'Você digitou os valores {numeros}');
	
print(f'O maior número digitado foi {max(numeros)} nas posições ', end='');
for pos,num in enumerate(numeros):
	if(num == max(numeros)):
		print(f'{pos}... ', end='');

print(f'\nO menor número digitado foi {min(numeros)} nas posições ', end='');
for pos,num in enumerate(numeros):
	if(num == min(numeros)):
		print(f'{pos}... ', end='');