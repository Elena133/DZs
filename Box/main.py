from boxing import boxMy
import time

fighterOne = boxMy(input("First Fighter Name:  "))
fighterTwo = boxMy(input("Second Fighter Name:  "))

healthOne = fighterOne.health
healthTwo = fighterTwo.health

while healthOne > 0 or healthTwo > 0:
    dOne = fighterOne.getDamage()
    dTwo = fighterTwo.getDamage()
    healthOne = healthOne - dTwo
    healthTwo = healthTwo - dOne
    if healthTwo > 0:
        print(healthTwo, fighterTwo.name,"'s remained healthy, after ", fighterOne.name, 'hit for ', dOne)
        time.sleep(2)  # Delays for 2 seconds.
    else:
        print(fighterTwo.name, 'lost')
        break
    if healthOne > 0:
        print(healthOne, fighterOne.name,"'s remained healthy, after ", fighterTwo.name, 'hit for ', dTwo)
        time.sleep(2)  # Delays for 2 seconds.
    else:
        print(fighterOne.name, 'lost')
        break
