def task_1():
    line = input('Введите строку символов: ')
    count = 1
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            count += 1
        else:
            if count > 1:
                print(line[i]+str(count), end='')
            else:
                print(line[i], end='')
            count = 1
    if count > 1:
        print(line[len(line)-1]+str(count), end='')
    else:
        print(line[len(line)-1], end='')

def task_1_1():
    line = input('Введите строчку для дешифровки: ')
    for i in range(len(line)):
        if line[i].isdigit():
            print(line[i-1]*(int(line[i])-1), end='')
        else:
            print(line[i], end='')

def task_2():
    line = input('Введите строку символов: ')
    dict = {}
    for i in line:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    for i in range(3):
        print(dict[i][0], end=' ')


def task_3():
    n = int(input())

    first_r = {
        1: 'один', 
        2: 'два', 
        3: 'три', 
        4: 'четыре', 
        5: 'пять',
        6: 'шесть',
        7: 'семь', 
        8: 'восемь', 
        9: 'девять'
    }

    second_r = {
        10: 'десять',
        20: 'двадцать',
        30: 'тридцать',
        40: 'сорок',
        50: 'пятьдесят',
        60: 'шестьдесят',
        70: 'семьдесят',
        80: 'восемьдесят',
        90: 'девяносто'
    }

    between10and20 = {
        11: 'одиннадцать', 
        12: 'двенадцать', 
        13: 'тринадцать',              
        14: 'четырнадцать', 
        15: 'пятнадцать', 
        16: 'шестнадцать',           
        17: 'семнадцать', 
        18: 'восемнадцать',
        19: 'девятнадцать'
    }

    third_r = {
        100: 'сто', 
        200: 'двести', 
        300: 'триста', 
        400: 'четыреста',
        500: 'пятьсот', 
        600: 'шестьсот',
        700: 'семьсот',
        800: 'восемьсот', 
        900: 'девятьсот'
    }

    if n == 1000:
        print('тысяча')
        return

    if n > 1000:
        print('Число больше 1000')
        return

    n1 = n % 10
    n2 = n % 100 - n1
    n3 = n - (n1 + n2)

    if n in range(0, 10):
         print(first_r[n])
    elif n in range(11, 20):
        print(between10and20[n])
    elif n in second_r:
        print(second_r[n])
    elif n in range(20, 100):
        print(second_r[n2] + ' ' + first_r[n1])
    elif(n in third_r):
        print(third_r[n3])
    elif n > 100 and n2 == 0:
        print(third_r[n3] + ' ' + first_r[n1])
    elif n >= 100 and n % 100 not in second_r and n not in range (110, 120):
        print(third_r[n3] + ' ' + second_r[n2] + ' ' + first_r[n1])
    elif n in range(111, 120):
        print(third_r[n3] + ' ' + between10and20[n2 + n1])
    else:
        print(third_r[n3] + ' ' + second_r[n2])


if __name__ == '__main__':
    task = input("Enter task number: ")
    if task == '1':
        task_1()
    elif task == '1.1':
        task_1_1()
    elif task == '2':
        task_2()
    elif task == '3':
        task_3()