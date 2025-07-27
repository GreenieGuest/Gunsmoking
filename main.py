import random
from time import sleep

class Player:
    def __init__(self, name, spinTokens):
        self.name = name
        self.spinTokens = spinTokens

names_string = input("Enter names of contestants, separated by a comma. (Example: 'Alpha,Bravo,...')\n")
names = names_string.split(",")

players = [Player(item, 1) for item in names]

print("Gunsmoking.")
sleep(1)
currentHolder = random.choice(players) # First spin is always random.
chamber = random.randint(1, 6)
chance = 6

while len(players) > 1:
    if currentHolder.spinTokens > 0:
        print(f"The gun is passed to {currentHolder.name}*.")
    else:
        print(f"The gun is passed to {currentHolder.name}.")
    print(f"The chance is 1 out of {chance}.")

    # Re-Spin Pass
    if (currentHolder.spinTokens > 0):
        usage = random.randint(1, chance) # Lower chances = more likelihood of re-spinning the barrel
        if usage == 1:
            sleep(.5)
            print("...")
            sleep(3)
            print(f"{currentHolder.name} uses their Re-Spin token.")
            chamber = random.randint(1, 6)
            chance = 6
            currentHolder.spinTokens -= 1
            sleep(1)
            print(f"The chance is 1 out of {chance}.")

    # From here on out, it is basic Russian Roulette
    sleep(.5)
    print("...")
    sleep(random.randint(1, 5))
    if chance != chamber:
        print("Click.")
        sleep(.5)
        print(f"{currentHolder.name} survives.")
        nomination = random.choice(players)
        while nomination == currentHolder:
            nomination = random.choice(players)
        currentHolder = nomination
        sleep(1)

        # Rules: the game progresses by players nominating each other until only one remains. Normally there is strategy involved, but this is a simulation

        print(f"They nominate {currentHolder.name}.")
        chance -= 1
        sleep(.5)
        
    else:
        print("BANG.")
        sleep(.5)
        print(f"{currentHolder.name} has been eliminated.")
        players.remove(currentHolder)
        sleep(2)
        print(f"And then there were {len(players)}...")
        sleep(2)

        print(f"The gun is reloaded.")
        currentHolder = random.choice(players)
        chamber = random.randint(1, 6)
        chance = 6
        sleep(.5)
print(f"The sole survivor is {currentHolder.name}.")
sleep(10)