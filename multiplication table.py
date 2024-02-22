for i in range(1, 12 + 1): # Formatting row number
      for j in range(1, 12 + 1):
          print("{:4d}".format(i * j),end="") # Formatting column number  
      print()
