import numpy as np
import matplotlib.pyplot as plt
import os


async def get_circul_balance(val: list, id_user: int, id_test: int):
    labels = ['Здоровье и физическая форма', 'Карьера и самореализация', 'Финансы и материальная стабильность', 'Личностный рост и обучение', 
              'Семья и близкие отношения', 'Социальная жизнь и друзья', 'Отдых и хобби', 'Духовность и внутренний комфорт']
    val = [v if v <= 10 else 10 for v in val]
    try:
        if len(labels) == len(val):
            # TODO Сделать дизайн диаграммы
            val += val[:1]
            angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
            angles += angles[:1]

            fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
            ax.fill(angles, val, color='cyan', alpha=0.25)
            ax.plot(angles, val, color='blue', linewidth=2)

            # Настройка осей
            ax.set_yticklabels([])
            ax.set_xticks(angles[:-1])
            ax.set_xticklabels(labels)

            image_path = os.path.join(os.getcwd(), "images", f"{id_user}_{id_test}.png")

            plt.savefig(image_path)
            print(image_path)
            return image_path
        else:
            print("Нет достаточных сведений о пользователи")
            return 0
    except ValueError:
        print(ValueError)


async def mood_diagramma(id_user, id_test, date, height):
    colors = ['red' if v <= 5 else 'yellow' if v <= 10 else 'green' for v in height]
    plt.bar(date, height,  color=colors, edgecolor='black')
    plt.ylim(0, 16)
    plt.xlabel('Дата')
    plt.ylabel('Настроение')

    image_path = os.path.join(os.getcwd(), "images", f"{id_user}_{id_test}.png")

    plt.savefig(image_path)
    return image_path

