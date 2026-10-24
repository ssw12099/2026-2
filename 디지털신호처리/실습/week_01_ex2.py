import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-0.01, 0.02, 1000)

# f0 = 0 Hz
x1 = 5 * np.cos(2 * np.pi * 0 * t)

plt.subplot(3, 1, 1)
plt.plot(t, x1)
plt.title("0 Hz")
plt.ylabel("x(t)")
plt.xlim(-0.01, 0.02)
plt.ylim(-6, 6)
plt.grid()


# f0 = 100 Hz
x2 = 5 * np.cos(2 * np.pi * 100 * t)

plt.subplot(3, 1, 2)
plt.plot(t, x2)
plt.title("100 Hz")
plt.ylabel("x(t)")
plt.xlim(-0.01, 0.02)
plt.ylim(-6, 6)
plt.grid()


# f0 = 200 Hz
x3 = 5 * np.cos(2 * np.pi * 200 * t)

plt.subplot(3, 1, 3)
plt.plot(t, x3)
plt.title("200 Hz")
plt.xlabel("time t (sec)")
plt.ylabel("x(t)")
plt.xlim(-0.01, 0.02)
plt.ylim(-6, 6)
plt.grid()

plt.tight_layout()
plt.show()