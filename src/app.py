import streamlit as st
import pandas as pd
from sales_reader import read_sales_data


def main():
    st.set_page_config(page_title="Sales Data Analyzer", layout="wide")

    menu = ["Home", "Load Data"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.title("Welcome to Sales Data Analyzer")
        st.write("Use the menu to load and view sales data.")
    elif choice == "Load Data":
        st.title("Load Sales Data")
        st.sidebar.markdown("### Upload or Select Data File")

        uploaded_file = st.sidebar.file_uploader("Choose an Excel file", type=["xlsx", "xls"])

        if uploaded_file is not None:
            try:
                valid_data, removed_data = read_sales_data(uploaded_file)

                st.success(f"Data loaded successfully! Total valid records: {len(valid_data)}")

                tab1, tab2 = st.tabs(["Valid Data", "Removed Data"])

                with tab1:
                    st.subheader(f"Valid Data ({len(valid_data)} records)")
                    if not valid_data.empty:
                        st.dataframe(valid_data, use_container_width=True)
                        st.download_button(
                            "Download Valid Data",
                            valid_data.to_csv(index=False),
                            "valid_data.csv",
                            "text/csv"
                        )
                    else:
                        st.info("No valid data records.")

                with tab2:
                    st.subheader(f"Removed Data ({len(removed_data)} records)")
                    if not removed_data.empty:
                        st.dataframe(removed_data, use_container_width=True)
                        st.download_button(
                            "Download Removed Data",
                            removed_data.to_csv(index=False),
                            "removed_data.csv",
                            "text/csv"
                        )
                    else:
                        st.info("No removed data records.")
            except Exception as e:
                st.error(f"Error loading data: {str(e)}")
        else:
            st.info("Please upload an Excel file to load data.")


if __name__ == "__main__":
    main()