def task_1():
    s = set()
    n = int(input('Длина набора: '))
    for i in range(n):
        s.add(int(input('Введите элемент: ')))
    print(len(s))

def task_2():
    a = set()
    b = set()
    a_sz = int(input('Длина набора а: '))
    for i in range(a_sz):
        a.add(int(input('Введите элемент набора а: ')))
    b_sz = int(input('Длина набора б: '))
    for i in range(b_sz):
        b.add(int(input('Введите элемент набора а: ')))
    print(a.issubset(b) and len(a) != len(b))

def task_3():
    cities = set()
    cities_size = int(input('Список городов: '))
    notEqual = 0
    for i in range(cities_size):
        cities.add(input('Запомнить город: '))
        notEqual = len(cities)
    cities.add(input('Входящий город: '))

    if len(cities) != notEqual:
        print('OK')
    else:
        print('REPEAT')

    return

if __name__ == '__main__':
    task = input("Enter task number: ")
    if task == '1':
        task_1()
    elif task == '2':
        task_2()
    elif task == '3':
        task_3()