
import numpy as np
import matplotlib.pyplot as plt

# 입력 신호
N = 128
n = np.arange(N)

xn = np.cos(0.48*np.pi*n) + np.cos(0.52*np.pi*n)

# FFT 및 IFFT
Xk = np.fft.fft(xn, N)
magXk = np.abs(Xk)

n1 = n[:int(N/2)]
magXk1 = magXk[:int(N/2)]

xnr = np.fft.ifft(Xk).real

# 그래프 3개를 한 창에 출력
fig, ax = plt.subplots(3, 1, figsize=(11, 9))

ax[0].stem(n, xn, "blue")
ax[0].grid()
ax[0].set_ylabel("Input x(n)")
ax[0].set_title("Input sequence x(n)")

ax[1].stem(n1, magXk1, "green")
ax[1].grid()
ax[1].set_ylabel("|X(k)|")
ax[1].set_title("FFT Spectrum")

ax[2].stem(n, xnr, "green")
ax[2].grid()
ax[2].set_ylabel("Reconstructed xr(n)")
ax[2].set_xlabel("n")
ax[2].set_title("IFFT")

plt.tight_layout()
plt.show()
