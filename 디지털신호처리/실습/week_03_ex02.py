# n 제곱 근 (5/5)

import matplotlib.pyplot as plt
import numpy as np

# z^6 = -8j
z = np.roots([1, 0, 0, 0, 0, 0, 8j])

fig, ax = plt.subplots(figsize=(7, 7))

# 반지름
r = np.sqrt(2)

# -------------------------
# 원 직접 그리기
# -------------------------
theta = np.linspace(0, 2*np.pi, 500)

x_circle = r * np.cos(theta)
y_circle = r * np.sin(theta)

ax.plot(x_circle, y_circle, color='black', linewidth=2)

# -------------------------
# 6개의 해 표시
# -------------------------
ax.scatter(z.real, z.imag, s=60, zorder=5)

# -------------------------
# 원점에서 각 해까지 선
# -------------------------
for root in z:
    ax.plot(
        [0, root.real],
        [0, root.imag],
        linewidth=1.5
    )

# -------------------------
# 점선
# -------------------------

# (1, 1)
ax.plot([1, 1], [0, 1], '--')
ax.plot([0, 1], [1, 1], '--')

# (-1, -1)
ax.plot([-1, -1], [0, -1], '--')
ax.plot([0, -1], [-1, -1], '--')

# -------------------------
# 숫자 표시
# -------------------------
ax.text(1.03, 0.08, '1', fontsize=13)
ax.text(1.05, 0.75, '1', fontsize=13)

ax.text(-1.18, -0.12, '-1', fontsize=13)
ax.text(-0.85, -1.15, '-1', fontsize=13)

# sqrt(2)
ax.text(
    0.45, 0.55,
    r'$\sqrt{2}$',
    fontsize=16,
    rotation=45
)

ax.text(
    -0.7, -0.65,
    r'$\sqrt{2}$',
    fontsize=16,
    rotation=45
)

# -------------------------
# x축, y축 가운데
# -------------------------
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# -------------------------
# 그래프 범위
# -------------------------
ax.set_xlim(-1.8, 1.8)
ax.set_ylim(-1.8, 1.8)

# ★ 중요: 원 찌그러짐 방지
ax.set_aspect('equal', adjustable='box')

# 눈금 제거
ax.set_xticks([])
ax.set_yticks([])

# x, y 표시
ax.text(1.65, 0.05, 'x', fontsize=15)
ax.text(0.05, 1.65, 'y', fontsize=15)

ax.set_title(r'Roots of $z^6=-8j$', fontsize=16)

plt.show()