import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(x, t):
    return np.sin(t) * np.sin(x)

# Méthode de Runge-Kutta d'ordre 4
def rk4(v, M0, t):
    '''
    :param v: fonction connue
    :param M0: conditions initiales
    :param t: variable contenant les points de subdivision
    :return: Solution approchée selon t
    '''
    i = len(t)
    M = [M0]       # On stocke les valeurs initiales
    for n in range(0, i-1):
        h = t[n+1] - t[n]
        v1 = v(M[n], t[n])
        v2 = v(M[n] + h * v1 / 2, t[n] + h / 2)
        v3 = v(M[n] + h * v2 / 2, t[n] + h / 2)
        v4 = v(M[n] + h * v3, t[n+1])
        M.append(M[n] + h * (v1 + 2 * v2 + 2 * v3 + v4) / 6)
    return M

if __name__ == '__main__':
    t = np.linspace(0, 50, 256)
    x = rk4(f, 1, t)
    plt.plot(t, x)
    plt.title("solution de x'=sin(t)sin(x)")
    plt.show()
