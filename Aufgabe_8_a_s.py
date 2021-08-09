
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

    print(f"{'Name':<15} {'age':<5}")
    for item, amount in myDict.items():
        print(f"{item:<15} {amount:<5}")

    return myDict

res = myfunc()
print(res)

