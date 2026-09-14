import torch

a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])
c = a + b

print("a:", a)
print("b:", b)
print("c:", c)
print("Shape:", c.shape)
print("Dtype:", c.dtype)
print("Device:", c.device)