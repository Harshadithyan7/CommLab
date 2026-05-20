# CommLab - Communications Engineering Lab

A comprehensive Python library for digital communications and signal processing experiments. This repository contains implementations of fundamental communication systems concepts including modulation schemes, channel simulation, matched filtering, and quantization analysis.

## Overview

CommLab is an educational resource designed for students and professionals studying digital communications engineering. It provides practical implementations of key communication theory concepts with visualization tools to understand signal behavior and system performance.

## Repository Structure

```
CommLab/
├── qpsk.py                # QPSK Modulation demonstration
├── bpskber.py             # BPSK Bit Error Rate (BER) simulation
├── berqpsk.py             # QPSK BER simulation
├── bppsk.py               # BPSK Performance simulation
├── pcm.py                 # Pulse Code Modulation (PCM) with quantization
├── eyediag.py             # Eye diagram visualization using raised cosine filter
├── matchedfilter.py       # Matched filter receiver implementation
└── README.md              # This file
```

## Features

### Digital Modulation
- **QPSK (Quadrature Phase Shift Keying)**: 4-level modulation with I/Q components
- **BPSK (Binary Phase Shift Keying)**: 2-level phase modulation
- Time-domain and frequency-domain visualizations

### Channel & Receiver
- **AWGN Channel Simulation**: Realistic noise for performance evaluation
- **Matched Filter**: Optimal receiver for AWGN channels
- **Pulse Shaping**: Raised cosine filter with configurable roll-off factor
- **Eye Diagram**: Visual analysis of signal quality

### Analysis & Metrics
- **Bit Error Rate (BER)**: Theoretical vs. simulated performance curves
- **Signal-to-Quantization Noise Ratio (SQNR)**: Quantization performance analysis
- **PCM Sampling & Quantization**: Complete digital signal chain

## Scripts & Their Functions

### 1. **qpsk.py** - QPSK Modulation
Demonstrates QPSK modulation where each symbol carries 2 bits.
- Splits input bits into I (odd) and Q (even) channels
- Modulates with cos and sin carriers
- Visualizes original signal, bit sequence, and component signals

**Key Parameters:**
- N=50 bits
- Oversampling factor (L=16)
- Carrier frequency (Fc=40 Hz)

**Output:** 4 subplots showing data, NRZ encoding, and modulated QPSK signal

---

### 2. **bpskber.py** - BPSK Bit Error Rate
Simulates BER performance of BPSK over AWGN channel.
- Tests across Eb/N0 range of 0-15 dB
- Generates 1 million random bits for statistical accuracy
- Plots simulated BER curve for system evaluation

**Key Parameters:**
- N=1,000,000 bits per SNR point
- Eb/N0 range: 0-15 dB

**Output:** Logarithmic BER vs. Eb/N0 plot

---

### 3. **berqpsk.py** - QPSK Bit Error Rate
Similar to BPSK BER but for QPSK modulation (4-level signaling).
- Evaluates performance of 2 bits per symbol
- Compares simulated vs. theoretical BER
- Demonstrates coding gain opportunities

**Key Parameters:**
- Multiple QPSK configurations
- SNR sweep for performance curves

**Output:** BER comparison plot

---

### 4. **bppsk.py** - BPSK Simulation
Complete BPSK transceiver chain simulation.
- Bit generation and NRZ encoding
- BPSK modulation and demodulation
- AWGN channel impairment
- Symbol and bit-level visualization

**Output:** Transmitter/receiver constellation and time-domain waveforms

---

### 5. **pcm.py** - Pulse Code Modulation
Comprehensive PCM system including sampling, quantization, and analysis.
- Samples sinusoidal message signal at Nyquist rate
- Uniform quantizer with configurable bit depth
- Calculates Signal-to-Quantization Noise Ratio (SQNR)
- Compares calculated vs. theoretical SQNR

**Key Parameters:**
- Message frequency (fm=100 Hz)
- Sampling frequency (fs=1500 Hz = 15×fm)
- Quantization bit depths from 1 to user-defined max

**Output:** Original signal, sampled signal, quantization levels, SQNR analysis

---

### 6. **eyediag.py** - Eye Diagram
Visualizes signal quality through eye diagram analysis.
- Uses raised cosine pulse shaping filter
- Demonstrates inter-symbol interference (ISI) effects
- Provides impulse response visualization
- Shows binary sequence and received signal

**Key Parameters:**
- Symbol duration (T=1 s)
- Sampling rate (fs=100 Hz)
- Roll-off factor (α=0.7)

**Output:** Input sequence, impulse response, received signal, eye diagram

---

### 7. **matchedfilter.py** - Matched Filter Receiver
Complete digital communication receiver using matched filtering.
- Bit generation and NRZ mapping
- Raised cosine pulse shaping
- AWGN channel simulation
- Matched filter detection
- Symbol timing and decision

**Signal Chain:**
1. Bit generation
2. Upsampling
3. Pulse shaping (raised cosine)
4. Channel (AWGN noise)
5. Matched filtering
6. Sampling at optimal time
7. Threshold decision

**Output:** Pulse shape, transmitted/received signals, matched filter output, detected bits

---

## Installation

### Prerequisites
- Python 3.6+
- NumPy
- Matplotlib
- SciPy (for matchedfilter.py)

### Setup

```bash
# Clone repository
git clone https://github.com/Harshadithyan7/CommLab.git
cd CommLab

# Install dependencies
pip install numpy matplotlib scipy
```

## Usage

Each script is standalone and can be run independently:

```bash
# Run QPSK modulation
python qpsk.py

# Run BPSK BER simulation
python bpskber.py

# Run PCM analysis
python pcm.py

# Run matched filter demonstration
python matchedfilter.py

# Generate eye diagram
python eyediag.py
```

### Example: Interactive PCM Simulation

```bash
python pcm.py
# When prompted: Enter the max value of bits: 8
```

## Key Concepts Covered

### Modulation Theory
- Signal constellation and decision boundaries
- Bandwidth efficiency and spectral properties
- Modulation index and phase relationships

### Channel Model
- Additive White Gaussian Noise (AWGN)
- Signal-to-Noise Ratio (SNR/Eb/N0)
- Bit Error Rate (BER) vs. SNR curves

### Detection & Filtering
- Matched filter theory and implementation
- Optimal sampling times
- Pulse shaping and Nyquist criteria

### Quantization
- Uniform and non-uniform quantization
- Quantization noise
- Signal-to-Quantization Noise Ratio (SQNR)
- PCM system analysis

### Signal Analysis
- Eye diagrams for ISI visualization
- Constellation diagrams
- Time-domain and frequency-domain plots

## Learning Resources

These scripts are ideal for:
- **ECE/EE Students:** Digital Communications courses (foundation level)
- **Self-Study:** Communication systems fundamentals
- **Research:** Baseline implementations for custom extensions
- **Projects:** Building blocks for communication system prototypes

### Recommended Study Order

1. **pcm.py** - Understand sampling and quantization
2. **qpsk.py** - Learn modulation basics
3. **eyediag.py** - Analyze signal quality
4. **matchedfilter.py** - Design optimal receivers
5. **bpskber.py / berqpsk.py** - Evaluate system performance

## Customization

Each script has adjustable parameters at the top:

```python
# Example: Adjust noise in matchedfilter.py
noise_variance = 0.05  # Decrease for cleaner signal

# Example: Change quantization bits in pcm.py
b_max = 10  # Increase for finer quantization
```

## Performance Notes

- **PCM.py:** Requires user input; use automated scripts for batch processing
- **BER Simulations:** May take 30-60 seconds per SNR point depending on CPU
- **Matched Filter:** Convolve operations are CPU-intensive; reduce `num_bits` for faster execution

## Output Examples

All scripts generate matplotlib figures:
- Time-domain waveforms
- Constellation diagrams
- BER curves (logarithmic scale)
- Eye diagrams
- Quantization characteristics

Use `plt.savefig()` to save plots or `plt.show()` for interactive viewing.

## Troubleshooting

### Plot windows not appearing?
```bash
# Use non-interactive backend
export MPLBACKEND=Agg
python script.py
```

### Division by zero in eyediag.py?
Already handled with np.isnan() and np.isinf() checks. Update if extending to different roll-off factors.

### Memory issues with large N in BER simulations?
Reduce N from 1,000,000 to 100,000 for faster iterations (trade-off: less accuracy)

```python
N = 100000  # Faster, less accurate
```

## Applications

These implementations demonstrate:
- **Digital Receiver Design:** Filter banks, matched filters
- **System Performance:** BER analysis, SNR optimization
- **Signal Integrity:** Eye diagram interpretation
- **Codec Development:** PCM encoding/decoding chains

## Future Enhancements

Potential extensions:
- [ ] M-ary PSK/QAM implementations
- [ ] Frequency-selective channel models
- [ ] Turbo/LDPC coding
- [ ] Equalization techniques
- [ ] OFDM implementation
- [ ] Real-world data imports

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open Pull Request

## License

This project is open source and available for educational use. Please cite if used in academic work.

## Author

**Harshadithyan7**

## Acknowledgments

- Based on digital communications fundamentals from standard textbooks
- Influenced by university lab courses in signal processing
- Educational implementations for learning purposes

## References

### Standard Textbooks
- Proakis & Salehi: "Digital Communications" (5th Ed.)
- Haykin & Moher: "Introduction to Analog and Digital Communications"
- Rice: "Digital Communications: A Discrete-Time Approach"

### Related Topics
- Information Theory and Coding
- Signal Processing
- Wireless Communications
- Statistical Signal Detection

---

**Last Updated:** May 2026

**Status:** Active (Educational Repository)

For questions or issues, please open an issue on GitHub.
