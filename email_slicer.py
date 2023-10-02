print("welcome")
def main():
    user_email = input("please enter your email ")
#idoko@gmail.com
    (user_name,domain)= user_email.split("@")
    (domain,extension)= domain.split(".")

    print(user_name)
    print(domain)
    print(extension)

main()