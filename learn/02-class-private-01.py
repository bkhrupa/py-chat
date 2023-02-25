
class Account:

    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def print_data(self):
        print(self.__name, self.__balance)


ac1 = Account('Odin', 1000)
ac1.print_data()
print(ac1.__dict__)
print(ac1._Account__name)

