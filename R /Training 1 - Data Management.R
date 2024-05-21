install.packages("readxl")
install.packages("dplyr")

# Laden der benötigten Pakete
library(readxl)
library(dplyr)

# Datensätze importieren
spotify1 <- read_excel("Teilprüfungsleistung 1/Spotify music_data1.xlsx")
spotify2 <- read_excel("Teilprüfungsleistung 1/Spotify music_data2.xlsx")


# Datensätze zusammenfügen
merged_spotify <- merge(spotify1, spotify2)

View(merged_spotify)
Summary(merged_spotify)

# Es handelt es sich hier, dass die beide Datensätze unterschiedliche Charaktereigenschaften haben.
# deshalb ist die Benutzung von merge() sinnvoll

# Erstellung verschidenen Teildatensätze
music1 <- merged_spotify %>%
  select(track_number, acousticness, instrumentalness, liveness, loudness, speechiness)

music2 <- merged_spotify %>%
  filter(artist %in% c("Britney Spears", "Katy Perry"))

music3 <- merged_spotify %>%
  filter(danceability > 0.6)

music4 <- merged_spotify %>%
  filter(artist == "WALK THE MOON") %>%
  select(track_number, danceability, duration_ms, liveness, loudness)

music4 <- music4 %>%
  mutate(new_variable = liveness * loudness)

# weitere Analyse
# 1. Identifiziere die Anzahl fehlender Werte in jeder Variable
missing_values <- sapply(merged_spotify, function(x) sum(is.na(x)))
#View(missing_values)

# 2. die fehlenden Werte ausschließen
spotify_gesamt <- na.omit(subset(merged_spotify))
#View(spotify_gesamt)

# Datei-Export
# Export als CSV
write.csv(spotify_gesamt,"spotify_gesamt.csv")
# Export als TXT
write.table(spotify_gesamt,"spotify_gesamt.txt", dec=",", sep = "\t")

# Export als XLSX
install.packages("openxlsx")
library(openxlsx)

write_xlsx(spotify_gesamt, "spotify_gesamt.xlsx")





