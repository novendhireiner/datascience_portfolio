# Aufgabe A
# Wine-Daten laden
#install.packages("rattle")
library(rattle)

data(wine)

# Deskriptive Statistik
summary(wine)

# Aufgabe B
# Multikollinearität vom Linearregression Modell
lrmodel <- lm(Type ~ Alcohol + Magnesium + Color, data = wine)
# VIF Berechnung
vif(lrmodel)

# Aufgabe C
# Multikolliniearität Untersuchung
#install.packages("rms")
library(rms)

model <- ols(Type ~ Alcohol + Magnesium + Color, data = wine)

# Berechnung des VIF
vif_values <- vif(model)

# Anzeigen der VIF-Werte
print(vif_values)

#Alcohol Magnesium     Color 
#1.483019  1.083642  1.431498 

# Aufgabe D 
omodel <- orm(Type ~ Alcohol + Magnesium + Color, data = wine, x = TRUE, y = TRUE)
omodel

#Logistic (Proportional Odds) Ordinal Regression Model

#orm(formula = Type ~ Alcohol + Magnesium + Color, data = wine, 
#    x = TRUE, y = TRUE)

#Model Likelihood               Discrimination    Rank Discrim.    
#Ratio Test                      Indexes          Indexes    
#Obs            178    LR chi2      96.35    R2                  0.472    rho     0.640    
#1              59    d.f.             3    R2(3,178)           0.408                     
#2              71    Pr(> chi2) <0.0001    R2(3,156.7)         0.449                     
#3              48    Score chi2   92.38    |Pr(Y>=median)-0.5| 0.274                     
#Distinct Y       3    Pr(> chi2) <0.0001                                                  
#Median Y         2                                                                        
#max |deriv| 0.0001                                                                        

#Coef    S.E.   Wald Z Pr(>|Z|)
#y>=2      27.7949 3.6367  7.64  <0.0001 
#y>=3      25.2053 3.5038  7.19  <0.0001 
#Alcohol   -2.1423 0.2991 -7.16  <0.0001 
#Magnesium -0.0285 0.0117 -2.43  0.0152  
#Color      0.7851 0.1105  7.10  <0.0001 


# Interpretation
# 1. Modelzusammenfassung:
# Es gibt insgesamt im Datensatz 178 Beobachtungen auf 3 verschiedene Winetypen.
# Typ 1 = 59 Mal, Typ 2 = 71 Mal und Typ 3 = 48 Mal
# Beim Likelihood-Quotient-Chi-Quadrat-Test, die Teststatistik mitsamt den Freiheitsgraden
# (df) Chi2 (3) = 96.35 hat eine Signifikanz von p < 0.0001. Der p-Wert liegt damit
# unter der typischen Verwerfungsgrenze von α = 0.05.
# H0 in diesem Fall wird verworfen. D.h. das Model mit den Prädiktoren "Alcohol", "Magnesium" und "Color"
# besser geeinet ist als das Nullmodell ohne jene Prädiktoren

# 2. Modellgüte
# Das Modell erreicht ein Nagelkerke R-Quadrat von 0.472

# 3. Koeffiziententabelle
# Auf die Tabelle liegt für die Prädictoren "Alcohol" und "Magnesium" über α = 0.05 auf -2.14 bzw. -0.02
# Der Koeffizient der intervallskalierten Variablen "Color" ist mit 0.78 größer als 0 und
# somit steigt die Wahrscheinlichkeit einer Entscheidung auf Weintyp mit Zunahme 
# der Farbintensität unter Kontrolle des Alcohol und Magnesium

# Empfehlung
# Aus diese Erkenntnisse kann man besser erkennen, dass:
# - Alkoholsgehalt auf den Wein ist die geringste Faktor und gefolgt von Magnesium.
# - Die Kunden haben größe Priörität auf Farbeinstensität von der Wein
# - Da die meistverkauf ist Weintyp 2, daher ist es zu empfehlen mehr auf diese Weintyp zu produzieren

# Aufgabe E
round(exp(coef(omodel)),3)

#         y>=2         y>=3      Alcohol    Magnesium        Color 
# 1.178077e+12 8.841086e+10 1.170000e-01 9.720000e-01 2.193000e+00 


# Interpretation
# Das OR bei "Color" mit 2.19 besagt, dass die Wahrscheinlichkeit, dass eine 
# höhere Verkauf von Wine 2.19 höher ist, wenn die Farbeintensität um 1 Einheit steigt, 
# und Konstanthaltung aller anderen Prädiktoren.
