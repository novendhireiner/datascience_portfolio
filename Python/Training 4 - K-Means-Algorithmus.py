import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Dummy-Daten erzeugen
np.random.seed(42)
data = np.random.rand(100, 2)

# Liste zum Speichern der Inertia-Werte
inertia_values = []

# Schleife über die Cluster-Anzahl von 1 bis 11
for n_clusters in range(1, 12):

    # K-Means-Modell erstellen
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)

    # K-Means auf den Daten ausführen
    kmeans.fit(data)
    
    # Inertia-Wert speichern
    inertia_values.append(kmeans.inertia_)

# Plot erstellen
plt.plot(range(1, 12), inertia_values, marker='o')
plt.xlabel('Anzahl der Cluster')
plt.ylabel('Inertia')
plt.title('Inertia-Wert in Abhängigkeit von der Anzahl der Cluster')
plt.show()
