# required bib
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rcParams

# read data from csv
df = pd.read_csv("crowdfunding.csv")
# print(df.columns) # check the name of the columns
# print(df)

# drop column "Unnamed: 0"
df.drop(columns=['Unnamed: 0'], inplace=True)
# print(df)
# print(df.columns) # check the name of the columns

# Let's have a look how much money was collected by each sector.
df_sector = df.groupby(['sector']).agg({'funded_amount': 'size'})
print(df_sector)
# print(df_sector.columns) # checking columns

df_sector.reset_index(inplace=True)  # reset index to get all columns
print(df_sector)
# print(df_sector.columns)

label = df_sector['sector']
sizes = df_sector['funded_amount']
explode = (0, 0, 0, 0, 0, 0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0)  # exploding  wedges  in a pie chart
# colors - # to change a color of wedges

# Matplotlib Pie chart
fig, ax = plt.subplots(figsize=[10, 10])  # fix the size of plot

ax.pie(x=sizes,
       labels=label,
       autopct='%1.1f%%'  # shows us the percentage distribution

       , labeldistance=1.07
       # ,rotatelabels=True
       , explode=explode
       , textprops={'fontsize': 12}
       , shadow=True
       , startangle=15

       )

ax.set_title("Money collected by sectors", fontsize=25, weight="bold", color='blue')

ax.axis('equal')  # the chart is displayed as a circle

# Problem
ax.legend(title="Sectors", loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=15, title_fontsize=20) #


# plt.show()  # to see only the graphics and not the coordinates


#Seaborn.barplot
# why some sectors collected a lot of money, was it a big investment or a lot of people had interest in this sector

df_ppl = df.groupby(['sector']).agg({'lender_count': 'size'})
# print(df_ppl)

df_ppl.reset_index(inplace=True)  # reset index to get all columns
print(df_ppl)

sns.set_theme(style="whitegrid")
plt.figure(figsize=(7,7))



ax = sns.barplot(x="lender_count"
                 ,y="sector"
                 ,data=df_ppl
                 ,palette="nipy_spectral"
                 ,saturation=.7
                 ,order=df_ppl.sort_values('lender_count', ascending = False).sector)



# set labels
plt.xlabel("Lenders", size=16, weight="bold", color = 'blue')
plt.ylabel("Sector", size=17, weight="bold", color = 'blue')
plt.title("Lender pro Sector", size=20, weight="bold")
plt.tick_params(labelsize=13)


plt.show()