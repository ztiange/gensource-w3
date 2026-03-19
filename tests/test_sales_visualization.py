import pytest
import pandas as pd
import plotly.graph_objects as go
from src.sales_visualization import (
    visualize_product_statistics,
    visualize_product_sales,
    visualize_daily_statistics,
    visualize_daily_sales_quantity,
    visualize_stacked_bar_chart,
    visualize_combined_analysis
)


def create_test_data():
    return pd.DataFrame({
        'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
        'Product': ['Coffee', 'Tea', 'Coffee', 'Tea'],
        'Quantity': [10, 5, 15, 8],
        'Price': [25.0, 15.0, 25.0, 15.0]
    })


def test_visualize_product_statistics_basic():
    data = create_test_data()
    fig = visualize_product_statistics(data)

    assert isinstance(fig, go.Figure)
    assert len(fig.data) > 0


def test_visualize_product_statistics_empty_dataframe():
    empty_df = pd.DataFrame(columns=['Date', 'Product', 'Quantity', 'Price'])
    fig = visualize_product_statistics(empty_df)

    assert isinstance(fig, go.Figure)
    assert len(fig.data) == 0


def test_visualize_product_sales_basic():
    data = create_test_data()
    fig = visualize_product_sales(data)

    assert isinstance(fig, go.Figure)
    assert len(fig.data) > 0


def test_visualize_product_sales_empty_dataframe():
    empty_df = pd.DataFrame(columns=['Date', 'Product', 'Quantity', 'Price'])
    fig = visualize_product_sales(empty_df)

    assert isinstance(fig, go.Figure)
    assert len(fig.data) == 0


def test_visualize_daily_statistics_basic():
    data = create_test_data()
    fig = visualize_daily_statistics(data)

    assert isinstance(fig, go.Figure)
    assert len(fig.data) > 0


def test_visualize_daily_statistics_empty_dataframe():
    empty_df = pd.DataFrame(columns=['Date', 'Product', 'Quantity', 'Price'])
    fig = visualize_daily_statistics(empty_df)

    assert isinstance(fig, go.Figure)
    assert len(fig.data) == 0


def test_visualize_daily_sales_quantity_basic():
    data = create_test_data()
    fig = visualize_daily_sales_quantity(data)

    assert isinstance(fig, go.Figure)
    assert len(fig.data) > 0


def test_visualize_daily_sales_quantity_empty_dataframe():
    empty_df = pd.DataFrame(columns=['Date', 'Product', 'Quantity', 'Price'])
    fig = visualize_daily_sales_quantity(empty_df)

    assert isinstance(fig, go.Figure)
    assert len(fig.data) == 0


def test_visualize_stacked_bar_chart_basic():
    data = create_test_data()
    fig = visualize_stacked_bar_chart(data)

    assert isinstance(fig, go.Figure)
    assert len(fig.data) > 0


def test_visualize_stacked_bar_chart_empty_dataframe():
    empty_df = pd.DataFrame(columns=['Date', 'Product', 'Quantity', 'Price'])
    fig = visualize_stacked_bar_chart(empty_df)

    assert isinstance(fig, go.Figure)
    assert len(fig.data) == 0


def test_visualize_combined_analysis_basic():
    data = create_test_data()
    fig_quantity, fig_sales = visualize_combined_analysis(data)

    assert isinstance(fig_quantity, go.Figure)
    assert isinstance(fig_sales, go.Figure)
    assert len(fig_quantity.data) > 0
    assert len(fig_sales.data) > 0


def test_visualize_combined_analysis_empty_dataframe():
    empty_df = pd.DataFrame(columns=['Date', 'Product', 'Quantity', 'Price'])
    fig_quantity, fig_sales = visualize_combined_analysis(empty_df)

    assert isinstance(fig_quantity, go.Figure)
    assert isinstance(fig_sales, go.Figure)
    assert len(fig_quantity.data) == 0
    assert len(fig_sales.data) == 0