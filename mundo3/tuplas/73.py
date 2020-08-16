brasileirao = ('Athletico-PR', 'Internacional', 'Atlético-MG', 'Grêmio', 'Atlético', 'Grêmio', 'Atlético-GO', 'Vasco da Gama', 'Bahia', 'São Paulo', 'Sport Recife', 'Flamengo',
				'Palmeiras', 'Bragantino-SP', 'Botafogo', 'Ceará SC', 'Corinthians', 'Goiás', 'Fluminense', 'Santos', 'Fortaleza', 'Coritiba')

print('-=' * 20);
print(f'Os primeiros 5 colocados são {brasileirao[:5]}');
print('-=' * 20);
print(f'Os últimos 4 colocados são {brasileirao[-4:]}');
print('-=' * 20);
print(f'Os times em ordem alfabética são {sorted(brasileirao)}');
print('-=' * 20);
print(f"O time Palmeiras está na posição {brasileirao.index('Palmeiras') + 1}");
print('-=' * 20);