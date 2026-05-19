import numpy as np
import matplotlib.pyplot as plt

b_max=int(input("Enter the max value of bits:"))
fm=100
fs=15*fm
dc=1

tm=np.arange(0,2/fm,0.0001)
xm=dc+np.sin(2*np.pi*fm*tm)

ts=np.arange(0,5/fm,1/fs)
xs=dc+np.sin(2*np.pi*fm*ts)

x_min=np.min(xm)
x_max=np.max(xm)
L=8
b_disp=3
l_disp=2**b_disp
q_levels=np.linspace(x_min,x_max,l_disp)


xq=[]
for s in xs:
    for q in q_levels:
        if s<=q:
            xq.append(q)
            break
xq=np.array(xq)

quantisation_noise=xs-xq

q_in=np.linspace(x_min,x_max,1000)
q_out=[]
for i in q_in:
    for q in q_levels:
        if i<=q:
            q_out.append(q)
            break
bits=range(1,b_max+1)
sqnr_calc=[]
sqnr_theory=[]
signal_power=((x_max-x_min)**2)/8

for b in bits:
    i=2**b
    step=(x_max-x_min)/i
    noise_pwr=step**2/12
    sqnr=signal_power/noise_pwr
    sqnr_calc.append(10*np.log10(sqnr))
    sqnr_theory.append(6*b+1.76)

plt.figure(figsize=(14,12))
plt.subplot(2,2,1)
plt.plot(tm,xm)
plt.title("original message signal")

plt.subplot(2,2,2)
plt.plot(ts,xs)
plt.title("sampled signal")

plt.subplot(2,2,3)
plt.plot(bits,sqnr_calc,'bo-',label='calculated sqnr')
plt.plot(bits,sqnr_theory,'rx-',label='theo sqnr')
plt.title('SQNR vs Number of bits')
plt.legend()
plt.grid()

plt.subplot(2,2,4)
plt.plot(q_in,q_out)
plt.tight_layout()
plt.show()