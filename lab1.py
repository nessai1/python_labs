def task_1():
    a = input("a: ")
    b = input("b: ")
    c = input("c: ")
    if a == b and b == c:
        print(3)
        return
    if a == b or a == c or b == c:
        print(2)
        return
    print(0)


def task_2_1():
    n = int(input("n: "))
    stage = ''
    for i in range(1, n+1):
        stage += str(i)
        print(stage)


def task_2_2():
    n = int(input("n: "))
    pos = int((n * 2 - 1) / 2)
    for i in range(1, n + 1):
        for j in range(pos - i + 1):
            print(end=" ")
        for j in range(1, i * 2):
            if j <= i:
                print(j, end="")
            else:
                print(i - (j - i), end="")
        for j in range(pos - i + 1):
            print(end=" ")
        print()


def task_2_3():
    n = int(input("Enter n = "))
    if n < 10:
        kol = n * 2 - 1
    elif n < 100:
        kol = 2 * 9 - 1 + 2 * 2 * (n - 9) - 1
    elif n < 1000:
        kol = 2 * 9 - 1 + 2 * 2 * n - 1 + 3 * 2 * n - 1
    f = False
    if kol % 2 == 0:
        f = True
    string = ""
    for i in range(1, n + 1):
        for j in range(1, i * 2):
            if j <= i:
                string += str(j)
                if f and j < 10:
                    string += " "
            else:
                string += str(i - (j - i))
                if f and i - (j - i) < 10:
                    string += " "
        string = string.center(kol + 17, ' ')
        print(string)
        string = ""


if __name__ == '__main__':
    task = input("Enter task number: ")
    if task == '1':
        task_1()
    elif task == '2.1':
        task_2_1()
    elif task == '2.2':
        task_2_2()
    elif task == '2.3':
        task_2_3()