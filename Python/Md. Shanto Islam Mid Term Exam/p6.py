import random
attemts = 3
randomNum = random.randint(1,100)
while attemts > 0:
    guess_num = int(input("Enter a number to guess random number: "))
    
    if guess_num == randomNum:
        print("Your guess correct!")
        break
    else:
        print("Your guess is incorrect!")
    
    attemts -= 1
    
    if attemts == 0:
        print("Your attemps chance ended!")