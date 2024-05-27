import streamlit as st
from data import util

st.title("Add a message to the database")
st.warning("If you see errors, ensure you've created the table(s) first using the `Seed and Reset All Tables` pages.")

table_name = "message"

conn = util.get_connection()
val_message = st.text_input("Message Text: ")
val_message_title = st.text_input("Message Title: ")
val_sender_uid = st.text_input("Message Sender's User ID (INT): ")
val_recipient_uid = st.text_input("Message Recipient's User ID (INT): ")
# if you add any extra input values, make sure they're also added to the list_of_values below. See input_value_3 as an example
# input_value_3 = st.text_input()...

list_of_values = [
    val_message,
    val_message_title,
    val_sender_uid,
    val_recipient_uid,
]

# We use a form to control when the page is (re)loaded and hence when the row is attempted to be added.
with st.form("form"):
    submitted = st.form_submit_button("Add new message")

if submitted:
    for value in list_of_values:
        if not value:
            st.write("Please fill in all fields.")
            st.stop()
    conn._instance.execute(
        # if you add more input values, add a question mark for each one
        f"insert into {
            table_name} (message, message_title, sender_id, recipient_id) values (?, ?, ?, ?)",
        list_of_values,
    )
    row_count = conn.query(
        f"select count(1) from {table_name}",
        ttl=0,  # don't cache results so changes in the database are immediately retrieved
    )
    st.write(f"{table_name} now has {row_count.iat[0, 0]} rows.")
