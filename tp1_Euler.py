import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(x, t):
    return np.sin(t) * np.sin(x)

def euler(f, x0, t):
    n = len(t)
    x = [x0]
    for k in range(0, n-1):
        h = t[k+1] - t[k]
        p1 = f(x[k], t[k])
        x.append(x[k] + h * p1)
    return x


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    t = np.linspace(0, 50, 256)
    #x = odeint(f, 1, t)     # permet d’obtenir une résolution numérique de référence pour une Equa Diff
    #plt.plot(t, x)
    #plt.title("solution de x'=sin(t)sin(x)")
    #plt.show()

    x1 = euler(f, 1, t)
    #plt.plot(t, x, '−−', label='Solution exacte')
    plt.plot(t, x1, label="Méthode d'Euler")
    plt.title("Méthode d'Euler")
    plt.legend(loc='upper left')
    plt.show()