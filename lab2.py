def task_1():
    print('Треугольник Паскаля')
    n = int(input('n: '))
    rs = [1]
    for i in range(n):
        print(rs)
        rs = [sum(x) for x in zip([0] + rs, rs + [0])]


def task_2():
    print('Треугольник Серпинского')
    n = int(input('n: '))
    depth = 2 ** n
    rs = [0] * depth
    for i in range(depth):
        rs[i] = [0] * depth
        rs[i][0] = 1
        rs[i][i] = 1

    for i in range(1, depth):
        for j in range(1, depth):
            rs[i][j] = (rs[i - 1][j - 1] + rs[i - 1][j]) % 2

    for i in range(depth):
        print(' ' * int(((depth - i) / 2)), end='')
        for j in range(depth):
            res = '*' if rs[i][j] == 1 else ' '
            print(res, end='')
        print()


if __name__ == '__main__':
    task = input("Enter task number: ")
    if task == '1':
        task_1()
    elif task == '2':
        task_2()