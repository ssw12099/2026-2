import matplotlib.pyplot as plt
import numpy as np

sample_counts = [11, 21, 31]

for i, n in enumerate(sample_counts):
    t = np.linspace(0, 3*np.pi, n)
    x = np.sin(t)

    plt.subplot(3, 1, i+1)
    plt.plot(t, x)
    plt.title(f"Example of plot(t,x): {n}-points")
    plt.grid()

plt.tight_layout()
plt.show()