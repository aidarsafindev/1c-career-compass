"""
Визуализация карьерного пути 1С-разработчика.

Выводит ASCII-график изменения пропорций навыков по грейдам.
"""


def visualize_career_path():
    """ASCII-визуализация карьерного пути."""
    grades = ["Junior", "Middle", "Senior", "Lead", "Architect", "CTO"]
    hard = [80, 60, 40, 30, 50, 20]
    soft = [15, 25, 35, 40, 30, 30]
    business = [5, 15, 25, 30, 20, 50]

    print("Пропорции навыков по грейдам")
    print("=" * 60)

    for i, grade in enumerate(grades):
        h = "#" * (hard[i] // 2)
        s = "+" * (soft[i] // 2)
        b = "$" * (business[i] // 2)

        bar = h + s + b
        print(f"{grade:<12} |{bar}")

    print()
    print("# = Hard Skills  |  + = Soft Skills  |  $ = Business Skills")
    print()

    print("Ключевые переходы:")
    print("-" * 40)
    transitions = [
        ("Junior -> Middle", "Из исполнителя в самостоятельного разработчика. Учится проектировать модули."),
        ("Middle -> Senior", "Из разработчика в технического лидера. Берёт ответственность за систему."),
        ("Senior -> Lead", "Из техлида в менеджера. Управляет командой, сроками, людьми."),
        ("Lead -> Architect", "Из менеджера в стратега. Определяет технологическое направление."),
        ("Architect -> CTO", "Из стратега в руководителя бизнеса. Технологии служат бизнесу."),
    ]

    for title, description in transitions:
        print(f"  {title}: {description}")
        print()


if __name__ == "__main__":
    visualize_career_path()
