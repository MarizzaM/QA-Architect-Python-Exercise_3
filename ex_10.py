counter = -1
while True:
    y = int(input('Enter positive number (exit - negative number): '))
    counter += 1
    if y < 0:
        break

print(f'Count of positive numbers is {counter}')
