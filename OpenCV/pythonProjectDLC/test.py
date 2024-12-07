import torch

matrix_tensor = torch.tensor([[1, 2]])
print("matrix_tensor:", matrix_tensor.shape)

print('------------------------')
print(matrix_tensor.squeeze(0))

print('------------------------')
print(matrix_tensor.unsqueeze(1))