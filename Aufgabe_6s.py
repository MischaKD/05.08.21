# Aufagabe_6_a

# from random import randint as rt
#
# farbe = ['green', 'red', 'yellow', 'blue']
# tag = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
#
# for i in tag:
#     farbe1 = rt(0, len(farbe)-1)
#     print(i + " " + farbe[farbe1])
#########################################################################

# Aufagabe_6_b
# Variant_1

# WTs = ["Mo","Di", "Mi", "Do","Fr"]
# for i in WTs:
#     a = int(input(f"Please type the time of you first Cafe on {i} "))
#     print(f'First Cafe on {i} at {a}')

# # Variant_2  und Aufagabe_6_c
# mylist = []
# WTs = ["Mo","Di", "Mi", "Do","Fr"]
# for i in WTs:
#     a = int(input(f"Please type the time of you first Cafe on {i} "))
#     mylist.append(a)
#
# for index, item in enumerate(WTs):
#     for index1, item1 in enumerate(mylist):
#         if index == index1:
#             print(f'First Cafe on {item} at {item1}')
# #########################################################################
# # Aufagabe_6_b_2
# for i, j in enumerate(WTs):
#     if mylist[i] == max(mylist):
#         print(f"The latest first Cafe was at {max(mylist)} and it was on {WTs[i]}")

# mylist.sort(reverse=True)


## Alternative
# mylist.sort()
# print(f"The latest firt Cafe at {mylist[-1]}")

#########################################################################

# Aufagabe_6_c
# WTs = ["Mo","Di", "Mi", "Do","Fr", "Sa", "So"]
# WT5s = WTs*5
# # print(WT5s)
# for i, y in enumerate(WT5s):
#     print(i, y)
#     # print(f'Heute ist {y}. Diese Woche ist Ihr Termin am {WTs[2]}, also in x Tagen')

WTs = ["Mo","Di", "Mi", "Do","Fr", "Sa", "So"]
W = range(1,6)
for a in W:
    if a % 2 !=0:
        for i, y in enumerate(WTs):
            if i <=2:
                print(f'Heute ist {y}. Woche {a}. Ihr Termin ist am {WTs[2]}, also in {2-i} Tagen')
    else:
        for i, y in enumerate(WTs):
            if i<=5:
                print(f'Heute ist {y}. Woche {a}. Ihr Termin ist am {WTs[4]}, also in {5-i} Tagen')



# WTs = ["Mo","Di", "Mi", "Do","Fr", "Sa", "So"]
# W = range(1,6)
# for i in W:
#     if i % 2 ==0:
#         for tag in WTs:
#             print("Ihr Friseurtermin liegt diese Woche am Mi, also in ")

