import matplotlib.pyplot as plt
import numpy as np

# z^6 = -8j
# z^6 + 8j = 0
z = np.roots([1, 0, 0, 0, 0, 0, 8j])

print(z)

fig, ax = plt.subplots(figsize=(7, 7))

# --------------------------------
# 1. 원의 반지름
# --------------------------------
# 8^(1/6) = sqrt(2)
r = np.sqrt(2)

# 원 그리기
circle = plt.Circle(
    (0, 0),
    r,
    fill=False,
    linewidth=2
)

ax.add_patch(circle)

# --------------------------------
# 2. 6개의 해를 점으로 표시
# --------------------------------
ax.scatter(
    z.real,
    z.imag,
    s=60,
    zorder=5
)

# --------------------------------
# 3. 원점에서 각 해까지 선
# --------------------------------
for root in z:
    ax.plot(
        [0, root.real],
        [0, root.imag],
        linewidth=1.5
    )

# --------------------------------
# 4. 슬라이드처럼 점선 표시
# (1, 1), (-1, -1)
# --------------------------------

# 오른쪽 위
ax.plot([1, 1], [0, 1], '--', linewidth=1)
ax.plot([0, 1], [1, 1], '--', linewidth=1)

# 왼쪽 아래
ax.plot([-1, -1], [0, -1], '--', linewidth=1)
ax.plot([0, -1], [-1, -1], '--', linewidth=1)

# --------------------------------
# 5. 숫자 표시
# --------------------------------
ax.text(1.02, 0.08, '1', fontsize=13)
ax.text(1.05, 0.75, '1', fontsize=13)

ax.text(-1.15, -0.12, '-1', fontsize=13)
ax.text(-0.85, -1.15, '-1', fontsize=13)

# sqrt(2) 표시
ax.text(
    0.45, 0.5,
    r'$\sqrt{2}$',
    fontsize=16,
    rotation=45
)

ax.text(
    -0.65, -0.55,
    r'$\sqrt{2}$',
    fontsize=16,
    rotation=45
)

# --------------------------------
# 6. x축, y축을 가운데로 이동
# --------------------------------
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# --------------------------------
# 7. 그래프 범위
# --------------------------------
ax.set_xlim(-1.8, 1.8)
ax.set_ylim(-1.8, 1.8)

# 원이 찌그러지지 않도록
ax.set_aspect('equal')

# 눈금 제거
ax.set_xticks([])
ax.set_yticks([])

# x, y 표시
ax.text(1.65, 0.05, 'x', fontsize=15)
ax.text(0.05, 1.65, 'y', fontsize=15)

ax.set_title(r'Roots of $z^6=-8j$', fontsize=16)

plt.show()