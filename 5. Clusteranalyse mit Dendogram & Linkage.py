# Dieses Skript führt eine hierarchische Clusteranalyse auf einem Satz von Datenpunkten durch und erstellt anschließend 
# mehrere Dendrogramme, um verschiedene Methoden der Clusterbildung zu vergleichen. Zuerst werden die x- und y-Koordinaten 
# der Datenpunkte in ein Array kombiniert. Dann wird die hierarchische Clusteranalyse mit der Ward-Methode durchgeführt, 
# die darauf abzielt, die Varianz innerhalb der Cluster zu minimieren. Ein Dendrogramm wird erstellt und dargestellt, 
# das die Hierarchie der Cluster sowie die Distanzen zwischen den Datenpunkten visualisiert.
#
# Nach der Darstellung des Dendrogramms mit der Ward-Methode werden weitere Dendrogramme für alternative Methoden der 
# Clusterbildung erstellt und angezeigt, darunter die complete, average und single linkage methods. Jedes Dendrogramm 
# veranschaulicht die Clusterstruktur basierend auf der jeweiligen Methode, wobei die Abstände zwischen den Datenpunkten 
# und den resultierenden Clustern visualisiert werden. Dies ermöglicht es, die unterschiedlichen Clustermethoden zu vergleichen 
# und deren Auswirkungen auf die Clusterstruktur zu verstehen, was wiederum Einblicke in die Datenstruktur und mögliche 
# Clusterzusammensetzungen liefert.

import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

x = [4, 6, 9, 4, 3, 11, 12, 6, 10, 12]
y = [22, 18, 25, 16, 16, 24, 24, 22, 21, 21]

# Kombiniere die x- und y-Koordinaten zu einem Array
data = np.array(list(zip(x, y)))

# Hierarchische Clusteranalyse
Z = linkage(data, method='ward')  # Verwendet die Ward-Methode für die Clusterbildung

# Dendrogramm erstellen
plt.figure(figsize=(10, 6))
plt.title('Dendrogramm')
plt.xlabel('Datenelemente')
plt.ylabel('Abstandsmaß')
dendrogram(Z, leaf_rotation=90., leaf_font_size=8.,)
plt.show()

# Linkage = ward
linkage_data = linkage (data, method='ward', metric='euclidean')
dendrogram (linkage_data)
plt.title ("Ward Methode")
plt.show()

# Linkage = complete
linkage_data = linkage (data, method='complete', metric='euclidean')
dendrogram (linkage_data)
plt. title ("Complete Methode")
plt.show()

# Linkage = average
linkage_data = linkage (data, method='average', metric='euclidean')
dendrogram(linkage_data)
plt. title ("Average Methode")
plt.show()

# Linkage = single
linkage_data = linkage (data, method='single', metric='euclidean')
dendrogram (linkage_data)
plt. title("Single Linkage Methode")
plt.show()