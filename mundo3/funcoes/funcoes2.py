print('-=' * 40);
help(print);
print('-=' * 40);
print(print.__doc__);
print('-=' * 40);

def contador(i=1, f=10, p=1):
	"""
	-> Faz uma contagem e mostra na tela.
		:param i: inicio da contagem
			é um parâmetro opcional de valor padrão 1
		:param f: fim da contagem
			é um parâmetro opcional de valor padrão 10
		:param p: passo da contagem
			é um parâmetro opcional de valor padrão 1
		:return: sem retorno
	"""
	c = i;
	while c <= f:
		print(f'{c} ', end='');
		c += p;
	print('FIM!');

contador(0, 100, 10);

print('-=' * 40);
help(contador);
print('-=' * 40);

def teste(b):
	global a;
	a = 8;
	b += 4;
	c = 2;

	print(f'A dentro vale {a}');
	print(f'B dentro vale {b}');
	print(f'C dentro vale {c}');

def teste2(b):
	a = 8;
	b += 4;
	c = 2;

	print(f'A dentro vale {a}');
	print(f'B dentro vale {b}');
	print(f'C dentro vale {c}');

def soma(a=0, b=0):
	return a+b;

print('-=' * 15);
a = 5;
teste(a);
print(f'\33[1;31;43mA fora vale {a}\033[m');
print('-=' * 15);

print('-=' * 15);
a = 5;
teste2(a);
print(f'\33[1;31;43mA fora vale {a}\033[m');
print('-=' * 15);
a=2;
b=10;
print(f'A soma de a={a} mais b={b} é igual a {soma(a+b)}');