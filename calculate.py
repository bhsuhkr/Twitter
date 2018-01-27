import csv
import pandas as pd

g=open('sum.csv', 'wt')

df1 = pd.read_csv('08_17_output.csv')
df2 = pd.read_csv('08_18_output.csv')
df3 = pd.read_csv('08_19_output.csv')
df4 = pd.read_csv('08_20_output.csv')
df5 = pd.read_csv('08_21_output.csv')
df6 = pd.read_csv('08_22_output.csv')
df7 = pd.read_csv('08_23_output.csv')
df8 = pd.read_csv('08_24_output.csv')
df9 = pd.read_csv('08_25_output.csv')
df10 = pd.read_csv('08_26_output.csv')
df11 = pd.read_csv('08_27_output.csv')
df12 = pd.read_csv('08_28_output.csv')
df13 = pd.read_csv('08_29_output.csv')
df14 = pd.read_csv('08_30_output.csv')
df15 = pd.read_csv('08_31_output.csv')
df16 = pd.read_csv('09_01_output.csv')
df17 = pd.read_csv('09_02_output.csv')
df18 = pd.read_csv('09_03_output.csv')
df19 = pd.read_csv('09_04_output.csv')
df20 = pd.read_csv('09_05_output.csv')
df21 = pd.read_csv('09_06_output.csv')
df22 = pd.read_csv('09_07_output.csv')
df23 = pd.read_csv('09_08_output.csv')
df24 = pd.read_csv('09_09_output.csv')
df25 = pd.read_csv('09_10_output.csv')
df26 = pd.read_csv('09_11_output.csv')
df27 = pd.read_csv('09_12_output.csv')
df28 = pd.read_csv('09_13_output.csv')
df29 = pd.read_csv('09_14_output.csv')
df30 = pd.read_csv('09_15_output.csv')
df31 = pd.read_csv('09_16_output.csv')
df32 = pd.read_csv('09_17_output.csv')
df33 = pd.read_csv('09_18_output.csv')
df34 = pd.read_csv('09_19_output.csv')
df35 = pd.read_csv('09_20_output.csv')
df36 = pd.read_csv('09_21_output.csv')
df37 = pd.read_csv('09_22_output.csv')
df38 = pd.read_csv('09_23_output.csv')
df39 = pd.read_csv('09_24_output.csv')
df40 = pd.read_csv('09_25_output.csv')
df41 = pd.read_csv('09_26_output.csv')
df42 = pd.read_csv('09_27_output.csv')
df43 = pd.read_csv('09_28_output.csv')
df44 = pd.read_csv('09_29_output.csv')
df45 = pd.read_csv('09_30_output.csv')







abbr=['AK','AL','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN', 'IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY', 'NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']






writer = csv.writer(g)
writer.writerow(['State','Total Value'])
for x in range(len(abbr)):	
	#writer.writerow((df1[x,1]+df2[x,1])	
	writer.writerow((abbr[x],df1.iloc[x,1]+df2.iloc[x,1]+df3.iloc[x,1]+df4.iloc[x,1]+df5.iloc[x,1]+df6.iloc[x,1]+df7.iloc[x,1]+df8.iloc[x,1]+df9.iloc[x,1]+df10.iloc[x,1]+df11.iloc[x,1]+df12.iloc[x,1]+df13.iloc[x,1]+df14.iloc[x,1]+df15.iloc[x,1]+df16.iloc[x,1]+df17.iloc[x,1]+df18.iloc[x,1]+df19.iloc[x,1]+df20.iloc[x,1]+df21.iloc[x,1]+df22.iloc[x,1]+df23.iloc[x,1]+df24.iloc[x,1]+df25.iloc[x,1]+df26.iloc[x,1]+df27.iloc[x,1]+df28.iloc[x,1]+df29.iloc[x,1]+df30.iloc[x,1]+df31.iloc[x,1]+df32.iloc[x,1]+df33.iloc[x,1]+df34.iloc[x,1]+df35.iloc[x,1]+df36.iloc[x,1]+df37.iloc[x,1]+df38.iloc[x,1]+df39.iloc[x,1]+df40.iloc[x,1]+df41.iloc[x,1]+df42.iloc[x,1]+df43.iloc[x,1]+df44.iloc[x,1]+df45.iloc[x,1]))
	


#print(df2.iloc[0:50,1])

g.close()
