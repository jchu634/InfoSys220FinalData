import streamlit as st
from data import util

st.title("Add a Transaction to the database")
st.warning("If you see errors, ensure you've created the table(s) first using the `Seed and Reset All Tables` pages.")

table_name = "fiscal_transaction"

conn = util.get_connection()
val_transaction_date = st.date_input("Transaction Date: ")
val_transaction_amount = st.number_input("Transaction Amount: ", step=0.01)
val_payee_uid = st.number_input("Payee UserID: ", step=1)
val_payor_uid = st.number_input("Payor UserID: ", step=1)

# if you add any extra input values, make sure they're also added to the list_of_values below. See input_value_3 as an example
# input_value_3 = st.text_input()...

list_of_values = [
    val_transaction_date,
    val_transaction_amount,
    val_payor_uid,
    val_payee_uid,

]

# We use a form to control when the page is (re)loaded and hence when the row is attempted to be added.
with st.form("form"):
    submitted = st.form_submit_button("Add new Transaction")

if submitted:
    for value in list_of_values:
        if not value:
            st.write("Please fill in all fields.")
            st.stop()
    conn._instance.execute(
        f"insert into \
            {table_name} (transaction_date, amount, payor_user_id, payee_user_id) values (?, ?, ?, ?)",
        list_of_values,
    )
    row_count = conn.query(
        f"select count(1) from {table_name}",
        ttl=0,  # don't cache results so changes in the database are immediately retrieved
    )
    st.write(f"{table_name} now has {row_count.iat[0, 0]} rows.")
