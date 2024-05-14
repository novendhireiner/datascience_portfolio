# Dieser Code demonstriert die Anwendung von Polynom-Regression und k-facher Kreuzvalidierung für verschiedene Grade von Polynomen. Zuerst werden 
# Beispiel-Daten generiert, bestehend aus einer unabhängigen Variablen `x` und einer abhängigen Variablen `y`, die einer linearen Beziehung mit zufälligem 
# Rauschen folgt. Die möglichen Grade der Polynome werden definiert, und anschließend wird für jeden Grad ein Polynom-Modell erstellt. Das Polynom-Modell 
# wird durch `PolynomialFeatures` und `LinearRegression` aus Scikit-learn in einem Pipeline-Format erstellt, was die Implementierung erleichtert.
#
# In der Schleife über die verschiedenen Grade wird dann die k-fache Kreuzvalidierung durchgeführt. Dabei wird das Modell auf den Daten trainiert und auf 
# einem Teil der Daten validiert, wobei der mittlere quadratische Fehler (MSE) für jeden Validierungssatz berechnet wird. Der negative MSE wird verwendet, 
# da `cross_val_score` nach einer Score-Funktion sucht, die größer ist, wenn sie besser ist. Die negativen Werte werden dann gemittelt, um den durchschnittlichen
# negativen MSE für jedes Grad des Polynoms zu berechnen und ausgegeben. Dies ermöglicht es, die Leistung der Polynom-Modelle mit unterschiedlichen Komplexitäten 
# zu vergleichen und den Grad auszuwählen, der die beste Vorhersageleistung aufweist.

import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Generiere Beispiel-Daten mit random
np.random.seed(42)
X = np.random.rand(100, 1)
y = 3 * X.squeeze() + 2 + np.random.randn(100)

# Definiere die möglichen Grade
polynomial_degrees = [1, 2, 3, 4]

# Führe die k-fache Kreuzvalidierung durch
k_folds = 5  # Anzahl der Folds für die Kreuzvalidierung

for degree in polynomial_degrees:
    # Erstelle ein Polynom-Modell
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())

    # Führe die Kreuzvalidierung mit cross_val_score
    scores = cross_val_score(model, X, y, cv=k_folds, scoring='neg_mean_squared_error')

    # Berechne den Durchschnitt des negativen mittleren quadratischen Fehlers (negative MSE)
    average_neg_mse = np.mean(scores)

    print(f"Durchschnittlicher negativer MSE für Polynomgrad {degree}: {average_neg_mse:.4f}")
