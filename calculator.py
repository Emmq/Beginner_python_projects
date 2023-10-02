print("welcome to this calculator")
def main():
    first_num= int(input("please enter first number "))
    second_num= int(input("please enter second number "))
    operators= input("""
    please choose an operator from A to D
    A. Addition
    B. Subtraction
    C. Multiplication
    D. Division
    """).lower()

    def add(x,y):
        add_value= x+y
        print(f"{x} + {y} = {add_value}")
        return

    def sub(x,y):
        sub_value= x-y
        print(f"{x} - {y} = {sub_value}")
        return

    def mul(x,y):
        mul_value= x*y
        print(f"{x} * {y} = {mul_value}")
        return

    def div(x,y):
        div_value= x/y
        print(f"{x} / {y} = {div_value}")
        return
    
    if operators == "a":
        add(first_num,second_num)
    elif operators == "b":
        sub(first_num,second_num)
    elif operators == "c":
        mul(first_num,second_num)
    elif operators == "d":
        div(first_num,second_num)
    else:
        print("please choose a valid operator")

main()

while True:
    cont= input("do wish to continue? Yes/No ").lower()
    if cont == "yes":
        main()
    else:
        print("end")
        break
