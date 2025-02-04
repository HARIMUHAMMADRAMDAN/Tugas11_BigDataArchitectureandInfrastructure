import seaborn as sns
import matplotlib.pyplot as plt

# Data untuk grafik batang
data = {'Kategori': ['A', 'B', 'C', 'D'], 'Nilai': [5, 7, 3, 8]}

# Membuat grafik batang
sns.set(style="whitegrid")
plt.figure(figsize=(6, 4))
sns.barplot(x=data['Kategori'], y=data['Nilai'], palette="Blues_d")
plt.xlabel("Kategori")
plt.ylabel("Nilai")
plt.title("Grafik Batang Kategori vs Nilai")
plt.show()
