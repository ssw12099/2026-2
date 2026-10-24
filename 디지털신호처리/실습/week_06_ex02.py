import numpy as np
import matplotlib.pyplot as plt

# 시뮬레이션 파라미터
Fs = 1000
Ts = 1 / Fs
Ns = 2000

# 시간축 : 총 2초
t = np.arange(0, Ns) * Ts

# 기본 주파수
f0 = 1

# K 값
K_list = [1, 5, 11, 111]

plt.figure(figsize=(10, 9))

for i, K in enumerate(K_list):

    # 합성 신호 초기화
    y = np.zeros_like(t)

    # 홀수 고조파 더하기
    for k in range(1, K + 1, 2):
        y = y + (1 / k) * np.sin(2 * np.pi * k * f0 * t)

    # 사각파 크기를 ±1에 맞춤
    y = (4 / np.pi) * y

    # 그래프
    plt.subplot(4, 1, i + 1)
    plt.plot(t, y, 'b')
    plt.ylim(-1.5, 1.5)
    plt.xlim(0, 2)
    plt.grid()

    plt.ylabel('x(t)')
    plt.title('K = ' + str(K))

plt.xlabel('Time (sec)')
plt.tight_layout()
plt.show()