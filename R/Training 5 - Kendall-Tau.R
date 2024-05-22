# Laden des Datensatzes ToothGrowth
data("ToothGrowth")

# Überprüfen der Struktur des Datensatzes
str(ToothGrowth)

library(ggplot2)
# Streudiagramm erstellen
scatterplot <- ggplot(ToothGrowth, aes(x = dose, y = len)) +
  geom_point() +
  labs(x = "Dosis von Vitamin C", y = "Länge der Zahnwachstumsrate") +
  ggtitle("Streudiagramm von Länge der Zahnwachstumsrate vs. Vitamin C Dosis")

print(scatterplot)

# Berechnung des Kendall-Tau-Korrelationskoeffizienten
cor_test_result <- cor.test(ToothGrowth$len, ToothGrowth$dose, method = "kendall")

print(cor_test_result)

#Kendall's rank correlation tau
#data:  ToothGrowth$len and ToothGrowth$dose
#z = 6.8404, p-value = 7.896e-12
#alternative hypothesis: true tau is not equal to 0
#sample estimates:
#      tau 
#0.6959839 

install.packages("DescTools")
library(DescTools)

# Berechnung des 95%-Konfidenzintervalls für Kendall-Tau
kendall_ci <- KendallTauB(ToothGrowth$len, ToothGrowth$dose, conf.level = 0.95)

# Anzeigen des Konfidenzintervalls
print(kendall_ci)

#tau_b    lwr.ci    upr.ci 
#0.6959839 0.6191527 0.7728151 

# Interpretation:
# Der Kendall-Korrelationskoeffizient in diesem Fall beträgt 0.695 mit p-value = 7.896e-12.
# Es handelt sich hier um sehr kleine Signifikanz
# H0 mit keiner Korrelation der beiden Variablen wegen p < 0.05 wird verworfen
# das mit dem 95%-Konfidenzintervall keine Null beinhaltet, liegt es somit eine
# positive Korrelation zwischen Variable "Dosis von Vitamin C" und " Länge der Zahnwachstumsrate vor
