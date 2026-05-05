import pandas as pd


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

    # Датасет не имеет дибликатов или дублей, но код очистки будет также приведён ниже
    # Удаление дубликатов
    # data = data.drop_duplicates().reset_index(drop=True)

    # Удаление пропусков (прямой способ, в случае если бы количество строк с пропущенными значениями
    #                     составляло бы малый процент от всех данных)
    # data = data.dropna().reset_index(drop=True)

    return data


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Создание новых признаков.
    """
    data = df.copy()

    return data


def preprocess_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """
    Полный пайплайн подготовки: очистка + генерация фичей.
    """
    df_cleaned = clean_data(df)
    df_engineered = feature_engineering(df_cleaned)
    return df_engineered
