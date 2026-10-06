# n 제곱 근 (4/5)

import matplotlib.pyplot as plt
import numpy as np

# z^4 = -64  ->  z^4 + 64 = 0
z = np.roots([1, 0, 0, 0, 64])

fig, ax = plt.subplots(figsize=(7, 7))

# -----------------------------
# 1. 원 그리기
# -----------------------------
r = 2 * np.sqrt(2)

circle = plt.Circle(
    (0, 0),          # 원의 중심
    r,               # 반지름
    fill=False,       # 안쪽 색칠 X
    linewidth=2
)
ax.add_patch(circle)

# -----------------------------
# 2. 해 4개 점으로 표시
# -----------------------------
ax.scatter(z.real, z.imag, s=60, zorder=5)

# -----------------------------
# 3. 원점에서 각 해까지 선 그리기
# -----------------------------
for root in z:
    ax.plot(
        [0, root.real],
        [0, root.imag],
        linewidth=1.5
    )

# -----------------------------
# 4. 세로 점선
# -----------------------------
ax.plot([2, 2], [0, 2], '--', linewidth=1)
ax.plot([2, 2], [0, -2], '--', linewidth=1)

ax.plot([-2, -2], [0, 2], '--', linewidth=1)
ax.plot([-2, -2], [0, -2], '--', linewidth=1)

# -----------------------------
# 5. 좌표 이름 표시
# -----------------------------
ax.text(2.1, 2.15, r'$(2\sqrt{2},\ \frac{\pi}{4})$', fontsize=13)
ax.text(-3.8, 2.15, r'$(2\sqrt{2},\ \frac{3\pi}{4})$', fontsize=13)

ax.text(-3.8, -2.5, r'$(2\sqrt{2},\ \frac{5\pi}{4})$', fontsize=13)
ax.text(2.1, -2.5, r'$(2\sqrt{2},\ \frac{7\pi}{4})$', fontsize=13)

# -----------------------------
# 6. 실수부/허수부 2, -2 표시
# -----------------------------
ax.text(2, 0.15, '2', fontsize=12)
ax.text(-2.2, 0.15, '-2', fontsize=12)

ax.text(0.15, 2, '2', fontsize=12)
ax.text(0.15, -2.2, '-2', fontsize=12)

# -----------------------------
# 7. x축, y축 중앙으로
# -----------------------------
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# -----------------------------
# 8. 그래프 설정
# -----------------------------
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)

# 원이 찌그러지지 않도록
ax.set_aspect('equal')

ax.set_title(r'Roots of $z^4=-64$', fontsize=16)

plt.show()