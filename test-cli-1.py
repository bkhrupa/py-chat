

def pr(name='Default', age='Unknown'):
    print('Name', name, 'age:', age)


def pr_people(*people):
    for person in people:
        print(person)


pr(age='23', name='Foo')
pr('AAA', 18)
pr()
pr_people('Odin', 'Thor', 'Loki')

# ---
print('- - - - -')


def math_sum(num1, num2):
    return num1 + num2


print(math_sum(1, 2))
sum1 = math_sum(3, 5);
print(sum1)
print(math_sum(sum1, 2))

