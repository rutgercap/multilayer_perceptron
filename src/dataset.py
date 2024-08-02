from pathlib import Path
import pandas as pd
from sklearn.preprocessing import RobustScaler 


def dataset_from_path(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    df = pd.read_csv(path, header=None)
    columns = list(df.columns)
    columns[0] = "index"
    columns[1] = "diagnosis"
    for i in range(2, len(columns)):
        columns[i] = f"feature_{i - 2}"
    df.columns = columns
    return df

def normalize_data(df: pd.DataFrame) -> pd.DataFrame:
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    scaler = RobustScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])
    return df