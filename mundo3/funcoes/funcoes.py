from time import sleep;

def title(msg):
	print('-' * 30);
	print(f'	{msg}	');
	print('-' * 30);

def sum(a, b):
	print(f'a = {a}, b = {b}');
	print(a+b);

#desempacotamento
def contador(* num):
	print(num);
	print(f'O tamanho da tupla é {len(num)}');

def dobra(lst):
	pos = 0;
	print(lst);
	while pos < len(lst):
		lst[pos] *= 2;
		pos +=1;
	print(f'A lista dobrada fica: {lst}');

def teste(i, f, p):
	print(f'Contagem de {i} ate {f} de {p} em {p}');
	cont = i;
	while cont <= f:
		print(f'{cont} ', end='', flush=True);
		sleep(0.20);
		cont += p;
	print('FIM!');

#Programa Principal
title('CURSO EM VÍDEO');
title('CURSO DE PYTHON');
title('GUSTAVO GUANABARA');

sum(2, 3);
sum(b=4, a=2);
contador(2, 4, 5, 3);
contador(2, 3);
contador(2, 4, 53);

dobra([2, 4, 5]);

teste(1, 20, 2);
