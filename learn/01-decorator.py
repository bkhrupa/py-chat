
def deco(calback):
    def inner(*args, **kwargs):
        print('start inner')
        result = calback(*args, **kwargs)
        print('end inner')

        return result

    return inner


def say(name):
    print('say hello', name)


print("deco(say)('Odin')")
deco(say)('Odin')


def sum(a, b):
    return a + b


print("sum(1, 2)")
print(sum(1, 2))

s = deco(sum)
print("s = deco(sum)")
print(s(1, 2))

@deco
def multiply(a, b):
    return a * b


print('multiply(2, 2)')
print(multiply(2, 2))
