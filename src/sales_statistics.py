import pandas as pd
from typing import Dict


def calculate_product_statistics(valid_data: pd.DataFrame) -> pd.DataFrame:
    if valid_data.empty:
        return pd.DataFrame(columns=['Product', 'Total_Quantity', 'Total_Sales'])

    valid_data = valid_data.copy()
    valid_data['Sales'] = valid_data['Quantity'] * valid_data['Price']

    product_stats = valid_data.groupby('Product').agg(
        Total_Quantity=('Quantity', 'sum'),
        Total_Sales=('Sales', 'sum')
    ).reset_index()

    return product_stats


def calculate_daily_statistics(valid_data: pd.DataFrame) -> pd.DataFrame:
    if valid_data.empty:
        return pd.DataFrame(columns=['Date', 'Total_Sales'])

    valid_data = valid_data.copy()
    valid_data['Sales'] = valid_data['Quantity'] * valid_data['Price']

    daily_stats = valid_data.groupby('Date').agg(
        Total_Sales=('Sales', 'sum')
    ).reset_index()

    return daily_stats


def get_statistics_summary(valid_data: pd.DataFrame) -> Dict:
    if valid_data.empty:
        return {
            'total_products': 0,
            'total_quantity': 0,
            'total_sales': 0.0
        }

    valid_data = valid_data.copy()
    valid_data['Sales'] = valid_data['Quantity'] * valid_data['Price']

    return {
        'total_products': valid_data['Product'].nunique(),
        'total_quantity': int(valid_data['Quantity'].sum()),
        'total_sales': float(valid_data['Sales'].sum())
    }