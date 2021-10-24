
def get_in_range(_min, _max):
    while True:
        number = int(input(f'please enter number in range({_min}-{_max}'))
        if number >= _min and number <= _max:
            return number