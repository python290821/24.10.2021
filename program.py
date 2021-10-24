import statistics

_lst = [2,1,3,5, -100, 200]
print(_lst[0:4])
print(_lst[:4])
print(_lst[0:4:2])
print(_lst[-1:0:-1]) # backwards

for i in sorted(_lst, reverse=True):
    print(i)
print('------------------')
for x in reversed(_lst):
    print(x)
print('------------------')
print(_lst)
for x in range(len(_lst)):
    print(f'#{x}: {_lst[x]}')
print('------------------')
_grades = []
x = int(input('Enter grade (-1 to exit): ' ))
while x != -1:
    _grades.append(x)
    x = int(input('Enter grade (-1 to exit): '))
_max = max(_grades)
_min = min(_grades)
_avg = sum(_grades) / len(_grades)
_mean = statistics.mean(_grades)
print(f'max : {_max}, min: {_min}, avg: {_avg} {_mean}')

