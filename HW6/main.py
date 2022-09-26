from datetime import datetime
import time
import os

square = '$$'
space = '\u0020'
numbers = {'0': (square*6, square*6, square*2 + space*4 + square*2, square*2 + space*4 + square*2, square*2 + space*4 + square*2, square*2 + space*4 + square*2, square*2 + space*4 + square*2, square*6, square*6),
           '1': (space*8 + square*2, space*8 + square*2, space*8 + square*2, space*8 + square*2, space*8 + square*2, space*8 + square*2, space*8 + square*2, space*8 + square*2, space*8 + square*2),
           '2': (square*6, square*6, square*2 + space*4 + square*2, space*8 + square*2, space*6 + square*2 + space*2, space*4 + square*2 + space*4, space*2 + square*2 + space*6, square*6, square*6),
           '3': (square*6, square*6, space*8 + square*2, space*8 + square*2, space*4 + square*4, space*8 + square*2, space*8 + square*2, square*6, square*6),
           '4': (square*2 + space*4 + square*2, square*2 + space*4 + square*2, square*2 + space*4 + square*2, square*2 + space*4 + square*2, square*6, square*6, space*8 + square*2, space*8 + square*2, space*8 + square*2),
           '5': (square*6, square*6, square*2 + space*8, square*6, square*6, space*8 + square*2, space*8 + square*2, square*6, square*6),
           '6': (square*6, square*6, square*2 + space*8, square*6, square*6, square*2 + space*4 + square*2, square*2 + space*4 + square*2, square*6, square*6),
           '7': (square*6, square*6, space*7 + square*2 + space, space*6 + square*2 + space*2, space*5 + square*2 + space*3, space*4 + square*2 + space*4, space*3 + square*2 + space*5, space*2 + square*2 + space*6, space + square*2 + space*7),
           '8': (square*6, square*6, square*2 + space*4 + square*2, square*2 + space*4 + square*2, square*6, square*2 + space*4 + square*2, square*2 + space*4 + square*2, square*6, square*6),
           '9': (square*6, square*6, square*2 + space*4 + square*2, square*6, square*6, space*8 + square*2, space*8 + square*2, square*6, square*6),
           ':': (space*4, square*2, square*2, space*4, space*4, space*4, square*2, square*2, space*4)
        }

while True:
    current_time = datetime.now().time()
    current_time_str = current_time.strftime('%H%M%S')
    os.system('cls||clear') #screen clean
    for pos1, pos2, pos3, pos4, pos5, pos6, separator in zip(numbers[current_time_str[0]], numbers[current_time_str[1]], numbers[current_time_str[2]], numbers[current_time_str[3]], numbers[current_time_str[4]], numbers[current_time_str[5]], numbers[':']):
        print(pos1, pos2, separator, pos3, pos4, separator, pos5, pos6)
    time.sleep(.00001)
    
    