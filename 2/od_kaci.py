def load_lines(file_name: str):
    #Nacte radky ze souboru, bez prazdnych znaku.
    with open(file_name) as file:
        return [line.strip() for line in file]
move_info = load_lines("input_course.sql")
print(len(move_info))

horiz_pose = 0
depth = 0
aim = 0

for el in move_info:
    t, i = el.split()
    print(t)
    print(i)
    if t == "forward":
        depth += aim * int(i)
        horiz_pose += int(i)
    elif t == "down":
        aim += int(i)
        depth += int(i)
    elif t == "up":
        aim -= int(i)
        depth -= int(i)

print(horiz_pose*depth)