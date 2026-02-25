import numpy as np
import matplotlib.pyplot as plt

print("🌱 GreenSpace AI - MVP")

# Ввод координат
lat = float(input("Введите широту: "))
lon = float(input("Введите долготу: "))
year1 = int(input("Введите первый год: "))
year2 = int(input("Введите второй год: "))

# Симуляция спутниковых каналов (как реальные матрицы пикселей)
nir_1 = np.random.uniform(0.6, 0.9, (300, 300))
red_1 = np.random.uniform(0.2, 0.4, (300, 300))

nir_2 = np.random.uniform(0.4, 0.8, (300, 300))
red_2 = np.random.uniform(0.3, 0.5, (300, 300))

# Расчёт NDVI
ndvi_1 = (nir_1 - red_1) / (nir_1 + red_1)
ndvi_2 = (nir_2 - red_2) / (nir_2 + red_2)

mean1 = np.mean(ndvi_1)
mean2 = np.mean(ndvi_2)

change = ((mean2 - mean1) / mean1) * 100

print("\n📊 Результаты анализа:")
print(f"Координаты участка: {lat}, {lon}")
print(f"NDVI в {year1}: {mean1:.3f}")
print(f"NDVI в {year2}: {mean2:.3f}")
print(f"Изменение: {change:.2f}%")

# Автоматическая аналитика
if change < -10:
    status = "⚠ Возможная деградация леса"
elif change > 5:
    status = "🌿 Состояние леса улучшилось"
else:
    status = "📈 Существенных изменений не обнаружено"

print("Вывод:", status)

# График
years = [year1, year2]
values = [mean1, mean2]

plt.figure()
plt.plot(years, values)
plt.ylabel("NDVI")
plt.title("Изменение состояния леса")
plt.show()
