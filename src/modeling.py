import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import f1_score


def get_preprocessor(X: pd.DataFrame) -> ColumnTransformer:
    """
    Создает трансформер колонок для стандартизации числовых
    и OHE-кодирования категориальных признаков.
    """
    num_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    cat_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), num_cols),
            ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_cols)
        ])
    return preprocessor


def evaluate_model(model, X_train, y_train, X_val, y_val):
    """
    Обучает модель и возвращает F1_macro метрику на валидации.
    """
    model.fit(X_train, y_train)
    y_pred = model.predict(X_val)
    f1 = f1_score(y_val, y_pred, average='macro')
    return f1
