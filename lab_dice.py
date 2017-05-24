from random import randint

def dice_roll(num_dice, num_side):
    num_dice = int(num_dice)
    num_side = int(num_side)
    while num_dice > 0:
        print("Roll: ", randint(1, num_side))
        num_dice = num_dice - 1

num_dice = input("How many dice do you want to roll? ")
num_side = input("How many sides do you want each dice to have? ")

print(dice_roll(num_dice, num_side))
