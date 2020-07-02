# Write an if statement to determine whether a variable holding a year is a leap year.

year = int(input("Enter any year"))

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(f'{year} is leap year')
else:
    print(f'{year} is not leap year')
