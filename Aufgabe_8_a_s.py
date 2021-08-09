
#Aufgabe_8_a_s
# def myfunc(x, y):
#     a = x + y
#     return a
#
# print("The result ist " + str(myfunc(5,6)))

#Aufgabe_8_b_s

def myfunc():
    active = True
    myDict = {}
    while active:
        name = input("Please enter your name: name 0 will terminate: ")
        if name == "0":
            active = False
            break
        age = int(input("Please enter you age: "))
        myDict[name] = age

    # print(f"{'Name':<15} {'age':<5}")
    # for item, amount in myDict.items():
    #     print(f"{item:<15} {amount:<5}")

    return myDict

res = myfunc()
print(res)


#Aufgabe_8_c_s

print("Aufgabe c:")
from datetime import date, time, datetime                  # datetime importieren

def conftime():
    my_Confirmed_Dict = {}                                     # leeres Dictionary erzeugen
    for name,age in res.items():                            # myDict aus vorheriger Aufgabe
        print (name,age)                                           # Ausgabe der Eintraege
    #    print(age)                                             # Ausgabe der Eintraege
        ans = input("Confirm User? (y)")                       # Abfrage zur Bestaetigung
        if ans == "y":
    #        my_Confirmed_Dict[name]=age
    # get time entry
            today = date.today()                               # Zeitangabe erzeugen
            now = datetime.now()
            current_time = time(now.hour,now.minute, now.second)
            combined_time = datetime.combine(today, current_time)
    #        print(combined_time,type(combined_time))
    # create new dict for every key (user)
            new_dict = {}                                      # neues Dictionary fuer
            new_dict["age"] = age                              # bestaetigte User anlegen
            new_dict["time"] = combined_time                   # Umwandlung von datetime objekt in string mit str()
            my_Confirmed_Dict[name] = new_dict

    #print(my_Confirmed_Dict)

    msg = f"     {'User':10s}       {'age':3}                                 {'date'}  "
    print(msg)
    for key,item in my_Confirmed_Dict.items():
         var = item["time"].strftime("%A, %B %Y %H-%M-%S")
         print(f"User {key:10s} is    {item['age']:3d}  years old and was confirmed at {var}. ")

conftime()
