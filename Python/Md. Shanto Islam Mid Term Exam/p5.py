import math

num = 23

for i in range(2, int(math.sqrt(num))):
    if num%i == 0:
        print(i)
        print("Number is not prime")
        break
else:
    print("Number is prime")