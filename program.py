
for x in [1,4,76,10]:
    print(x, end=' ')

print()
for x in (1,4,76,10):
    print(x, end=' ')

print()
#            key:  value  , key: value,  key: value
for key in { 404: 'python', 405: 'java', 408:'.NET'}:
    print(key, end=' ')

y = 5
is_even = y % 2 == 0

# _is_y_2 = y == 2
if y == 2:
    is_y_2 = True
else:
    is_y_2 = False

print()
def func1():
    return None

print(func1())