year = int(input("Enter Year: "))
is_leap_year = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

if is_leap_year:
    print("Leap Year")
else:
    print("Not Leap Year")
