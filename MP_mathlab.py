'''write a program that prints out the sine and cosine of
the angles ranging from 0 to 345 degrees in 15 degrees increments
each result should be rounded to 4 decimal places
'''
#import sin and cosine -- trigonometry functions
import math

for i in range(0,350,15):
    #math.radians -- radians to degrees conversion
    x = math.sin(math.radians(i))
    y = math.cos(math.radians(i))
    print(i, round(x,4), round(y,4))
