# Dieses Skript verwendet die Python-Bibliothek Faker, um synthetische Nutzerdaten zu generieren und sie in einem 
# Pandas DataFrame zu organisieren. Zuerst wird der Faker initialisiert, der für die Generierung von Namen, Adressen und 
# geografischen Koordinaten verwendet wird. Die Funktion generate_user_data() wird definiert, um zufällige Nutzerdaten 
# zu erstellen, einschließlich einer Benutzer-ID, einem Namen, einer Adresse und einer geografischen Lage.
#
# Anschließend wird eine Liste von 10 Einträgen generiert, indem die generate_user_data()-Funktion wiederholt aufgerufen wird. 
# Jeder Eintrag enthält eine eindeutige Benutzer-ID, einen zufälligen Namen, eine Adresse und eine geografische Lage.
# Diese Einträge werden dann in einem Pandas DataFrame organisiert, wobei die Spalten entsprechend den Nutzerdaten 
# benannt werden. Schließlich wird der erstellte DataFrame ausgegeben, um die synthetischen Nutzerdaten anzuzeigen.
#
# Dieses Skript ermöglicht die schnelle Erzeugung von synthetischen Nutzerdaten für Testzwecke oder Demonstrationszwecke 
# und zeigt, wie Python-Bibliotheken wie Faker und Pandas effektiv zusammenarbeiten können, um Daten zu generieren und 
# zu organisieren.

import pandas as pd
import random
from faker import Faker

# Initialisiere den Faker
fake = Faker('de_DE')

# Funktion zur Generierung von synthetischen Nutzerdaten
def generate_user_data():
    user_id = random.randint(0, 100)
    name = fake.name()
    address = fake.address()
    geo_location = (fake.latitude(), fake.longitude())
    return user_id, name, address, geo_location

# Erzeuge den Datensatz mit 10 Einträgen
data = [generate_user_data() for _ in range(10)]

# Erstelle ein Pandas DataFrame
columns = ['User_ID', 'Name', 'Address', 'Geo_Location']
df = pd.DataFrame(data, columns=columns)

# Zeige den erstellten DataFrame an
print(df)
