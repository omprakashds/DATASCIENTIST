def print_pyramid(rows):
  """Prints a basic pyramid of numbers."""
  for i in range(rows):
      # Print spaces for alignment
      for j in range(rows - i - 1):
          print(" ", end="") 

      # Print the numbers in increasing and decreasing order
      for j in range(1, i + 2):
          print(j, end="")  

      for j in range(i, 0, -1):
          print(j, end="")  

      print()  # Move to the next line

# Example usage
rows = 5
print_pyramid(rows)
