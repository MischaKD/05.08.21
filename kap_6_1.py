# Kapitel 6
# colours = ["green","Red","yellow","blue"]
# for x in colours:
#    # print(x)
#    # if x.lower() == "red":  # if-Bedingung, Prüfung auf Gleichheit
#    #     print(x,"found!")
#
#    if x.lower() != "red":  # if-Bedingung, Prüfung auf Ungleichheit
#        print(x," is not red!", sep = "")

# x = "red"
# print(x,x == "red", type(x == "red"))

# colour = "red"
# # if colour == "red":                                   # if-Bedingung, Prüfung auf Gleichheit
# if True:
#    print(colour)

# if isinstance(colour,str):
#    print(str(colour)+ " is a member of the str class")
#         print("gesuchte Farbe red nicht gefunden ! ")      # Ausführen, wenn if-Bedingung zutrifft.
#         print("if-Bedingung beendet")
#     if colour != "red":                            # if-Bedingung, Prüfung auf Ungleichheit
#         print(colour)


# print("for-Schleife beendet")

# Prüfung auf Gleichheit mit   "=="
# Prüfung auf Ungleichheit mit "!="

# size = 20
# minsize = 12
# maxsize = 21

# #
# if size >= minsize:
#    print("size is larger than minsize.")
#
# print(size <= maxsize,type(size <= maxsize))
#
# if size <= maxsize:
#    print("size is smaller than maxsize.")
#
# print(size >= minsize,type(size >= minsize)) # Bedingungspruefung OHNE if-Anweisung ergibt eine Bool'sche Variable

# print(size <= maxsize,type(size >= minsize))

# var = size <= maxsize # ergibt bool, Zuweisung auf "var"
# print(var,type(var))
#
# if var:
#    print("condition is True.")

# small_fee = "yes"
# size = "huge"
# age = 17

# if age >= 18:
# if age >= 18 and size== "huge": # True and True = True
# if age >= 18 or size == "huge": # True or False = True
#
#    small_fee = "no"
#
# print("Reduzierter Eintrittspreis "+ small_fee)
#
# print(age >= 18 and size == "huge")
# print(age >= 18 or size == "huge")

# #
# colours = ["green","red","yellow","blue"]
# print("red" in colours)                     # Abfragebedingung "in" Liste
#
# if "red" in colours:
#    print("yes, red ist enthalten")
#
# if "purple" not in colours:                 # Abfragebedingung "nicht in" Liste
#    print("yes, purple ist nicht enthalten")
#
# open_door = 0
# enable_access = True  # Boolsche Variablen
# enable_access = False

# print(type(enable_access))

# deny_write = False
#
# if enable_access: #   # boolsche Variable direkt in Bedingungsprüfung schreiben
#    open_door = 1

# print(f"open door: {open_door}")

# shoe_size = 43
# if shoe_size > 43:                   # Bedingungsprüfung wird ausgefuehrt
#     print("This shoe will fit!")     # Bei True wird der eingerückte block ausgeführt
# else:
#     print("This shoe will not fit.")  # Bei False - Bedingung wird der else-Block
#                                     ## ausgeführt
#
#
# group_size = 42
# #
# if group_size < 5:
#     print("This group is too small")
# #
# elif 5 <= group_size < 10:
#     print("Hello, small group!")
#
# #elif group_size > 20:                    # bei dem ersten Auftreten der True-Bedingung wird nicht weiter geprüft!
# #    print("Hallo, group of 20")
# #
# elif 10 <= group_size < 35:
#     print("Hello, group!")
# #
# else:
#     print("This Group is too big!")
#
#
# Write_permission_granted = False # Anfangswerte der Variablen
# open_door = 0                    # Anfangswerte der Variablen
# #
# group_size = 28                   # Variablen fuer Bedingungspruefung
# Room_access = True              # Variablen fuer Bedingungspruefung
# #
# if group_size > 20:
#    Write_permission_granted = True
# ##
# if Room_access:
#    open_door = 1
# #
# print(Write_permission_granted, open_door)


# colours = ["green","red","yellow","blue"]
#
# for colour in colours:
#    if colour =="red":
#        print("found " + colour)
#    else:
#        print("None found")
#
# if not False:
#    print("Hi")

# True entspricht manchmal 1 oder einen anderen Zahl ausser Zahl
# False entspricht manchmal 0

# colours = [1,2,3]
#
# print("len:",len(colours))
# if colours: # Mindestanforderung für "if colours:" Liste, aber Sie darf leer sein. Dann ergibt die Pruefung "False"
#    print("OK")
#    print("len:",len(colours))
#    print("Non-empty list found")
# else: # bei leerer Liste
#    print("Leere Liste")
#    print("len(else):",len(colours))
#    print("Empty list found!")
#
# found = False

# names = {}
# #
# if names:
#    print("Non-empty Dictionary found")
# else:
#    print("Empty Dictionary found")
# # #
# print(bool(names))
# Empty Dictionary found


colours = ["green", "red", "yellow", "blue", "violett", "brown"]  # laufen durch 2 Listen
mycolours = ["green", "orange", "red", "magenta"]
# #
# found = False  # Startwert fuer Hilfsvariable "found"
#
for colour in colours:
#     #    print(colour, end = " ")
    var = colour in mycolours  # mit "in" wird geprueft, ob die aktuelle Farbe in der 2. Liste existiert, BOOL
    print(var)
#     if var:
#         print("Colour " + colour + "  is in both lists")
#         found = True
# #
# # if found == True:
# if found:
#     print("Found at least one match.")
# else:
#     print("Sorry, no matches found")
#
