import re

print('Calc ;)')
print("Type 'quit' to exit\n")

previous = 0
run = True


def preform_math():
    global run
    global previous

    if previous == 0:
        equation = input('Enter Equation')
    else:
        equation = input(str(previous))

    if (equation == 'quit'):
        print('Goodbye')
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    preform_math()
