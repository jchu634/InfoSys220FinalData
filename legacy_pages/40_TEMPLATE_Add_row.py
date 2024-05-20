import streamlit as st
from data import util

st.title("Add a row to pet_owners")

table_name = "pet_owners"

conn = util.get_connection()
person_value = st.text_input("Value for person (text)")
pet_value = st.text_input("Value for pet (text)")
# if you add any extra input values, make sure they're also added to the list_of_values below. See input_value_3 as an example
# input_value_3 = st.text_input()...

list_of_values = [
    person_value,
    pet_value,
    # input_value_3,
]
# We use a form to control when the page is (re)loaded and hence when the row is attempted to be added.
with st.form("form"):
    submitted = st.form_submit_button("Add new row")

if submitted:
    conn._instance.execute(
        f"insert into {table_name} values (?, ?)", # if you add more input values, add a question mark for each one
        list_of_values,
    )
    row_count = conn.query(
        f"select count(1) from {table_name}",
        ttl=0, # don't cache results so changes in the database are immediately retrieved
    )
    st.write(f"{table_name} now has {row_count.iat[0,0]} rows.")
