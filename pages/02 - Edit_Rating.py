import streamlit as st
from data import util

st.title("Edit a User Review")

conn = util.get_connection()
val_search_review_id = st.number_input(
    "User Review ID (INT): ", step=1)
val_new_rating = st.number_input(
    "New Rating: ", step=1, min_value=1, max_value=5)
val_new_description = st.text_input("New Description: ")

# A query to get the current review details as a preview
preview_results = conn.query(
    'SELECT id, review, rating, rated_user_id, rating_user_id \
        FROM user_rating \
        WHERE id = :val_search_review_id',
    params=dict(val_search_review_id=val_search_review_id)
)
st.write("Current Review:")
st.dataframe(
    preview_results,
    use_container_width=True,
    hide_index=True,
)

# Where the query to update stuff actually gets run
with st.form("form"):
    submitted = st.form_submit_button("Update Review")

if submitted:
    conn._instance.execute(
        f"UPDATE user_rating SET rating = :val_new_rating, review = :val_new_description WHERE id = :val_search_review_id",
        dict(val_new_rating=val_new_rating, val_new_description=val_new_description,
             val_search_review_id=val_search_review_id),
    )
    results_df = conn.query(
        'SELECT id, review, rating, rated_user_id, rating_user_id \
        FROM user_rating \
        WHERE id = :val_search_review_id',
        params=dict(val_search_review_id=val_search_review_id),
        ttl=0,  # don't cache results so changes in the database are immediately retrieved
    )
    st.write(f'User Review: {val_search_review_id} has been updated')
    st.dataframe(
        results_df,
        use_container_width=True,
        hide_index=True,
    )

############################################################################################################

st.title("Edit a Kitchen Review")
conn = util.get_connection()
val_search_review_id = st.number_input(
    "Kitchen Review ID (INT): ", step=1)
val_new_rating = st.number_input(
    "New Rating: ", step=1, min_value=1, max_value=5, key=2)
val_new_description = st.text_input("New Description: ", key=3)

# A query to get the current review details as a preview
preview_results = conn.query(
    'SELECT id, review, rating, rated_kitchen_id, rating_user_id \
        FROM kitchen_rating \
        WHERE id = :val_search_review_id',
    params=dict(val_search_review_id=val_search_review_id)
)
st.write("Current Review:")
st.dataframe(
    preview_results,
    use_container_width=True,
    hide_index=True,
)

# Where the query to update stuff actually gets run
with st.form("KitchenReviewEditUpdateForm"):
    submitted = st.form_submit_button("Update Review")

if submitted:
    conn._instance.execute(
        f"UPDATE kitchen_rating SET rating = :val_new_rating, review = :val_new_description WHERE id = :val_search_review_id",
        dict(val_new_rating=val_new_rating, val_new_description=val_new_description,
             val_search_review_id=val_search_review_id),
    )
    results_df = conn.query(
        'SELECT id, review, rating, rated_kitchen_id, rating_user_id \
        FROM kitchen_rating \
        WHERE id = :val_search_review_id',
        params=dict(val_search_review_id=val_search_review_id),
        ttl=0,  # don't cache results so changes in the database are immediately retrieved
    )
    st.write(f'User Review: {val_search_review_id} has been updated')
    st.dataframe(
        results_df,
        use_container_width=True,
        hide_index=True,
    )
