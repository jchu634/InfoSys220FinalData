import streamlit as st
from data import util

st.title("Get a User Review(s)/Rating(s) via Recipient UID")
st.warning("If you see errors, ensure you've created the table(s) first using the `Seed and Reset All Tables` pages.")

conn = util.get_connection()
val_search_uid = st.number_input(
    "User ID (INT) of User receiving Reviews: ", step=1)
sort = st.selectbox(
    "Sort by", ['id', 'rating', 'review', 'rated_user_id', 'rating_user_id'])
sort_direction = st.checkbox("Sort in descending order", value=False)

result_df = conn.query(
    'SELECT id, review, rating, rated_user_id, rating_user_id \
    FROM user_rating \
    WHERE rated_user_id = :val_search_uid',
    params=dict(val_search_uid=val_search_uid),
    ttl=0,  # don't cache results so changes in the database are immediately retrieved
)

# result_df = conn.query(
#     'SELECT user_rating.id as rating_id, review, rating, rated_user_id, rating_user_id, firstName || " " || lastName AS rating_user_full_name \
#     FROM user_rating \
#         INNER JOIN \
#         ( SELECT id, firstName, lastName FROM user ) as user\
#             ON user_rating.rated_user_id = user.id \
#         WHERE rated_user_id = :val_search_uid',
#     params=dict(val_search_uid=val_search_uid),
#     ttl=0,  # don't cache results so changes in the database are immediately retrieved
# )
result_df = result_df.sort_values(by=sort, ascending=not sort_direction)

util.showResults(result_df, val_search_uid)

############################################################################################################
st.title("Get a User Review(s)/Rating(s) via Writer UID")
st.warning("If you see errors, ensure you've created the table(s) first using the `Seed and Reset All Tables` pages.")

conn = util.get_connection()
val_search_uid = st.number_input(
    "User ID (INT) of User giving Reviews: ", step=1)
sort = st.selectbox(
    "Sort by", ['id', 'rating', 'review', 'rated_user_id', 'rating_user_id'], key=2)
sort_direction = st.checkbox("Sort in descending order", value=False, key=3)

result_df = conn.query(
    "select * from user_rating where rating_user_id = :val_search_uid",
    params=dict(val_search_uid=val_search_uid),
    ttl=0,  # don't cache results so changes in the database are immediately retrieved
)
result_df = result_df.sort_values(by=sort, ascending=not sort_direction)
util.showResults(result_df, val_search_uid)

############################################################################################################
st.title("Get a Kitchen Review(s)/Rating(s) via User UID")
st.warning("If you see errors, ensure you've created the table(s) first using the `Seed and Reset All Tables` pages.")

conn = util.get_connection()
val_search_uid = st.number_input(
    "User ID (INT) of User giving Reviews to Kitchen: ", step=1)
sort = st.selectbox(
    "Sort by", ['id', 'review', 'rating', 'rated_kitchen_id', 'rating_user_id'])
sort_direction = st.checkbox("Sort in descending order", value=False, key=4)

result_df = conn.query(
    f"select * from kitchen_rating where rating_user_id = :val_search_uid",
    params=dict(val_search_uid=val_search_uid),
    ttl=0,  # don't cache results so changes in the database are immediately retrieved
)
result_df = result_df.sort_values(by=sort, ascending=not sort_direction)

util.showResults(result_df, val_search_uid)

############################################################################################################
st.title("Get a Kitchen Review(s)/Rating(s) via Kitchen UID")
st.warning("If you see errors, ensure you've created the table(s) first using the `Seed and Reset All Tables` pages.")

conn = util.get_connection()
val_search_uid = st.number_input(
    "Kitchen ID (INT): ", step=1)
sort = st.selectbox(
    "Sort by", ['id', 'review', 'rating', 'rated_kitchen_id', 'rating_user_id'], key=6)
sort_direction = st.checkbox("Sort in descending order", value=False, key=5)

result_df = conn.query(
    f"select * from kitchen_rating where rated_kitchen_id = :val_search_uid",
    params=dict(val_search_uid=val_search_uid),
    ttl=0,  # don't cache results so changes in the database are immediately retrieved
)
result_df = result_df.sort_values(by=sort, ascending=not sort_direction)

util.showResults(result_df, val_search_uid)
