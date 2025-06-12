import random 
while True:
  print("Choose number from 1 to 10\n")
  number_computer_guess = random.randrange(1,11)
  number_we_guess = int(input("Enter the number to guess: "))
  if number_computer_guess == number_we_guess:
    print(f'computer choose number {number_computer_guess} You choose number {number_we_guess} True guess\n')
    print("You win the game 😊")
    break
  else:
    print(f'computer choose number {number_computer_guess} You choose number {number_we_guess} Wrong guess\n')