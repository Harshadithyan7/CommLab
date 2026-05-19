import numpy as np
import matplotlib.pyplot as plt

T=1
fs=100
rolloff=0.7

g=lambda t: np.sinc(t)*np.cos(np.pi*rolloff*t)/(1-(2*rolloff*t)**2)

binary_seq=np.array([0,1,1,0,0,1,0,1,1,0,1,0,0,1,1,0])
j=binary_seq*2-1

t=np.arange(-2*T,(len(j)+2)*T, 1/fs)

y=sum(j[k]*g(t-k*T) for k in range (len(j)))

#Plotting
fig,a = plt.subplots(2,2)
a[0,1].plot(t,y)
a[0,1].set_title('Recieved Signal')
a[0,1].set_xlabel('Time(s)')
a[0,1].set_ylabel('Amplitude')

x=np.arange(-T,T,1/fs)
for i in range(2*fs, len(y)-3*fs,fs):
    a[1,1].plot(x,y[i:i+2*fs], color='blue')
a[1][1].set_title("Eye Diagram")
a[0][0].step(np.arange(len(binary_seq)),binary_seq)
a[0][0].set_title("input sequence")
t_imp=np.arange(-5,5,0.01)
a[1][0].plot(t_imp,g(t_imp))
a[1][0].set_title("impulse response")
plt.tight_layout()
plt.show()
