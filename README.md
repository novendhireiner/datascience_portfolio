Willkommen in meinem Data Science Portfolio auf GitHub! Hier präsentiere ich eine Zusammenstellung meiner eigenen Trainingsprojekte und Codebeispiele. Dieses Portfolio dient nicht nur als Schaufenster meiner Fähigkeiten, sondern auch als Nachweis meines Fortschritts und meiner Erfahrungen in diesem Bereich.

# Inhalt
Mein Portfolio umfasst verschiedene Projekte und Codebeispiele, die ich während meiner Weiterbilung zum Agile Data Analyst entwickelt habe. Von einfachen Übungen bis hin zu komplexen Projekten decke ich eine Vielzahl von Themen ab, darunter Datenbereinigung und -exploration, maschinelles Lernen, Visualisierungstechniken in verschiedenen Programierssprachen, nämlich Python, SQL, R und verschiedenen Business Intelligence Tools. Jedes Projekt wird mit detaillierten Erklärungen und Anleitungen vorgestellt, um meine Herangehensweise und meine Fähigkeiten zu veranschaulichen. 

# Zielgruppe
Dieses Portfolio richtet sich an potenzielle Arbeitgeber, Kollegen und die Data Science-Community, die einen Einblick in meine Fähigkeiten und Erfahrungen im Bereich Data Science erhalten möchten. Es soll nicht nur mein Engagement und meine Fähigkeiten demonstrieren, sondern auch als Inspirationsquelle und Lernressource für andere dienen, die sich für Data Science interessieren.

# Beitragen
Dieses Portfolio wird regelmäßig aktualisiert, wenn ich neue Projekte und Codebeispiele hinzufüge oder bestehende aktualisiere. Ich bin immer offen für Feedback und Anregungen zur Verbesserung meiner Arbeit. Wenn du Fragen zu meinen Projekten hast oder Vorschläge für zukünftige Projekte hast, zögere nicht, mir eine Nachricht zu senden oder einen Kommentar zu hinterlassen.

# Hinweis
Bitte beachte, dass die in diesem Portfolio präsentierten Projekte und Codebeispiele ausschließlich meine eigene Arbeit darstellen. Wenn du Teile meines Codes verwenden möchtest, kontaktiere mich bitte durch [![Linkedin](https://i.sstatic.net/gVE0j.png) LinkedIn](https://www.linkedin.com/in/nrmaturbongs), um eine Genehmigung zu erhalten.

Vielen Dank, dass du mein Data Science-Portfolio besuchst! Ich hoffe, dass es dir gefällt und dir einen Einblick in meine Arbeit und meine Leidenschaft für Data Science bzw. Analyse gibt.

<hr>

## Inhaltsverzeichnis
* [Python](#Python)
* [R](#R)
* [SQL](#SQL)
* [Business Intelligence](#BI)

<hr>

## Python

  #### [Training 1 - Datenbereinigung](https://github.com/novendhireiner/datascience_portfolio/blob/main/Python/Training%201%20-%20Datenbereinigung.py)   
   <p>
   Der bereitgestellte Code zeigt eine Datenbereinigungs-Pipeline für eine CSV-Datei namens `dirtydata.csv`. Zuerst wird die Pandas-Bibliothek importiert, um DataFrames zu erstellen und zu bearbeiten. Dann wird die CSV-Datei in ein DataFrame geladen. Anschließend werden fehlende Werte in den Spalten "Dauer", "Kunden", "MinKauf" und "MaxKauf" durch den jeweiligen Durchschnittswert ersetzt. Danach werden Datumswerte in der Spalte "Datum" in das Datumsformat konvertiert. Dann werden Ausreißerwerte in den Spalten "Dauer", "Kunden", "MinKauf" und "MaxKauf" korrigiert. Schließlich werden Duplikate entfernt, und das bereinigte DataFrame wird ausgegeben.

Der Code bietet eine strukturierte Herangehensweise zur Bereinigung von Daten, indem er verschiedene Techniken wie das Auffüllen fehlender Werte mit Durchschnittswerten, die Korrektur von Datumsformaten, die Bearbeitung von Ausreißern und die Entfernung von Duplikaten verwendet. Durch diese Schritte wird die Datenqualität verbessert und das bereinigte DataFrame wird ausgegeben, um die Wirksamkeit der Datensäuberung zu demonstrieren.
   </p>

   #### [Training 2 - Entropy & Information Gain](https://github.com/novendhireiner/datascience_portfolio/blob/main/Python/Training%202%20-%20Entropy%20%26%20Information%20Gain.py)   
   <p>
   Der vorliegende Code führt verschiedene Datenanalysen für zwei Tabellenblätter aus einer Excel-Datei durch. Zunächst werden die Daten aus der Excel-Datei in Pandas DataFrames geladen. Dann wird die Funktion `entropy()` definiert, um die Entropie zu berechnen, und `information_gain()`, um den Informationsgewinn für jedes Feature zu ermitteln. Im ersten Teil des Codes wird der Informationsgewinn für jedes Feature im ersten Tabellenblatt berechnet und ausgegeben. 

Im zweiten Teil werden die einzelnen Features mit Bezug auf die Klasse “Draussen Essen” im zweiten Tabellenblatt kategorisiert und der Informationsgewinn für jedes Feature (Windgeschwindigkeit, Temperatur und Luftfeuchtigkeit) berechnet und ebenfalls ausgegeben. Darüber hinaus werden statistische Analysen wie Mittelwert, Median, Standardabweichung und Korrelation zwischen verschiedenen Variablen für das zweite Tabellenblatt durchgeführt und ausgegeben.

Dieser Code ermöglicht eine umfassende Datenanalyse, indem er den Informationsgewinn für die verschiedenen Features in den beiden Tabellenblättern berechnet und statistische Kennzahlen sowie Korrelationen zwischen den Variablen im zweiten Tabellenblatt ermittelt. Diese Analysen bieten wertvolle Einblicke in die Struktur und Beziehungen innerhalb der Daten und können bei der Entscheidungsfindung und der Ableitung von Erkenntnissen helfen.
   </p>

   #### [Training 3 - k-fache Kreuzvalidierung](https://github.com/novendhireiner/datascience_portfolio/blob/main/Python/Training%203%20-%20%20k-fache%20Kreuzvalidierung.py) 
   <p>
   Dieser Code demonstriert die Anwendung von Polynom-Regression und k-facher Kreuzvalidierung für verschiedene Grade von Polynomen. Zuerst werden Beispiel-Daten generiert, bestehend aus einer unabhängigen Variablen `x` und einer abhängigen Variablen `y`, die einer linearen Beziehung mit zufälligem Rauschen folgt. Die möglichen Grade der Polynome werden definiert, und anschließend wird für jeden Grad ein Polynom-Modell erstellt. Das Polynom-Modell wird durch `PolynomialFeatures` und `LinearRegression` aus Scikit-learn in einem Pipeline-Format erstellt, was die Implementierung erleichtert.

In der Schleife über die verschiedenen Grade wird dann die k-fache Kreuzvalidierung durchgeführt. Dabei wird das Modell auf den Daten trainiert und auf einem Teil der Daten validiert, wobei der mittlere quadratische Fehler (MSE) für jeden Validierungssatz berechnet wird. Der negative MSE wird verwendet, da `cross_val_score` nach einer Score-Funktion sucht, die größer ist, wenn sie besser ist. Die negativen Werte werden dann gemittelt, um den durchschnittlichen negativen MSE für jedes Grad des Polynoms zu berechnen und ausgegeben. Dies ermöglicht es, die Leistung der Polynom-Modelle mit unterschiedlichen Komplexitäten zu vergleichen und den Grad auszuwählen, der die beste Vorhersageleistung aufweist.
   </p>

   #### [Training 4 - K-Means-Algorithmus](https://github.com/novendhireiner/datascience_portfolio/blob/main/Python/Training%204%20-%20K-Means-Algorithmus.py) 
   <p>
   Dieses Skript generiert Dummy-Daten und führt dann K-Means-Clustering mit verschiedenen Anzahlen von Clustern durch, um die Inertia-Werte zu untersuchen. Zuerst werden mithilfe von NumPy zufällige 2D-Daten generiert. Dann wird eine Schleife über die Anzahl der Cluster von 1 bis 11 durchgeführt, wobei für jede Anzahl von Clustern ein KMeans-Modell erstellt und auf den generierten Daten angewendet wird. Die Inertia, ein Maß für die Summe der quadratischen Abstände der Datenpunkte zu ihren zugehörigen Zentren, wird für jedes Modell gespeichert. Schließlich wird ein Liniendiagramm erstellt, das die Anzahl der Cluster gegen die entsprechenden Inertia-Werte darstellt. 

Die Visualisierung dieses Skripts ermöglicht es, die optimale Anzahl von Clustern für die vorliegenden Daten zu ermitteln, indem sie die Inertia-Werte für verschiedene Clusteranzahlen darstellt. Die Kurve zeigt typischerweise einen Abwärtstrend, wobei die Inertia mit zunehmender Anzahl von Clustern abnimmt. Der Punkt, an dem die Abnahme der Inertia abflacht deutet darauf hin, dass die zusätzlichen Cluster keine wesentliche Verbesserung der Datenpartitionierung bieten. Diese Analyse hilft bei der Auswahl einer angemessenen Anzahl von Clustern für die K-Means-Clusteranalyse und liefert Einblicke in die Struktur und Verteilung der Daten.
   </p>
   
   #### [Training 5 - Clusteranalyse mit Dendogram & Linkage](https://github.com/novendhireiner/datascience_portfolio/blob/main/Python/Training%205%20-%20%20Clusteranalyse%20mit%20Dendogram%20%26%20Linkage.py) 
   <p>
   Dieses Skript führt eine hierarchische Clusteranalyse auf einem Satz von Datenpunkten durch und erstellt anschließend mehrere Dendrogramme, um verschiedene Methoden der Clusterbildung zu vergleichen. Zuerst werden die x- und y-Koordinaten der Datenpunkte in ein Array kombiniert. Dann wird die hierarchische Clusteranalyse mit der Ward-Methode durchgeführt, die darauf abzielt, die Varianz innerhalb der Cluster zu minimieren. Ein Dendrogramm wird erstellt und dargestellt, das die Hierarchie der Cluster sowie die Distanzen zwischen den Datenpunkten visualisiert.

Nach der Darstellung des Dendrogramms mit der Ward-Methode werden weitere Dendrogramme für alternative Methoden der Clusterbildung erstellt und angezeigt, darunter die complete, average und single linkage methods. Jedes Dendrogramm veranschaulicht die Clusterstruktur basierend auf der jeweiligen Methode, wobei die Abstände zwischen den Datenpunkten und den resultierenden Clustern visualisiert werden. Dies ermöglicht es, die unterschiedlichen Clustermethoden zu vergleichen und deren Auswirkungen auf die Clusterstruktur zu verstehen, was wiederum Einblicke in die Datenstruktur und mögliche Clusterzusammensetzungen liefert.
   </p>

   #### [Training 6 - Neural Network](https://github.com/novendhireiner/datascience_portfolio/blob/main/Python/Training%206%20-%20Neural%20Network.py) 
   <p>
   Dieses Skript implementiert ein neuronales Netzwerk mit einer Input-Schicht von 784 Neuronen, einer Hidden-Schicht mit 100 Neuronen und einer Output-Schicht mit 10 Neuronen. Es initialisiert Gewichtsmatrizen für die Verbindungen zwischen den Schichten mit zufälligen Werten. Die Aktivierungsfunktion ist die Sigmoid-Funktion, die verwendet wird, um die Aktivierung der Neuronen zu berechnen. Die `test`-Funktion nimmt einen Input-Vektor, die Gewichtsmatrizen und gibt den Output-Vektor des neuronalen Netzwerks zurück. Ein Beispiel-Datensatz wird erstellt, und durch die `test`-Funktion wird ein Output-Vektor berechnet und ausgegeben. Das Training des neuronalen Netzwerks wird durch die `train`-Funktion durchgeführt, die die Gewichte zwischen den Schichten basierend auf den Fehlergradienten aktualisiert.

Die `train`-Funktion führt eine Rückwärtsdurchlauf-Algorithmus (Backpropagation) durch, um die Gewichte des neuronalen Netzwerks anzupassen. Sie nimmt eine Liste von Eingangsdaten, die Gewichtsmatrizen, eine Liste von Zielwerten und eine Lernrate als Eingabe. Die Eingangsdaten werden durch das Netzwerk geleitet, und die Fehler an der Ausgangsschicht werden berechnet. Die Fehler werden dann zurück in das Netzwerk propagiert, um die Fehler in der Hidden-Schicht zu berechnen. Schließlich werden die Gewichte zwischen den Schichten aktualisiert, um den Fehler zu reduzieren und das Netzwerk zu trainieren.
   </p>

   #### [Training 7 - Neural Network - Performance Test](https://github.com/novendhireiner/datascience_portfolio/blob/main/Python/Training%207%20-%20Neural%20Network%20-%20Performance%20Test.py) 
   <p>
   Dieses Skript implementiert ein neuronales Netzwerk mit verschiedenen Aktivierungsfunktionen und führt Training und Evaluation auf einem fiktiven Datensatz durch. Zuerst werden Annahmen über die Daten und Hyperparameter getroffen, einschließlich der Dimensionen der Eingabe- und Ausgabeschichten, der Lernrate und der Anzahl der Epochen. Trainings- und Testdaten werden erstellt, wobei Trainingsdaten in einem DataLoader geladen werden, um die Daten in Batches zu verarbeiten. Die Ground-Truth-Labels werden ebenfalls für die Evaluierung vorbereitet.

Die Klasse NeuralNetwork definiert das neuronale Netzwerk mit anpassbaren Aktivierungsfunktionen wie Sigmoid, Leaky ReLU, PreLU und ELU. Die Methode train_and_evaluate trainiert das Modell unter Verwendung des Kreuzentropieverlusts und evaluiert es anhand der Genauigkeit auf den Testdaten. Das Training und die Bewertung werden für jedes Aktivierungsfunktionsszenario durchgeführt und die entsprechenden Genauigkeiten ausgegeben.

Dieses Skript bietet einen Einblick in die Leistung verschiedener Aktivierungsfunktionen in neuronalen Netzwerken und zeigt, wie man mit PyTorch schnell experimentieren und Ergebnisse analysieren kann.
   </p>

   #### [Training 8 - Syntetischer Datensatz](https://github.com/novendhireiner/datascience_portfolio/blob/main/Python/Training%208%20-%20Syntetischer%20Datensatz.py) 
   <p>
   Dieses Skript verwendet die Python-Bibliothek Faker, um synthetische Nutzerdaten zu generieren und sie in einem Pandas DataFrame zu organisieren. Zuerst wird der Faker initialisiert, der für die Generierung von Namen, Adressen und geografischen Koordinaten verwendet wird. Die Funktion `generate_user_data()` wird definiert, um zufällige Nutzerdaten zu erstellen, einschließlich einer Benutzer-ID, einem Namen, einer Adresse und einer geografischen Lage.

Anschließend wird eine Liste von 10 Einträgen generiert, indem die `generate_user_data()`-Funktion wiederholt aufgerufen wird. Jeder Eintrag enthält eine eindeutige Benutzer-ID, einen zufälligen Namen, eine Adresse und eine geografische Lage. Diese Einträge werden dann in einem Pandas DataFrame organisiert, wobei die Spalten entsprechend den Nutzerdaten benannt werden. Schließlich wird der erstellte DataFrame ausgegeben, um die synthetischen Nutzerdaten anzuzeigen.

Dieses Skript ermöglicht die schnelle Erzeugung von synthetischen Nutzerdaten für Testzwecke oder Demonstrationszwecke und zeigt, wie Python-Bibliotheken wie Faker und Pandas effektiv zusammenarbeiten können, um Daten zu generieren und zu organisieren.
   </p>
   
<hr>

   #### [Projekt 1 - statistiche Analyse](https://github.com/novendhireiner/datascience_portfolio/blob/main/Python/Projekt%201%20-%20statistiche%20Analyse.py) 
   <p>
   Dieses Skript demonstriert die Datenaufbereitung und -analyse von Gehaltsdaten mithilfe von Pandas und statistischen Methoden. Zuerst wird eine CSV-Datei mit Gehaltsinformationen eingelesen und anschließend gereinigt, indem NaN-Werte entfernt und Ausreißer, die Gehälter über 150.000 überschreiten, durch den Durchschnitt ersetzt werden. Der bereinigte Datensatz wird dann von Duplikaten befreit. Anschließend werden statistische Kennzahlen wie Modus, Median, Mittelwert und Standardabweichung für die Gehaltsdaten berechnet sowie die Korrelation zwischen Gehalt und Position ermittelt.

Das Skript führt auch lineare Regression und Polynomregression bis zum Grad 4 durch, um die Beziehung zwischen Gehalt und Position (Level) zu untersuchen. Die Steigung und der Y-Achsenabschnitt der linearen Regression werden ausgegeben, während die Koeffizienten der Polynomregression für verschiedene Grade sowie der mittlere quadratische Fehler für jedes Polynom visualisiert werden. Dieses Skript bietet eine umfassende Analyse der Gehaltsdaten und ermöglicht es, Trends und Muster in den Daten zu identifizieren.
   </p>

   #### [Projekt 2 - Visualizierung & Klasifizierung](https://github.com/novendhireiner/datascience_portfolio/blob/main/Python/Projekt%202%20-%20Visualisierung%20%26%20Klasifizierung.py) 
   <p>
  Dieses Skript verwendet Daten aus einer CSV-Datei, die mobile Telefoninformationen enthält, und führt Datensvisualisierung und Klassifizierung durch. Zuerst werden die Daten eingelesen und dann verschiedene Scatterplots erstellt, um Beziehungen zwischen verschiedenen Merkmalen zu visualisieren, wie z.B. Batterie-Leistung und interner Speicher, Frontkamera-Megapixel und Bluetooth, sowie interner Speicher und Frontkamera-Megapixel.

Für die Klassifizierung werden die Features und die Zielvariable ausgewählt und die Zielvariable kodiert, um sie für die Klassifikationsalgorithmen vorzubereiten. Die Features werden standardisiert, um sicherzustellen, dass alle Features auf die gleiche Skala gebracht werden. Die Daten werden dann in Trainings- und Testdaten aufgeteilt. Ein k-Nearest-Neighbor-Algorithmus wird initialisiert und mit den Trainingsdaten trainiert. Anschließend werden Vorhersagen mit den Testdaten durchgeführt, und die Genauigkeit des Algorithmus wird berechnet und ausgegeben. Der Algorithmus wird mit verschiedenen Algorithmen, einschließlich `auto`, `kd_tree`, `ball_tree` und `brute`, durchgeführt, um die Leistung zu vergleichen.
   </p>

   #### [Projekt 3 - Convolutionan Neural Network - Bildklassifizierung](https://github.com/novendhireiner/datascience_portfolio/blob/main/Python/Projekt%203%20-%20Convolutionan%20Neural%20Network%20Kaggle%20Birds%20525%20Species%20Image%20Classification.ipynb) 
   <p>
  Dieser Code demonstriert die Anwendung von Convolutional Neural Networks (CNNs) für die Bildklassifizierung mit PyTorch. Zunächst werden die Bilddaten vorbereitet, indem sie in Trainings- und Validierungssets aufgeteilt und vorverarbeitet werden, einschließlich Änderungen der Größe und Normalisierung.

Dann wird ein benutzerdefiniertes CNN-Modell namens BirdNet definiert, das aus mehreren Faltungs- und Pooling-Schichten sowie vollständig verbundenen Schichten besteht. Das Modell wird mit einem Kreuzentropieverlust trainiert und optimiert.

Während des Trainings werden Verluste berechnet und die Gewichte aktualisiert, und die Leistung des Modells wird auf dem Validierungsdatensatz überwacht. Nach Abschluss des Trainings wird die Entwicklung von Trainings- und Validierungsverlusten sowie die Validierungsgenauigkeit für jede Epoche angezeigt. Dieser Code bietet eine robuste Grundlage für das Training von CNNs zur Bildklassifizierung mit PyTorch.
   </p>
<hr>

## R
#### [Training 1 - Data Management](https://github.com/novendhireiner/datascience_portfolio/blob/main/R/Training%201%20-%20Data%20Management.R)   
   <p>
Hier habe ich versucht, Datenmanagement mit R durchzuführen, insbesondere mit den Datensätzen über Spotify-Songs. Die Aufgabe bestand darin, zwei verschiedene Datensätze zu importieren, die verschiedene Informationen über Spotify-Songs enthalten: "Spotify music_data1.xls" mit Songtiteln und Künstlern sowie "Spotify music_data2.xls" mit Charaktereigenschaften der Songs. Der erste Schritt war der Import dieser Datensätze in R und das Speichern in Data Frames namens „spotify1“ und „spotify2“. Anschließend habe ich diese Datensätze zusammengeführt und mich entschieden, die `merge()`-Funktion zu verwenden, da diese für die Kombination von Datensätzen mit unterschiedlichen Charaktereigenschaften am geeignetsten ist.

Nachdem die Datensätze zusammengeführt waren, habe ich verschiedene Teildatensätze erstellt, um spezifische Analysen durchzuführen. Beispielsweise enthält der Datensatz „music1“ die Track-Nummer und bestimmte Eigenschaften wie Acousticness, Instrumentalness, Liveness, Loudness und Speechiness. Ein weiterer Datensatz „music2“ filtert nur Songs von Britney Spears oder Katy Perry. Für „music3“ habe ich Songs mit einer Danceability größer als 0,6 gefiltert, und „music4“ zeigt spezifische Merkmale der Band WALK THE MOON an. Zusätzlich wurde in „music4“ eine neue Variable erstellt, indem Liveness und Loudness multipliziert wurden. Schließlich habe ich fehlende Werte im Gesamt-Datensatz „spotify_gesamt“ identifiziert und ausgeschlossen, um die Analyse zu optimieren. Zum Abschluss wurden die bereinigten Daten in verschiedene Dateiformate exportiert: CSV, TXT und XLSX.
   </p>

#### [Training 2 - Datenanalyse Diagrammerstellung](https://github.com/novendhireiner/datascience_portfolio/blob/main/R/Training%202%20-%20Datenanalyse%20Diagrammerstellung.R)   
   <p>
ich habe eine detaillierte Analyse der Luftqualität anhand des in R verfügbaren Datensatzes "airquality" durchgeführt. Die Aufgabe bestand darin, verschiedene Diagramme zu erstellen und zu interpretieren, um ein besseres Verständnis der Zusammenhänge zwischen Temperatur, Ozonkonzentration und den verschiedenen Monaten zu erlangen. 

<table>
  <tr>
    <td align="center">Streudiagramm</td>
     <td align="center">Balkendiagramm</td>
     <td align="center">Boxplot</td>
  </tr>
  <tr>
    <td valign="top"><img src="https://github.com/novendhireiner/datascience_portfolio/blob/main/R/Scatterplot.png"></td>
    <td valign="top"><img src="https://github.com/novendhireiner/datascience_portfolio/blob/main/R/Balkendiagramm.png"></td>
    <td valign="top"><img src="https://github.com/novendhireiner/datascience_portfolio/blob/main/R/Boxplot.png"></td>
  </tr>
 </table>

Zunächst habe ich ein Streudiagramm (Scatterplot) erstellt, das die Temperatur (Temp) gegenüber der Ozonkonzentration (Ozone) darstellt und die Punkte nach dem Monat (Month) färbt. Dieses Diagramm zeigt deutlich, dass die Ozonkonzentration tendenziell mit steigender Temperatur zunimmt und diese Beziehung je nach Monat variiert. Durch die farbliche Unterscheidung nach Monaten werden saisonale Muster sichtbar, die auf die Veränderungen der Luftqualität im Jahresverlauf hinweisen.

Des Weiteren habe ich ein Balkendiagramm erstellt, das die durchschnittliche Ozonkonzentration für jeden Monat darstellt. Dieses Diagramm zeigt, dass die durchschnittliche Ozonkonzentration in den Monaten Juli und August tendenziell höher ist als in den anderen Monaten, was auf stärkere Sonneneinstrahlung und höhere Temperaturen in diesen Sommermonaten hinweisen könnte. 

Schließlich habe ich ein Boxplot für die Temperatur (Temp) für jeden Monat erstellt. Dieses Diagramm verdeutlicht die Verteilung der Temperaturwerte und zeigt, dass die Temperaturen in den Monaten Mai bis September variieren, mit einigen Ausreißern in den Monaten Juni und Juli. Insgesamt geben diese Diagramme wertvolle Einblicke in die saisonalen Schwankungen der Luftqualität und die damit verbundenen Umweltbedingungen.
   </p>

#### [Training 3 - Liniendiagramm](https://github.com/novendhireiner/datascience_portfolio/blob/main/R/Training%203%20-%20Liniendiagramme.R)   
   <p>
In diesem Training habe ich eine detaillierte Analyse der Luftqualität anhand des Datensatzes „airquality“ und des Vergleich der Arbeitskraft in den USA von 1967 bis 2015 anhand des "economics"-Datensatzes durchgeführt, wobei ich verschiedene Liniendiagramme mit ggplot2 erstellt und interpretiert habe. 
     
Zunächst habe ich den Datensatz „airquality“ in R geladen und fehlende Werte bereinigt. Anschließend habe ich ein einfaches Liniendiagramm erstellt, das den Verlauf der Ozonkonzentration im Laufe der Tage darstellt. Um die Visualisierung zu verbessern, habe ich das Diagramm angepasst, indem ich eine gestrichelte Linie und Datenpunkte hinzugefügt sowie die Achsenbeschriftungen angepasst habe. Die x-Achse wurde durch Haupt- und Hilfsgitterlinien detailliert beschriftet, was die Lesbarkeit und Interpretation der Daten erleichtert.
<table>
  <tr>
    <td align="center">Erstellung</td>
     <td align="center">Anpassung</td>
     <td align="center">Verbesserung mit Gitterlinien</td>
  </tr>
  <tr>
    <td valign="top"><img src="https://github.com/novendhireiner/datascience_portfolio/blob/main/R/3a.%20Line%20Diagram%202.png"></td>
    <td valign="top"><img src="https://github.com/novendhireiner/datascience_portfolio/blob/main/R/3a.%20Line%20Diagram%203.png"></td>
    <td valign="top"><img src="https://github.com/novendhireiner/datascience_portfolio/blob/main/R/3a.%20Line%20Diagram%204.png"></td>
  </tr>
 </table>

Die Interpretation der Ergebnisse zeigt, dass die Ozonkonzentration im Laufe der Tage Schwankungen unterliegt, wobei ein klarer Trend schwer zu erkennen ist. Die höchsten Ozonkonzentrationen wurden um den 25. Tag herum beobachtet, während die niedrigsten Konzentrationen um den 21. Tag auftraten. Die gestrichelte Linie und die eingefügten Datenpunkte helfen, den Verlauf und die spezifischen Messwerte der Ozonkonzentration besser nachzuvollziehen. Die angepasste x-Achsenbeschriftung trägt zusätzlich zur besseren Visualisierung bei, indem sie es ermöglicht, die Tageswerte präziser abzulesen und die Entwicklung der Ozonkonzentration im Verlauf des Monats detailliert zu verfolgen. 

Weiteren Teil habe ich die Daten transformiert, um die Anzahl der Erwerbstätigen und Erwerbslosen zu visualisieren. Ich habe das Liniendiagramm so angepasst, dass die Erwerbstätigen und Erwerbslosen in unterschiedlichen Farben und Linienstilen dargestellt werden.

<table>
  <tr>
    <td align="center">Erstellung</td>
     <td align="center">Anpassung</td>
  </tr>
  <tr>
    <td valign="top"><img src="https://github.com/novendhireiner/datascience_portfolio/blob/main/R/3b.%20Line%20Diagramm%203.png"></td>
    <td valign="top"><img src="https://github.com/novendhireiner/datascience_portfolio/blob/main/R/3b.%20Line%20Diagramm%204.png"></td>
  </tr>
 </table>

Die Visualisierung zeigt, dass die Anzahl der Erwerbstätigen einen aufsteigenden Trend aufweist, während die Anzahl der Erwerbslosen über die Jahre hinweg relativ konstant bleibt, mit einer leichten Zunahme um das Jahr 2009 herum. Durch die Anpassung der Achsenbeschriftungen und die Verwendung von Farben und Linienstilen werden die Trends und Veränderungen in der Arbeitskraft deutlich sichtbar. Die Darstellung der Arbeitskraft in Tausenden erleichtert das Verständnis der Größenordnung der Daten. Insgesamt bietet dieses Diagramm einen klaren Überblick über die Entwicklungen auf dem Arbeitsmarkt in den USA über fast fünf Jahrzehnte hinweg.
   </p>

#### [Training 4 - ANOVA für abhängige Stichprobe](https://github.com/novendhireiner/datascience_portfolio/blob/main/R/Training%204%20-%20ANOVA.R)   
   <p>
in diesem Training habe ich den Datensatz von Orthodont analisiert, der Daten über die Veränderung einer kieferorthopädischen Messung im Laufe der Zeit für 27 Kinder enthält. Die deskriptive Analyse zeigte, dass der Abstand zwischen der Hypophyse und der Pterygomaxillarspalte mit dem Alter tendenziell zunimmt. Die Berechnung der Mittelwerte und Standardabweichungen der Messungen für verschiedene Altersgruppen sowie die Erstellung von Boxplots halfen, diese Veränderung zu visualisieren und zu interpretieren. 
<table>
  <tr>
    <td align="center">Boxplot</td>
     <td align="center">QQ-Plot</td>
  </tr>
  <tr>
    <td valign="top"><img src="https://github.com/novendhireiner/datascience_portfolio/blob/main/R/4A.%20Boxplot.png"></td>
    <td valign="top"><img src="https://github.com/novendhireiner/datascience_portfolio/blob/main/R/4B.2.%20QQ-Plot.png"></td>
  </tr>
 </table>
Die Boxplots zeigten, dass die Verteilung der Messungen über die Altersgruppen hinweg relativ konsistent war, mit einem klaren Anstieg des mittleren Abstands von 8 bis 14 Jahren.

Zur Überprüfung der Voraussetzungen für die ANOVA mit Messwiederholungen wurden mehrere Tests durchgeführt. Die Identifizierung von Ausreißern ergab, dass es insgesamt sechs Ausreißer gab, die jedoch nicht extrem waren. Die Normalverteilung der Daten innerhalb jedes Messzeitpunkts wurde durch QQ-Plots bestätigt, die zeigten, dass die Verteilungen ungefähr normal waren. 

Die Überprüfung der Sphärizität mittels Mauchly's Test ergab, dass die Sphärizitätsannahme erfüllt war (p = 0.233).
```
Effect     W     p p<.05
1    age 0.758 0.233 
```
Die anschließende ANOVA mit Messwiederholungen zeigte signifikante Unterschiede zwischen den Messzeitpunkten (p < 0.05). 
```
ANOVA Table (type III tests)
  Effect DFn DFd     F        p p<.05   pes
1    age   3  78 38.04 2.99e-15     * 0.594
```

Post-hoc-Tests bestätigten, dass die Messungen zwischen fast allen Altersgruppen signifikant variierten, mit Ausnahme der Altersgruppen 8 und 10. Diese Ergebnisse zeigen, dass das Wachstum der gemessenen Distanz über die Jahre signifikante Veränderungen aufweist, was wichtige Implikationen für das Verständnis des kieferorthopädischen Wachstums bei Kindern hat.
```
       .y. group1 group2 n1 n2 statistic df        p    p.adj p.adj.signif
1 distance      8     10 27 27 -2.547017 26 1.70e-02 1.03e-01           ns
2 distance      8     12 27 27 -6.309715 26 1.11e-06 6.66e-06         ****
3 distance      8     14 27 27 -8.656874 26 3.90e-09 2.34e-08         ****
4 distance     10     12 27 27 -3.486636 26 2.00e-03 1.10e-02            *
5 distance     10     14 27 27 -8.440819 26 6.38e-09 3.83e-08         ****
6 distance     12     14 27 27 -4.196573 26 2.80e-04 2.00e-03           **

```
   </p>

#### [Training 5 - Kendall-Tau Koeefizientkorrelation](https://github.com/novendhireiner/datascience_portfolio/blob/main/R/Training%205%20-%20Kendall-Tau.R)   
   <p>
In dieserm Training untersuchte ich die Korrelation zwischen der Dosis von Vitamin C und der Zahnwachstumsrate bei Meerschweinchen mithilfe des Kendall-Tau-Korrelationskoeffizienten. Der Datensatz "ToothGrowth" wurde zunächst geladen und die Struktur mit der Funktion str() überprüft, um ein Verständnis für die enthaltenen Variablen zu erlangen. Anschließend wurde ein Streudiagramm erstellt, das die Beziehung zwischen der Dosis von Vitamin C und der Zahnwachstumsrate visualisiert. Dies ermöglichte eine erste visuelle Einschätzung, ob es eine Beziehung zwischen diesen beiden Variablen gibt. 
     
<table>
  <tr>
    <td align="center">Streudiagramm</td>
  </tr>
  <tr>
    <td valign="top"><img src="https://github.com/novendhireiner/datascience_portfolio/blob/main/R/5B.%20Scatterplot.png"></td>
  </tr>
 </table>
Die grafische Darstellung zeigte eine positive Korrelation, was darauf hindeutete, dass höhere Dosen von Vitamin C tendenziell mit einer größeren Zahnwachstumsrate verbunden sind.

Um diese visuelle Einschätzung zu quantifizieren, wurde der Kendall-Tau-Korrelationskoeffizient berechnet. Das Ergebnis zeigte einen Koeffizienten von 0.696 mit einem äußerst signifikanten p-Wert von 7.896e-12. Dies deutet auf eine starke positive Korrelation hin, bei der höhere Dosen von Vitamin C zu einer größeren Zahnwachstumsrate führen. Zur weiteren Bestätigung der Signifikanz dieser Korrelation wurde ein 95%-Konfidenzintervall berechnet, das von 0.619 bis 0.773 reicht. Da dieses Intervall keine Null umfasst, kann mit hoher Sicherheit gesagt werden, dass eine positive Korrelation zwischen den Variablen besteht. Diese Ergebnisse unterstützen die Hypothese, dass Vitamin C einen positiven Einfluss auf die Zahnwachstumsrate bei Meerschweinchen hat.
   </p>

#### [Training 6 - Ordinal logistische Regression](https://github.com/novendhireiner/datascience_portfolio/blob/main/R/Training%206%20-%20Ordinal%20logistische%20Regression.R)   
   <p>
Hier wurde der Zusammenhang zwischen verschiedenen chemischen Eigenschaften von Weinen und ihrer Qualitätsstufe mittels ordinaler logistischer Regression untersucht. Zunächst wurde der "wine"-Datensatz aus dem "rattle"-Paket geladen und eine deskriptive Statistik durchgeführt, um grundlegende Informationen über die enthaltenen Variablen zu gewinnen. Insbesondere wurden der Alkoholgehalt, der Magnesiumgehalt und die Farbintensität als unabhängige Variablen ausgewählt, um deren Einfluss auf die Qualitätsstufe der Weine, dargestellt durch die Variable "Type", zu analysieren. Um sicherzustellen, dass die Voraussetzungen für eine lineare Regression erfüllt sind, wurde die Multikollinearität der unabhängigen Variablen überprüft. Die berechneten Variance Inflation Factors (VIF) lagen alle unter dem kritischen Wert von 5, was auf eine geringe Multikollinearität hinweist.

Anschließend wurde ein ordinal logistisches Regressionsmodell erstellt, das die Weintypen als abhängige Variable und die chemischen Eigenschaften Alkohol, Magnesium und Farbe als unabhängige Variablen verwendete. Die Ergebnisse des Modells zeigten, dass alle drei Prädiktoren signifikante Einflussgrößen sind, wobei der Alkoholgehalt und der Magnesiumgehalt negativ und die Farbintensität positiv mit der Qualitätsstufe korrelieren. Der Likelihood-Quotient-Chi-Quadrat-Test ergab eine hohe Signifikanz (p < 0.0001), was darauf hinweist, dass das Modell mit den Prädiktoren besser geeignet ist als ein Nullmodell ohne diese Prädiktoren. Das Modell erreichte ein Nagelkerke R-Quadrat von 0.472, was auf eine gute Modellgüte hinweist. Die Odds-Ratios zeigten, dass eine Erhöhung der Farbintensität um eine Einheit die Wahrscheinlichkeit einer höheren Qualitätsstufe um das 2.19-fache erhöht, während höhere Werte für Alkohol und Magnesium die Wahrscheinlichkeit einer höheren Qualitätsstufe senken. Diese Erkenntnisse können genutzt werden, um die chemischen Eigenschaften von Weinen besser zu verstehen und die Produktionsprozesse sowie die Auswahl von Weinen für den Verkauf zu optimieren.
   </p>

#### [Projekt 1 - Shiny App](https://github.com/novendhireiner/datascience_portfolio/blob/main/R/Projekt%201%20-%20Shiny%20App.R)   
   <p>
In diesem Projekt habe ich versucht, eine interaktive Shiny-Anwendung zur Analyse des "palmerpenguins"-Datensatzes aufzubauen. Die Anwendung ermöglicht es den Benutzern, die Flossenlänge von Pinguinen zu visualisieren und zu filtern. Der Datensatz "penguins" wurde zuerst bereinigt, indem fehlende Werte entfernt wurden, um eine vollständige Analyse zu gewährleisten. Die Benutzeroberfläche (UI) der Anwendung ist mit fluidPage gestaltet, die eine Titelzeile und ein Hauptfeld enthält, in dem ein Boxplot dargestellt wird. Ein seitliches Bedienfeld bietet einen Schieberegler, mit dem Benutzer die Pinguine basierend auf der Flossenlänge filtern können. Dies ermöglicht eine dynamische und intuitive Untersuchung der Daten.

Im Server-Teil der Anwendung wird eine reaktive Funktion verwendet, um die Pinguindaten basierend auf den Benutzereingaben im Schieberegler zu filtern. Der gefilterte Datensatz wird dann verwendet, um einen Boxplot zu erstellen, der die Flossenlänge der Pinguine nach Art darstellt. Der Boxplot wird in Echtzeit aktualisiert, wenn der Benutzer die Filtereinstellungen anpasst. Diese interaktive Visualisierung hilft, Unterschiede in der Flossenlänge zwischen den Pinguinarten zu erkennen und bietet eine benutzerfreundliche Möglichkeit, die Daten zu erkunden. Durch die Kombination von Shiny und ggplot2 wird eine leistungsstarke und flexible Plattform zur Datenvisualisierung geschaffen, die sowohl für Bildungs- als auch für Forschungszwecke genutzt werden kann.
<table>
  <tr>
    <td align="center">Shiny App UI</td>
  </tr>
  <tr>
    <td valign="top"><img src="https://github.com/novendhireiner/datascience_portfolio/blob/main/R/Shiny%20App%20UI.png"></td>
  </tr>
 </table>
   </p>
<hr>

## SQL
#### [Training 1 - Erstellung der Datenbank](https://github.com/novendhireiner/datascience_portfolio/blob/main/SQL/Training%201%20-%20Datenbank.sql)   
   <p>
Auf dieses Skript befindet sich eine umfassende Lösung zur Erstellung und Verwaltung von zwei Tabellen für eine fiktive Firma: "Mitarbeiter" und "Abteilung". Das Ziel dieser Aufgabe ist es, eine robuste Datenbankstruktur zu entwerfen, die durch den Einsatz von Primärschlüsseln, Fremdschlüsseln, Indizes und Views effiziente und konsistente Datenverwaltung ermöglicht. Die Tabelle "Mitarbeiter" enthält die Spalten "ID", "Name" und "Abteilungs_ID", während die Tabelle "Abteilung" die Spalten "ID" und "Name" umfasst. Primärschlüssel werden für beide Tabellen festgelegt, um eindeutige Identifikatoren zu gewährleisten. Durch die Definition eines Fremdschlüssels in der Tabelle "Mitarbeiter", der auf die "ID" der Tabelle "Abteilung" verweist, wird eine relationale Verknüpfung hergestellt, die Datenintegrität und referenzielle Integrität sicherstellt.

Das beigefügte SQL-Skript demonstriert die Erstellung der Tabellen und das Einfügen von Beispieldaten. Die Wahl der Datentypen basiert auf den spezifischen Anforderungen jeder Spalte: "int" für numerische Identifikatoren und "varchar(255)" für textbasierte Namen. Diese Auswahl stellt sicher, dass die Tabellen sowohl flexibel als auch skalierbar sind. Die Beziehung zwischen den Tabellen wird durch den Fremdschlüssel "Abteilungs_ID" in der Tabelle "Mitarbeiter" realisiert, der auf die "ID" der Tabelle "Abteilung" verweist. Diese Struktur ermöglicht es, die Abteilungszugehörigkeit jedes Mitarbeiters effizient zu verfolgen. Optional können zusätzliche INSERT-Anweisungen verwendet werden, um die Funktionalität der Tabellen mit realistischen Beispieldaten zu demonstrieren, wodurch die Praktikabilität und Benutzerfreundlichkeit der Datenbanklösung verdeutlicht wird.
   </p>

#### [Training 2 - SQL-Ausdrücken](https://github.com/novendhireiner/datascience_portfolio/blob/main/SQL/Training%202%20-%20SQL%20Ausdrücken.sql)   
   <p>
In diesem Training präsentiere ich eine praxisorientierte Aufgabe zur Anwendung von SQL-Ausdrücken in einer Datenbank. Die Aufgabe besteht darin, zwei Tabellen für eine fiktive Firma zu erstellen: "Kunden" und "Bestellungen". Die Tabelle "Kunden" enthält die Spalten "KundenID", "Name" und "Land", während die Tabelle "Bestellungen" die Spalten "BestellID", "KundenID", "Produkt" und "Preis" umfasst. Nach der Erstellung der Tabellen werden einige Datensätze in beide Tabellen eingefügt, um eine realistische Datengrundlage zu schaffen. Im Anschluss wird eine SQL-Abfrage ausgeführt, um alle Kunden aus einem bestimmten Land, beispielsweise Deutschland, anzuzeigen.

Diese Aufgabe illustriert die grundlegenden Konzepte der relationalen Datenbankgestaltung, wie die Definition von Primär- und Fremdschlüsseln sowie das Einfügen von Beispieldaten. Der SQL-Code zeigt die Erstellung der Datenbank und Tabellen, das Einfügen von Datensätzen und die Ausführung einer Abfrage, um spezifische Informationen abzurufen. Diese Struktur ermöglicht es, die Beziehungen zwischen Kunden und ihren Bestellungen zu verwalten und gezielte Datenabfragen durchzuführen, die wertvolle Einblicke in die Kundenbasis und deren Bestellverhalten bieten. Die Aufgabe demonstriert die Effizienz und Flexibilität von SQL bei der Verwaltung und Analyse von Unternehmensdaten.
   </p>

#### [Training 3 - ER-Diagram]()   
   <p>
hier stelle ich eine Aufgabe vor, die sich mit der Erstellung und Verwaltung von Datenbanktabellen auf Basis eines ER-Diagramms befasst. 
<table>
  <tr>
    <td align="center">ER-Diagramm</td>
  </tr>
  <tr>
    <td valign="top"><img src="https://github.com/novendhireiner/datascience_portfolio/blob/main/SQL/3.%20ER-Diagramm.png"></td>
  </tr>
 </table>
Ziel der Aufgabe ist es, SQL-Anweisungen zu schreiben, um drei Tabellen zu erstellen: "Studierende", "Kurse" und "Einschreibungen". Diese Tabellen repräsentieren die Beziehungen zwischen Studierenden und den Kursen, in die sie eingeschrieben sind. Die Tabelle "Studierende" enthält die Spalten "Matrikelnummer", "Name" und "Email". Die Tabelle "Kurse" umfasst die Spalten "KursID", "Titel" und "Dozent". Die Verknüpfung zwischen diesen beiden Tabellen erfolgt über die Tabelle "Einschreibungen", die die Spalten "Matrikelnummer", "KursID" und "Semester" enthält. Nach der Erstellung der Tabellen werden einige Beispieldatensätze eingefügt, um die Funktionalität zu demonstrieren. Abschließend wird eine SELECT-Anweisung ausgeführt, die alle Studierenden und die von ihnen belegten Kurse anzeigt.

Diese Aufgabe illustriert die grundlegenden Konzepte der relationalen Datenbankmodellierung, einschließlich der Definition von Primär- und Fremdschlüsseln, der Dateneingabe und der Ausführung komplexer Abfragen. Durch die klare Struktur und die sorgfältige Gestaltung der Datenbanktabellen wird eine effiziente Verwaltung und Abfrage der Daten ermöglicht. Die bereitgestellten SQL-Skripte zeigen, wie man Datenbanken erstellt, Daten einfügt und Abfragen formuliert, um spezifische Informationen abzurufen. Diese Techniken sind essenziell für die Verwaltung von Studierenden- und Kursinformationen in einer universitären Umgebung und können leicht auf andere Anwendungsfälle übertragen werden.
   </p>

<hr>

## BI
#### [Power BI & Tableau](https://github.com/novendhireiner/datascience_portfolio/tree/main/BI) 
   <p>
   In meinem Portfolio für Business Intelligence habe ich zwei beeindruckende Projekte vorgestellt, die die Leistungsfähigkeit von Datenvisualisierungswerkzeugen demonstrieren: Power BI und Tableau.

Für Tableau stehen zwei Dateien zur Verfügung: Die erste Datei ist ein Umsatz- und Kostenbericht des Superstore-Datensatzes nach Kategorie, Segment, Produktname und Länderzuordnung. Die zweite Datei präsentiert einen Umsatzbericht mit der Verwendung der Ranglistenfunktion, um Einsichten zu gewinnen.

Bei Power BI gibt es ebenfalls zwei Dateien, beide befassen sich mit Verkaufsanalysen. Diese interaktiven Dashboards wurden entwickelt, um komplexe Daten in aussagekräftige Einblicke zu verwandeln. Mit Power BI und Tableau habe ich effektive Visualisierungen erstellt, die es den Benutzern ermöglichen, Daten intuitiv zu verstehen und fundierte Geschäftsentscheidungen zu treffen.
   </p>
