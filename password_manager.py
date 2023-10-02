print("welcome")

def add():
    name = input("input your name ")
    psd = input("input passwod ")

    with open("manege.txt","a") as f:
        f.write(name+"|"+psd+"\n")

def view():
    pass

while True:
    aim = input("do you wish to 'add' or 'view' password? ")
    if aim == "add":
        add()
        break
    elif aim== "view":
        view()
        break
    else:
        print("pls type in 'view' or 'add'")
        continue
