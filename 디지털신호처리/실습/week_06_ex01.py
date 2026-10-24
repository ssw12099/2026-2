import numpy as np
import matplotlib.pyplot as plt

# 시뮬레이션 파라미터 설정
Fs = 100            # 샘플링 주파수 = 100 Hz
Ts = 1 / Fs         # 샘플링 주기(간격) = 0.01 sec
Ns = 300            # 샘플의 개수, 300 샘플

# X(시간축) 값
x0 = np.arange(0, Ns) * Ts
# 시간 축은 0.01초 * 300 샘플 = 전체 3초


# Y(크기) 값
y1t = 1.0 * np.sin(2 * np.pi * 1 * x0)      # 크기 1,   주파수 1 Hz
y2t = 1/3 * np.sin(2 * np.pi * 3 * x0)      # 크기 1/3, 주파수 3 Hz
y3t = 1/5 * np.sin(2 * np.pi * 5 * x0)      # 크기 1/5, 주파수 5 Hz

# 고조파 관계에 있는 3개 신호의 합
y0t = y1t + y2t + y3t


# 그래프 그리기
plt.subplot(4, 1, 1)
plt.plot(x0, y0t, 'b')
plt.ylim(-1, 1)
plt.grid()
plt.ylabel('x(t)')
plt.title('A periodic rectangular signal x(t)=x1(t)+x2(t)+x3(t)')


plt.subplot(4, 1, 2)
plt.plot(x0, y1t, 'b')
plt.ylim(-1, 1)
plt.grid()
plt.ylabel('x1(t)')


plt.subplot(4, 1, 3)
plt.plot(x0, y2t, 'b')
plt.ylim(-1, 1)
plt.grid()
plt.ylabel('x2(t)')


plt.subplot(4, 1, 4)
plt.plot(x0, y3t, 'b')
plt.ylim(-1, 1)
plt.grid()
plt.ylabel('x3(t)')


plt.show()