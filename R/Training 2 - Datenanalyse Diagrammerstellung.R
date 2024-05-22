#Scatterplot:
library(ggplot2)

data(airquality)
asdf
ggplot(airquality, aes(x = Temp, y = Ozone, color = factor(Month))) +
  geom_point() +
  labs(x = "Temperatur", y = "Ozonkonzentration", color = "Monat") +
  scale_color_discrete(name = "Monat")+
  ggtitle("Luftqualitätsvergleich zw. Temperatur und Ozonkonzentration")

#Interpretation:
#je höher die Temperatur ist, desto höhere die Ozonkonzentration ist. Es wird je nach Monat variiert.

#Balkendiagramm:
#den Durchschnitt der Ozonkonzentration pro Monat
average_ozone <- aggregate(Ozone ~ Month, data = airquality, FUN = mean)

#Balkendiagramm:
ggplot(average_ozone, aes(x = factor(Month), y = Ozone)) +
  geom_bar(stat = "identity", fill = "blue") +
  labs(x = "Monat", y = "Durchschnittliche Ozonkonzentration")+
  ggtitle("Balkendiagramm: Durchschnittliche Ozonkonzentration")

#Interpretation:
#Die durchschnittliche Ozonkonzentration im Monat 7 und 8 tendeziell höher als andere Monat.

#Boxplot:
ggplot(airquality, aes(x = factor(Month), y = Temp)) +
  geom_boxplot(fill = "blue") +
  labs(x = "Monat", y = "Temperatur") +
  ggtitle("Boxplot: Temperatur für jeden Monat")

#Interpretation:
#Temperaturwerte variieren im Monat 5 bis 9 je nach Kastenhöhe. Außreiser befinden sich im Monat 6 und 7.
