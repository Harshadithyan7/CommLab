import numpy as np
import matplotlib.pyplot as plt 

N=50 #number of bits
L=16 #oversampling factor
Fc=40 #carrier frequency
Fs=L*Fc #sampling frequency

bits=np.random.randint(2,size=N)
data=np.repeat(bits,L) #upsampling
odd=bits[0::2] #odd bits    
even=bits[1::2] #even bits
nrz1=2*odd -1 #NRZ for odd bits
odd_upsampled=np.repeat(nrz1,L) #upsampling for odd bits
nrz2=2*even -1 #NRZ for even bits
even_upsampled=np.repeat(nrz2,L) #upsampling for even bits

t=np.arange(len(odd_upsampled))/Fs #time vector
carrier_cos=np.cos(2*np.pi*Fc*t)
carrier_sin=np.sin(2*np.pi*Fc*t)

#Modulated signals
bpsk1=odd_upsampled*carrier_cos #modulated signal for odd bits
bpsk2=even_upsampled*carrier_sin #modulated signal for even bits
qpsk_signal=bpsk1 + bpsk2 #QPSK signal

#Plotting
plt.figure(figsize=(12,6))
plt.subplot(4,1,1)
plt.title("QPSK time domain signal")
plt.plot(t,qpsk_signal)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(4,1,2)
plt.title("Data")
plt.plot(data)
plt.xlabel("Bit index")
plt.ylabel("Bit value")
plt.grid()

plt.subplot(4,1,3)
plt.title("odd bits after nrz encoding and upsampling")
plt.plot(odd_upsampled)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.grid()

plt.subplot(4,1,4)
plt.title("Constellation diagram")
plt.scatter(nrz1,nrz2,color='magenta')
plt.xlabel("in-phase")
plt.ylabel("quadrature")
plt.grid()
plt.tight_layout()
plt.show()