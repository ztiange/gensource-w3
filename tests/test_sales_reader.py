import pytest
import pandas as pd
from src import read_sales_data


def test_read_sales_data_with_valid_file():
    valid_data, removed_data = read_sales_data('data/sales_january.xlsx')
    assert isinstance(valid_data, pd.DataFrame)
    assert isinstance(removed_data, pd.DataFrame)
    assert list(valid_data.columns) == ['Date', 'Product', 'Quantity', 'Price']
    assert len(valid_data) > 0


def test_read_sales_data_returns_correct_data_types():
    valid_data, _ = read_sales_data('data/sales_january.xlsx')
    assert pd.api.types.is_string_dtype(valid_data['Product'])
    assert pd.api.types.is_numeric_dtype(valid_data['Quantity'])
    assert pd.api.types.is_numeric_dtype(valid_data['Price'])


def test_read_sales_data_missing_columns_raises_error(tmp_path):
    invalid_file = tmp_path / "invalid.xlsx"
    df = pd.DataFrame({'Product': ['Coffee'], 'Quantity': [1]})
    df.to_excel(invalid_file, index=False)
    with pytest.raises(ValueError, match="Missing required columns"):
        read_sales_data(str(invalid_file))


def test_read_sales_data_filters_negative_quantity():
    valid_data, removed_data = read_sales_data('data/sales_january.xlsx')
    assert (valid_data['Quantity'] >= 0).all()
    assert (removed_data['Quantity'] < 0).any() or removed_data['Quantity'].isna().any()


def test_read_sales_data_filters_null_values():
    valid_data, removed_data = read_sales_data('data/sales_january.xlsx')
    assert valid_data.notna().all().all()


def test_read_sales_data_total_rows_conserved():
    valid_data, removed_data = read_sales_data('data/sales_january.xlsx')
    assert len(valid_data) + len(removed_data) > 0
