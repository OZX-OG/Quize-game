import random
from os import system

a, b = 1, 100
mini, maxi, trys = a, b, 6
ran_number =  random.randint(a, b)
# print(ran_number)

def score():
    system("cls")
    print(f"-----------------------")
    print(f"| number: {mini} < x < {maxi} |")
    print(f"-----------------------")
while True:
    if trys == 0: 
        system("cls")
        print(f"\t\t -------- You lose! -------- \n\t\t   Number is: {ran_number}, try again\n\t\t -------- You lose! -------- ")
        print("______________________________________________________________")
        mini, maxi, trys = a, b, 6
        ran_number = random.randint(a, b)


    print(f"You Have Only {trys} Trys, be careful")
    print(f"- Quest number between {a} and {b} -")

    try: clie_number = int(input("Quest: "))
    except ValueError: 
        score()
        continue
 
    if clie_number == ran_number:
        system("cls")
        print(f"\t\t -------- You win! -------- \n\t\t\tNumber is: {ran_number}\n\t\t -------- You win! -------- ")
        print("______________________________________________________________")
        
        mini, maxi, trys = a, b, 6
        ran_number = random.randint(a, b)
        # print(ran_number)
        continue

    elif clie_number > ran_number:
        if maxi > clie_number: maxi = clie_number; trys -= 1
        score()
        continue

    elif clie_number < ran_number:
        if mini < clie_number: mini = clie_number; trys -= 1
        score()
        continue