
def radar():
    with open("input.txt", "r") as file:
        radky = file.readlines()
        radky_int = [int(i.rstrip()) for i in radky]
        cnt = 0

        for i in range(len(radky_int) - 1):
            if radky_int[i] < radky_int[i + 1]:
                cnt += 1
        return cnt

print(radar())