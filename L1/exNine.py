input_number = input('Enter a number:')

roman_numbers = ['I', 'XV', 'V', 'IX', 'X', 'L', 'C', 'D', 'CM', 'M']
integer_numbers = ['1', '5', '10', '50', '100', ]
convertion = []

for i in range(len(integer_numbers)):
    count = int(input_number / integer_numbers[i])
    convertion.append(roman_numbers[i] * count)
    input_number -= integer_numbers[i] * count
    print(''.join(convertion))
