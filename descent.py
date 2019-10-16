# https://www.codingame.com/ide/puzzle/the-descent

import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

# init variables
mountain = {}
mountain_max = 0
mountain_maxindex = 0

# game loop
while True:
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        mountain[i] = mountain_h
        print(f"Height of mountain {i} : {mountain[i]}")
    
	# Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    mountain_max = 0
    mountain_maxindex = 0
    for i in range(8):
        if mountain[i] > mountain_max :
            mountain_maxindex = i		
            mountain_max = mountain[i]

    # The index of the mountain to fire on.
    print(f"Fire on mountain {mountain_maxindex} : {mountain[mountain_maxindex]}")