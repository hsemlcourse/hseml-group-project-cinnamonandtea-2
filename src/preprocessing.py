import pandas as pd
import numpy as np


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Очистка датасета
    """
    data = df.copy()

    # В датасете имеется 3 таргета, необходимо оставить интересующий таргет sleep_disorder_risk
    # Лишние таргеты повышают риск возникновения утечки данных
    other_targets = ['cognitive_performance_score', 'felt_rested']
    cols_to_drop = [col for col in other_targets if col in data.columns]

    if cols_to_drop:
        data = data.drop(columns=cols_to_drop)

    # Обработка выбросов в числовых признаках (метод IQR)
    # Используем отсечение, чтобы не терять строки
    num_cols = data.select_dtypes(include=['float64', 'int64']).columns
    num_cols =[c for c in num_cols if c != 'sleep_disorder_risk'] # Исключаем таргет
    
    for col in num_cols:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        # Все, что выходит за границы, приравниваем к границам
        data[col] = np.clip(data[col], lower_bound, upper_bound)

    # Датасет не имеет дубликатов или дублей, но код очистки будет также приведён ниже
    # Удаление дубликатов
    # data = data.drop_duplicates().reset_index(drop=True)

    # Удаление пропусков (прямой способ, в случае если бы количество строк с пропущенными значениями
    #                     составляло бы малый процент от всех данных)
    # data = data.dropna().reset_index(drop=True)

    return data


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Создание новых признаков на основе существующих.
    """
    data = df.copy()
    
   # 1. deep_sleep_hours (Абсолютное количество часов глубокого сна)
    # Используем sleep_duration_hrs и deep_sleep_percentage
    if 'sleep_duration_hrs' in data.columns and 'deep_sleep_percentage' in data.columns:
        data['deep_sleep_hours'] = data['sleep_duration_hrs'] * (data['deep_sleep_percentage'] / 100.0)
        
    # 2. sleep_stress_ratio (Отношение сна к уровню стресса)
    # Используем sleep_duration_hrs и stress_score
    if 'sleep_duration_hrs' in data.columns and 'stress_score' in data.columns:
        data['sleep_stress_ratio'] = data['sleep_duration_hrs'] / (data['stress_score'] + 1e-5) # Защита от деления на 0
        
    # 3. Возрастные группы (категориальный признак)
    if 'age' in data.columns:
        bins = [0, 25, 40, 60, 100]
        labels = ['Young', 'Adult', 'Middle-aged', 'Senior']
        data['age_group'] = pd.cut(data['age'], bins=bins, labels=labels, right=False)
        
    return data


def preprocess_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """
    Полный пайплайн подготовки: очистка + генерация фичей.
    """
    df_cleaned = clean_data(df)
    df_engineered = feature_engineering(df_cleaned)
    return df_engineered
