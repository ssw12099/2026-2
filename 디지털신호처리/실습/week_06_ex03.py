import numpy as np
import matplotlib.pyplot as plt

# 시간축
t = np.linspace(0, 3, 1000)

K = 7

# 정현파 성분
x1 = (8 / np.pi**2) * np.cos(2 * np.pi * t)

x2 = (8 / np.pi**2) * (1 / 3**2) * np.cos(2 * np.pi * 3 * t)

x3 = (8 / np.pi**2) * (1 / 5**2) * np.cos(2 * np.pi * 5 * t)

# 삼각파 = 정현파의 합
x = x1 + x2 + x3


plt.figure(figsize=(10, 7))

# x(t)
plt.subplot(4, 1, 1)
plt.plot(t, x, 'b')
plt.title('A periodic triangle signal x(t)=x1(t)+x2(t)+x3(t)')
plt.ylabel('x(t)')
plt.ylim(-2, 2)
plt.grid(True)

# x1(t)
plt.subplot(4, 1, 2)
plt.plot(t, x1, 'b')
plt.ylabel('x1(t)')
plt.ylim(-2, 2)
plt.grid(True)

# x2(t)
plt.subplot(4, 1, 3)
plt.plot(t, x2, 'b')
plt.ylabel('x2(t)')
plt.ylim(-2, 2)
plt.grid(True)

# x3(t)
plt.subplot(4, 1, 4)
plt.plot(t, x3, 'b')
plt.ylabel('x3(t)')
plt.xlabel('t')
plt.ylim(-2, 2)
plt.grid(True)

plt.tight_layout()
plt.show()