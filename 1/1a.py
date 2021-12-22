
def radar_window():
    with open("input.txt", "r") as file:
        radky = file.readlines()
        radky_int = [int(i.rstrip()) for i in radky]
        cnt = 0

        for i in range(len(radky_int) - 3):
            if radky_int[i] + radky_int[i + 1] + radky_int[i + 2] < radky_int[i + 1] + radky_int[i + 2] + radky_int[i + 3]:
                cnt += 1
        return cnt

print(radar_window())
