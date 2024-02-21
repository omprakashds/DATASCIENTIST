import random

def   Guess():
  randint = random.randint(1, 100)
  number = int(input("Guess a number between 1 and 100: "))
  if number == randint:
    print("You guessed the number!")  
  elif number > randint:
    print(f"Too high. The answer was {randint}")
  elif number < randint:
    print(f"Too low. The answer was {randint}")
    return (number)
result = Guess()
print(result)