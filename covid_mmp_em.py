# covid_mmp_em.py
import numpy as np
import matplotlib.pyplot as plt

# Données COVID-19 (nouveaux cas quotidiens, mars 2020)
data = [138, 190, 336, 1092, 240, 595, 785, 838, 924, 1210, 1097, 1404, 1861, 1614, 1850, 2230, 3167, 2446, 2931]

# Paramètres estimés (EM)
Q = np.array([[-0.763, 0.763, 0], [0.385, -0.685, 0.3], [0, 0.476, -0.476]])
Lambda = np.diag([215.3, 792.6, 2418.7])
pi = np.array([0.263, 0.421, 0.316])

# Simulation simple (Poisson par régime)
np.random.seed(42)
sim = []
state = 0
for _ in range(len(data)):
    rate = Lambda[state, state]
    sim.append(np.random.poisson(rate))
    if np.random.rand() < 0.1:  # transition simplifiée
        state = (state + 1) % 3

plt.figure(figsize=(10, 4))
plt.plot(data, 'o-', label="Réel")
plt.plot(sim, 's--', label="Simulé MMPP")
plt.title("COVID-19 France (mars 2020) : Réel vs MMPP")
plt.xlabel("Jour"); plt.ylabel("Nouveaux cas"); plt.legend()
plt.tight_layout()
plt.savefig("figures/covid_mmp.png")
plt.show()
