import streamlit as st
from data import util
import datetime


st.title("Get Transactions via TransactionID")
st.warning("If you see errors, ensure you've created the table(s) first using the `Seed and Reset All Tables` pages.")

conn = util.get_connection()
val_transaction_id = st.number_input("Transaction ID: ", step=1)

sort = st.selectbox("Sort by", ['id', 'transaction_date', 'amount'])
sort_direction = st.checkbox("Sort in descending order", value=False)

result_df = conn.query(
    'SELECT * FROM fiscal_transaction WHERE id = :val_search_uid',
    params=dict(val_search_uid=val_transaction_id),
    ttl=0,  # don't cache results so changes in the database are immediately retrieved
)
result_df = result_df.sort_values(by=sort, ascending=not sort_direction)
util.showResults(result_df, val_transaction_id)

############################################################################################################

st.title("Get Transactions via Payor UID")
st.warning("If you see errors, ensure you've created the table(s) first using the `Seed and Reset All Tables` pages.")

conn = util.get_connection()
val_payor_uid = st.number_input("Payor UID: ", step=1)

sort = st.selectbox("Sort by", ['id', 'transaction_date', 'amount'], key=1)
sort_direction = st.checkbox("Sort in descending order", value=False, key=2)

result_df = conn.query(
    'SELECT * FROM fiscal_transaction WHERE payor_user_id = :val_search_uid',
    params=dict(val_search_uid=val_payor_uid),
    ttl=0,  # don't cache results so changes in the database are immediately retrieved
)
result_df = result_df.sort_values(by=sort, ascending=not sort_direction)
util.showResults(result_df, val_payor_uid)

############################################################################################################

st.title("Get Transactions via Payee UID")
st.warning("If you see errors, ensure you've created the table(s) first using the `Seed and Reset All Tables` pages.")

conn = util.get_connection()
val_payee_uid = st.number_input("Payee UID: ", step=1)

sort = st.selectbox("Sort by", ['id', 'transaction_date', 'amount'], key=3)
sort_direction = st.checkbox("Sort in descending order", value=False, key=4)

result_df = conn.query(
    'SELECT * FROM fiscal_transaction WHERE payee_user_id = :val_search_uid',
    params=dict(val_search_uid=val_payee_uid),
    ttl=0,  # don't cache results so changes in the database are immediately retrieved
)
result_df = result_df.sort_values(by=sort, ascending=not sort_direction)
util.showResults(result_df, val_payee_uid)

############################################################################################################

st.title("Get Transactions within a Date Range")
st.warning("If you see errors, ensure you've created the table(s) first using the `Seed and Reset All Tables` pages.")

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)

conn = util.get_connection()
try:
    val_date_start, val_date_end = st.date_input(
        "Date Range: ", (today, tomorrow))
except ValueError:
    # This is because date_input rturns a single date, before the user has selected the second date
    pass

sort = st.selectbox("Sort by", ['id', 'transaction_date', 'amount'], key=5)
sort_direction = st.checkbox("Sort in descending order", value=False, key=6)

with st.form("form"):
    submitted = st.form_submit_button("Search")

if submitted:
    result_df = conn.query(
        'SELECT * FROM fiscal_transaction WHERE transaction_date BETWEEN :val_date_start AND :val_date_end',
        params=dict(val_date_start=val_date_start, val_date_end=val_date_end),
        ttl=0,  # don't cache results so changes in the database are immediately retrieved
    )
    result_df = result_df.sort_values(by=sort, ascending=not sort_direction)
    util.showResults(result_df, val_payee_uid)
