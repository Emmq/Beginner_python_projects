import random
print("welcome to this dice game")

x = random.randint(1,6)
y = random.randint(1,6)
def dice(i):
    return "\u2680\u2681\u2682\u2683\u2684\u2685"[i-1]

print(dice(x)+" "+dice(y))

