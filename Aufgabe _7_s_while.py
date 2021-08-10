# Aufgabe 7_c:

# import datetime
#
# active = True
# dt_list = []
# while active:
#     ans = input("Enter druecken um Zeit zu speichern, 'o' zum Beenden: ")
#     if ans == "0":
#         active = False
#     now1 = datetime.datetime.now()
#     dt_list.append(now1)
#     # print(now1, type(now1))
# print("Eingabezeiten")
# for i in dt_list:
#     print(i.strftime("%X"))

# Aufgabe 7_a:

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
    print(f"{item:<15s} {amount:<5}")








