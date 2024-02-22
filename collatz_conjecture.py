a = int(input("Enter the number: "))
def collatz_conjecture(a):
  while a !=1:
    if a%2 == 0:
      a = a/2
      print(a)
    elif a%2 == 1:
      a = 3*a+1
      print(a)
    elif a==1:
     break

collatz_conjecture(a)