import random
from math import ceil

def genMaze(array):
    # width and height dont include outside walls
    # -2 to remove walls
    width = len(array[0])-2
    height = len(array)-2

    halfWidth = width/2 if width%2 == 0 else ceil(width/2)
    halfHeight = height/2 if height%2 == 0 else ceil(height/2)

    # split into quarters... i cant spell :(
    for row in range(len(array)):
        for i in range(len(array[row])):
            if i == halfWidth:
                array[row][i].state = "wall"
            if row == halfHeight:
                array[row][i].state = "wall"
    