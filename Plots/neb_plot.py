import numpy as np
import matplotlib.pyplot as plt
import sys

# Check if files are provided
if len(sys.argv) < 2:
    print("Usage: python3 neb_plot.py <file1> <file2> ...")
    sys.exit(1)

# Initialize plot
plt.figure(figsize=(8, 6))

# Loop over all provided files
for file in sys.argv[1:]:
    try:
        neb_energy = np.loadtxt(file)
        neb_energy[:, 1] -= neb_energy[0, 1]  # Normalize energy
        plt.plot(neb_energy[:, 0], neb_energy[:, 1], label=file)
    except Exception as e:
        print(f"Error reading {file}: {e}")

# Customize plot
plt.xlabel("Reaction Coordinate")
plt.ylabel("Relative Energy (eV)")
plt.title("NEB Energy Profile")
plt.legend()
plt.grid(True)

# Show plot
plt.show()

