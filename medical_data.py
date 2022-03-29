import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("medical_examination.csv")
df['overweight']=(df["weight"]/((df["height"]/100)**2)).apply(lambda x : 1 if x >25 else 0)
#### use lambda for larger data rather than for or any loop 
print(df.head(10))

df["cholesterol"] = df["cholesterol"].apply(lambda x: 1 if x>1 else 0)
df["gluc"] = df['gluc'].apply(lambda x: 1 if x>1 else 0)
print(df.head(10))
df_cat = pd.melt(df,id_vars=["cardio"], value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])
print("\n")
print(df_cat)

df_cat['total']=0
df_cat = df_cat.groupby(["cardio","variable","value"], as_index = False).count()
print(df_cat)

fig = sns.catplot(x="variable", y="total", hue="value", kind="bar", col ="cardio",data=df_cat)
#fig = sns.catplot(x="variable", y="count", hue="value", kind="bar", col ="cardio",data=df_cat).fig
fig.savefig('catlop.png')
plt.show()
print("showing \n")
print(df[df['height'] >= df['height'].quantile(0.025)])
df_heat = df[
	(df['ap_lo']<=df['ap_hi'])&
	(df['height'] >= df['height'].quantile(0.025))&
	(df['height'] <= df['height'].quantile(0.975))&
	(df['weight'] >= df['weight'].quantile(0.025))&
	(df['weight'] <= df['weight'].quantile(0.975))
	]

corr =  df_heat.corr(method="pearson")
print(corr)

mask = np.triu(corr)
print(mask)
fig, axes =plt.subplots(figsize=(12,12))
axes = sns.heatmap(corr, mask=mask, square=True, annot=True,  vmax=.3,fmt=".1f",linewidth=.5,cbar_kws = {'shrink':0.5})
plt.show()
#ax = sns.heatmap(flights, annot=True, fmt="d")