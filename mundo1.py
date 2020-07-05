import math
#from math import sqrt, floor
#quando voce importa as funcoes separadamente nao precisa usar o math.sqrt(). So sqrt() ja funciona
import random
import emoji
import pygame
import datetime

print('Hello World')

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = input('Digite um valor inutil:')

print(type(n1), type(n2), type(n3))
print(n3.isnumeric())
print(n3.isalpha())
print(n3.isalnum())
soma = n1 + n2

print('A soma é', soma)
#Esse eh um comentario

print('A soma entre', n1, 'e', n2, 'vale', soma)
print('A soma entre {} e {} vale {}\n' .format(n1, n2, soma))


nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

print('')

print('Observe como {:.3f} só tem 3 casas decimais'.format(8/3))
print('Observe como {:2} foi alinhado com o número de baixo como se tivessem 2 dígitos'.format(4))
print('Observe como {:2} foi alinhado com o número de cima mesmo tendo 2 dígitos\n'.format(10))
print('Isso está escrito em um print', end='')
print("e isso está escrito em outro, mas eles estão na mesma linha porque utilizei o end=''")
print("Isso está escrito em um print \ne isso está escrito no mesmo print, mas estão separados por causa do '\ n'\n")

print('O número {} arredondado para cima fica {}, para baixo fica {} e truncado fica {}'.format(5.4, math.ceil(5.4), math.floor(5.4), math.trunc(5.4)))

print('Seu número inteiro aleatório do dia é {}'.format(random.randint(1, 1000)))
print(emoji.emojize('Olá, Mundo :earth_americas:\n', use_aliases=True))

# pygame.init()
# pygame.mixer.music.load('som_teste.mp3')
# pygame.mixer.music.play()
# pygame.event.wait()

frase = 'Curso em Vídeo Python';
print(type(frase));
print(frase);
print(frase[9]);
print(frase[9:14]);
print(frase[9:21:2]);
print(frase[:5]);
print(frase[15:]);
print(frase[9::3]);

print('\nFAZENDO ANÁLISE\n');

print(len(frase));
print(frase.count('o'));
print(frase.count('o', 0, 13));
print(frase.find('deo'));
print(frase.find('Android'));
print('Curso' in frase);

print('\nFAZENDO TRANSFORMAÇÃO\n');

print(frase.replace('Python','Android'));
print(frase.upper());
print(frase.lower());
print(frase.capitalize());
print(frase.title());

frase2 = '   Aprenda Python  ';
print(frase.strip(frase2));
print(frase.rstrip(frase2));
print(frase.lstrip(frase2));

print('\nFAZENDO DIVISÃO\n');

print(frase);
print(frase.split());
print(frase.split()[3]);

print('\nFAZENDO JUNÇÃO\n');
print('-'.join(frase));
print('-'.join(frase.split()));

print('\nRepare abaixo o uso das aspas 3 vezes'.upper());
print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Suspendisse ac erat semper, dictum ante vitae, facilisis enim. Nulla vitae massa blandit, feugiat arcu ut, tincidunt nulla. Duis quis eleifend leo.
Nullam in pretium ligula, ac finibus nunc. Curabitur leo nisi, lobortis sit amet ipsum vel, finibus tincidunt orci.
Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
Praesent sollicitudin magna elementum ligula dignissim, vel dapibus quam tristique.\n""");

print('''Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Suspendisse ac erat semper, dictum ante vitae, facilisis enim. Nulla vitae massa blandit, feugiat arcu ut, tincidunt nulla. Duis quis eleifend leo.
Nullam in pretium ligula, ac finibus nunc. Curabitur leo nisi, lobortis sit amet ipsum vel, finibus tincidunt orci.
Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
Praesent sollicitudin magna elementum ligula dignissim, vel dapibus quam tristique.\n''');

print(frase.replace('Python', 'Android'));
print(frase);
frase = frase.replace('Python', 'Android');
print(frase + '\n');

if nome == 'julio':
	print("'{}'! Que nome lindo você tem!".format(nome));
else:
	print("Nossa! '{}'é um nome bem estranho!".format(nome));

print('A data de hoje é {}/{}/{}'.format(datetime.date.today().day, datetime.date.today().month, datetime.date.today().year));
print('A data de hoje é {}\n'.format(datetime.date.today()));

print('\33[1;31;43mCores em python no terminal\033[m')