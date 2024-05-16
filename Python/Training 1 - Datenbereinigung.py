import pandas as pd

#CSV-Datei einlesen
df = pd.read_csv('dirtydata.csv')

#Reinigung 1 - NA Wert to Mean
x = df ["Dauer"].mean()
df["Dauer"].fillna(x, inplace= True)

y = df ["Kunden"].mean()
df["Kunden"].fillna(y, inplace= True)

z = df ["MinKauf"].mean()
df["MinKauf"].fillna(z, inplace= True)

w = df ["MaxKauf"].mean()
df["MaxKauf"].fillna(w, inplace= True)

#Reinigung 2 - Datumsangaben
df['Datum']= pd.to_datetime(df['Datum'])

new_df = df.dropna()

#Reinigung 3 - Ausreißer bearbeitet
new_df.loc[7,'Dauer'] = 45
new_df.loc[2,'Kunden'] = 103
new_df.loc[6,'MinKauf'] = 136
new_df.loc[1,'MaxKauf'] = 479
new_df.loc[19,'MaxKauf'] = 323

#Reinigung 4 - Duplikate enfert
new_df.drop_duplicates(inplace = True)

print(new_df.to_string())
