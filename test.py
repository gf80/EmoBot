import matplotlib.pyplot as plt
import numpy as np

# Данные для кругового графика баланса
categories = [
    "Карьера", "Финансы", "Здоровье", "Личностный рост",
    "Друзья и семья", "Романтика", "Развлечения", "Среда"
]
values = [7, 6, 8, 5, 7, 6, 4, 7]  # Оценки удовлетворенности по каждой категории от 0 до 10

# Функция для создания круга баланса
def create_balance_wheel(categories, values):
    # Повторяем начальное значение, чтобы график был замкнутым
    categories = categories + [categories[0]]
    values = values + [values[0]]

    # Устанавливаем количество секторов и углы
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()

    # Создаем фигуру
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    
    # Строим график
    ax.fill(angles, values, color='skyblue', alpha=0.25)
    ax.plot(angles, values, color='blue', linewidth=2)

    # Добавляем названия категорий
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, color="black", fontsize=12)

    # Добавляем подписи и границы
    ax.spines['polar'].set_visible(False)
    ax.grid(color="gray", linestyle="--", linewidth=0.5)
    plt.title("Круг Баланса Жизни", size=15, color="blue")

    plt.show()

# Вызов функции
create_balance_wheel(categories, values)
