# 1
ex = [1, 2, 3, 4, 5, 6, 7]
arr = [[i] * i for i in ex if i % 2 == 0]
print(arr)

# 2
x = int(input())
y = int(input())
if -1 <= x <= 1 and -1 <= y <= 1:
    print('Принадлежит')
else:
    print('Не принадлежит')

# 3
arr = [1, 2, 4, 5, 6, 7, 7]
newArr = []
for t in arr:
    if t % 2 == 0:
        newArr.append(t)
print(newArr)

# 4
print('Введите имя:')
name = input()
print(f'Привет, {name}!')

# 5
a = input()
print(f'The next number for the number {a} is {int(a) + 1}. The previous number for the number {a} is {int(a) - 1}.')
