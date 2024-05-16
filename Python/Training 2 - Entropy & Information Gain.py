import numpy as np
import pandas as pd

# Daten aus Excel-File importieren
excel_file = 'ProjectData.xlsx'
df1 = pd.read_excel(excel_file, sheet_name='Tabellenblatt1')
df2 = pd.read_excel(excel_file, sheet_name='Tabellenblatt2')

# Informationsgewinn Tabelle1

def entropy(labels):
    unique_labels, counts = np.unique(labels, return_counts=True)
    probabilities = counts / len(labels)
    entropy = -np.sum(probabilities * np.log2(probabilities))
    return entropy

# Funktion zum Berechnen des Informationsgewinns
def information_gain(data, feature, target):
    total_entropy = entropy(data[target])
    feature_values = data[feature].unique()
    weighted_entropy = 0
    for value in feature_values:
        subset = data[data[feature] == value]
        subset_entropy = entropy(subset[target])
        weighted_entropy += len(subset) / len(data) * subset_entropy
    information_gain = total_entropy - weighted_entropy
    return information_gain

# Datensatz
data1 = df1

# Informationsgewinn für jedes Feature berechnen
target = 'Draussen Essen'
information_gewinn1 = {}
for feature in data1.columns:
    if feature != target:
        information_gewinn1[feature] = information_gain(data1, feature, target)


# Ausgabe der Informationsgewinne 1
print('Tabelle 1: \n')
for feature, gain in information_gewinn1.items():
    print(f'Informationsgewinn für {feature}: {round(gain,2)}')

# Informationsgewinn Tabellenblatt 2
# Kategorisierung der Features
df2['Windgeschwindigkeit_Kategorie'] = pd.cut(df2['Windgeschwindigkeit'], bins=[0, 5, 11, 19], labels=['1-5 km/h', '6-11 km/h', '12-19 km/h'])
df2['Temperatur_Kategorie'] = pd.cut(df2['Temperatur'], bins=[0, 18, 28, 40], labels=['kalt', 'mild', 'heiss'])
df2['Luftfeuchtigkeit_Kategorie'] = pd.cut(df2['Luftfeuchtigkeit'], bins=[0, 5, 10], labels=['niedrig', 'hoch'])

# Datensatz
data2 = df2

# Informationsgewinn für jedes Feature berechnen
target = 'Aussenverkauf'
information_gewinn2 = {}
for feature in data2.columns:
    if feature != target:
        information_gewinn2[feature] = information_gain(data2, feature, target)

# Ausgabe der Informationsgewinne
print ('\nTabelle 2: \n')
for feature, gain in information_gewinn2.items():
    print(f'Informationsgewinn für {feature}: {round(gain,2)}')

# Statistische Analyse Tabellenblatt 2
mean_df2 = df2.mean()
median_df2 = df2.median()
std_df2 = df2.std()
corr_feu_temp = df2['Luftfeuchtigkeit'].corr(df2['Temperatur'])
corr_wind_feu = df2['Windgeschwindigkeit'].corr(df2['Luftfeuchtigkeit'])
corr_wind_temp = df2['Windgeschwindigkeit'].corr(df2['Temperatur'])

# Ausgabe der Ergebnisse
print('\nStatistische Analyse Tabellenblatt 2:')

print('\nMittelwert von:')
print(mean_df2)
print('\nMedian von:')
print(median_df2)
print('\nStandardabweichung von:')
print(std_df2)

print('\nKorrelation Luftfeuchtigkeit und Temperatur:')
print(round(corr_feu_temp,2))
print('\nKorrelation Windgeschwindigkeit und Luftfeuchtigkeit:')
print(round(corr_wind_feu,2))
print('\nKorrelation Windgeschwindigkeit und Temperatur:')
print(round(corr_wind_temp,2))
