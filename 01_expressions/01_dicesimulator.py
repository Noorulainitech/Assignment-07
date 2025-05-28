import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(f"Die 1: {die1}, Die 2: {die2}")

def main():
    print("Rolling the dice 3 times:")
    roll_dice()
    roll_dice()
    roll_dice()

main()
