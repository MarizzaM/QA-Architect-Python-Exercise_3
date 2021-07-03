import random

lucky_list = random.sample(range(2, 49), 5)
print(lucky_list)
attempts = 0
while len(lucky_list) != 0:

    myGuess = int(input(f'#{attempts+1} Guess the number from 2 to 49: '))

    while myGuess not in lucky_list:
        if myGuess > max(lucky_list):
            print('Too high')
        else:
            print('Too low')
        attempts += 1
        myGuess = int(input(f'#{attempts+1} Guess the number from 2 to 49: '))

    attempts += 1
    lucky_list.remove(myGuess)
    print(f'Success! Left to guess {len(lucky_list)} numbers')

print(f'Well done! it took you {attempts} attempts')
