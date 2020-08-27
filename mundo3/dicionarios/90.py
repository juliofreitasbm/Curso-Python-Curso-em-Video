aluno = {};

aluno['nome'] = str(input('Nome: '));
aluno['media'] = float(input('Média: '));

if aluno['media'] >= 6.0:
	aluno['situacao'] = 'Aprovado';
else:
	aluno['situacao'] = 'Reprovado';

print(f'Nome é igual a {aluno["nome"].capitalize()}');
print(f'Média é igual a {aluno["media"]}');
print(f'Situação é igual a {aluno["situacao"]}');
