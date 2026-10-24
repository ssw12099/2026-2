import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-0.035, 0.045, 1000)

x = 20 * np.cos(2 * np.pi * 40 * t - 0.4 * np.pi)

plt.plot(t, x)

plt.title("x(t) = 20cos(2pi(40)t - 0.4pi)")
plt.xlabel("t (sec)")
plt.ylabel("x(t)")
plt.grid()

plt.xlim(-0.035, 0.045)

plt.tight_layout()
plt.show()