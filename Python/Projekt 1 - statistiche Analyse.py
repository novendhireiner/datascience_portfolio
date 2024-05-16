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
