def is_prime(num):
  """Checks if a number is prime (without optimization)."""

  if num <= 1:
      return False

  divisor = 2
  while divisor < num:  # Check all divisors up to the number itself
      if num % divisor == 0:
          return False
      divisor += 1 

  return True

# Get input from the user
num = int(input("Enter a number: "))

# Check and print the result
if is_prime(num):
  print(num, "is a prime number.")
else:
  print(num, "is not a prime number.")
