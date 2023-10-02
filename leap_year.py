#conditions to leap year
#1. if the year divide by 4 is qual to whole number
#2. if the year divided by 100 is not equal to a whole number
#3. if the year divided by 400 is equal to a whole number

def check(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("it is a leap year")
        else:
            print("it is a leap year")
    else:
        print("not leap year")

check(int(input("enter a year ")))

