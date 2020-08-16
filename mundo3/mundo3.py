lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita');

print(lanche[2]);
print(lanche[0:2]);
print(lanche[::-1]);
print(f'{len(lanche)}\n');

for comida in lanche:
	print(f'Eu vou comer {comida}');

print('Comi bagarai!\n');

for contador in range(0, len(lanche)):
	print(f'Eu vou comer {lanche[contador]} na posição {contador}');

print('Também comi bagarai\n');

for posicao, comida in enumerate(lanche):
	print(f'Eu vou comer {comida} na posição {posicao}');

print('Comi bagarai de novo\n');

print(sorted(lanche));

a = (2, 5, 4);
b = (5, 8, 1, 2);
c = a + b;

print(f'\n{c}');
print(len(c));
print(c.count(5));
print(c.index(8));
print(c.index(2, 1)); #Procura o elemento dois a partir da posição 1

pessoa = ('Gustavo', 39, 'M', 99.88);
del(pessoa); #Eh possivel deletar uma tupla inteira