# 1c-career-compass

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Author: Aydar Safin](https://img.shields.io/badge/Author-Aydar%20Safin-blue)
![Course](https://img.shields.io/badge/Mini--Course-6%20modules-green)

> Карьерный компас для 1С-разработчика. Junior → Middle → Senior → Lead → Architect → CTO.
> Матрица компетенций, чек-листы самооценки, шаблон IDP, анализатор разрывов, мини-курс.

**Автор:** Айдар Сафин, Главный разработчик Центра экспертизы 1С, Магнит
**Контакты:** aidar@aidarsafin.ru
**Репозиторий:** [github.com/aidarsafindev/1c-career-compass](https://github.com/aidarsafindev/1c-career-compass)
**Лицензия:** MIT (текст курса — авторское право)

---

## Что внутри

- **Матрица компетенций** — три группы навыков (Hard, Soft, Business) с детализацией по шести грейдам
- **Чек-лист самооценки** — оценка себя по шкале 1-5 для каждого навыка
- **Шаблон IDP** — Individual Development Plan на 6 месяцев
- **Чек-лист повышения** — что проверить перед разговором о повышении
- **Визуализация карьерного пути** — ASCII-график изменения пропорций навыков
- **Анализатор разрывов** — топ-5 навыков с максимальным разрывом до целевого грейда
- **Мини-курс** — пошаговое руководство по каждому грейду с примерами и фишками

---

## Мини-курс: от Junior до CTO

Полное пошаговое руководство по карьерному росту 1С-разработчика —
в файле [COURSE.md](COURSE.md).

Курс состоит из 6 модулей:

| # | Грейд | Суть роли |
|---|-------|-----------|
| 1 | **Junior** | Исполнитель. Пишет код по спецификации |
| 2 | **Middle** | Самостоятельный. Проектирует модули |
| 3 | **Senior** | Технический лидер. Проектирует системы |
| 4А | **Lead** | Управленец. Отвечает за команду |
| 4Б | **Architect** | Стратег. Определяет архитектуру |
| 5 | **CTO** | Бизнес-лидер. Технологии служат бизнесу |

---

## Быстрый старт

```bash
git clone https://github.com/aidarsafindev/1c-career-compass.git
cd 1c-career-compass

# Установить зависимости
pip install pyyaml

# Визуализация карьерного пути
python scripts/visualize.py

# Анализ разрывов (укажите целевой грейд)
python scripts/skill-gap.py senior

# Шаблон самооценки
cat templates/self-assessment.md

# Шаблон IDP
cat templates/idp-template.md
