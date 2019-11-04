from boxing import Boxer
import time
import boxing

fighterOne = Boxer(input("First Fighter Name:  "))
fighterTwo = Boxer(input("Second Fighter Name:  "))
turn = 20
while fighterOne.receiveHeath() > 0 and fighterTwo.receiveHeath() > 0:
    if turn % 2 == 0:
        fighterOne.hit(fighterTwo)
        time.sleep(2)  # Delays for 2 seconds.
        turn = turn - 1
    else:
        fighterTwo.hit(fighterOne)
        time.sleep(2)  # Delays for 2 seconds.
winner = fighterOne if fighterTwo.receiveHeath() == 0 else fighterTwo
print(f'{winner.name} won')
