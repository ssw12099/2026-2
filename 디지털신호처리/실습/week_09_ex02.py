
import numpy as np
import matplotlib.pyplot as plt

# 한 화면에 그래프 2개 배치
fig, ax = plt.subplots(1, 2, figsize=(14, 5))


# 1. 정규화된 Sinc 함수
x = np.linspace(-6, 6, 1201)
y = np.sinc(x)

ax[0].plot(x, y, "blue")
ax[0].grid()
ax[0].set_xlabel("x")
ax[0].set_ylabel("sinc(x)")
ax[0].set_title("Normalized Sinc Function")


# 2. PDF의 X(w) 계산
w = np.arange(-2*np.pi, 2*np.pi, 0.1)
N = len(w)

Xw = np.zeros(N)
T = 1

for i in range(-int(N/2), int(N/2)):
    if i == 0:
        Xw[i+int(N/2)] = T
    else:
        Xw[i+int(N/2)] = np.sin(i*T/2)/(i/2)


# 3. 푸리에 변환 그래프
ax[1].plot(w, Xw, "blue")
ax[1].stem(w, Xw, "blue")
ax[1].grid()

ax[1].set_xlabel("w, in radians")
ax[1].set_ylabel("X(w)")
ax[1].set_title("Fourier Transform of a non-periodic signal")


# 그래프 간격 자동 조정
plt.tight_layout()

# 한 창에 출력
plt.show()
