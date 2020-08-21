'''
numbers = [];

for p in range (0, 5):
	num = int(input('Digite um valor: '));

	if p == 0 or num > max(numbers):
		numbers.append(num)
		print('Adicionado ao final da lista...')
	elif num < min(numbers):
		numbers.insert(0, num);
		print('Adicionado na posição 0 da lista...')
	else:
		for position,number in enumerate(numbers):
			if num > numbers[position] and num < numbers[position + 1]:
				numbers.insert(position + 1, num);
				print(f'Adicionado na posição {position + 1} da lista...');

print('-=' * 30);
print(f'Os valores digitados em ordem foram {numbers}');
'''
lista = []
for c in range (0, 5):
		n = int(input('Digite um valor: '))
		if  c == 0 or n > lista[-1]:
			lista.append(n)
			print('Adicionado ao final da lista...');
		else:
			pos = 0;
			while pos < len(lista):
				if n <= lista[pos]:
					lista.insert(pos, n)
					print(f'Adicionado na posição {pos} da lista...');
					break;
				pos += 1;
			
print('-=' * 30);
print(f'Os valores digitados em ordem foram {lista}');