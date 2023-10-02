"""
loan= $400k
term= 30yrs
interest= 5%

calculate = p(r/n)/(1-(1+r/n)**(-nt))

p= 400k
r= (5/100) = 0.05
n= 12
t= 30yr
"""
p = int(input("enter the pricipal "))
r = int(input("enter the ther interest rate "))
r = r/100
n = int(input("enter the number of payment in a year "))
t = int(input("enter the term of loam "))

calculate = p*(r/n)/(1-(1+r/n)**(-(n*t)))

calculate = "%.2f" %calculate

print(calculate)

