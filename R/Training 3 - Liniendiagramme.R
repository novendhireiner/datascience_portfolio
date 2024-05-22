# Teil A
# Schritt 1: Laden des Datensatzes "airquality" und Datenreinigung
data(airquality)
airquality <- na.omit(airquality) 

# Schritt 2: Liniendiagramms mit ggplot2
# install.packages("ggplot2")
library(ggplot2)
ggplot(airquality, aes(x = Day, y = Ozone)) +
  geom_line()+
  ggtitle("Line Diagram 2: Ozonkonzentration im Laufe der Tage")

# Schritt 3: Diagrammanpassen
ggplot(airquality, aes(x = Day, y = Ozone)) +
  geom_line(linetype = "dashed", color = "blue") + 
  geom_point(color = "red") +  
  labs(x = "Tag", y = "Ozonkonzentration")+
  ggtitle("Line Diagram 3: Ozonkonzentration im Laufe der Tage")

# Schritt 4: Anpassen der x-Achsenbeschriftung (Hauptgitter und Hilfsgitter)
ggplot(airquality, aes(x = Day, y = Ozone)) +
  geom_line(linetype = "dashed", color = "blue") +
  geom_point(color = "red") +
  labs(x = "Tag", y = "Ozonkonzentration") +
  ggtitle("Line Diagram 4: Ozonkonzentration im Laufe der Tage")+
  scale_x_continuous(breaks = seq(1, max(airquality$Day), by = 5), minor_breaks = seq(1, max(airquality$Day), by = 1))

# Schritt 5: Interpretation des Ergebnisses
# Das Liniendiagramm zeigt die Veränderung von der Ozonkonzentration im Laufe der Tage (1 bis 31). 
# Es ist zu erkennen, dass die Ozonkonzentratioin im Laufe der Tage schwankt. 
# Hier ist einen Trend schwer zu erkenne, da schwankt sich die Ozonkonzentration jeden Tag auf mehrere Punkt.
# Aber ist die Ozonkonzentration tendenziell geringer bis Tag 21 und steigt danach bis zum Tag 31 auf.
# Es sind die höchsten und niedrigsten Ozon Konzentration am Tag 25 bzw. 21 zu beobachten.
# Die gestrichelte Linie hilft dabei, den Verlauf der Daten zu verfolgen und mögliche Trends zu erkennen. Datenpunkte geben Ihnen die konkreten Messwerte an bestimmten Tagen
# Die angepasste x-Achsenbeschriftung mit Hauptgitter und Hilfsgitter erleichtert das Ablesen der Tageswerte und trägt zur besseren Visualisierung bei.


# Teil B
# Schritt 1: Lade den Datensatz und Datenreinigung
data(economics)
economics <- na.omit(economics)
data(economics_long)
# Schritt 2: Datensatz auf Long-Format transformieren
# install.packages("tidyverse")
library(tidyverse)

# angenommen ist die Population nur für volljährige Arbeitskraft
economics$employ <- economics$pop - economics$unemploy

economics_long <- economics %>%
  pivot_longer(cols = c(unemploy, employ),
               names_to = "Status",
               values_to = "Anzahl")

# Schritt 3: Line Diagram erstellen
# install.packages("ggplot2")
library(ggplot2)

ggplot(economics, aes(x = date)) +
  geom_line(aes(y = employ, color = "Erwerbstätige"), size = 1) +
  geom_line(aes(y = unemploy, color = "Erwerbslose"), size = 1)

# Schritt 4:
ggplot(economics, aes(x = date)) +
  geom_line(aes(y = employ/1000, color = "Erwerbstätige"), size = 1) +
  geom_line(aes(y = unemploy/1000, color = "Erwerbslose"), size = 1) +
  labs(x = "Jahr", y = "Anzahl der Arbeitskraft (in tausend)",
       color= "Legende") +
  ggtitle("Liniendiagramm: Arbeitskraftvergleich")+
  scale_color_manual(values = c("Erwerbstätige" = "blue", "Erwerbslose" = "red")) +
  scale_linetype_manual(values = c("Erwerbstätige" = "solid", "Erwerbslose" = "dashed")) +
  theme_minimal()

# Schritt 5: Interpretation
# Das Liniendiagramm zeigt das Vergleich von Arbeitskraft in der USA im Jahr 1967 bis 2015.
# Daraus kann man erkennen, dass die Anzahl der Erwerbstätige eine aufsteigender Trend hat
# wobei die Anzahl der Erwerbslose eine stetiger Trend mit leicht Veränderung im ca. Jahr 2009 bis 2010
