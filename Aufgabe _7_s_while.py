import datetime

active = True
dt_list = []
while active:
    ans = input("Enter druecken um Zeit zu speichern, 'o' zum Beenden: ")
    if ans == "0":
        active = False
    now1 = datetime.datetime.now()
    dt_list.append(now1)
    # print(now1, type(now1))
print("Eingabezeiten")
for i in dt_list:
    print(i.strftime("%X"))



