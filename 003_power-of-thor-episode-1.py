# https://www.codingame.com/ide/puzzle/power-of-thor-episode-1

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
MAX_X = 39
MAX_Y = 17
MIN_X = 0
MIN_Y = 0

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
actual_tx = initial_tx
actual_ty = initial_ty
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    dist_x = light_x - actual_tx
    dist_y = light_y - actual_ty
    
    if dist_y > 0 and actual_ty < MAX_Y and dist_x > 0 and actual_tx < MAX_X :
        print("SE")
        actual_tx = actual_tx + 1 
        actual_ty = actual_ty + 1 

    if dist_y > 0 and actual_ty < MAX_Y and dist_x < 0 and actual_tx > MIN_X :
        print("SW")
        actual_tx = actual_tx - 1 
        actual_ty = actual_ty + 1 

    if dist_y < 0 and actual_ty > MIN_Y and dist_x > 0 and actual_tx < MAX_X :
        print("NE")
        actual_tx = actual_tx + 1 
        actual_ty = actual_ty - 1

    if dist_y < 0 and actual_ty > MIN_Y and dist_x < 0 and actual_tx > MIN_X :
        print("NW")
        actual_tx = actual_tx - 1 
        actual_ty = actual_ty - 1

    if dist_y > 0 and actual_ty < MAX_Y and dist_x == 0 :
        print("S")
        actual_ty = actual_ty + 1 
    if dist_y < 0 and actual_ty > MIN_Y and dist_x == 0 :
        print("N")
        actual_ty = actual_ty - 1
    if dist_x > 0 and actual_tx < MAX_X and dist_y == 0 :
        print("E")
        actual_tx = actual_tx + 1 
    if dist_x < 0 and actual_tx > MIN_X  and dist_y == 0 :
        print("W")
        actual_tx = actual_tx - 1
    # A single line providing the move to be made: N NE E SE S SW W or NW
