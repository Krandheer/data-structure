import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

z = 0.8 + 0.5j

max_power = 200
powers = []
z_current = z

for n in range(max_power + 1):
    powers.append(z_current)
    z_current *= z

powers = np.array(powers)
magnitudes = np.abs(powers)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

ax1.set_title(f"Powers of {z} in Complex Plane")
ax1.set_xlabel("Real Part")
ax1.set_ylabel("Imaginary Part")
ax1.grid(True)
ax1.axhline(y=0, color="k", linestyle="-", alpha=0.3)
ax1.axvline(x=0, color="k", linestyle="-", alpha=0.3)
ax1.set_xlim(-1, 1)
ax1.set_ylim(-1, 1)

# Draw unit circle
circle = plt.Circle((0, 0), 1, fill=False, color="red", alpha=0.3)
ax1.add_artist(circle)

# Magnitude subplot
ax2.set_title("Magnitude vs Power")
ax2.set_xlabel("Power (n)")
ax2.set_ylabel("Magnitude")
ax2.grid(True)
ax2.set_ylim(0, 1)


# Animation function
def update(frame):
    # Clear previous points
    ax1.clear()
    ax2.clear()

    # Redraw complex plane setup
    ax1.set_title(f"Powers of {z} in Complex Plane")
    ax1.set_xlabel("Real Part")
    ax1.set_ylabel("Imaginary Part")
    ax1.grid(True)
    ax1.axhline(y=0, color="k", linestyle="-", alpha=0.3)
    ax1.axvline(x=0, color="k", linestyle="-", alpha=0.3)
    ax1.set_xlim(-1, 1)
    ax1.set_ylim(-1, 1)
    ax1.add_artist(plt.Circle((0, 0), 1, fill=False, color="red", alpha=0.3))

    # Plot points up to current frame
    ax1.scatter(
        powers[: frame + 1].real,
        powers[: frame + 1].imag,
        c=np.arange(frame + 1),
        cmap="viridis",
    )
    ax1.plot(powers[: frame + 1].real, powers[: frame + 1].imag, "b-", alpha=0.3)

    # Redraw magnitude plot setup
    ax2.set_title("Magnitude vs Power")
    ax2.set_xlabel("Power (n)")
    ax2.set_ylabel("Magnitude")
    ax2.grid(True)
    ax2.set_ylim(0, 1)

    # Plot magnitudes up to current frame
    powers_range = np.arange(frame + 1)
    ax2.plot(powers_range, magnitudes[: frame + 1], "g-")
    ax2.scatter(powers_range, magnitudes[: frame + 1], c=powers_range, cmap="viridis")

    # Add text showing current power and magnitude
    if frame > 0:
        current_mag = magnitudes[frame]
        ax2.text(
            0.02,
            0.98,
            f"Power: {frame}\nMagnitude: {current_mag:.4f}",
            transform=ax2.transAxes,
            verticalalignment="top",
        )


# Create animation
anim = FuncAnimation(fig, update, frames=max_power + 1, interval=200, repeat=False)

plt.tight_layout()
plt.show()
