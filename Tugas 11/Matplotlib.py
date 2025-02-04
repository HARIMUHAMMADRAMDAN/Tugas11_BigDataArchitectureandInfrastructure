import matplotlib.pyplot as plt

# Data untuk grafik
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Membuat grafik garis
plt.figure(figsize=(6, 4))
plt.plot(x, y, marker='o', linestyle='-', color='b', label="Penjualan")
plt.xlabel("Bulan")
plt.ylabel("Jumlah Penjualan")
plt.title("Grafik Penjualan per Bulan")
plt.legend()
plt.grid()
plt.show()
