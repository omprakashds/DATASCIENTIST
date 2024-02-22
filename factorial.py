def factorial(a):
  result = 1
  while a > 1:  
      result *= a
      a -= 1
  return result

while True:
  try:
      a = int(input("Enter the number: ")) 
      if a < 0:
          print("Factorial is not defined for negative numbers.")
      else:
          print(factorial(a))  # Calculate and print the factorial
          break  # Exit the loop if the input is valid
  except ValueError:
      print("Invalid input. Please enter a positive integer.") 

print(factorial(a))
