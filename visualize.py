import numpy as np
import matplotlib.pyplot as plt

# Данные для диаграммы

values = [1, 2, 2, 3, 4, 5, 6, 7]
id_user = 1234


def value_lab(val:list, id:int):
    # TODO Исправить разные псих проблемы
    labels = ['Спорт', 'Тело', 'Работа', 'Отдых', 'Позитив', 'Негатив', 'Доброта', 'Злость']
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

            plt.savefig(f'E:\HomeChill\EmoBot\EmoBot\images\{id}.png')
        else:
            print("Нет достаточных сведений о пользователи")
            return 0
    except ValueError:
        print(ValueError)


value_lab(values, id_user)

