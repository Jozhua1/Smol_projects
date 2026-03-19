import random

while True:
   choice = input('Roll the dice? (y/n): ').lower()
   
   
   if choice == 'y':
        dicenum = input('how many dice do you want to roll?')
        dicenum = int(dicenum)#convert the string to an integer

        for i in range(dicenum): #loop to roll the dice the number of times specified by the user
         print(random.randint(1, 100))

   elif choice == 'n': 
      print('Thanks for playing!')
      break
   else:
      print('You can one type y and n bro')