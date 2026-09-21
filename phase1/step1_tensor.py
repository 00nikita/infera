import torch

print("\n--- Memory experiment ---")

x = torch.randn(1000, 1000)

print("Shape:", x.shape)
print("Dtype:", x.dtype)
print("Elements:", x.numel())
print("Bytes per element:", x.element_size())
print("Total bytes:", x.numel() * x.element_size())
print("Total MB:", (x.numel() * x.element_size()) / (1024 ** 2))