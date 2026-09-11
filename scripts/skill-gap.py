"""
Анализатор разрывов в навыках.

Сравнивает самооценку разработчика с целевыми значениями для грейда.
Показывает топ-5 навыков с наибольшим разрывом.
"""

import sys
import yaml


def load_matrix(path: str = "matrix/competencies.yaml") -> dict:
    """Загружает матрицу компетенций."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_target_levels(matrix: dict, grade: str) -> dict:
    """Возвращает целевые уровни навыков для грейда."""
    targets = {}

    for group_key, group in matrix["competency_groups"].items():
        for comp_key, comp in group["competencies"].items():
            levels = comp.get("levels", {})
            if grade in levels:
                target = min(len(levels[grade]), 5)
            elif grade == "junior":
                target = 2
            elif grade == "middle":
                target = 3
            elif grade == "senior":
                target = 4
            elif grade in ("lead", "architect"):
                target = 4
            elif grade == "cto":
                target = 4
            else:
                target = 3

            targets[f"{group_key}.{comp_key}"] = target

    return targets


def analyze_gaps(targets: dict, self_assessment: dict) -> list:
    """Находит наибольшие разрывы."""
    gaps = []
    for skill, target in targets.items():
        current = self_assessment.get(skill, 0)
        gap = target - current
        if gap > 0:
            gaps.append({
                "skill": skill,
                "current": current,
                "target": target,
                "gap": gap,
            })
    gaps.sort(key=lambda x: x["gap"], reverse=True)
    return gaps


def main():
    grade = sys.argv[1] if len(sys.argv) > 1 else "middle"

    matrix = load_matrix()
    targets = get_target_levels(matrix, grade)

    print(f"Целевой грейд: {grade}")
    print("Ожидаемый уровень навыков:")
    for skill, target in targets.items():
        print(f"  {skill}: {target}")

    print()
    print("Пример анализа разрывов (самооценка — заглушка):")

    # Заглушка самооценки
    self_assessment = {
        "hard_skills.platform": 3,
        "hard_skills.databases": 2,
        "hard_skills.integrations": 1,
        "hard_skills.devops": 2,
        "soft_skills.communication": 2,
        "soft_skills.mentoring": 1,
        "business_skills.business_domain": 3,
    }

    gaps = analyze_gaps(targets, self_assessment)
    print()
    print("Топ-5 навыков для развития:")
    for i, gap in enumerate(gaps[:5], 1):
        print(f"  {i}. {gap['skill']}: {gap['current']}/5 -> цель {gap['target']}/5 (разрыв: {gap['gap']})")


if __name__ == "__main__":
    main()
