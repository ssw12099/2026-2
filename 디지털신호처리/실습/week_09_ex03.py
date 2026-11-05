
import numpy as np
import matplotlib.pyplot as plt

# 1. DFT 함수
def dfs(xn):
    N = len(xn)
    n = np.arange(N)
    k = np.arange(N)

    WN = np.exp(-1j*2*np.pi/N)
    kn = np.outer(k,n)
    WNkn = WN**kn

    return np.dot(WNkn,xn)


# 2. IDFT 함수
def idfs(Xk):
    N = len(Xk)
    n = np.arange(N)
    k = np.arange(N)

    WNast = np.exp(1j*2*np.pi/N)
    kn = np.outer(k,n)
    WNastkn = WNast**kn

    return np.dot(WNastkn,Xk)/N


# 3. 입력 신호
xn = np.array([1,2,3,4])

Xk = dfs(xn)
xnr = idfs(Xk)

print("원본:", xn)
print("DFT:", np.round(Xk,6))
print("IDFT:", np.round(xnr.real,6))


# 4. 그래프 3개를 한 창에 출력
n = np.arange(len(xn))

fig, ax = plt.subplots(1,3,figsize=(13,4))

ax[0].stem(n,xn)
ax[0].grid()
ax[0].set_title("Original x[n]")
ax[0].set_xlabel("n")

ax[1].stem(n,np.abs(Xk))
ax[1].grid()
ax[1].set_title("DFT |X[k]|")
ax[1].set_xlabel("k")

ax[2].stem(n,xnr.real)
ax[2].grid()
ax[2].set_title("Reconstructed x[n]")
ax[2].set_xlabel("n")

plt.tight_layout()
plt.show()
