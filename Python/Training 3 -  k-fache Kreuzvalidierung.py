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
