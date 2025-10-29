# ipp_simulation.py
import numpy as np
import matplotlib.pyplot as plt

def ipp_to_h2(lmbda, sigma1, sigma2):
    A = lmbda + sigma1 + sigma2
    disc = A**2 - 4*lmbda*sigma2
    sqrt_disc = np.sqrt(max(disc, 0))
    mu1 = 0.5 * (A + sqrt_disc)
    mu2 = 0.5 * (A - sqrt_disc)
    p = (lmbda - mu2) / (mu1 - mu2) if abs(mu1 - mu2) > 1e-12 else 0.5
    return p, mu1, mu2

def simulate_ipp(T, lmbda, sigma1, sigma2, seed=42):
    np.random.seed(seed)
    t, state = 0.0, 1
    arrivals = []
    while t < T:
        rate_out = sigma2 if state == 1 else sigma1
        rate_arr = lmbda if state == 1 else 0
        dt_arr = np.random.exponential(1/rate_arr) if rate_arr > 0 else np.inf
        dt_trans = np.random.exponential(1/rate_out)
        dt = min(dt_arr, dt_trans)
        if t + dt > T: break
        t += dt
        if dt_arr < dt_trans:
            arrivals.append(t)
        else:
            state = 1 - state
    return np.array(arrivals)

# === Exécution ===
if __name__ == "__main__":
    T, lmbda, sigma1, sigma2 = 50, 1.2, 0.6, 0.3
    arrivals = simulate_ipp(T, lmbda, sigma1, sigma2)
    inter = np.diff(np.concatenate(([0], arrivals)))
    p, mu1, mu2 = ipp_to_h2(lmbda, sigma1, sigma2)

    plt.figure(figsize=(10, 4))
    plt.hist(inter, bins=50, density=True, alpha=0.7, label="Empirique")
    x = np.linspace(0, inter.max(), 300)
    plt.plot(x, p*mu1*np.exp(-mu1*x) + (1-p)*mu2*np.exp(-mu2*x), 'r-', lw=2, label="H₂ théorique")
    plt.title("IPP : Inter-arrivées vs H₂")
    plt.xlabel("Temps"); plt.ylabel("Densité"); plt.legend()
    plt.tight_layout()
    plt.savefig("figures/ipp_h2.png")
    plt.show()
