produtos = ('lápis', 1.75,
			'borracha', 2,
			'caderno', 15.9,
			'estojo', 25.0,
			'transferidor', 4.2,
			'compasso', 9.99,
			'mochila', 120.32,
			'canetas', 22.30,
			'livro', 34.90)

print('-' * 40);
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-' * 40);


for p in range(0, len(produtos), 2):
	print('{:.<30}R${:8.2f}'.format(produtos[p].capitalize(), produtos[p+1]))

print('-' * 40);

for p in range(0, len(produtos)):
	if p%2 == 0:
		print(f'{produtos[p].capitalize():.<30}', end='');
	else:
		print(f'R${produtos[p]:>8.2f}');

print('-' * 40);