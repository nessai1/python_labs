def task_0():
    lst = [2, 1, 0, 4, 3]
    rs = []
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            rs.append(lst[i])
    print(rs)

def task_1():
    lst = [-4100, 12, 65, 700, 61000]
    mx = max(lst)
    mn = min(lst)

    for i in range(len(lst)):
        if lst[i] == mx:
            lst[i] = mn
        elif lst[i] == mn:
            lst[i] = mx
    print(lst)

def task_2():
    l1 = [5, 3, 76, 14, 44]
    l2 = [44, 21, 12, 76]
    cnt = 0
    for i in l1:
        for j in l2:
            if i == j:
                cnt += 1
                break
    print(cnt)

def task_3():
    result = {}
    strings = []
    print("1. ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']\n2. ['aaa', 'bbb', 'ccc']\n3. ['abc', 'abc', 'abc']\n")
    v = int(input("Выберете вариант входных данных:\n"))
    if v == 1:
        n = 7
        strings = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
    elif v == 2:
        n = 3
        strings = ['aaa', 'bbb', 'ccc']
    elif v == 3:
        n = 3
        strings = ['abc', 'abc', 'abc']
    else:
        print("Неверный вариант")
        return

    cnt = 1
    strings.sort()

    for i in range(len(strings) - 1):
        if strings[i] == strings[i + 1]:
            cnt += 1
        else:
            result[strings[i]] = cnt
            cnt = 1
    result[strings[n - 1]] = cnt
    print(result)



if __name__ == '__main__':
    task = input("Enter task number: ")
    if task == '0':
        task_0()
    elif task == '1':
        task_1()
    elif task == '2':
        task_2()
    elif task == '3':
        task_3()