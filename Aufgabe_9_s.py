# #Aufgabe_9_a_s
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def pri(self):
#         print(f"My name is {self.name}, and I am {self.age} year old:")
#         # print(self.name)
#
# new_person = Person("Ivan", "19")
# new_person.pri()


#Aufgabe_9_b_s
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def pri(self):
        print(f"My name is {self.name}, and I am {self.age} year old!")
        # print(self.name)

    def new_data(self, new_name, new_age):
        self.name = new_name
        self.age = new_age
        print(f"Another is {self.name}, and the new age is {self.age}!")


new_person = Person("Ivan", 19)
new_person.pri()

new_person.new_data("Roma", 20)
# print(new_person.name)
# print(new_person.age)
