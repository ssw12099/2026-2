from numpy import cos, pi, linspace
import matplotlib.pyplot as plt
from numpy.fft import rfft

n = linspace(0, 512/8000., 512)

dtmf_1 = cos(697*2*pi*n) + cos(1209*2*pi*n)
dtmf_5 = cos(770*2*pi*n) + cos(1336*2*pi*n)
dtmf_9 = cos(852*2*pi*n) + cos(1477*2*pi*n)

DTMF_1 = rfft(dtmf_1)
DTMF_5 = rfft(dtmf_5)
DTMF_9 = rfft(dtmf_9)

plt.subplot(321)
plt.plot(dtmf_1[0:100])

plt.subplot(322)
plt.plot(abs(DTMF_1[0:256]))

plt.subplot(323)
plt.plot(dtmf_5[0:100])

plt.subplot(324)
plt.plot(abs(DTMF_5[0:256]))

plt.subplot(325)
plt.plot(dtmf_9[0:100])

plt.subplot(326)
plt.plot(abs(DTMF_9[0:256]))

plt.show()