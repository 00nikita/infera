import torch

A = torch.tensor([
    [1.0, 2.0],
    [3.0, 4.0]
])

B = torch.tensor([
    [5.0, 6.0],
    [7.0, 8.0]
])

C = A @ B
D = A*B

print("A:")
print(A)

print("\nB:")
print(B)

print("\nA @ B:")
print(C)

print("\n A*B:")
print(D)