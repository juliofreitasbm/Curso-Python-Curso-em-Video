palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
			'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro');
vogal = ('a', 'e', 'i', 'o', 'u');


for palavra in palavras:
	print(f'Na palavra {palavra.upper()} temos', end=' ');
	for letra in palavra:
		if letra in vogal:
			print (letra, end=' ');
	print('');


for p in palavras:
	print(f'\nNa palavra {p.upper()} temos ', end='');
	for letra in p:
		if letra.lower() in 'aeiou':
			print(letra, end=' ');