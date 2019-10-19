# The Descent
# Based on https://www.codingame.com/ide/puzzle/the-descent

import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

# Init variables
land = 0
altitude = 9
mountain = {}
mountain_max = 0
mountain_min = 0
mountain_maxindex = 0
mountain_minindex = 0

# Game start
# print(f"Let's destroy those mountains to secure our landing...")
   
# Input values
for i in range(8):
    mountain_h = int(input())  # represents the height of one mountain.
    mountain[i] = mountain_h
    
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# Print Heights
for i in range(8):
    # print(f"Height of mountain {i} : {mountain[i]}")
	pass

# Descent loop
l = 0
while land == 0:
    # for l in range(8):
    altitude = 9 - int(l)

    # Calculate max value for targeting and min value for landing
    mountain_max = 0
    mountain_min = 0
    mountain_maxindex = 0
    for i in range(8):
        if mountain[i] > mountain_max :
            mountain_maxindex = i		
            mountain_max = mountain[i]
        if mountain[i] < mountain_min :
            mountain_minindex = i		
            mountain_min = mountain[i]
	        
    # Bombing
    print(f"{mountain_maxindex}")
    if mountain_max == 0 :
        # print(f"Congratulations, you can land with your spaceship!")
        land = 1
    else :
        # print(f"Your spaceship targeted mountain {mountain_maxindex}, your altitude is now {altitude}")
        mountain[mountain_maxindex] = 0;
        if altitude > mountain_max :
            # print(f"BOOOOMM!! Nice Shot!")
            pass

    altitude = altitude -1

    # Print New Heights
    for i in range(8):
        # print(f"Height of mountain {i} : {mountain[i]}")
        pass

    l = l + 1
# game loop ends