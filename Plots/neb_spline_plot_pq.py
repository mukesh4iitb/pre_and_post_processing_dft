import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Set publication-quality plot parameters
plt.rcParams.update({
    "text.usetex": False,               # Use MathText (not external LaTeX)
    "svg.fonttype": "none",             # Keep text editable in SVG
    "font.family": "Times New Roman",   # Use Times New Roman
    "font.size": 16,
    "axes.labelsize": 18,
    "axes.titlesize": 18,
    "legend.fontsize": 14,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14,
    "lines.linewidth": 2.0,
    "axes.linewidth": 1.5,
})


# Check if files are provided
if len(sys.argv) < 2:
    print("Usage: python3 neb_plot.py <file1> <file2> ...")
    sys.exit(1)

# Initialize plot
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)  # High DPI for sharp output



#data=np.loadtxt("spline.dat")
#plt.plot(data[:, 0], data[:, 2])
#
#plt.scatter(images[:, 0], images[:, 2])
#
#plt.show()



# Loop over all provided files
for file in sys.argv[1:]:
    try:
        neb_spline = np.loadtxt(file)
        #In nebspline.pl has 20 pt between any two image, so selecting each 20th images.
        sel=[i for i in range(0, neb_spline.shape[0], 20)] 
        images=neb_spline[sel]

        ax.plot(neb_spline[:, 0], neb_spline[:, 2], linestyle="-", label=file)
        ax.scatter(images[:, 0], images[:, 2], marker="o")
    except Exception as e:
        print(f"Error reading {file}: {e}")

# Customize plot
ax.set_xlabel(r"Reaction Coordinate")
ax.set_ylabel(r"Relative Energy (eV)")
ax.set_title(r"NEB Energy Profile")
ax.legend(frameon=False, loc="best")
#ax.grid(True, linestyle="--", linewidth=0.6, alpha=0.7)

# Improve tick formatting
ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6))

# Save as high-resolution PNG & PDF
#plt.tight_layout()
plt.savefig("NEB_Spline_profile.pdf", format="pdf", bbox_inches="tight")
plt.savefig("NEB_Spline_Profile.png", format="png", dpi=300, bbox_inches="tight")
plt.savefig("NEB_Spline_Profile.svg", format="svg", dpi=300, bbox_inches="tight")

# Show plot
plt.show()

