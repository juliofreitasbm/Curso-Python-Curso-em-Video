nome = input('Qual é seu nome? ');

if nome.upper() == 'JULIO':
	print('Que nome bonito!');
elif nome.upper() == 'PEDRO' or nome.upper() == 'MARIA' or nome.upper() == 'PAULO':
	print('Seu nome é bem popular no Brasil!');
elif nome.upper() in 'ANA CLÁUDIA JÉSSICA JULIANA':
	print('Belo nome feminino!');
else:
	print('Seu nome é bem interessante!');

print('Tenha um bom dia, {}'.format(nome));

print('\nCONVERTENDO NÚMEROS\n');

numero = int(input('Digite um número: '));
print('{} em binário é {}, em octal é {} e em hexadecimal é {}'.format(numero, bin(numero)[2:], oct(numero)[2:], hex(numero)[2:]));

media = 6;

if 7 > media >= 5:
	print('\nA media ta legal!\n');

idade = int(input('Digite uma idade: '));

if idade <= 9:
	print('Classificação: MIRIM');
elif idade <=14:
	print('Classificação: INFANTIL');
elif idade <=19:
	print('Classificação: JUNIOR');
elif idade <=25:
	print('Classificação: SÊNIOR');
else:
	print('Classificação: MASTER');

r1 = 1;
r2 = 1;
r3 = 1;

if r1 == r2 and r2 == r3:
	print('\nVeja essa comparação sendo feita da forma tradicional!\n');

if r1 == r2 == r3:
	print('\nOlha como essa comparação é feita de forma diferente. Louquíssimo!\n');

print('INÍCIO');
for c in range(0, 6):
	print('Oi');
print('FIM\n');

print('INÍCIO');
for c in range(6, 0, -1):
	print('Oi');
print('FIM\n');

print('INÍCIO');
for c in range(0, 6, 2):
	print('Oi');
print('FIM\n');



sexo = 'M';
if sexo == 'M' or sexo =='m':
	print("Olha só como o usuário pode digitar 'M' ou 'm' para o sexo Masculino ");

sexo = 'm';
if sexo in 'Mm':
	print("Olha só como o usuário pode digitar 'M' ou 'm' para o sexo Masculino ");

'''Olha só, esse é um comentário
de multiplas linhas
Muito legal!'''

""" Esse também é um comentário 
de multiplas linhas
Muito interessante!"""

n = int(input('\nDigite um número para calcular o Fatorial: '));
c = n;
fatorial = 1;

while c > 0:
	print('{}'.format(c), end='');
	print(' x ' if c > 1 else ' = ', end='');
	fatorial *= c;
	c -= 1;

print('{}'.format(fatorial))

nome = 'José';
idade = 24;

print(f"\nVeja nessa fstring que o {nome} tem {idade} anos");


var_a = var_b = var_c = 0;
#Olha que legal acima eu criando e iniciando um monte de variáveis simultaneamente