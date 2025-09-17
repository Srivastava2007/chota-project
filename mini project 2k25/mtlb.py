import numpy as np
import matplotlib.pyplot as plt
# Constants
NUM_BITS = 1000
QBER_THRESHOLD = 0.11  # 11% typical threshold for BB84
# Basis encoding: 0 = rectilinear (+), 1 = diagonal (x)
# Bit encoding in bases:
# Rectilinear: 0 -> |0>, 1 -> |1>
# Diagonal: 0 -> |+>, 1 -> |->
# For simulation, we just track bits and bases.
def generate_bits_and_bases(num_bits):
    bits = np.random.randint(0, 2, num_bits)
    bases = np.random.randint(0, 2, num
