from random import randint

sorteados = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10));
print(f"Os valores sorteados foram: ", end='');
for num in sorteados:
		print(f'{num} ', end='');

print(f'\n\nO menor valor foi {sorted(sorteados)[0]}');
print(f'O maior valor foi {sorted(sorteados)[-1]}\n'); 

print(f'O menor valor foi {min(sorteados)}');
print(f'O maior valor foi {max(sorteados)}'); 