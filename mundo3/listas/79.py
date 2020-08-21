numbers = []

while True:
	num = int(input('Enter a value: ')); 
	if num in numbers:
		print('Duplicate value! I will not add it.');
	else:
		numbers.append(num);
		print('Added value successfully!');

	answer = input('Would you like to continue? [Y/N] ');
	if answer in 'nN':
		break;
		
print('-=' * 30);
print(f'You entered the values {sorted(numbers)}');