print("welcome, convert your dollar to naira")
def main():
    dollar= int(input("please enter dollar value "))
    naira= dollar * 784
    print(f"{dollar:,} dollar is equivalent to {naira:,} naira")

main()
while True:
    cont = input("do you wish to continue ? Yes/No ").lower()
    if cont == "yes":
        main()
    else:
        print("End")
        break