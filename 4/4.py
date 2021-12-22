
with open("input_4.txt", "r") as file:
    lines = file.readlines()
    lines_clear = [i.rstrip() for i in lines]

numbers_raw = lines_clear[0].split(",")
numbers = [int(i) for i in numbers_raw]
boards = lines_clear[2:]
boards_splited = [list(map(int, i.split())) for i in boards if len(i) > 0]
boards_separate = [boards_splited[i:i + 5] for i in range(0, len(boards_splited), 5)]


vertical_lines = []
for i in range(len(boards_separate)):
    for j in range(5):
        line = []
        for k in range(5):
            line.append(boards_separate[i][k][j])
        vertical_lines.append(line)
vertical_lines_separate = [vertical_lines[i:i + 5] for i in range(0, len(vertical_lines), 5)]


def giant_squid(num, horizontal, vertical):

    for n in num:
        for i in range(len(horizontal)):
            for j in range(5):
                if n in horizontal[i][j]:
                    horizontal[i][j].remove(n)
        for i in range(len(vertical)):
            for j in range(5):
                if n in vertical[i][j]:
                    vertical[i][j].remove(n)

        for board in horizontal:
            for lin in board:
                if len(lin) == 0:
                    winning_board = horizontal.index(board)
                    return n, vertical[winning_board]
        for board in vertical:
            for lin in board:
                if len(lin) == 0:
                    winning_board = vertical.index(board)
                    return n, horizontal[winning_board]


data = giant_squid(numbers, boards_separate, vertical_lines_separate)


def final(data):
    res = 0
    for el in data[1]:
        res += sum(el)
    return res * data[0]

print(final(data))