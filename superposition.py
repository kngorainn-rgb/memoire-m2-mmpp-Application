# superposition.py
import numpy as np

def kronecker_sum(Q1, Q2, L1, L2):
    I1, I2 = np.eye(Q1.shape[0]), np.eye(Q2.shape[0])
    Q = np.kron(Q1, I2) + np.kron(I1, Q2)
    L = np.kron(L1, I2) + np.kron(I1, L2)
    return Q, L

# === Exemple ===
Q1 = np.array([[-0.25, 0.25], [2.0, -2.0]])
L1 = np.diag([2, 10])
Q2 = np.array([[-0.02, 0.02], [0.1, -0.1]])
L2 = np.diag([5, 20])

Q, L = kronecker_sum(Q1, Q2, L1, L2)
print("Q (4x4) :\n", np.round(Q, 3))
print("Λ (diag) :", np.diag(L))
print("Norme L2 vs théorie : à implémenter dans simulation")
