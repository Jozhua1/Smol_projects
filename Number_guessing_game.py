import random
range1 = int(input('Give a number range to guess between: '))

while True:
            
 try:#try to catch the error if the user enters a non-integer value
    guess = int(input('Guess the number between 1 and '+str(range1)+': '))
    
    for i in range(range1):
         number_to_guess = random.randint(1, range1)#generate a random number between 1 and the specified range

    if guess < number_to_guess:
        print('Too low!')
    elif guess > number_to_guess:
        print('Too high!')
    else:
        print('Congratulations! You guessed the number.')
        break
 except ValueError:
    print('Please enter a valid number')


    