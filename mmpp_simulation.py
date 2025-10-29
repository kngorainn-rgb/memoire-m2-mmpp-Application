# mmpp_simulation.py
import numpy as np
from scipy.linalg import expm
import matplotlib.pyplot as plt

class TwoStateMMPP:
    def __init__(self, sigma1=1.0, sigma2=2.0, lambda1=3.0, lambda2=4.0):
        self.sigma1, self.sigma2 = sigma1, sigma2
        self.lambda1, self.lambda2 = lambda1, lambda2
        self.Q = np.array([[-sigma1, sigma1], [sigma2, -sigma2]])
        self.Lambda = np.diag([lambda1, lambda2])
        self.M = self.Q - self.Lambda
        self.F_inf = -np.linalg.inv(self.M) @ self.Lambda
        self.pi = np.array([sigma2, sigma1]) / (sigma1 + sigma2)
        self.p = (self.pi * [lambda1, lambda2]) / (self.pi @ [lambda1, lambda2])

    def simulate(self, T=1000, seed=42):
        np.random.seed(seed)
        t, state = 0.0, 0
        times, states, arrivals = [0.0], [state], []
        while t < T:
            rate_out = self.sigma1 if state == 0 else self.sigma2
            rate_arr = self.lambda1 if state == 0 else self.lambda2
            dt_arr = np.random.exponential(1/rate_arr) if rate_arr > 0 else np.inf
            dt_trans = np.random.exponential(1/rate_out)
            dt = min(dt_arr, dt_trans)
            if t + dt > T: break
            t += dt
            if dt_arr < dt_trans:
                arrivals.append(t)
            else:
                state = 1 - state
            times.append(t); states.append(state)
        return np.array(times), np.array(states), np.array(arrivals)

    def F_t(self, t):
        return (np.eye(2) - expm(self.M * t)) @ self.F_inf

# === Exécution ===
if __name__ == "__main__":
    mmpp = TwoStateMMPP()
    times, states, arrivals = mmpp.simulate(T=1000)
    print(f"Événements : {len(arrivals)} | États finaux : {states[-1]}")
    print(f"F(∞) théorique :\n{mmpp.F_inf}")
    print(f"p théorique : {mmpp.p}")
    # Figure
    plt.figure(figsize=(10, 3))
    plt.step(times, states, where='post')
    plt.title("Trajectoire MMPP simulée")
    plt.xlabel("Temps"); plt.ylabel("État")
    plt.yticks([0, 1])
    plt.tight_layout()
    plt.savefig("figures/mmpp_traj.png")
    plt.show()
