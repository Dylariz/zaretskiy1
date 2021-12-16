ex = [1, 2, 3, 4, 5, 6, 7]
arr = [[i]*i for i in ex if i % 2 == 0]
print(arr)

x = int(input())
y = int(input())
if -1 <= x <= 1 and -1 <= y <= 1:
    print('Принадлежит')
else:
    print('Не принадлежит')
