"""

Temperatures

Based on https://www.codingame.com/ide/puzzle/temperatures

The Goal
    In this exercise, you have to analyze records of temperature to
    find the closest to zero.

    Sample temperatures- Here, -1 is the closest to 0.

Rules
    Write a program that prints the temperature closest to 0 among
    input data. If two numbers are equally close to zero, positive
    integer has to be considered closest to zero (for instance, if
    the temperatures are -5 and 5, then display 5).

Input
    Your program must read the data from the standard input and
    write the result on the standard output.

Input
    Line 1: N, the number of temperatures to analyze
    Line 2: A string with the N temperatures expressed as integers ranging from -273 to 5526

Output
    Display 0 (zero) if no temperatures are provided.
    Otherwise, display the temperature closest to 0.

Constraints
    0 ≤ N < 10000

Date: October, 19 2019
""" 

import sys
import math

DEBUG = 0
DMAX = 5526
DMIN = 0
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
d_min = DMAX
index = 0
min_index = index
t_min = DMAX
n = int(input())  # the number of temperatures to analyse
if n == 0 :
    print(f"0")
else :
    for i in input().split():
        # t: a temperature expressed as an integer ranging from -273 to 5526
        index = index + 1
        t = int(i)
        d = abs (t - DMIN)
        if d < d_min or (d == d_min and t > 0) :
            t_min = t
            min_index = index
            d_min = d
        if DEBUG :
            print(f"t[{index}]= {t}; Dist: {d}, t_min = t[{index}]: {t}")
            pass

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    print(f"{t_min}")