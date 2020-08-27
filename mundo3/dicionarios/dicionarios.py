dados = dict()
#ou dados = {}

dados = {
	'nome':'Pedro',
	'idade':25
};
dados['sexo'] = 'M';
del dados['idade'];

print(f'{dados}\n');

filme = {
	'titulo':'Star Wars',
	'ano':1977,
	'diretor':'George Lucas'
}
print(filme.values());
print(filme.keys());
print(filme.items());
print();

for k,v in filme.items():
	print(f'o {k} é {v}');

print(f'\nO {filme["diretor"]} é diretor do filme {filme["titulo"]}');
