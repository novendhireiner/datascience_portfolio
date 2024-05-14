# Dieses Skript demonstriert die Datenaufbereitung und -analyse von Gehaltsdaten mithilfe von Pandas und statistischen 
# Methoden. Zuerst wird eine CSV-Datei mit Gehaltsinformationen eingelesen und anschließend gereinigt, indem NaN-Werte entfernt
# und Ausreißer, die Gehälter über 150.000 überschreiten, durch den Durchschnitt ersetzt werden. Der bereinigte Datensatz wird
# dann von Duplikaten befreit. Anschließend werden statistische Kennzahlen wie Modus, Median, Mittelwert und Standardabweichung
# für die Gehaltsdaten berechnet sowie die Korrelation zwischen Gehalt und Position ermittelt.
#
# Das Skript führt auch lineare Regression und Polynomregression bis zum Grad 4 durch, um die Beziehung zwischen Gehalt und 
# Position (Level) zu untersuchen. Die Steigung und der Y-Achsenabschnitt der linearen Regression werden ausgegeben, während 
# die Koeffizienten der Polynomregression für verschiedene Grade sowie der mittlere quadratische Fehler für jedes Polynom 
# visualisiert werden. Dieses Skript bietet eine umfassende Analyse der Gehaltsdaten und ermöglicht es, Trends und Muster 
# in den Daten zu identifizieren.

import pandas as pd
import statistics as st
import numpy as np
import matplotlib.pyplot as plt

#CSV-Datei einlesen
df = pd.read_csv('Salaries.csv')

#Datenreinigung
new_df = df.dropna()

for x in new_df.index:
    if new_df.loc[x, "Salary"]> 150000:
        new_df.loc[x, "Salary"]= round(df ["Salary"].mean(),2)

new_df.drop_duplicates(inplace = True)

# Mean Median & Modus von Gehalt bzw. Position 
x = new_df ["Position"].mode()
y = new_df ["Salary"].mode()
z = new_df ["Salary"].median()
a = new_df ["Salary"].mean()
stdab = new_df.std()

korr = st.correlation(new_df["Level"], new_df["Salary"])

print(new_df.to_string())

print('\n Modus für Position: ',x)
print('Modus für Salary: ',y)
print('Median für Salary: ',z)
print('Mean für Salary: ',a)
print('Standardabweichung: \n',stdab)
print('Korrelation zwischen Position und Gehalt: \n',korr,'\n')

#Lineare Regression
def linear_regression(data):
    x = data['x']
    y = data['y']
    coefficients = np.polyfit(x, y, 1)
    slope = coefficients[0]
    intercept = coefficients[1]
    return slope, intercept

#Polynomregression
def polynomial_regression(data, degree):
    x = data['x']
    y = data['y']
    coefficients = np.polyfit(x, y, degree)
    return coefficients

#Polynome plotten
def plot_polynomials(data, degrees):
    x = data['x']
    y = data['y']
    plt.scatter(x, y, label='Daten')
    for degree in degrees:
        coefficients = polynomial_regression(data, degree)
        polynomial = np.poly1d(coefficients)
        plt.plot(x, polynomial(x), label=f'Grad {degree}')
    plt.legend()
    plt.show()

# Schritt 4: Mittleren quadratischen Fehler berechnen
def mean_squared_error(data, degree):
    x = data['x']
    y = data['y']
    coefficients = polynomial_regression(data, degree)
    polynomial = np.poly1d(coefficients)
    predicted_values = polynomial(x)
    mse = np.mean((predicted_values - y) ** 2)
    return mse

#Datensatz
data = pd.DataFrame({'x': new_df["Level"], 'y': new_df["Salary"]})

#Lineare Regression
slope, intercept = linear_regression(data)
print('Lineare Regression:')
print('Steigung:', slope)
print('Y-Achsenabschnitt:', intercept)

# Polynomregression bis Grad 4
degrees = [1, 2, 3, 4]
print('\nPolynomregression:')
for degree in degrees:
    coefficients = polynomial_regression(data, degree)
    print(f'Grad {degree}:', coefficients)

# Polynome plotten
plot_polynomials(data, degrees)

# Mittleren quadratischen Fehler berechnen
print('\nMittlerer quadratischer Fehler:')
for degree in degrees:
    mse = mean_squared_error(data, degree)
    print(f'Grad {degree}:', mse)