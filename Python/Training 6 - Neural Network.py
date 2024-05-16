import numpy as np
import numpy
import scipy

# Anzahl der Neuronen in den Schichten
input_neurons = 784
hidden_neurons = 100
output_neurons = 10

# Gewichtsmatrizen initialisieren
weights_input_hidden = np.random.uniform(-0.5, 0.5, (hidden_neurons, input_neurons))
weights_hidden_output = np.random.uniform(-0.5, 0.5, (output_neurons, hidden_neurons))

# Aktivierungsfunktion (zum Beispiel Sigmoid)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Signalübertragungsfunktion
def test(input_vector, weights_input_hidden, weights_hidden_output):
    hidden_input = np.dot(weights_input_hidden, input_vector)
    hidden_output = sigmoid(hidden_input)
    output_input = np.dot(weights_hidden_output, hidden_output)
    output_vector = sigmoid(output_input)
    return output_vector

# Beispiel-Datensatz (Input-Vektor mit 784 Pixeln)
input_vector = np.random.random(input_neurons)

# Signalübertragung durchführen
output_vector = test(input_vector, weights_input_hidden, weights_hidden_output)

# Ausgabe des ersten Elements des Output-Vektors
print(output_vector[0])

def train(input_list, w_ih, w_ho, target_list, learning_rate):
    input_vector = numpy.array(input_list, ndmin=2).T
    targets = numpy.array(target_list,ndmin=2).T

    #berechne den Inputvektor für das Hidden Layer
    input_hidden = numpy.dot(w_ih, input_vector)

    #berechne den Outputvektor aus dem Hidden Layer
    output_hidden = scipy.special.expit (input_hidden) 
    
    #berechne den Inputvektor für die Ausgangsschicht
    input_final = numpy.dot(w_ho, output_hidden)
    
    #berechne den Outputvektor der Ausgangsschicht
    output_final = scipy.special.expit (input_final)

    #Fehler an der Ausgangsschicht
    output_errors = targets - output_final

    #Fehler in der Hidden Layer
    hidden_errors = numpy.dot(w_ho. T, output_errors)
    
    #Aktualisierung Gewichte zwischen Hidden Layer und Ausgangsschicht
    w_ho += learning_rate * numpy.dot((output_errors*output_final* (1-output_final)),numpy.transpose(output_hidden))
    #Aktualisierung Gewichte zwischen Input Layer und Hidden Layer
    w_ih += learning_rate * numpy.dot((hidden_errors*output_hidden* (1-output_hidden)),numpy.transpose(input_vector))
