import streamlit as st
from data import util

st.title("Create and Read a table")

table_name = "..."  # edit this: choose a table from the VALID_TABLE_NAMES in data/util.py

# We use a form to control when the page is (re)loaded and hence when the data is reset or retrieved.
st.write(f"Table name is `{table_name}`")
select_query = f"select * from {table_name}"
st.write(f"Query is: `{select_query}`")

with st.form("form"):
    should_reset = st.checkbox("(Re)create database with table?")
    submitted = st.form_submit_button("Run")

if submitted:
    conn = util.get_connection()
    if should_reset:
        util.reset_table(conn, table_name)

    result_df = conn.query(
        select_query,
        ttl=0,  # don't cache results
    )
    st.dataframe(
        result_df,
        use_container_width=True,
        hide_index=True,
    )
