import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

A = np.array([30, 50])
B = np.array([-10, 2])

dot_AB = np.dot(A, B)
R = A + B
magnitude_R = np.linalg.norm(R)

norm_A = np.linalg.norm(A)
norm_B = np.linalg.norm(B)

cos_theta = dot_AB / (norm_A * norm_B)
theta_deg = np.degrees(np.arccos(cos_theta))

print("Vektor A =", A) 
print("Vektor B =", B)
print("Dot product A·B =", dot_AB)
print("Resultan (A + B) =", R)
print("Panjang Resultan |R| =", round(magnitude_R, 2))
print("Sudut antara A dan B =", round(theta_deg, 2), "derajat")

plt.figure(figsize=(8, 8))
plt.axhline(0, color='black', linewidth=1.2)
plt.axvline(0, color='black', linewidth=1.2)
plt.grid(True, alpha=0.3, linestyle='--')

# Plot Vektor
plt.quiver(0, 0, A[0], A[1], angles='xy', scale_units='xy', scale=1, 
           color='r', width=0.008, label="A", zorder=4)
plt.quiver(0, 0, B[0], B[1], angles='xy', scale_units='xy', scale=1, 
           color='g', width=0.008, label="B", zorder=4)
plt.quiver(0, 0, R[0], R[1], angles='xy', scale_units='xy', scale=1, 
           color='m', width=0.008, label="Resultan (A + B)", zorder=4)

# Garis Jajar Genjang
plt.plot([A[0], R[0]], [A[1], R[1]], 'k--', alpha=0.4, linewidth=1.2)
plt.plot([B[0], R[0]], [B[1], R[1]], 'k--', alpha=0.4, linewidth=1.2)

# Titik Ujung
plt.scatter(*A, color='red', s=60, zorder=5)
plt.scatter(*B, color='green', s=60, zorder=5)
plt.scatter(*R, color='purple', s=60, zorder=5)

# Label Koordinat (Offset disesuaikan dengan skala puluhan)
plt.text(A[0] + 1, A[1] + 1, f"A({A[0]}, {A[1]})", fontsize=11, color='red', fontweight='bold')
plt.text(B[0] - 8, B[1] - 3, f"B({B[0]}, {B[1]})", fontsize=11, color='green', fontweight='bold')
plt.text(R[0] + 1, R[1] + 1, f"R({R[0]}, {R[1]})", fontsize=11, color='purple', fontweight='bold')

# Perhitungan Sudut & Busur
angle_A = np.degrees(np.arctan2(A[1], A[0])) % 360
angle_B = np.degrees(np.arctan2(B[1], B[0])) % 360

start_angle = min(angle_A, angle_B)
end_angle = max(angle_A, angle_B)

# Jika selisih sudut > 180, ambil sudut dalam
if end_angle - start_angle > 180:
    start_angle, end_angle = end_angle, start_angle + 360

# Radius busur menggunakan skalar proporsional terhadap vektor terpendek
arc_radius = min(norm_A, norm_B) * 0.6
arc = Arc((0, 0), width=arc_radius * 2, height=arc_radius * 2, angle=0,
          theta1=start_angle, theta2=end_angle, color='blue', linewidth=2)
plt.gca().add_patch(arc)

# Posisi Label Sudut Theta
mid_angle = (start_angle + end_angle) / 2
label_dist = arc_radius * 1.3
x_label = label_dist * np.cos(np.radians(mid_angle))
y_label = label_dist * np.sin(np.radians(mid_angle))

plt.text(x_label, y_label, f"$\\theta$ = {round(theta_deg, 2)}°",
         fontsize=10, color='blue', ha='center', va='center',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='lightblue', alpha=0.8))

# Atur Batas Sumbu & Label Kuadran
plt.xlim(-20, 40)
plt.ylim(-15, 65)

plt.text(20, 30, "Kuadran I", fontsize=10, color='gray', alpha=0.5, style='italic')
plt.text(-12, 30, "Kuadran II", fontsize=10, color='gray', alpha=0.5, style='italic')
plt.text(-12, -8, "Kuadran III", fontsize=10, color='gray', alpha=0.5, style='italic')
plt.text(20, -8, "Kuadran IV", fontsize=10, color='gray', alpha=0.5, style='italic')

plt.xlabel("Sumbu X", fontsize=12, fontweight='bold')
plt.ylabel("Sumbu Y", fontsize=12, fontweight='bold')
plt.title("Resultan Jajar Genjang dan Sudut Vektor A & B", fontsize=13, fontweight='bold', pad=12)
plt.legend(loc='upper left', fontsize=10)
plt.gca().set_aspect('equal', adjustable='box')

plt.tight_layout()
plt.show()