import json
import matplotlib.pyplot as plt

# import matplotlib.cm as cm

# Explore the structure of the data.
filename = 'eq_data_1_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)

# print(type(all_eq_data))                                  # detect type of data from json file
# it is a dictionary.
# print(all_eq_data.keys())                                 # let's look at it's "key" entries.
# print(json.dumps(all_eq_data, indent=4, sort_keys=True))  # pretty print json data
# print(json.dumps(all_eq_data, indent=4))                  # pretty print json data

all_eq_dicts = all_eq_data['features']  # key "Features" enthält die interesssanten Daten
# print(all_eq_dicts, type(all_eq_dicts))                   # enthält Liste
# print(all_eq_dicts[0],type(all_eq_dicts[0]))              # Alle Daten aus "Features" sind jetzt in all_eq_dicts.
# print(all_eq_dicts[0].keys())
# print(all_eq_dicts[0]["properties"].keys())#
# print(all_eq_dicts[0]["properties"]["mag"])
# print(all_eq_dicts[0]["properties"]["place"])
# print(all_eq_dicts[0]["geometry"].keys())

# print(all_eq_dicts[0]['geometry']["coordinates"])
# print(all_eq_dicts[0]['geometry']["coordinates"][0])
# #
mags, plas, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:  # all_eq_dicts enthält Liste. Diese kann durchlaufen werden.
    #    print(eq_dict)
    mag = eq_dict['properties']['mag']  #
    #     print(mag)
    pla = eq_dict['properties']['place']  #
    #     print(pla)
    lon = eq_dict['geometry']['coordinates'][0]  # Ausgabe durch Angabe der passenden Keys und "subkeys".
    #     print(lon)
    lat = eq_dict['geometry']['coordinates'][1]
    #     print(lat)
    #
    mags.append(mag)
    plas.append(pla)
    lons.append(lon)
    lats.append(lat)
#
# print(mags[0:5])
# print(plas[0:5])
# print(lons[0:5])
# print(lats[0:5])
#
smags = mags[:]  # echte Kopie einer Liste erzeugen
# smags2 = []
#
# for entry in smags:  # herkoemmliche for-Schleife
#    entry = entry * 5
#    smags2.append(entry)
#
# smags2 = [entry*10 for entry in mags[:]]  # List comprehension
smags2 = list(map(lambda i: i * 10, mags[:]))
#
# print(plt.style.available) # List all available matplotlib styles
# plt.style.use("ggplot") # "ggplot" style
# plt.style.use("fivethirtyeight") # "fivethirtyeight" style
# plt.style.use("bmh") # "bmh" style
# plt.style.use("classic") # "classic" style
# plt.style.use("Solarize_Light2") # "Solarize_Light2" style
# plt.style.use("seaborn-poster") # "Solarize_Light2" style
#
# plt.scatter(lons, lats, s = smags2, label="eq magnitudes", c="red")
plt.scatter(lons, lats, marker="o", c=mags, s=mags, label="eq magnitudes")  # c = Graustufenwert
# plt.scatter(lons,lats,marker = "o",c = (0.4,0.7,0.9,1.0), s = 40)                  # c = RGBA-Wert
# plt.scatter(lons,lats,marker = "^",c='b', s = 40, alpha = 0.5)                     # c = single letter
# plt.scatter(lons,lats,marker = "^",c = 'teal', s = 40, alpha = 1.0)                # c = CSS Name
# plt.scatter(lons,lats,marker = "^", c ='tab:blue', s = 40, alpha = 0.5)            # c = Tableau palette
#                                                                                    # c = liste(len(Anzahl Scatter-Punkte))
# plt.scatter(lons, lats, marker = "o", c = 'C3', s = 10, label = "eqs magnitude")   # c = CN Farbzyklus ('C0-C9')
#
plt.colorbar()  # default colorbar: "viridis"
plt.grid()
# plt.legend()
plt.xlabel("longitude")
plt.ylabel("latitude")
#
# mng = plt.get_current_fig_manager()   # all OS
# mng.frame.Maximize(True)              # other OS
# mng.window.showMaximized()            # windows
plt.show()
