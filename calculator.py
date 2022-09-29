doesUserWantToExit = False
import os

while doesUserWantToExit == False:                             # User does not want to exit
    os.system('cls')

    # A calculator for mathematical operations on two numbers provided by the user
    print("""Welcome user, please type the number next to the option you want to choose  -
    1. Addition
    2. Subtraction
    3. Multplication
    4. Division""")

    user_choice = int(input("Enter your choice: "))
    if not(user_choice >=1 and user_choice<=4):             # not whithin range
        print("Not supported choice")
    else:                                                   # within range
        print("Enter two numbers")
        firstnumber = float(input())
        secondnumber = float(input())

        if user_choice == 1:
            print(firstnumber+secondnumber)
        elif user_choice == 2:
            if firstnumber>secondnumber:
                print(firstnumber-secondnumber)
            else:
                print(secondnumber-firstnumber)
        elif user_choice == 3:
            print(firstnumber*secondnumber)    

        elif user_choice == 4:
            if secondnumber == 0:
                print("Cannot divide by 0, sorry!")
            else:    
                print(firstnumber/secondnumber)
    
    continueOrNot = input("Do you want to continue? (y/n)")
    if continueOrNot == 'y':
        doesUserWantToExit = False
    elif continueOrNot == 'n':
        doesUserWantToExit = True
    else:
        print('Wrong input!!!!')
        break

print("SAYONARA!")