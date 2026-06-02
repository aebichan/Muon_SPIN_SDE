import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

table_path = Path("dataset_mu_Li_OU_alpha_Ntraj_90k.npz")

if not table_path.exists():
    raise FileNotFoundError(
        "Could not find dataset_mu_Li_OU_alpha_Ntraj_90k.npz. "
        "Download the split files from the GitHub Release page and "
        "reconstruct the NPZ file using:\n\n"
        "cat dataset_mu_Li_OU_alpha_Ntraj_90k.npz.part_* "
        "> dataset_mu_Li_OU_alpha_Ntraj_90k.npz"
    )

data = np.load(table_path)

D_mu_vals = data["D_mu_vals"]
D_Li_vals = data["D_Li_vals"]
nu_mu_vals = data["nu_mu_vals"]
nu_Li_vals = data["nu_Li_vals"]
alpha_vals = data["alpha_vals"]
B_L_vals = data["B_L_vals"]
t = data["t_array"]
G = data["G_table"]

print("Loaded:", table_path)
print("G_table shape:", G.shape)
print("Axis order:")
print("G_table[i_D_mu, i_D_Li, i_nu_mu, i_nu_Li, i_alpha, i_B_L, i_t]")

# Choose one example curve.
i_D_mu = 8
i_D_Li = 0
i_nu_mu = 0
i_nu_Li = 0
i_alpha = 0
i_B_L = 0

Gz = G[i_D_mu, i_D_Li, i_nu_mu, i_nu_Li, i_alpha, i_B_L, :]

print("\nExample parameters:")
print(f"D_mu  = {D_mu_vals[i_D_mu]:.6g} microsecond^-1")
print(f"D_Li  = {D_Li_vals[i_D_Li]:.6g} microsecond^-1")
print(f"nu_mu = {nu_mu_vals[i_nu_mu]:.6g} microsecond^-1")
print(f"nu_Li = {nu_Li_vals[i_nu_Li]:.6g} microsecond^-1")
print(f"alpha = {alpha_vals[i_alpha]:.6g} microsecond^-2")
print(f"B_L   = {B_L_vals[i_B_L]:.6g} G")

plt.figure()
plt.plot(t, Gz)
plt.xlabel(r"$t$ ($\mu$s)")
plt.ylabel(r"$G_z(t)$")
plt.title("Example muon spin polarization curve")
plt.tight_layout()
plt.savefig("example_curve.png", dpi=300)

print("\nSaved: example_curve.png")
