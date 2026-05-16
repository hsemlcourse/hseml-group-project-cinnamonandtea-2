[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/kOqwghv0)
# ML Project — Предсказание риска возникновения нарушний сна

**Студент:** Кудрявцева Василиса Сергеевна

**Группа:** БИВ235


## Оглавление

1. [Описание задачи](#описание-задачи)
2. [Структура репозитория](#структура-репозитория)
3. [Запуски](#быстрый-старт)
4. [Данные](#данные)
5. [Результаты](#результаты)
7. [Отчёт](#отчёт)


## Описание задачи

<!-- Кратко опишите задачу: что предсказываем, какой датасет, метрика качества -->

**Задача:** Мультиклассовая классификация

**Датасет:** [Sleep Health & Daily Performance Dataset](https://www.kaggle.com/datasets/mohankrishnathalla/sleep-health-and-daily-performance-dataset)

**Целевая метрика:** F1_macro

Цель проекта - построить классифицирующую модель, определить группу риска возникновения нарушний сна (Healthy, Mild, Moderate, Severe)  у человека на основе данных о его сне, образе жизни и демографии

## Структура репозитория

```
.
├── data
│   ├── processed               # Очищенные и обработанные данные
│   └── raw                     # Исходные файлы
├── models                      # Сохранённые модели 
├── notebooks
│   ├── 01_eda.ipynb            # EDA
│   ├── 02_baseline.ipynb       # Baseline-модель
│   └── 03_experiments.ipynb    # Эксперименты и ablation study
├── presentation                # Презентация для защиты
├── report
│   ├── images                  # Изображения для отчёта
│   └── report.md               # Финальный отчёт
├── src
│   ├── preprocessing.py        # Предобработка данных
│   └── modeling.py             # Обучение и оценка моделей
├── tests
│   └── test.py                 # Тесты пайплайна
├── Dockerfile                  # Инструкция для сборки образа
├── docker-compose.yml          # Оркестрация контейнера
├── Makefile                    # Утилита для запуска проверок
├── requirements.txt            # Зависимости
└── README.md
```

## Запуск

**Локальный запуск**
```bash
# 1. Клонировать репозиторий
git clone <url>
cd <repo-name>

# 2. Создать виртуальное окружение
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows

# 3. Установить зависимости
pip install -r requirements.txt

```

**Запуск через Docker**
```bash
docker-compose up --build
```

## Линтеры
Для проверки качества кода (PEP8) используется утилита make:
```bash
make lint
```

## Данные
- `data/raw/` — исходные файлы
- `data/processed/` — предобработанные данные


## Результаты

| Модель | F1-macro (Val) | Примечание |
|--------|----------------|------------|
|LightGBM (Tuned)|	0.8529|	Лучшая модель (GridSearchCV)|
|LightGBM (Default)|	0.8482|	Все признаки|
|Random Forest (Default)|	0.7709|	Все признаки|
|Logistic Regression|	0.7198|	Baseline|
|Random Forest + PCA|	0.6239|	35 компонент|
|KNN|	0.4843|	Baseline|


## Отчёты

Промежуточный отчёт по cp1: [`report/cp1.md`](report/cp1.md)
Финальный отчёт: [`report/report.md`](report/report.md)
