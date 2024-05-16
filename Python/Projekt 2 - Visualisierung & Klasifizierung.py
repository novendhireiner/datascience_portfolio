import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('MobilePhone.csv')

#Datavisualisierung
# Scatter Plot: Battery Power und Internal Memory
plt.scatter(df['battery_power'], df['int_memory'] ,c=df['Price Range'].map({'l': 'red', 'm': 'blue', 'h': 'green'}))
plt.xlabel('Battery Power')
plt.ylabel('Internal Memory')
plt.title('Battery Power vs. Internal Memory')
plt.show()

# Scatter Plot: Front Kamera Megapixel und Bluetooth
plt.scatter(df['frontcamermegapixels'], df['blue'], c=df['Price Range'].map({'l': 'red', 'm': 'blue', 'h': 'green'}))
plt.xlabel('Front Camera Megapixel')
plt.ylabel('Bluetooth')
plt.title('Front Camera Megapixel vs. Bluetooth')
plt.show()

# Scatter Plot: Internal Memory und Front Kamera Megapixel
plt.scatter(df['int_memory'], df['frontcamermegapixels'], c=df['Price Range'].map({'l': 'red', 'm': 'blue', 'h': 'green'}))
plt.xlabel('Internal Memory')
plt.ylabel('Front Camera Megapixel')
plt.title('Internal Memory vs. Front Camera Megapixel')
plt.show()


#Data-Klasifizierung
# Features und Zielvariable auswählen
X = df[['battery_power', 'frontcamermegapixels']]
y = df['Price Range']

#Data-Standardisierung
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# StandardScaler initialisieren und auf die Features anpassen und transformieren
scaler = StandardScaler()
X_standardized = scaler.fit_transform(X)

# Daten in Trainings- und Testdaten aufteilen
X_train, X_test, y_train, y_test = train_test_split(X_standardized, y_encoded, test_size=0.5, random_state=42)

# k-Nearest-Neighbor-Algorithmus initialisieren und trainieren mit verschidenen Algorithmen 'auto', 'kd_tree', 'ball_tree', 'brute'
knn = KNeighborsClassifier(n_neighbors=30, algorithm='auto')
knn.fit(X_train, y_train)

# Vorhersagen mit den Testdaten
y_pred = knn.predict(X_test)
print('Testdaten: \n', y_test)
print('Vorhersage mit den Testdaten: \n', y_pred)


#Genauigkeit des Algorithmus berechnen
accuracy = accuracy_score(y_test, y_pred)
print('Genauigkeit:', accuracy)
