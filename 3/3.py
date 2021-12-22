import math

def binary_diagnostic(my_input):
    gamma_rate = ""
    epsilon_rate = ""

    for i in range(len(my_input[0])):
        zeros = 0
        ones = 0
        for num in my_input:
            if num[i] == "0":
                zeros += 1
            else:
                ones += 1

        if zeros > ones:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


with open("input_3.txt", "r") as file:
    lines = file.readlines()
    lines_clear = [i.rstrip() for i in lines]



print(binary_diagnostic(lines_clear))