class Person:
    def __init__(self, name="Bill", age=30):
        # print("Constructor...")
        self.__name = name
        self.__age = age

    def person_info(self):
        print(self.__name, ", ", self.__age, " years old", sep="")

    def __del__(self):
        pass
        # print("Destructor...")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return "Name: " + self.__name + ", age: " + str(self.__age)


bill = Person()
bill.age = 12
print(bill)

adam = Person("Adam", 34)
eva = Person("Eva", 27)
tina = Person("Tina", 29)
sara = Person("Sara", 39)

person_list = []
person_list.append(bill)
person_list.append(adam)
person_list.append(tina)
person_list.append(sara)
for item in person_list:
    item.age += 1
    item.person_info()
