# # a = 'ala ma kota.'
# # a = a.replace('ala', 'jan')
# # print(a)
#
# tab = [1, 2, 3, 4, 18, 1, 43]
# print(tab)
# print(tab.sort())
# print(tab)
# tab = [4, 4, 25, 2]
# print(tab)
# print(sorted(tab))
# print(tab)
# dic = {10: 5, 'abc': [1, 2, 3, 4]}
# print(dic['abc'][-1])

class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} - {self.age}'
        # return self.name + ' - ' + str(self.age)


animal = Animal('Lion', 35)
print(animal)


class Human(Animal):
    _age_out = 0

    def __init__(self, last_name, first_name, age, name):
        super().__init__(f'{name}, {age}', age)
        self.first_name = first_name
        self.last_name = last_name
        # self.name = f'{first_name} {last_name}'
        self.age = age

    def name(self):
        return f'{self.first_name} {self.last_name}'

    # def __str__(self):
    #     return f'{self.name}, {self.age}'


    def add(self):
        self.age += 1

    @staticmethod
    def static():
        """
        This method does not use attributes
        :return:
        """
    @classmethod
    def incremented_out_age(cls):
        return cls._age_out + 1

def main():
    human = Human('Walezy', 'Henryk', 15, 'Homo Sapiens')
    print(human)
    print(human.incremented_out_age())


main()
