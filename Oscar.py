import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

num_samples = 2000
input_size = 10
output_size = 1

"""Create a random dataset for regression"""
X = np.random.rand(num_samples, input_size).astype(np.float32)
y = np.random.rand(num_samples, output_size).astype(np.float32)

split_ratio = 0.75
split_idx = int(num_samples * split_ratio)

X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]

"""Now we convert the data into the tensor format using PyTorch"""
X_train_tensor = torch.from_numpy(X_train)
y_train_tensor = torch.from_numpy(y_train)
X_test_tensor = torch.from_numpy(X_test)
y_test_tensor = torch.from_numpy(y_test)

"""Now we implement the CNN class"""
"""
Notes about x = x.unsqueeze(1):
    In PyTorch, the unsqueeze() method is used to add a new dimension to a tensor x at a specified position.
    This operation increases the dimensionality of the tensor by one.

    In other words, the above method is used to insert a dimension at a specified index along the tensor.
    For example, x = x.unsqueeze(1) adds a new dimension at index 1 (the second) of the tensor x.

    If x is a 1D tensor (a vector) of shape (batch_size,), calling x.unsqueeze(1) would transform it into a 
    2D tensor (matrix) of shape (batch_size, 1). This operation effectively adds a new dimension to the tensor, 
    turning it into a column vector.

    Mohammad used x = x.unsqueeze(1):
        This operation is often necessary in neural network architectures, especially when dealing with 
        convolutional neural networks or when tensor shapes need to be compatible with certain operations or 
        layers that expect specific input shapes. In CNNs, for example, adding extra dimensions might be necessary 
        to ensure the input tensor conforms to the expected input shapes for convolutional operations, which often 
        involve working with multi-dimensional data such as images or 1D sequences.  
"""
flatten_ratio = 8


class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv1d(1, 16, kernel_size=3)  # Adjust input channels to 1
        self.fc1 = nn.Linear(16 * flatten_ratio, output_size)

    def forward(self, x):
        """We want to add a new channel dimension"""
        x = x.unsqueeze(1)
        x = self.conv1(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        return x


model = CNN()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

num_epochs = 10
batch_size = 16

for epoch in range(num_epochs):
    for i in range(0, len(X_train_tensor), batch_size):
        inputs = X_train_tensor[i:i + batch_size]
        targets = y_train_tensor[i:i + batch_size]

        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()

        print(f"Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item()}")

"""For model evaluation"""
with torch.no_grad():
    predicted = model(X_test_tensor)
    test_loss = criterion(predicted, y_test_tensor)  # Fixed variable name
    print(f"Test Loss: {test_loss.item()}")


"""How to use this model in real life after training"""
input_sample = torch.randn(1, input_size).float()
input_sample_redim = input_sample.unsqueeze(0).unsqueeze(0)
with torch.no_grad():
    model.eval()
    output_example = model(input_sample)

print("Random input tensor: ")
print(input_sample)
print("\nOutput prediction for Maria:")
print(output_example)

if output_example.numel() == 1: # if output tensor has a single value
    output_float = output_example.item()
else:
    output_float = output_example[0][0].item() # get the first element if the output is small

print("Predicted output Converted to float is", output_float)

"""
numel function is pytorch is a short form for thr phrase "number of elements". It's a method that
returns the total number of elements in a tensor.

For instance if you have a tensor example with a shape of (2, 3, 4) calling tensor_example.numel() woul
return 24 because there are a total of 24 elements in the tensor (2*3*4=24)
"""