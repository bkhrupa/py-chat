

def pr_name_and_age(name='Default', age='Unknown'):
    print('Name', name, 'age:', age)


def pr_people(*people):
    for person in people:
        print(person)


pr_name_and_age(age='23', name='Foo')
pr_name_and_age('AAA', 18)
pr_name_and_age()
pr_people('Odin', 'Thor', 'Loki')

# ---
print('- - - - -')


def math_sum(num1, num2):
    return num1 + num2


print(math_sum(1, 2))
sum1 = math_sum(3, 5);
print(sum1)
print(math_sum(sum1, 2))


# ---
print('- - - - -')

check = 'thor'

if check == 'odin':
    print('is Odin')
elif check == 'thor':
    print('is Thor')
else:
    print('unknown')