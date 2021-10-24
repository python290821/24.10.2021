
def get_in_range(_min = 1, _max = 100):
    while True:
        number = int(input(f'please enter number in range({_min}-{_max}'))
        if number >= _min and number <= _max:
            return number

x = get_in_range(10)
x = get_in_range(1, 10)