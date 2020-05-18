import argparse
import sys
import random


class Monyhall(argparse.Action):
    def __init__(self, args, **kwargs):
        number = int(args[1])
        switch = bool(args[2])
        win = 0
        loose = 0

        for i in range(number):
            doors = [1, 2, 3]
            pick = random.randint(1, len(doors))
            correctDoor = random.randint(1, len(doors))
            wrongDoors = doors.copy()
            wrongDoors.remove(correctDoor)
            removedDoor = random.randint(0, len(wrongDoors)-1)
            if (wrongDoors[removedDoor] == pick):
                removedDoor -= 1

            numberToRemove = wrongDoors[removedDoor]
            doors.remove(numberToRemove)

            if (switch):
                pick = doors[doors.index(pick)-1]

            if pick == correctDoor:
                win += 1
            else:
                loose += 1

        print("win", win)
        print("loose", loose)


Monyhall(sys.argv)
