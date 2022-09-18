# Есть робот.
# Принимаем команду для робота, up/down/left/right, через пробел количество шагов(integer). Выход из ввода команд по пробелу.
# Задача: посчитать отрезок между начальным и конечным положением робота.
import math

steps = []
commands = ["U","D","L","R"]
while True:
    a = input("Enter commands for robot. For example: 'U 3' or 'D 6'(Enter a space for exit): ")
    if (a[0] not in commands) or (a[1] != " ") or a[2:].isdigit() == False:
        if a == " ":
            break
        print("Command format is false!")
    else:
        step = steps.append(a)
    
print("You typed:", ', '.join(steps))

start_x = int(input("Enter start point X(integer): "))
start_y = int(input("Enter start point Y(integer): "))

finish_x = start_x
finish_y = start_y
for i in steps:
    match i[0]:
        case "U":
            finish_y += int(i[2:])
        case "D":
            finish_y -= int(i[2:])
        case "L":
            finish_x -= int(i[2:])
        case "R":
            finish_x += int(i[2:])
start_to_finish = math.sqrt((finish_x - start_x)**2 + (finish_y - start_y)**2)
start_to_finish = round(start_to_finish, 2)

print("The distance between start and finish points is", start_to_finish)







    