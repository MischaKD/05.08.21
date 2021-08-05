# Aufgabe 6 b
# wds = ["Mo","Di","Mi","Do","Fr"] # Liste Mo-Fr
# coffee_dict = {}
# for i in wds:
#     coffee_dict[i] = int(input(f"Um wieviel Uhr war der erste Kaffee am {i}? "))
# #print(coffee_dict)
# val_list = list(coffee_dict.values())
# #print(val_list)
# max_val = max(val_list)# auch key Argument verwendbar
# #print(max_val)
#
# for i,j in enumerate(val_list):
#     if j == max_val:
#         print(f"Der späteste Kaffee war am {wds[i]}.")
# Aufgabe 6c
wds =["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
for i in range(5):
    for wdi,j in enumerate(wds):
        #print(wdi)    # Wochentag-index
        #print(i%2)
        k = 2+2*(i%2) # Friseurtermin-index
        #print(k)
        print(f"Woche {i}: heute ist {j}. F-Termin diese Woche ist {wds[k]}. ", end = "")
        f_index = k - wdi # Tage bis zum Friseur (pro Woche)
        if f_index > 0:
            print(f"Noch {f_index} Tage bis zum Friseurtermin.")
        elif f_index == 0:
            print(f"Heute ist der Friseurtermin.")
        elif f_index < 0:
            print(f"Der Friseurtermin war diese Woche vor {-f_index} Tagen.")
        else:
            print("Some Error ocurred.")
