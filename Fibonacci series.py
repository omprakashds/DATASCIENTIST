def fibonacci(n):
  """Calculates the first 'n' numbers of the Fibonacci sequence."""

  a, b = 0, 1  # Initialize the first two values
  count = 0

  while count < n:
      print(a, end=" ")
      a, b = b, a + b  # Update values for the next iteration
      count += 1

# Example usage
fibonacci(10)  # Print the first 10 Fibonacci numbers
