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


# #Aufgabe_9_b_s
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def pri(self):
#         print(f"My name is {self.name}, and I am {self.age} year old!")
#         # print(self.name)
#
#     def new_data(self, new_name, new_age):
#         self.name = new_name
#         self.age = new_age
#         print(f"Another is {self.name}, and the new age is {self.age}!")
#
#
# new_person = Person("Ivan", 19)
# new_person.pri()
#
# new_person.new_data("Roma", 20)
# # print(new_person.name)
# # print(new_person.age)

#Aufgabe_9_c_s

class Aufgabe_8():
    def __init__(self):
        self.active = True
        self.myDict = {}
    def myfunc(self):
        while self.active:
            name = input("Please enter your name: name 0 will terminate: ")
            if name == "0":
                active = False
                break
            age = int(input("Please enter you age: "))
            self.myDict[name] = age

        # print(f"{'Name':<15} {'age':<5}")
        # for item, amount in myDict.items():
        #     print(f"{item:<15} {amount:<5}")

        return self.myDict

aufgabe9c = Aufgabe_8()
# print(aufgabe9c.myfunc())
res = aufgabe9c.myfunc()
print(res)

