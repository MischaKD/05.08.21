#Aufgabe_9_a_s
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def pri(self):
        print(f"My name is {self.name}, and I am {self.age} year old:")
        # print(self.name)

new_person = Person("Ivan", "19")
new_person.pri()