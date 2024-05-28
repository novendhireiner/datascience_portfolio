import pandas as pd
import plotly.express as px
import streamlit as st

# Daten Aufbereitung
data = pd.read_excel("Energiepreise an private Haushalt 2008-2023.xlsx")

# Streamlit-Anwendung starten
st.title("Energiepreise an private Haushalt von 2008 bis 2023 Benchmarking Dashboard")

# Erstellen einer neuen Spalte 'periode' aus 'Jahr' und 'Halbjahr'
data['periode'] = data['Jahr'].astype(str) + ' H' + data['Halbjahr'].astype(str)

# Multi-Select-Menü für die Auswahl der Energiequelle
energiequelle = st.multiselect(
    'Wähle eine oder mehrere Energiequelle aus:',
    options=data['Erzeugnis'].unique()
)

# Filtere die Daten basierend auf den ausgewählten Energiequellen
filtered_data_energiequellen = data[data['Erzeugnis'].isin(energiequelle)]

# Multi-Select-Menü für die Auswahl der Jahresverbrauchsklasse, basierend auf den ausgewählten Energiequellen
jahresverbrauchsklasse = st.multiselect(
    'Wähle eine oder mehrere Jahresverbrauchsklasse aus:',
    options=filtered_data_energiequellen['Jahresverbrauchsklassen'].unique()
)

# Multi-Select-Menü für die Auswahl der Preisarten
preisarten = st.multiselect(
    'Wähle eine oder mehrere Preisarten aus:',
    options=data['Preisarten'].unique()
)

# Filtere die Daten basierend auf den ausgewählten Energiequellen, Jahresverbrauchsklassen und Preisarten
filtered_data = filtered_data_energiequellen[
    (filtered_data_energiequellen['Jahresverbrauchsklassen'].isin(jahresverbrauchsklasse)) &
    (filtered_data_energiequellen['Preisarten'].isin(preisarten))
]

# Liniendiagramm erstellen
fig = px.line(filtered_data, x='periode', y='EUR_KWh', color='Erzeugnis', line_dash='Jahresverbrauchsklassen',
              title='Preisentwicklung der ausgewählten Energiequellen, Jahresverbrauchsklassen und Preisarten',
              labels={'EUR_KWh': 'Preis in EUR / kWh', 'periode': 'Periode'})


# Diagramm in Streamlit anzeigen
st.plotly_chart(fig)

# Tabelle anzeigen
st.subheader('Gefilterte Daten')
st.write(filtered_data)
