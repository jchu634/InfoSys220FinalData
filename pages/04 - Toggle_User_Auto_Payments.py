import streamlit as st
from data import util

st.title("Toggle a User's Auto Payments Setting")


conn = util.get_connection()
val_search_review_id = st.number_input(
    "User ID (INT):", step=1)
val_enable_auto_payments = st.checkbox("Enable Auto Payments", value=False)

with st.form("form"):
    submitted = st.form_submit_button("Update User Bank Info")

if submitted:
    conn._instance.execute(
        f"UPDATE user SET auto_payments = :val_enable_auto_payments WHERE id = :val_search_review_id",
        dict(val_enable_auto_payments=val_enable_auto_payments,
             val_search_review_id=val_search_review_id)
    )
    results_df = conn.query(
        'SELECT id, auto_payments\
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
