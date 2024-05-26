import streamlit as st
from data import util

st.title("Drop and Recreate tables")

# We use a form to control when the page is (re)loaded and hence when the data is reset or retrieved.
with st.form("form"):
    table_name = st.selectbox("Table name", util.VALID_TABLE_NAMES)
    submitted = st.form_submit_button("Run")

if submitted:
    assert table_name in util.VALID_TABLE_NAMES, "Invalid table name"

    conn = util.get_connection()

    util.recreate_table(conn, table_name)

    result_df = conn.query(
        f"select * from {table_name}",
        ttl=0,  # don't cache results so changes in the database are immediately retrieved
    )
    st.dataframe(
        result_df,
        use_container_width=True,
        hide_index=True,
    )
