import streamlit as st
from data import util

st.title("Edit a Transaction in the database")
st.warning("If you see errors, ensure you've created the table(s) first using the `Seed and Reset All Tables` pages.")

table_name = "fiscal_transaction"

conn = util.get_connection()
val_transaction_id = st.number_input("Transaction ID: ", step=1)

val_new_date = st.date_input("New Transaction Date: ")
val_set_new_date = st.checkbox("Set New Date")
val_new_amount = st.number_input("New Transaction Amount: ", step=0.01)
val_set_new_amount = st.checkbox("Set New Amount")

# A query to get the current review details as a preview
preview_results = conn.query(
    'SELECT * FROM fiscal_transaction WHERE id = :val_search_id',
    params=dict(val_search_id=val_transaction_id)
)
st.write("Current Transaction Details:")
st.dataframe(
    preview_results,
    use_container_width=True,
    hide_index=True,
)

# We use a form to control when the page is (re)loaded and hence when the row is attempted to be added.
with st.form("form"):
    submitted = st.form_submit_button("Edit Transaction")

if submitted:
    if not val_set_new_date and not val_set_new_amount:
        st.write("Please select at least one field to update.")
        st.stop()
    if val_set_new_date:
        conn._instance.execute(
            f"UPDATE fiscal_transaction SET transaction_date = :val_new_date WHERE id = :val_transaction_id",
            dict(val_new_date=val_new_date, val_transaction_id=val_transaction_id)
        )
    if val_set_new_amount:
        conn._instance.execute(
            f"UPDATE fiscal_transaction SET amount = :val_new_amount WHERE id = :val_transaction_id",
            dict(val_new_amount=val_new_amount,
                 val_transaction_id=val_transaction_id)
        )
    results_df = conn.query(
        'SELECT * FROM fiscal_transaction WHERE id = :val_search_id',
        params=dict(val_search_id=val_transaction_id),
        ttl=0,  # don't cache results so changes in the database are immediately retrieved
    )
    st.write("Updated Transaction Details:")
    st.dataframe(
        results_df,
        use_container_width=True,
        hide_index=True,
    )
