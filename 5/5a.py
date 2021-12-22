input_file = "input_5.txt"


def get_lines_one_list_raw(file):
    with open(file, "r") as file:
        lines = file.readlines()
    return lines


list_raw = get_lines_one_list_raw(input_file)


def cut_n(list_of_instructions):
    return [i.rstrip() for i in list_of_instructions]


list_without_n = cut_n(list_raw)


def split_strings_to_lists(list_of_instructions):
    return [i.split(" -> ") for i in list_of_instructions]


splitted_list_to_points = split_strings_to_lists(list_without_n)


def separate_points(list_of_instructions):
    lines_int = []
    for el in list_of_instructions:
        _ = []
        for num in el:
            _.append(num.split())
        lines_int.append(_)
    return lines_int


separated_points = separate_points(splitted_list_to_points)


def split_x_y(list):
    final = []
    for instruction in list:
        _ = []
        for point in instruction:
            _.append(point[0].split(","))
        final.append(_)
    return final


splitted_x_y = split_x_y(separated_points)


def string_to_integers(list):
    final = []
    for instruction in list:
        _ = []
        for point in instruction:
            point_list = []
            point_list.append(int(point[0]))
            point_list.append(int(point[1]))
            _.append(point_list)
        final.append(_)
    return final


instructions = string_to_integers(splitted_x_y)


def find_max_x_y(list):
    x_y = [0, 0]
    for instruction in list:
        for point in instruction:
            if point[0] > x_y[0]:
                x_y[0] = point[0]
            elif point[1] > x_y[1]:
                x_y[1] = point[1]
    return x_y


max_x_y = find_max_x_y(instructions)


def make_array(list):
    array = [[0] * (list[0] + 1) for _ in range(list[1] + 1)]
    # line = []
    # for y in range(list[1]):
    #     line.append(0)
    # for x in range(list[0]):
    #     array.append(line)
    return array


array = make_array(max_x_y)


def get_x1_y1_x2_y2(list):  # [[x1,y1],[x2,y2]] - return dict
    points = {"x1": list[0][0], "y1": list[0][1], "x2": list[1][0], "y2": list[1][1]}
    return points


def mark_positions(empty_list, list):
    for instruction in list:
        points = get_x1_y1_x2_y2(instruction)
        if points["x1"] == points["x2"]:  # souradice X jsou shodne
            x = points["x1"]
            if points["y1"] > points["y2"]:
                for i in range(points["y2"], points["y1"] + 1):
                    empty_list[i][x] += 1
            if points["y2"] > points["y1"]:
                for i in range(points["y1"], points["y2"] + 1):
                    empty_list[i][x] += 1


        elif points["y1"] == points["y2"]:  # souradnice Y jsou schodne
            y = points["y1"]
            if points["x1"] > points["x2"]:
                for i in range(points["x2"], points["x1"] + 1):
                    empty_list[y][i] += 1
            if points["x2"] > points["x1"]:
                for i in range(points["x1"], points["x2"] + 1):
                    empty_list[y][i] += 1

        elif points["x1"] < points["x2"] and points["y1"] < points["y2"]:
            for i in range(0, points["x2"] - points["x1"] + 1):
                empty_list[points["y1"] + i][points["x1"] + i] += 1

        elif points["x1"] > points["x2"] and points["y1"] > points["y2"]:
            for i in range(0, points["x1"] - points["x2"] + 1):
                empty_list[points["y2"] + i][points["x2"] + i] += 1

        elif points["x1"] < points["x2"] and points["y1"] > points["y2"]:
            for i in range(0, points["x2"] - points["x1"] + 1):
                empty_list[points["y2"] + i][points["x2"] - i] += 1

        elif points["x1"] > points["x2"] and points["y1"] < points["y2"]:
            for i in range(0, points["x1"] - points["x2"] + 1):
                empty_list[points["y1"] + i][points["x1"] - i] += 1

    return empty_list


mark_positions(array, instructions)


res = 0
for line in array:
    for el in line:
        if el >= 2:
            res += 1
print(res)
