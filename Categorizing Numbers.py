enter_number = int(input("Enter a number: "))
if enter_number > 0:
  print("The number is positive")
  if enter_number % 2 == 0:
      print(f"{enter_number} is even")
  else:
      print(f"{enter_number} is odd")
elif enter_number == 0:
  print(f"{enter_number} is zero")  
elif enter_number < 0:
  print("The number is negative")
  if enter_number % 2 == 0:
      print(f"{enter_number} is even")
  else:
      print(f"{enter_number} is odd")
