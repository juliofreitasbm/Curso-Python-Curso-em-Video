from random import randint
from time import sleep
from operator import itemgetter
'''
jogadores = {}

print('Valores sorteados: ')
for c in range(0, 4):
	jogadores[f'jogador{c+1}'] = randint(1, 6);

for k, v in jogadores.items():
	print(f'    O {k} tirou {v}');
	sleep(0.5);

print('Ranking dos jogadores:');
'''
jogo = {'jogador1': randint(1, 6),
		'jogador2': randint(1, 6),
		'jogador3': randint(1, 6),
		'jogador4': randint(1, 6)};
ranking = {}

#print(jogo);
print('Valores sorteados: ');

for k, v in jogo.items():
	print(f'	{k} tiou {v} no dado.');
	sleep(0.5);

#itemgetter() se o argumento for 0 ordena por chave, se for 1 ordena por valor
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
#print(ranking);

print('Ranking dos jogadores: ')
for i, v in enumerate(ranking):
	print(f'	{i+1}º lugar: {v[0]} com {v[1]}.');
	sleep(0.5);