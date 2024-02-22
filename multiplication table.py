def create_multiplication_table(size):
  """Creates a neatly formatted multiplication table up to the given size."""

  # Header Row
  print("   ", end="")
  for i in range(1, size + 1):
      print("{:4d}".format(i), end="")  # Formatting column headers
  print() 

  # Separator Line
  print("   ", "-" * (size * 4 + 1)) 

  # Table Content
  for i in range(1, size + 1):
      print("{:2d} |".format(i), end="")  # Formatting row number
      for j in range(1, size + 1):
          print("{:4d}".format(i * j), end="")  
      print()  

# Example usage
size = 12
create_multiplication_table(size)
