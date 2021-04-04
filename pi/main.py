#main

import random
import math


def get_throws(t):
    throws = []
    for i in range(t):
        x_value = random.random()
        y_value = random.random()
        x = x_value * 5
        y = y_value * 5
        coords = (x, y)
        throws.append(coords)
    return throws

def in_circle(throws, d):
    in_the_circle = []
    r = d/2
    for throw in throws:
        distance = math.sqrt((r - throw[0])**2 + (r - throw[1])**2)
        if distance < r:
            x = 1
            in_the_circle.append(x)

    return in_the_circle

def get_pi(circle_num, t):
    cnum = len(circle_num)
    pi = ((4*cnum)/ (t))
    return pi


if __name__ == "__main__":
    d = 5.0
    t = 10000000000
    throws = get_throws(t)
    #print(throws)
    circle_num = in_circle(throws, d)
    #print(circle_num)
    pi_value = get_pi(circle_num, t)
    print(pi_value)
