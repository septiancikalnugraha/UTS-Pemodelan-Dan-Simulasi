import numpy as np
import matplotlib.pyplot as plt

# Matriks peluang transisi dari periode sebelumnya ke saat ini
transition_matrix_previous_to_current = np.array([
    [0.714, 0.196, 0.089],  # D to D, M, S
    [0.464, 0.429, 0.107],  # M to D, M, S
    [0.625, 0.125, 0.250],  # S to D, M, S
])

# Matriks peluang transisi dari saat ini ke periode mendatang
transition_matrix_current_to_future = np.array([
    [0.825, 0.143, 0.032],  # D to D, M, S
    [0.120, 0.680, 0.200],  # M to D, M, S
    [0.167, 0.250, 0.583],  # S to D, M, S
])

# Label untuk states
states = ["Drinking Of You (DOY)", "Mhimhithaitea", "Sruput"]

# Distribusi awal pelanggan berdasarkan pangsa pasar awal
initial_distribution = np.array([0.56, 0.28, 0.16])  # Dari tabel pangsa pasar sebelumnya

# Fungsi untuk memprediksi distribusi setelah beberapa langkah
def predict_distribution(initial_distribution, steps, matrix):
    distributions = [initial_distribution]
    current_distribution = initial_distribution
    for _ in range(steps):
        current_distribution = np.dot(current_distribution, matrix)
        distributions.append(current_distribution)
    return np.array(distributions)

# Jumlah periode untuk prediksi
num_steps = 10

# Prediksi untuk periode sebelumnya ke saat ini
distributions_previous_to_current = predict_distribution(initial_distribution, num_steps, transition_matrix_previous_to_current)

# Prediksi untuk periode saat ini ke mendatang
distributions_current_to_future = predict_distribution(initial_distribution, num_steps, transition_matrix_current_to_future)

# Plot hasil distribusi untuk periode sebelumnya ke saat ini
plt.figure(figsize=(12, 6))
for i, state in enumerate(states):
    plt.plot(range(num_steps + 1), distributions_previous_to_current[:, i], marker='o', label=f"{state} (Prev to Curr)")

# Plot hasil distribusi untuk periode saat ini ke mendatang
for i, state in enumerate(states):
    plt.plot(range(num_steps + 1), distributions_current_to_future[:, i], marker='x', linestyle='--', label=f"{state} (Curr to Future)")

plt.title("Prediksi Distribusi Pelanggan Menggunakan Rantai Markov")
plt.xlabel("Periode")
plt.ylabel("Proporsi Pelanggan")
plt.legend()
plt.grid(True)
plt.show()
