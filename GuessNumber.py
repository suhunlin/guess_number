import random
from random import randint
random_num = random.randint(1,100)
print(random_num)
user_input = int(input("Please input a number to guess(between 1~100):"))

while True:
    if random_num == user_input:
        print("Congratulation !!!")
        break
    else:
        temp_num = user_input
        if random_num > user_input:
            user_input = int(input("Please input a number to guess(between 100 ~ %d):" %user_input))
            if user_input <= temp_num :
                print("The number toot small!!!Try again!!!")
                user_input = temp_num
        else:
            user_input = int(input("Please input a number to guess(between %d ~ 1):" %user_input))
            if user_input >= temp_num:
                print("The number toot bigger!!!Try again!!!")
                user_input = temp_num

