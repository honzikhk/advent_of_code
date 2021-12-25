
input_file = "input_6.sql"

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


def minus_one(list):
    _ = []
    for num in list:
        _.append(num - 1)
    return _


one_minus = minus_one(integers)


def check_six_and_zeros_add_eight_and_sixs(list):
    for i in range(len(list)):
        if list[i] == -1:
            list[i] = 6
            list.append(int(8))
    return list


def iteration(list):
    temp_list = list
    cnt = 0
    while cnt < 256:
        #print(temp_list)
        #cont = int(input(f"Cnt: {cnt}. Put 1 for another step: "))
        #if cont == 1:
        temp_list = minus_one(temp_list)
        temp_list = check_six_and_zeros_add_eight_and_sixs(temp_list)
        cnt += 1
    return len(temp_list)


print(iteration(integers))







