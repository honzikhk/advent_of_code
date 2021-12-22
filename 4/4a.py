

def giant_squid(num, horizontal):

    for n in num:
        for board in horizontal:
            for lin in board:
                for i in range(5):
                    if lin[i] == n:
                        lin[i] = "x"
        #print(horizontal)


        for board in horizontal:
            for lin in board:
                cnt = 0
                for el in lin:
                    if el == "x":
                        cnt += 1
                        if cnt == 5:
                            mezi = board
                            horizontal.remove(board)

        for board in horizontal:
            for i in range(5):
                cnt = 0
                for lin in board:
                    if lin[i] == "x":
                        cnt += 1
                        if cnt == 5:
                            #mezi = horizontal
                            horizontal.remove(board)

        if len(horizontal) == 0:
            print(f"Posledni tazene cislo: {n}")
            print(f"Soucet zbyvajicich cisel na boardu: {sum_last_board(mezi)}")
            print(f"Výsledek: {n * sum_last_board(mezi)}")
            break


def sum_last_board(data):
    res = 0
    for el in data:
        for ele in el:
            if isinstance(ele, int):
                res += ele
    return res


with open("input_4.txt", "r") as file:
    lines = file.readlines()
    lines_clear = [i.rstrip() for i in lines]

numbers_raw = lines_clear[0].split(",")
numbers = [int(i) for i in numbers_raw]
boards = lines_clear[2:]
boards_splited = [list(map(int, i.split())) for i in boards if len(i) > 0]
boards_separate = [boards_splited[i:i + 5] for i in range(0, len(boards_splited), 5)]



giant_squid(numbers, boards_separate)


