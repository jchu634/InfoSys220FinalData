import streamlit as st
from data import util

st.title("Add a User Review/Rating to the database")
st.warning("If you see errors, ensure you've created the table(s) first using the `Seed and Reset All Tables` pages.")

conn = util.get_connection()
val_message_user = st.text_input("Review (Text): ")
val_rating_user = st.number_input(
    "Rating (INT): ", step=1, max_value=5, min_value=1)
val_recipient_uid_user = st.text_input(
    "User being Reviewed's ID (INT): ")
val_reviewer_uid_user = st.text_input("Reviewer's User ID (INT): ")

list_of_values = [
    val_message_user,
    val_rating_user,
    val_recipient_uid_user,
    val_reviewer_uid_user,
]

# We use a form to control when the page is (re)loaded and hence when the row is attempted to be added.
with st.form("form"):
    submitted = st.form_submit_button("Add new User Rating")

if submitted:
    for value in list_of_values[1::]:
        if not value:
            st.write("Please fill in all necessary fields.")
            st.stop()
    conn._instance.execute(
        # if you add more input values, add a question mark for each one
        f"insert into user_rating (review, rating, rated_user_id, rating_user_id) values (?, ?, ?, ?)",
        list_of_values,
    )
    row_count = conn.query(
        f"select count(1) from user_rating",
        ttl=0,  # don't cache results so changes in the database are immediately retrieved
    )
    st.write(f"user_rating now has {row_count.iat[0, 0]} rows.")

############################################################################################################
st.title("Add a Kitchen Review/Rating to the database")
st.warning("If you see errors, ensure you've created the table(s) first using the `Seed and Reset All Tables` pages.")

conn = util.get_connection()
val_message_kitchen = st.text_input(
    "Review (Text): ", key="kitchen_rating_message")
val_rating_kitchen = st.number_input(
    "Rating (INT): ", step=1, max_value=5, min_value=1, key="kitchen_rating_rating")
val_kitchen_uid_kitchen = st.text_input(
    "Kitchen's ID (INT): ", key="kitchen_rating_kitchen_id")
val_reviewer_uid_kitchen = st.text_input(
    "Reviewer's User ID (INT): ", key="kitchen_rating_reviewer_id")

list_of_values = [
    val_message_kitchen,
    val_rating_kitchen,
    val_kitchen_uid_kitchen,
    val_reviewer_uid_kitchen,
]

# We use a form to control when the page is (re)loaded and hence when the row is attempted to be added.
with st.form("kitchen_rating_form"):
    submitted = st.form_submit_button("Add new Kitchen Rating")

if submitted:
    for value in list_of_values[1::]:
        if not value:
            st.write("Please fill in all necessary fields.")
            st.stop()
    conn._instance.execute(
        # if you add more input values, add a question mark for each one
        f"insert into kitchen_rating (review, rating, rated_kitchen_id, rating_user_id) values (?, ?, ?, ?)",
        list_of_values,
    )
    row_count = conn.query(
        f"select count(1) from kitchen_rating",
        ttl=0,  # don't cache results so changes in the database are immediately retrieved
    )
    st.write(f"kitchen_rating now has {row_count.iat[0, 0]} rows.")
