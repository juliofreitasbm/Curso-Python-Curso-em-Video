import moeda

preco = float(input('Digite o preço: R$'));
print(f'A metade de {moeda.tmoeda(preco)} é {moeda.tmoeda(moeda.metade(preco))}');
print(f'O dobro de {moeda.tmoeda(preco)} é {moeda.tmoeda(moeda.dobro(preco))}');
print(f'Aumentando em 10%, temos {moeda.tmoeda(moeda.aumentar(preco, 10))}');
print(f'Reduzindo em 13%, temos {moeda.tmoeda(moeda.diminuir(preco, 13))}');