# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 15:23:09 2025

@author: Rufus
"""

import numpy as np
import matplotlib.pyplot as plt

fb = 5
fc = 20
fs = 30 * fc
Tb = 1 / fb      


x = [1, 0, 1, 1, 0] 

inp = np.array([2*val - 1 for val in x])

samples_per_bit = int(Tb * fs)
print(samples_per_bit)
t = np.arange(0, len(inp)*Tb, 1/fs)


nrz = np.repeat(inp, samples_per_bit)


carrier = np.sin(2 * np.pi * fc * t)


received_bpsk = nrz * carrier

noise = np.random.randn(len(received_bpsk))
bpsk_noise = received_bpsk+noise


demodulator_product = bpsk_noise * carrier
print(demodulator_product)

detected_bits = []
for i in range(len(x)):
    start = i * samples_per_bit
    end   = (i + 1) * samples_per_bit
    
    integration_value = np.sum(demodulator_product[start:end])
    
    if integration_value > 0:
        detected_bits.append(1)
    else:
        detected_bits.append(0)


detected_signal = np.repeat(detected_bits, samples_per_bit)


plt.figure(figsize=(9,7))

plt.subplot(5,1,1)
plt.plot(t, nrz, drawstyle='steps-post')
plt.title("Message Signal (Polar NRZ)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(5,1,2)
plt.plot(t, carrier)
plt.title("Carrier signal")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(5,1,3)
plt.plot(t, received_bpsk)
plt.title("BPSK Modulated Signal")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(5,1,5)
plt.plot(t, detected_signal, drawstyle='steps-post')
plt.title(" Detected Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(5,1,4)
plt.plot(t, bpsk_noise)
plt.title("Noise")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()

print("Detected bits:", detected_bits)