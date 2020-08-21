expressao = str(input('Digite a expressão: '));
parenteses = []

for let in expressao:
	if let == '(':
		parenteses.append(let);
	elif let == ')' and len(parenteses) == 0:
		parenteses.append(')');
		break;
	elif let == ')' and  parenteses[-1] == '(':
		parenteses.pop();

	print(f'Só os parênteses ficam {parenteses}');

#print(f'A expressão é {expressao}');

if len(parenteses) == 0:
	print('A expressão é válida!');
else:
	print('A expressão é inválida!');


