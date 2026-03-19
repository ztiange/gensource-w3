import pandas as pd
from typing import Tuple


def read_sales_data(file_path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    df = pd.read_excel(file_path)
    required_columns = ['Product', 'Quantity', 'Price']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    result = df[required_columns].copy()
    result['Quantity'] = pd.to_numeric(result['Quantity'], errors='coerce')
    result['Price'] = pd.to_numeric(result['Price'], errors='coerce')

    valid_mask = result.notna().all(axis=1) & (result['Quantity'] >= 0)
    valid_data = result[valid_mask].reset_index(drop=True)
    removed_data = result[~valid_mask].reset_index(drop=True)

    return valid_data, removed_data
