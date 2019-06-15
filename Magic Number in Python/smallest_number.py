import random
number = 10
min=9
for i in range(number):
    j=random.randint(0,9)
    if(j<min):
        min=j

print("Minium number is "+str(min))
