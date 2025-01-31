import numpy as np
import matplotlib.pyplot as plt

# Dados da viga
L = 30  # Comprimento total da viga (m)
x = np.linspace(0, L, 1000)  # Pontos ao longo da viga

# Força de cisalhamento (V)
V = np.piecewise(x,
                 [x < 10, (x >= 10) & (x < 20), x >= 20],
                 [lambda x: 6.67,  # 0 < x < 10
                  lambda x: 1.67,  # 10 < x < 20
                  lambda x: 1.67 - 2 * (x - 20)])  # 20 < x < 30

# Momento fletor (M)
M = np.piecewise(x,
                 [x < 10, (x >= 10) & (x < 20), x >= 20],
                 [lambda x: 6.67 * x,  # 0 < x < 10
                  lambda x: 6.67 * x - 5 * (x - 10),  # 10 < x < 20
                  lambda x: 6.67 * x - 5 * (x - 10) - (x - 20)**2])  # 20 < x < 30

# Plotando os gráficos
plt.figure(figsize=(12, 6))

# Gráfico da força de cisalhamento (V)
plt.subplot(2, 1, 1)
plt.plot(x, V, label="Força de Cisalhamento (V)", color="blue")
plt.title("Diagrama de Força de Cisalhamento (V)")
plt.xlabel("Posição ao longo da viga (m)")
plt.ylabel("Força de Cisalhamento (kN)")
plt.grid(True)
plt.axhline(0, color="black", linewidth=0.5)
plt.legend()

# Gráfico do momento fletor (M)
plt.subplot(2, 1, 2)
plt.plot(x, M, label="Momento Fletor (M)", color="red")
plt.title("Diagrama de Momento Fletor (M)")
plt.xlabel("Posição ao longo da viga (m)")
plt.ylabel("Momento Fletor (kN·m)")
plt.grid(True)
plt.axhline(0, color="black", linewidth=0.5)
plt.legend()

plt.tight_layout()
plt.show()