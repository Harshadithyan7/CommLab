import numpy as np 
import matplotlib.pyplot as plt 
from scipy.signal import convolve

numbits=10
oversampling_factor = 8
rolloff = 0.4
nums_taps=101
noise_variance = 0.1

message_bits= np.random.randint(0,2,numbits)
oversampled_signals=np.repeat(message_nrz,oversampling_factor)

def raised_cosine_filter(alpha,span,sps):
    t=np.linspace(-span/2,span/2,span*sps)
    h=np.zeros_like(t)
    for i,t_val in enumerate(t):
        h[i]=np.sinc(t_val)*np.cos(np.pi*alpha*t_val)/(1-(2*alpha*t_val)**2)
    return h/np.sqrt(np.sum(h**2))

pulse=raised_cosine_filter(rolloff,nums_taps//oversampling_factor, oversampling_factor)
baseband_signal=convolve(oversampled_signals,pulse,mode='same')

noise=np.sqrt(noise_variance)*np.random.randn(len(baseband_signal))
received_signal=baseband_signal+noise
matched_output=convolve(received_signal,pulse,mode='same')

samp