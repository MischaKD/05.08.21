# required bib
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rcParams



# read data from csv
df = pd.read_csv("crowdfunding.csv")
print(df)
#
print(df.columns)

# drop column "Unnamed: 0"
df.drop(columns=['Unnamed: 0'], inplace=True)
print(df)

print(df.columns)


# Let's have a look how much money was collected by each sector.

df_sector = df.groupby(['sector']).agg({'funded_amount': 'size'})
df_sector.reset_index(inplace=True) # reset index
print(df_sector)
print(df_sector.columns)


#Matplotlib Pie chart
label = df_sector['sector']
sizes = df_sector['funded_amount']
explode = (0, 0, 0, 0, 0, 0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0)  # exploding  wedges  in a pie chart
# colors - # to change a color of wedges


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

ax.legend(label, bbox_to_anchor=[0.92, 0.7])

plt.show()  # to see only the graphics and not the coordinates