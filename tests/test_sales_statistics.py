import pytest
import pandas as pd
from src.sales_statistics import (
    calculate_product_statistics,
    calculate_daily_statistics,
    get_statistics_summary
)


def test_calculate_product_statistics_basic():
    data = pd.DataFrame({
        'Product': ['Coffee', 'Tea', 'Coffee'],
        'Quantity': [2, 1, 3],
        'Price': [5.0, 3.0, 5.0]
    })
    result = calculate_product_statistics(data)

    assert len(result) == 2
    coffee_row = result[result['Product'] == 'Coffee'].iloc[0]
    assert coffee_row['Total_Quantity'] == 5
    assert coffee_row['Total_Sales'] == 25.0


def test_calculate_product_statistics_empty_dataframe():
    empty_df = pd.DataFrame(columns=['Product', 'Quantity', 'Price'])
    result = calculate_product_statistics(empty_df)

    assert len(result) == 0
    assert list(result.columns) == ['Product', 'Total_Quantity', 'Total_Sales']


def test_calculate_daily_statistics_basic():
    data = pd.DataFrame({
        'Date': ['2024-01-01', '2024-01-01'],
        'Product': ['Coffee', 'Tea'],
        'Quantity': [2, 1],
        'Price': [5.0, 3.0]
    })
    result = calculate_daily_statistics(data)

    assert len(result) == 1
    assert result.iloc[0]['Date'] == '2024-01-01'
    assert result.iloc[0]['Total_Sales'] == 13.0


def test_calculate_daily_statistics_multiple_days():
    data = pd.DataFrame({
        'Date': ['2024-01-01', '2024-01-01', '2024-01-02'],
        'Product': ['Coffee', 'Tea', 'Coffee'],
        'Quantity': [2, 1, 3],
        'Price': [5.0, 3.0, 5.0]
    })
    result = calculate_daily_statistics(data)

    assert len(result) == 2
    assert result[result['Date'] == '2024-01-01'].iloc[0]['Total_Sales'] == 13.0
    assert result[result['Date'] == '2024-01-02'].iloc[0]['Total_Sales'] == 15.0


def test_calculate_daily_statistics_empty_dataframe():
    empty_df = pd.DataFrame(columns=['Date', 'Product', 'Quantity', 'Price'])
    result = calculate_daily_statistics(empty_df)

    assert len(result) == 0
    assert list(result.columns) == ['Date', 'Total_Sales']


def test_get_statistics_summary_basic():
    data = pd.DataFrame({
        'Product': ['Coffee', 'Tea', 'Coffee'],
        'Quantity': [2, 1, 3],
        'Price': [5.0, 3.0, 5.0]
    })
    result = get_statistics_summary(data)

    assert result['total_products'] == 2
    assert result['total_quantity'] == 6
    assert result['total_sales'] == 28.0


def test_get_statistics_summary_empty_dataframe():
    empty_df = pd.DataFrame(columns=['Product', 'Quantity', 'Price'])
    result = get_statistics_summary(empty_df)

    assert result['total_products'] == 0
    assert result['total_quantity'] == 0
    assert result['total_sales'] == 0.0


def test_statistics_with_real_data():
    from src import read_sales_data
    valid_data, _ = read_sales_data('data/sales_january.xlsx')

    product_stats = calculate_product_statistics(valid_data)
    assert len(product_stats) > 0
    assert 'Total_Quantity' in product_stats.columns
    assert 'Total_Sales' in product_stats.columns

    summary = get_statistics_summary(valid_data)
    assert summary['total_products'] > 0
    assert summary['total_quantity'] > 0
    assert summary['total_sales'] > 0