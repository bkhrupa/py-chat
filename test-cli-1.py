

def pr(name='Default', age='Unknown'):
    print('Name', name, 'age:', age)


def pr_people(*people):
    for person in people:
        print(person)


pr(age='23', name='Foo')
pr('AAA', 18)
pr()

pr_people('Odin', 'Thor', 'Loki')
