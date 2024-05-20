import streamlit as st
from data import util

st.title("Seed and Reset All Tables")

# We use a form to control when the page is (re)loaded and hence when the data is reset or retrieved.
with st.form("form"):
    submitted = st.form_submit_button("Seed and Reset Tables")

if submitted:
    for table_name in util.VALID_TABLE_NAMES:
        conn = util.get_connection()
        util.reset_table(conn, table_name)

    st.write("All tables have been reset and seeded.")
