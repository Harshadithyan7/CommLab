import numpy as np 
import matplotlib.pyplot as plt

N=1000000
EbnodB=range(0,15)
ber=[]
for eb in EbnodB:
    Ebno=10**(eb/10)
    tx=2*(np.random.randn(N)>0.5)-1
    noise=np.random.randn(N)/np.sqrt(2*Ebno)
    rx=tx+noise
    rx_bits=np.sign(rx)
    errors=np.sum(tx!=rx_bits)
    ber.append(errors/N)
plt.semilogy(EbnodB,ber,label="simulation")
plt.grid()
plt.legend()
plt.show()