fh = open('Output.txt', 'w')

# Binary to Decimal

binary_number = input('Enter the number base 2: ')
decimal_result = int(binary_number, 2)
fh.write(f'Binary to Decimal: {decimal_result}\n')

# Decimal to binary

decimal_number = int(input('Enter the number from base 10: '))
binary_result = bin(decimal_number)[2:]
fh.write(f'Decimal to Binary: {binary_result}')

fh.close()
