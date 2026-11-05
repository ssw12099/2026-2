
import numpy as np

# 1. 벡터와 행렬 생성
a = np.array([0, 1, 2, 3])
b = np.arange(10).reshape(2, 5)

print("벡터:", a)
print("행렬:\n", b)
print("shape:", b.shape)
print("ndim:", b.ndim)
print("size:", b.size)
print("b[1,2]:", b[1,2])

# 2. 행렬 사칙연산
a = np.array([[1,2,3],[3,2,5]])
b = np.array([[-1,3,5],[1,4,2]])

print("\nA+B:\n", a+b)
print("A-B:\n", a-b)
print("A*B:\n", a*b)
print("A/B:\n", a/b)

# 3. 행렬곱
c = np.array([1,2,3,3,2,5]).reshape(3,2)

print("\nA*C:\n", np.dot(a,c))
print("B*C:\n", np.dot(b,c))

# 4. 전치행렬을 이용한 곱
print("\nA*B.T:\n", np.dot(a,b.T))
print("A.T*B:\n", np.dot(a.T,b))

# 5. 벡터 전치, 공액 복소수, 내적
x = np.array([1+2j, 3+4j])
y = np.array([2+0j, 0+1j])

print("\n공액 복소수:", np.conjugate(x))
print("전치:\n", x.reshape(1,-1).T)
print("복소수 내적:", np.vdot(x,y))
