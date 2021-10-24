# https://docs.python.org/3/library/stdtypes.html#string-methods
################################### 1
# input user first and last name
# i.e. moshe cohen
# if the user ented more then 2 words
# i.e. cohen levi david , then input again
# until 2 words were given
# then print first name and last name in seperated lines
'''
while True:
    fullname = input('please enter your full name [2 words]: ')
    # 'avi cohen levi' ==> ['avi', 'cohen', 'levi']
    #                         0       1        2
    # list_names[0] = 'avi'
    # list_names[1] = 'cohen'
    # list_names[2] = 'levi'
    list_names = fullname.split()
    if len(list_names) == 2:
        print(f'first name: {list_names[0]}')
        print(f'last name:  {list_names[1]}')
        break
'''


################################### 2
# input a string from the user (hint: use replace and find...)
# print:
# i.e. '123' -- int
# i.e. '5.7' -- float
# i.e. '5.7.1' -- illegal
# i.e. ' 123' -- int hint: leftstrip
# i.e. ' 12 3' -- illegal hint: leftstrip
# i.e. ' 1.23' -- float
# i.e. 'a' -- alpha (isaplha)
# i.e. 'a1' -- mix
def print_number_type(number):
    number = number.lstrip()  # '  12'
    number = number.rstrip() # '12  '
    if number.count(' ') == 0:
        number_of_dots = number.count('.')
        if number_of_dots <= 1:
            if number.isdigit():
                print('int')
                return
            if number.replace(".", "").isdigit():
                print('float')
                return
            if number.isalnum():
                print('mix or alpha')
                return
    print('illegal')
    return

number = input('please enter int or float: ')
print_number_type(number)

