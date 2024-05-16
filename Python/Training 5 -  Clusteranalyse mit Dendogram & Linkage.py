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
