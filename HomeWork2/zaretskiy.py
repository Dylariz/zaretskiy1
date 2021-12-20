import math


# 1
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# 2
s = 0


def season(month):
    global s
    if 1 <= month <= 2 or month == 12:
        s = "Зима"
    elif 3 <= month <= 5:
        s = "Весна"
    elif 6 <= month <= 8:
        s = "Лето"
    else:
        s = "Осень"


season(5)
print(s)


# 3
def is_prime(num):
    if num > 2:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False


print(is_prime(4))


# 4
def reverse_list(lst):
    n_lst = []
    for i in range(0, len(lst), 1):
        n_lst.append(lst[len(lst) - i - 1])
    return n_lst


lst = [1, 2, 3, 4, 6, 7]
print(reverse_list(lst))

# 5
str = "Привет мир!"
str = str.upper()
print(str[4: 9])


# 6

