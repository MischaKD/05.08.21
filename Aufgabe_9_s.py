# #Aufgabe_9_a_s
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def pri(self):
#         print(f"My name is {self.name}, and I am {self.age} year old:")
#         # print(self.name)
 #   #    return self.name, self.age

# if __name__ == "__main__"
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
# print(res) for task 9c


# # Instantiierung der Klasse
# print(__name__)
# if __name__=="__main__":
#     myDict = {}
#     mySol = Aufg9(myDict)           # Instantiierung der Klasse
#     res = mySol.ask_name()          # Methode aufrufen, Resultat (Rueckgabewert von "return") landet in "res".
# #    print(res)                     # Der Rueckgabewert ist jedoch nicht unbedingt erforderlich, um diesen an die naechste Methode
# #                                   # weiterzureichen, hier wird die alternative Methode der Uebergabe ueber Instanzattribute
#                                     # verwendet.
#     mySol.print_usr()               # Methode verwendet Instanzattribute, um Werte mit der vorherigen Methode auszutauschen.

##########################################
#Aufgabe_9_d_s

print("Aufgabe c:")
from datetime import date, time, datetime                  # datetime importieren

class Aufgabe_9d:
# def conftime(res): # only used for Module
    def __init__(self):
        self.my_Confirmed_Dict = {}
        self.new_dict = {}
    def conftime(self):
        for name,age in res.items():                            # myDict aus vorheriger Aufgabe
           print (name,age)                                           # Ausgabe der Eintraege
           # print(age)                                             # Ausgabe der Eintraege
           ans = input("Confirm User? (y)")                       # Abfrage zur Bestaetigung
           if ans == "y":
                self.my_Confirmed_Dict[name]=age
                print(self.my_Confirmed_Dict)
         # get time entry
                today = date.today()                               # Zeitangabe erzeugen
                now = datetime.now()
                current_time = time(now.hour,now.minute, now.second)
                combined_time = datetime.combine(today, current_time)
                print(combined_time,type(combined_time))
         # create new dict for every key (user)
         #        new_dict = {}                                      # neues Dictionary fuer
                self.new_dict["age"] = age                              # bestaetigte User anlegen
                self.new_dict["time"] = combined_time                   # Umwandlung von datetime objekt in string mit str()
                self.my_Confirmed_Dict[name] = self.new_dict
                print(self.my_Confirmed_Dict)

    #print(my_Confirmed_Dict)

        msg = f"     {'User':10s}       {'age':3}                                 {'date'}  "
        print(self.my_Confirmed_Dict)
        print(msg)
        for key,item in self.my_Confirmed_Dict.items():
             var = item["time"].strftime("%A, %B %Y %H-%M-%S")
             print(f"User {key:10s} is    {item['age']:3d}  years old and was confirmed at {var}. ")

aufgabe9d = Aufgabe_9d()
print(aufgabe9d.conftime())

# # Instantiierung der Klasse
# print(__name__)
# if __name__=="__main__":
#     myDict = {}
#     mySol = Aufg9(myDict)           # Instantiierung der Klasse
#     mySol.ask_name()          # Methode aufrufen, Resultat (Rueckgabewert von "return") landet in "res".
#     mySol.print_usr()               # Methode verwendet Instanzattribute, um Werte mit der vorherigen Methode auszutauschen.



