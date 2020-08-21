#lanche = list();
lanche = ['hamburguer', 'suco', 'pizza', 'pudim'];

print(lanche);

lanche[3] = 'picolé';
print(lanche);


lanche.append('cookie');
print(lanche);

lanche.insert(0, 'hotdog');
print(lanche);

del lanche[3];
print(lanche);

lanche.pop(3);
print(lanche);

lanche.remove('suco');
print(lanche);

lanche.pop();
print(lanche);

if 'hamburguer' in lanche:
	lanche.remove('hamburguer');
print(lanche);

if 'hamburguer' in lanche:
	lanche.remove('hamburguer');
else:
	print('hamburguer não existe em lanche');
print(lanche);

valores = list(range(4,20))
print(valores);
valores.sort(reverse=True);
print(valores);
valores.sort();
print(valores, end='\n\n\n');

#vincula a lista A e a lista B
a = [2, 3, 4, 7];
b = a;
b[2] = 8;
print(f'Lista A: {a}');
print(f'Lista B: {b}\n');

#cria uma cópia da lista A dentro da lista B
a = [2, 3, 4, 7];
b = a[:];
b[2] = 8;
print(f'Lista A: {a}');
print(f'\n\nLista B: {b}');


#testando diferença entre vincular uma lista a outra e copiar uam lista para outra
teste = list();
teste.append('Gustavo');
teste.append(40);
print(teste);

galera = list();
galera2 = list()

galera.append(teste);
galera2.append(teste[:]);

teste[0] = 'Maria';
teste[1] = 22;

galera.append(teste);
galera2.append(teste[:]);
print(galera);
print(galera2, end='\n\n');

galera = [['João', 19],['Ana', 33],['Joaquim', 13], ['Maria', 45]];
print(galera[2][1]);
for p in galera:
	print(f'{p[0]} tem {p[1]} anos de idade.');

print('\n\n');
galera.clear();
galera2.clear();
dado = [];
for c in range (0,3):
	dado.append(str(input('Nome: ')));
	dado.append(int(input('Idade: ')));
	galera.append(dado);
	galera2.append(dado[:]);
	dado.clear();

print(galera);
print(galera2);
'''
for p in galera:
	if p[1] >= 21:
		print(f'{p[0]} é maior de idade');
'''