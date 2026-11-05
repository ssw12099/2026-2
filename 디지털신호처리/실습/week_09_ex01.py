import numpy as np
import matplotlib.pyplot as plt

# PDF 실습 1~7번을 하나의 창(4행 x 2열)에 표시합니다.
# 복소지수 시퀀스(5번)는 실수부와 크기를 별도 칸에 나타냅니다.
fig, axes = plt.subplots(4, 2, figsize=(14, 13), constrained_layout=True)
axes = axes.ravel()


def draw_stem(ax, n, x, title, y_label="x(n)"):
    ax.stem(n, x, linefmt="b-", markerfmt="bo", basefmt="r-")
    ax.set_title(title, fontsize=12)
    ax.set_xlabel("n")
    ax.set_ylabel(y_label)
    ax.grid(True, alpha=0.45)


# 1. 이산 신호의 표현
n = [-3, -2, -1, 0, 1, 2, 3, 4]
xn = [2, 1, -1, 0, 1, 4, 3, 7]
draw_stem(axes[0], n, xn, "1. Discrete sequence")


# 2. 단위 임펄스 시퀀스
def impseq(n0, n1, n2):
    n = np.arange(n1, n2 + 1)
    return (n == n0).astype(int)


n1, n2 = 0, 20
n = np.arange(n1, n2 + 1)
draw_stem(axes[1], n, impseq(0, n1, n2), "2. Unit impulse sequence")


# 3. 단위 계단 시퀀스
def stepseq(n0, n1, n2):
    n = np.arange(n1, n2 + 1)
    return (n >= n0).astype(int)


draw_stem(axes[2], n, stepseq(0, n1, n2), "3. Unit step sequence")


# 4. 실수 지수 시퀀스
n = np.arange(20)
xn = 0.7 ** n
draw_stem(axes[3], n, xn, "4. Real exponential (a = 0.7)")


# 5. 복소지수 시퀀스 x(n) = exp((2 + j3)n)
n = np.linspace(0, 10, 100)
xn = np.exp((2 + 3j) * n)
draw_stem(axes[4], n, xn.real, "5-1. Complex exponential: real part", "Re{x(n)}")
draw_stem(axes[5], n, np.abs(xn), "5-2. Complex exponential: magnitude", "|x(n)|")
axes[4].ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
axes[5].ticklabel_format(axis="y", style="sci", scilimits=(0, 0))


# 6. 정현파 시퀀스 x(n) = 3cos(0.1*pi*n + pi/2)
n = np.linspace(0, 10 * np.pi, 100)
xn = 3 * np.cos(0.1 * np.pi * n + np.pi / 2)
draw_stem(axes[6], n, xn, "6. Sinusoidal sequence", "Amplitude")


# 7. 주기 시퀀스: [1,2,3,4,5,6,7]을 5회 반복
xn = [1, 2, 3, 4, 5, 6, 7] * 5
n = np.arange(len(xn))
draw_stem(axes[7], n, xn, "7. Periodic sequence", "Amplitude")

fig.suptitle("Discrete Signal Practice (1–7)", fontsize=17)
plt.show()
