import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from typing import Tuple


def visualize_product_statistics(valid_data: pd.DataFrame) -> go.Figure:
    if valid_data.empty:
        return go.Figure()

    valid_data = valid_data.copy()
    valid_data['Sales'] = valid_data['Quantity'] * valid_data['Price']

    product_stats = valid_data.groupby('Product').agg(
        Total_Quantity=('Quantity', 'sum'),
        Total_Sales=('Sales', 'sum')
    ).reset_index()

    fig = px.bar(
        product_stats,
        x='Product',
        y='Total_Quantity',
        title='各商品销售量统计',
        labels={'Product': '商品', 'Total_Quantity': '销售量'},
        color='Total_Quantity',
        color_continuous_scale='Blues'
    )
    fig.update_layout(xaxis_tickangle=-45)
    return fig


def visualize_product_sales(valid_data: pd.DataFrame) -> go.Figure:
    if valid_data.empty:
        return go.Figure()

    valid_data = valid_data.copy()
    valid_data['Sales'] = valid_data['Quantity'] * valid_data['Price']

    product_stats = valid_data.groupby('Product').agg(
        Total_Sales=('Sales', 'sum')
    ).reset_index()

    fig = px.pie(
        product_stats,
        values='Total_Sales',
        names='Product',
        title='各商品销售额占比',
        hole=0.4
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig


def visualize_daily_statistics(valid_data: pd.DataFrame) -> go.Figure:
    if valid_data.empty:
        return go.Figure()

    valid_data = valid_data.copy()
    valid_data['Sales'] = valid_data['Quantity'] * valid_data['Price']
    valid_data['Date'] = pd.to_datetime(valid_data['Date']).dt.strftime('%Y-%m-%d')

    daily_stats = valid_data.groupby('Date').agg(
        Total_Sales=('Sales', 'sum')
    ).reset_index()

    fig = px.line(
        daily_stats,
        x='Date',
        y='Total_Sales',
        title='每日销售额趋势',
        labels={'Date': '日期', 'Total_Sales': '销售额'},
        markers=True
    )
    fig.update_layout(xaxis_tickangle=-45)
    return fig


def visualize_daily_sales_quantity(valid_data: pd.DataFrame) -> go.Figure:
    if valid_data.empty:
        return go.Figure()

    valid_data = valid_data.copy()
    valid_data['Sales'] = valid_data['Quantity'] * valid_data['Price']
    valid_data['Date'] = pd.to_datetime(valid_data['Date']).dt.strftime('%Y-%m-%d')

    daily_stats = valid_data.groupby('Date').agg(
        Total_Quantity=('Quantity', 'sum')
    ).reset_index()

    fig = px.bar(
        daily_stats,
        x='Date',
        y='Total_Quantity',
        title='每日销售量统计',
        labels={'Date': '日期', 'Total_Quantity': '销售量'},
        color='Total_Quantity',
        color_continuous_scale='Viridis'
    )
    fig.update_layout(xaxis_tickangle=-45)
    return fig


def visualize_stacked_bar_chart(valid_data: pd.DataFrame) -> go.Figure:
    if valid_data.empty:
        return go.Figure()

    valid_data = valid_data.copy()
    valid_data['Sales'] = valid_data['Quantity'] * valid_data['Price']
    valid_data['Date'] = pd.to_datetime(valid_data['Date']).dt.strftime('%Y-%m-%d')

    daily_product_stats = valid_data.groupby(['Date', 'Product']).agg(
        Total_Sales=('Sales', 'sum')
    ).reset_index()

    fig = px.bar(
        daily_product_stats,
        x='Date',
        y='Total_Sales',
        color='Product',
        title='每日各产品销售额堆叠图',
        labels={'Date': '日期', 'Total_Sales': '销售额', 'Product': '商品'}
    )
    fig.update_layout(xaxis_tickangle=-45, barmode='stack')
    return fig


def visualize_combined_analysis(valid_data: pd.DataFrame) -> Tuple[go.Figure, go.Figure]:
    if valid_data.empty:
        return go.Figure(), go.Figure()

    valid_data = valid_data.copy()
    valid_data['Sales'] = valid_data['Quantity'] * valid_data['Price']
    valid_data['Date'] = pd.to_datetime(valid_data['Date']).dt.strftime('%Y-%m-%d')

    product_stats = valid_data.groupby('Product').agg(
        Total_Quantity=('Quantity', 'sum'),
        Total_Sales=('Sales', 'sum')
    ).reset_index()

    fig_quantity = px.bar(
        product_stats,
        x='Product',
        y='Total_Quantity',
        title='各商品销售量对比',
        labels={'Product': '商品', 'Total_Quantity': '销售量'},
        color='Total_Quantity',
        color_continuous_scale='Blues'
    )
    fig_quantity.update_layout(xaxis_tickangle=-45)

    fig_sales = px.pie(
        product_stats,
        values='Total_Sales',
        names='Product',
        title='各商品销售额占比',
        hole=0.4
    )
    fig_sales.update_traces(textposition='inside', textinfo='percent+label')

    return fig_quantity, fig_sales