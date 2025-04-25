import streamlit as st

st.set_page_config(
    page_title="Finquery",
    page_icon="📈"
)

st.title("📈 Finquery")
st.markdown("""
This agent can help you with SQL queries and Python code for data analysis. Configure your MySQL database
            connection using the sidebar.""")
st.markdown("Some sample queries:")
st.markdown("""
            - What were the top-selling products last month?
            - Plot a line chart of the monthly sales data
            - What were the top-selling products of all time?
            - What is the minimum sale amount?
            """)
