import os

def course():
    with open("input_course.sql", "r") as file:
        radky = file.readlines()
        radky_ciste = [i.rstrip().split() for i in radky]
        print(radky_ciste)
        horizontal_position = 0
        depth = 0
        aim = 0
        for i in radky_ciste:
            if i[0] == "forward":
                horizontal_position += int(i[1])
                depth += aim * int(i[1])
            elif i[0] == "down":
                aim += int(i[1])
            elif i[0] == "up":
                aim -= int(i[1])
        print(f"hloubka je: {depth} a horizontalni pozice: {horizontal_position}")
        return depth * horizontal_position

print(course())