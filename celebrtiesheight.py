import pandas
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv

df = pandas.read_csv(r"C:\Users\zyaus\udemyProjects\self\celebeheights\celeb_data.csv")
df2 = df.dropna(subset = ["height"])
#print(df)

#Female heights:
females= []
female_heights = []

for i, row in df2.iterrows():
    
    if "Actress" in (df2.loc[i, "Role"]):
        
        females.append(df2.loc[i])
        #df[i][3].replace('(', "")


for i in range(len(females)):
    try:
        female_heights.append(float((females[i][3]).replace('(', "").split()[2]))
    except ValueError:
        female_heights.append(float((females[i][3]).replace('(', "").split()[1]))


males= []
male_heights = []

for i, row in df2.iterrows():
    
    if "Actor" in (df2.loc[i, "Role"]):
        
        males.append(df2.loc[i])
        #df[i][3].replace('(', "")


for i in range(len(males)):
    try:
        male_heights.append(float((females[i][3]).replace('(', "").split()[2]))
    except ValueError:
        male_heights.append(float((females[i][3]).replace('(', "").split()[1]))
      
      

plt.subplot(1,2,1)
plt.hist(female_heights, edgecolor = "black", linewidth=1.2)
plt.xlabel("Height in Meters")
plt.ylabel("Count")
plt.title("Height distribution among female celebrities", fontsize = 6)
plt.yticks(np.arange(0,21, step = 2))

plt.subplot(1,2,2)
plt.hist(male_heights,edgecolor = "black", linewidth=1.2)
plt.xlabel("Height in Meters")
plt.ylabel("Count")
plt.title("Height distribution among male celebrities", fontsize = 6)
plt.yticks(np.arange(0,21, step = 2))


plt.show()