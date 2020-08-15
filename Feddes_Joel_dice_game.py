#Joel Feddes
#This program is designed to use two dice to determine, depending on your results, whether you win the game, lose, or need to keep rolling reach a result (win or lose).
#On the first role if you role a 7 or 11 you win the game. If you roll a 2,3, or 12 you lose.
#if your result isn't any of those combinations, you will roll again in an attempt to get that same result on your next roll. If you roll a 7 you lose.
#If you do not roll the targeted number or 7, you will be asked to roll again until one instance occurs (win or lose).
#After winning or losing, you will be asked if you want to play again.


import random

print("Welcome to Joel's dice game")

roll_again = "y"

while roll_again == "y":
    input("\nPress Enter to roll.").strip().lower()

    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)

#setup for if you roll a 7 or a 11 on the first roll.
    
    if dice_1 + dice_2 == 7 or dice_1 + dice_2 == 11:
        
        one_kind_sum = dice_1 + dice_2
        
        print("You rolled a %d and a %d, for a total of %d.\nYou won!" % (dice_1, dice_2, one_kind_sum))

#Condition if you roll a 2, 3, or 12 on the first roll (lose).
        
    elif dice_1 + dice_2 == 2 or dice_1 + dice_2 == 3 or dice_1 + dice_2 == 12:
        combine_rolls = dice_1 + dice_2

        print("You rolled %d and %d, for a total of %d.\nYou lost!" % (dice_1, dice_2, combine_rolls))

#If user rolls neither a winning or a losing roll, he/she will enter the second loop until he/she does either win or lose.

    else:
        sum_rolls = dice_1 + dice_2
        input("you rolled %d and %d, for a total of %d.\nYour target is now %d. Don't roll a 7!.\n\nPress Enter to roll" % (dice_1, dice_2, sum_rolls, sum_rolls)).strip().lower()

        roll_once_again = ""

        while roll_once_again == "":
            
            dice_3 = random.randint(1,6)
            dice_4 = random.randint(1,6)

#line for If the combined rolls are equal to the target, the user wins.
            
            if dice_3 + dice_4 == sum_rolls:
                print("You rolled a %d and a %d which combines to be %d!" % (dice_3, dice_4, sum_rolls))
                print("Congradulations. Because you rolled the target, you won!")
                break

#If the user rolls a 7 condition.
    
            elif dice_3 + dice_4 == 7:
                print("You rolled %d and %d, for a total of 7.\nYou lost because you rolled a 7." % (dice_3, dice_4))  
                break

#If the user does not win or lose on the previous roll, this line will restart the secondary loop (not restart the program from the begining).
            
            else:
                another_sum = dice_3 + dice_4
                print("You rolled %d and %d, for a total of %d." % (dice_3, dice_4, another_sum))
                input("\nPress Enter to roll").strip().lower()
                
#I had some issues when the second loop (within the first else statement) was satisfied. I pressed y to play again, but it would start me up at the second loop again.
#After some google searches, I discovered breaks and that fixed the issue.
                
    roll_again = input("\nDo you want to play again? (y or n) ").strip().lower()
    
print("\nThank you for playing.")
            




        
