# Dieses Skript generiert Dummy-Daten und führt dann K-Means-Clustering mit verschiedenen Anzahlen von Clustern durch, 
# um die Inertia-Werte zu untersuchen. Zuerst werden mithilfe von NumPy zufällige 2D-Daten generiert. 
# Dann wird eine Schleife über die Anzahl der Cluster von 1 bis 11 durchgeführt, wobei für jede Anzahl von Clustern 
# ein KMeans-Modell erstellt und auf den generierten Daten angewendet wird. Die Inertia, ein Maß für die Summe 
# der quadratischen Abstände der Datenpunkte zu ihren zugehörigen Zentren, wird für jedes Modell gespeichert. 
# Schließlich wird ein Liniendiagramm erstellt, das die Anzahl der Cluster gegen die entsprechenden Inertia-Werte darstellt. 
# Dies ermöglicht es, den "Elbeneffekt" zu visualisieren und potenzielle Anomalien in den Daten zu identifizieren.
#
# Die Visualisierung dieses Skripts ermöglicht es, die optimale Anzahl von Clustern für die vorliegenden Daten zu ermitteln, 
# indem sie die Inertia-Werte für verschiedene Clusteranzahlen darstellt. Die Kurve zeigt typischerweise einen Abwärtstrend, 
# wobei die Inertia mit zunehmender Anzahl von Clustern abnimmt. Der Punkt, an dem die Abnahme der Inertia abflacht 
# deutet darauf hin, dass die zusätzlichen Cluster keine wesentliche Verbesserung der Datenpartitionierung bieten. 
# Diese Analyse hilft bei der Auswahl einer angemessenen Anzahl von Clustern für die K-Means-Clusteranalyse und 
# liefert Einblicke in die Struktur und Verteilung der Daten.

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
