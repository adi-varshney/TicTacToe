class Dog:
    species = 'mammal'

    def bark(self, age):
        return "WOOFs! My name is {}. I am {} years old".format(self.name, age)

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius**2*Circle.pi

    def get_circumference(self):
        circumference = self.radius * Circle.pi * 2
        circumference = round(circumference, 2)
        return circumference


my_circle = Circle(21)
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumference())
print(my_circle.area)
# my_dog = Dog('Golden Retriever', 'Tony')
# my_dog1 = Dog('Huskey', 'Jack')
#
# print(my_dog.breed)
# print(my_dog.bark(4))
# print(my_dog1.bark(6))

# my_sample = Dog()
# print(type(my_sample))
