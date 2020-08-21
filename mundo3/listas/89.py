'''
nomes = []
notas1 = []
notas2 = []
medias = []


notas = [notas1, notas2, medias]
tabela = [nomes, notas]

num = 1;
while True:
	nomes.append(str(input('Nome: ')));
	nota1 = float(input('Nota 1: '));
	nota2 = float(input('Nota 2: '));

	notas1.append(nota1);
	notas2.append(nota2);
	medias.append((nota1 + nota2)/2);

	continuar = str(input('Quer continuar? [S/N] '));
	if continuar in 'Nn':
		break;

print(f'{tabela}');
'''

ficha = list()
while True:
	nome = str(input('Nome: '));
	nota1 = float(input('Nota 1: '));
	nota2 = float(input('Nota 2: '));
	media = (nota1 + nota2)/2
	ficha.append([nome, [nota1, nota2], media]);
	resp = str(input('Quer continuar? [S/N] '));
	if resp in 'Nn':
		break;

print('-=' * 30);
print(f'{"No. ":<4}{"NOME":<10}{"MÉDIA":>8}');
for i, a in enumerate(ficha):
	print(f'{i:<4}{a[0].capitalize():<10}{a[2]:>8.1f}');

while True:
		print('-' * 35)
		opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '));
		if opc == 999:
			print ('FINALIZANDO...');
			break;
		if opc <= len(ficha) - 1:
			print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}');
print('<<< VOLTE SEMPRE >>>');