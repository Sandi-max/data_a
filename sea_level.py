import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


df = pd.read_csv("epa-sea-level.csv")
x = df["Year"]
y = df["CSIRO Adjusted Sea Level"]

fig,ax = plt.subplots()
plt.scatter(x,y)

res= linregress(x,y)
#print(res)
x_p = pd.Series([i for i in range(1880,2050)])
y_p = res.slope*x_p+res.intercept
plt.plot(x_p,y_p,"r")
#af = df[df['Year']>=2000]

new_df = df[df['Year']>=2000]
new_x = new_df["Year"]
new_y = new_df["CSIRO Adjusted Sea Level"]
res_n = linregress(new_x,new_y)

x_pp = pd.Series([i for i in range(2000,2050)])
y_pp = res_n.slope*x_pp+res_n.intercept
plt.plot(x_pp,y_pp,"b")

ax.set_title("rising sea level")

print(new_df.head())
#print("printing af ")
#print(af)
#print(y_p)
#print(x_p)


plt.show()