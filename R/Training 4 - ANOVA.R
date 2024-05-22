# Teil A
library(dplyr)
library(rstatix)
data("Orthodont")

descriptive_stats <- Orthodont %>%
  group_by(age) %>%
  summarise(
    Mean = mean(distance),
    SD = sd(distance)
  )
print(descriptive_stats)

#age  Mean    SD
#<dbl> <dbl> <dbl>
#  1     8  22.2  2.43
#2    10  23.2  2.16
#3    12  24.6  2.82
#4    14  26.1  2.77

# Boxplots zur Visualisierung der Verteilung
library(ggplot2)
boxplot_plot <- ggplot(Orthodont, aes(x = factor(age), y = distance)) +
  geom_boxplot() +
  labs(x = "Alter", y = "Abstand (distance)") +
  ggtitle("Boxplot der Abstand je Altersgruppe")

print(boxplot_plot)

# Interpretation Teil A
# Auf der Boxplot zeigt sich an, dass die Abstand zwischen der Hypophyse und der Pterygomaxillarspalte
# von der Probanden zwischen dem Alter 8 bis 14 steigt.

# Teil B
# 1. Überprüfung auf Ausreißer
Orthodont %>%
group_by(age) %>%
identify_outliers(distance) %>%
as.data.frame()

#age distance Subject    Sex is.outlier is.extreme
#1   8     27.5     M10   Male       TRUE      FALSE
#2   8     17.0     M13   Male       TRUE      FALSE
#3   8     16.5     F10 Female       TRUE      FALSE
#4  12     31.0     M09   Male       TRUE      FALSE
#5  12     31.0     M10   Male       TRUE      FALSE
#6  14     19.5     F10 Female       TRUE      FALSE

# 2. Überprüfung der Normalverteilung 
#install.packages("ggpubr")
library(ggpubr)
ggqqplot(Orthodont, "distance", facet.by = "age")+
  ggtitle("QQ-Plot für Verteilung der Abstand je nach Altersgruppe")

# Interpretation Teil B
# B.1. Es gibt insgesamt 6 Ausreißer (3 von Age 8, 2 von Age 12 und 1 von Age 14)
# B.2. Auf dem QQ-Plot sind die Abstand (distance) von aller Alter in etwa normal verteilt.



# Teil C
rep_anova <- anova_test(data = Orthodont, dv = distance, wid =Subject,
                        within = age, effect.size = "pes")

rep_anova$`Mauchly's Test for Sphericity`
#Effect     W     p p<.05
#1    age 0.758 0.233 

get_anova_table(rep_anova)
#ANOVA Table (type III tests)
#  Effect DFn DFd     F        p p<.05   pes
#1    age   3  78 38.04 2.99e-15     * 0.594

# Interpretation
# B.3. da der p-Wert = 0.233 und > 0.05 ist, deshalb die Sphärizität vorliegt

Orthodont %>%
  pairwise_t_test(distance~age, paired = TRUE,
                  p.adjust.method = "bonferroni") %>%
as.data.frame()

#       .y. group1 group2 n1 n2 statistic df        p    p.adj p.adj.signif
#1 distance      8     10 27 27 -2.547017 26 1.70e-02 1.03e-01           ns
#2 distance      8     12 27 27 -6.309715 26 1.11e-06 6.66e-06         ****
#3 distance      8     14 27 27 -8.656874 26 3.90e-09 2.34e-08         ****
#4 distance     10     12 27 27 -3.486636 26 2.00e-03 1.10e-02            *
#5 distance     10     14 27 27 -8.440819 26 6.38e-09 3.83e-08         ****
#6 distance     12     14 27 27 -4.196573 26 2.80e-04 2.00e-03           **

#Interpretation Teil C
# 1. Der p-Wert = 2.99e-15 ist sehr klein und liegt unter dem Alpha-Niveau von 0.05
#    Deshalb kann H0-Hypothese von Gleichheit der Messwerte zwischen den Alter verworfen werden
# 2. Bei den Post-hoc-Tests ist erkennbar, dass sich zwischen der Altersgruppe jeweils 
#    aufgrund p.adj < alpha signifikant voneinander unterscheiden, außer Alter 8 und 10.
#    In der Spalte p.adj.signif wurd dies mit "*" angezeigt. Bei Alter 8 und 10 wird "ns" als
#    nicht signifikant gegeben.


