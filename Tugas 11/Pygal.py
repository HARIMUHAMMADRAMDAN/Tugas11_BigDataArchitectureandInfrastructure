import pygal

# Membuat pie chart
pie_chart = pygal.Pie()

# Menambahkan data dengan label dan nilai
pie_chart.title = "Distribusi Data Kategori"
pie_chart.add("A", 5)
pie_chart.add("B", 7)
pie_chart.add("C", 3)
pie_chart.add("D", 8)

# Menambahkan keterangan nilai pada setiap segmen
pie_chart.legend = True  # Menampilkan legenda
pie_chart.render_to_file("pie_chart_with_labels.svg")  # Simpan sebagai file SVG
