def metade(x=0):
	return x/2;

def dobro(x=0):
	return x*2;

def aumentar(x=0, p=0):
	return x*(100+p)/100;

def diminuir(x=0, p=0):
	return x*(100-p)/100;

def tmoeda(preco=0 , moeda='R$'):
	return f'{moeda}{preco:>8.2f}'.replace('.', ',')