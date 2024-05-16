import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import accuracy_score
from torch.utils.data import DataLoader, TensorDataset

# Annahmen über die Daten und Hyperparameter
input_size = 784  
hidden_size = 128  
output_size = 10  
learning_rate = 0.001
num_epochs = 10


# Annahme: Testdaten für Torch-Tensoren
num_test_samples = 1000  
input_data = torch.randn(num_test_samples, input_size)  

# Annahme: Trainingsdaten und Labels sind in Torch-Tensoren
train_data = torch.randn(1000, input_size) 
train_labels = torch.randint(0, output_size, (1000,)) 

# Erstellen eines DataLoader für die Trainingsdaten
batch_size = 32 
train_dataset = TensorDataset(train_data, train_labels)
train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

# ground_truth_labels entsprechen den tatsächlichen Labels Ihrer Trainingsdaten
ground_truth_labels = train_labels.numpy()  # Konvertieren in Numpy-Array


# Daten laden und vorverarbeiten
# Definition des Neural Network
class NeuralNetwork(nn.Module):
    def __init__(self, activation=None, param=None):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)

        if activation == 'leaky_relu':
            self.activation = nn.LeakyReLU(negative_slope=param if param is not None else 0.01)
        elif activation == 'prelu':
            self.activation = nn.PReLU()
        elif activation == 'elu':
            self.activation = nn.ELU(alpha=param if param is not None else 1.0)
        else:
            self.activation = nn.Sigmoid()

    def forward(self, x):
        x = self.fc1(x)
        x = self.activation(x)
        x = self.fc2(x)
        return x

def train_and_evaluate(model, dataloader, ground_truth_labels):
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=learning_rate)

    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0

        for inputs, labels in dataloader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()

        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {running_loss:.4f}")

    model.eval()
    predictions = torch.argmax(model(input_data), dim=1)
    accuracy = accuracy_score(ground_truth_labels, predictions)
    return accuracy

# Trainieren und evaluieren mit Sigmoid
sigmoid_model = NeuralNetwork()
sigmoid_accuracy = train_and_evaluate(sigmoid_model, train_dataloader, ground_truth_labels)
print("Accuracy with Sigmoid:", sigmoid_accuracy)
print('\n')

# Trainieren und evaluieren mit Leaky ReLU für verschiedene Parameter
leaky_relu_params = [0.01, 0.05, 0.1, 0.5]
for param in leaky_relu_params:
    leaky_relu_model = NeuralNetwork(activation='leaky_relu', param=param)
    leaky_relu_accuracy = train_and_evaluate(leaky_relu_model, train_dataloader, ground_truth_labels)
    print(f"Accuracy with Leaky ReLU (param={param}):", leaky_relu_accuracy)
    print('\n')

# Trainieren und evaluieren mit PreLU
prelu_model = NeuralNetwork(activation='prelu')
prelu_accuracy = train_and_evaluate(prelu_model, train_dataloader, ground_truth_labels)
print("Accuracy with PreLU:", prelu_accuracy)
print('\n')

# Trainieren und evaluieren mit ELU für verschiedene Parameter
elu_params = [0.1, 0.2, 0.3]
for param in elu_params:
    elu_model = NeuralNetwork(activation='elu', param=param)
    elu_accuracy = train_and_evaluate(elu_model, train_dataloader, ground_truth_labels)
    print(f"Accuracy with ELU (param={param}):", elu_accuracy)
    print('\n')
