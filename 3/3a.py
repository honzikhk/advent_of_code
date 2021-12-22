
def oxygen_generator_rating(my_input):
    mod_input = my_input
    for i in range(len(my_input[0])):
        zeros = []
        ones = []
        for num in mod_input:
            if num[i] == "0":
                zeros.append(num)
            else:
                ones.append(num)
        if len(mod_input) == 1:
            return mod_input
        elif len(zeros) == 1 and len(ones) == 1:
            return ones
        elif len(zeros) == len(ones):
            mod_input = ones
        elif len(zeros) > len(ones):
            mod_input = zeros
        else:
            mod_input = ones


def co2_scrubber_rating(my_input):
    mod_input = my_input
    for i in range(len(my_input[0])):
        zeros = []
        ones = []
        for num in mod_input:
            if num[i] == "0":
                zeros.append(num)
            else:
                ones.append(num)
        if len(mod_input) == 1:
            return mod_input
        elif len(zeros) == 1 and len(ones) == 1:
            return zeros
        elif len(zeros) == len(ones):
            mod_input = zeros
        elif len(zeros) < len(ones):
            mod_input = zeros
        else:
            mod_input = ones


def life_support_rating():
    oxygen = int(oxygen_generator_rating(lines_clear)[0], 2)
    co2 = int(co2_scrubber_rating(lines_clear)[0], 2)
    return oxygen * co2


with open("input_3.txt", "r") as file:
    lines = file.readlines()
    lines_clear = [i.rstrip() for i in lines]


print(life_support_rating())
