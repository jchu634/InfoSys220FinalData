import streamlit as st
from data import util

st.title("Get Kitchens via Kitchen ID")
st.warning("If you see errors, ensure you've created the table(s) first using the `Seed and Reset All Tables` pages.")

conn = util.get_connection()
val_kitchen_id = st.number_input(
    "Kitchen ID (INT): ", step=1)

result_df = conn.query(
    'SELECT k.id, name, pricing, address, appliances, description, start_date || " - " || end_date AS availability_range\
    FROM kitchen AS k\
    INNER JOIN kitchen_availability AS ka ON k.id = ka.kitchen_id\
    WHERE kitchen_id = :val_search_uid',
    params=dict(val_search_uid=val_kitchen_id),
    ttl=0,  # don't cache results so changes in the database are immediately retrieved
)
util.showResultsWImages(result_df, val_kitchen_id)

############################################################################################################

st.title("Get Kitchens via Owner UID")
st.warning("If you see errors, ensure you've created the table(s) first using the `Seed and Reset All Tables` pages.")

conn = util.get_connection()
val_owner_uid = st.number_input(
    "Kitchen Owner User ID (INT):", step=1)
sort = st.selectbox(
    "Sort by", ['id', 'name', 'pricing', 'address', 'owner_id', 'appliances', 'description'], key=1)
sort_direction = st.checkbox("Sort in descending order", value=False)

result_df = conn.query(
    'SELECT k.id, name, pricing, address, appliances, description, start_date || " - " || end_date AS availability_range\
    FROM kitchen AS k\
    INNER JOIN kitchen_availability AS ka ON k.id = ka.kitchen_id\
    WHERE owner_id = :val_search_uid',
    params=dict(val_search_uid=val_owner_uid),
    ttl=0,  # don't cache results so changes in the database are immediately retrieved
)
result_df = result_df.sort_values(by=sort, ascending=not sort_direction)
util.showResultsWImages(result_df, val_owner_uid)

############################################################################################################

st.title("Get Kitchens via Name")
st.warning("If you see errors, ensure you've created the table(s) first using the `Seed and Reset All Tables` pages.")

conn = util.get_connection()
val_kitchen_name = st.text_input(
    "User ID (INT) of User giving Reviews to Kitchen: ")
sort = st.selectbox(
    "Sort by", ['id', 'review', 'rating', 'rated_kitchen_id', 'rating_user_id'])
sort_direction = st.checkbox("Sort in descending order", value=False, key=4)

result_df = conn.query(
    'SELECT k.id, name, pricing, address, appliances, description, strftime("%Y-%m-%d", start_date) || " - " || strftime("%Y-%m-%d", end_date) AS availability_range\
    FROM kitchen AS k\
    INNER JOIN kitchen_availability AS ka ON k.id = ka.kitchen_id\
    WHERE name = :val_search_uid',
    params=dict(val_search_uid=val_kitchen_name),
    ttl=0,  # don't cache results so changes in the database are immediately retrieved
)
result_df = result_df.sort_values(by=sort, ascending=not sort_direction)

util.showResultsWImages(result_df, val_kitchen_name)

############################################################################################################

st.title("Get Kitchens via Address")
st.warning("If you see errors, ensure you've created the table(s) first using the `Seed and Reset All Tables` pages.")

conn = util.get_connection()
val_address = st.text_input(
    "Search via Address: ")
sort = st.selectbox(
    "Sort by", ['id', 'name', 'pricing', 'address', 'owner_id', 'appliances', 'description'], key=5)
sort_direction = st.checkbox("Sort in descending order", value=False, key=6)

result_df = conn.query(
    'SELECT k.id, name, pricing, address, appliances, description, strftime("%Y-%m-%d", start_date) || " - " || strftime("%Y-%m-%d", end_date) AS availability_range\
    FROM kitchen AS k\
    INNER JOIN kitchen_availability AS ka ON k.id = ka.kitchen_id\
    WHERE name = :val_search_uid',
    params=dict(val_search_uid=val_address),
    ttl=0,  # don't cache results so changes in the database are immediately retrieved
)
result_df = result_df.sort_values(by=sort, ascending=not sort_direction)
util.showResultsWImages(result_df, val_address)
