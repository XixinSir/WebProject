class Person():
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        """
        这里要写成return的格式
        :return:
        """
        return self.name

    def fun1(self):
        print("my name {name}, my age is {age}".format(name=self.name, age=self.age))

info = {
    "name": "Michael",
    "age": 43,
    "height": 180,
    "weight": 150
}
print(info)
person1 = Person(**info)
person1.fun1()
print(person1)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=")
class ChinaPerson(Person):
    def __init__(self, name, age, height, weight):
        super().__init__(name, age, height, weight)

person2 = ChinaPerson(**info)
person2.fun1()
print(person2)
