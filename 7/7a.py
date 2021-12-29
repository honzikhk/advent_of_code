
input_file = "input_7.sql"


def get_lines_one_list_raw(file):
    with open(file, "r") as file:
        lines = file.readlines()
    return lines


list_raw = get_lines_one_list_raw(input_file)


def cut_n(list):
    return [list[0].strip()]


cutted = cut_n(list_raw)


def split_the_big_string(list):
    return list[0].split(",")


splitted = split_the_big_string(cutted)


def make_int(list):
    return [int(i) for i in list]


integers = make_int(splitted)


def find_lowest(list):
    return min(list)


def find_highest(list):
    return max(list)


highest_position = find_highest(integers)


def count_fuel(list):
    lvl_vs_fuel = {}
    for level in range(highest_position + 1):
        fuel = 0
        for position in integers:
            if level > position:
                for _ in range(1, (level - position) + 1):
                    fuel += _
            elif level < position:
                for _ in range(1, (position - level) + 1):
                    fuel += _
            else:
                fuel += 0
        lvl_vs_fuel[level] = fuel
    return lvl_vs_fuel


dictionary_of_lvl_and_fuel = count_fuel(integers)
print(dictionary_of_lvl_and_fuel)

def find_cheapest_position(dict_data):
    cheapest = dict_data[0]
    level = 0
    for lvl in dict_data:
        if dict_data[lvl] < cheapest:
            cheapest = dict_data[lvl]
            level = lvl
    return cheapest


print(find_cheapest_position(dictionary_of_lvl_and_fuel))