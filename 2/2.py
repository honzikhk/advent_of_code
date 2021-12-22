
def course():
    with open("input_course.sql", "r") as file:
        radky = file.readlines()
        radky_ciste = [i.rstrip().split() for i in radky]
        horizontal_position = 0
        depth = 0
        for i in radky_ciste:
            if i[0] == "forward":
                horizontal_position += int(i[1])
            elif i[0] == "down":
                depth += int(i[1])
            elif i[0] == "up":
                depth -= int(i[1])
        print(f"horizontalni pozice: {horizontal_position} a hloubka je: {depth}")
        return depth * horizontal_position

print(course())