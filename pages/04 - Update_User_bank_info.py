import streamlit as st
from data import util

st.title("Edit a User's Bank Info")
st.info("Note: The preview may not update immediately after submitting changes.")

conn = util.get_connection()
val_search_review_id = st.number_input(
    "User ID (INT):", step=1)
val_bank_number = st.text_input("New Bank number: ")

# A query to get the current review details as a preview
preview_results = conn.query(
    'SELECT id, bank_number\
        FROM user\
        WHERE id = :val_search_review_id',
    params=dict(val_search_review_id=val_search_review_id)
)
st.write("Current User Details:")
st.dataframe(
    preview_results,
    use_container_width=True,
    hide_index=True,
)

# Where the query to update stuff actually gets run
with st.form("form"):
    submitted = st.form_submit_button("Update User Bank Info")

if submitted:
    conn._instance.execute(
        f"UPDATE user SET bank_number = :val_bank_number WHERE id = :val_search_review_id",
        dict(val_bank_number=val_bank_number,
             val_search_review_id=val_search_review_id)
    )
    results_df = conn.query(
        'SELECT id, bank_number\
        FROM user\
        WHERE id = :val_search_review_id',
        params=dict(val_search_review_id=val_search_review_id),
        ttl=0,  # don't cache results so changes in the database are immediately retrieved
    )
    st.write(f"User: {val_search_review_id}'s bank info has been updated")
    st.dataframe(
        results_df,
        use_container_width=True,
        hide_index=True,
    )
