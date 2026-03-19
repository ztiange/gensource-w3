import streamlit as st
import pandas as pd
from sales_reader import read_sales_data
from sales_statistics import (
    calculate_product_statistics,
    calculate_daily_statistics,
    get_statistics_summary
)


def main():
    st.set_page_config(page_title="销售数据分析系统", layout="wide")

    st.title("销售数据加载")

    col1, col2 = st.columns([2, 1])
    with col1:
        uploaded_file = st.file_uploader("选择 Excel 文件", type=["xlsx", "xls"])
    with col2:
        st.write("")

    if uploaded_file is not None:
        try:
            valid_data, removed_data = read_sales_data(uploaded_file)
            st.session_state['valid_data'] = valid_data
            st.session_state['removed_data'] = removed_data

            st.success(f"数据加载成功！有效记录数：{len(valid_data)}")

            tab1, tab2, tab3 = st.tabs(["有效数据", "已剔除数据", "统计信息"])

            with tab1:
                st.subheader(f"有效数据 ({len(valid_data)} 条记录)")
                if not valid_data.empty:
                    st.dataframe(valid_data, use_container_width=True)
                    st.download_button(
                        "下载有效数据",
                        valid_data.to_csv(index=False),
                        "valid_data.csv",
                        "text/csv"
                    )
                else:
                    st.info("没有有效数据记录。")

            with tab2:
                st.subheader(f"已剔除数据 ({len(removed_data)} 条记录)")
                if not removed_data.empty:
                    st.dataframe(removed_data, use_container_width=True)
                    st.download_button(
                        "下载已剔除数据",
                        removed_data.to_csv(index=False),
                        "removed_data.csv",
                        "text/csv"
                    )
                else:
                    st.info("没有已剔除数据记录。")

            with tab3:
                st.subheader("概览统计")
                summary = get_statistics_summary(valid_data)
                m1, m2, m3 = st.columns(3)
                m1.metric("商品种类", summary['total_products'])
                m2.metric("总销量", summary['total_quantity'])
                m3.metric("总销售额", f"¥{summary['total_sales']:.2f}")

                st.subheader("商品销售统计")
                product_stats = calculate_product_statistics(valid_data)
                if not product_stats.empty:
                    st.dataframe(product_stats, use_container_width=True)
                    st.download_button(
                        "下载商品统计",
                        product_stats.to_csv(index=False),
                        "product_statistics.csv",
                        "text/csv"
                    )
                else:
                    st.info("没有商品统计数据。")

                st.subheader("每日销售统计")
                daily_stats = calculate_daily_statistics(valid_data)
                if not daily_stats.empty:
                    st.dataframe(daily_stats, use_container_width=True)
                    st.download_button(
                        "下载每日统计",
                        daily_stats.to_csv(index=False),
                        "daily_statistics.csv",
                        "text/csv"
                    )
                else:
                    st.info("没有每日统计数据。")
        except Exception as e:
            st.error(f"加载数据错误：{str(e)}")
    else:
        st.info("请上传 Excel 文件以加载数据。")


if __name__ == "__main__":
    main()