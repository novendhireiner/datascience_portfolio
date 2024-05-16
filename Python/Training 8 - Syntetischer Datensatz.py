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
