import datetime
import streamlit as st
from data import util
from io import StringIO

st.title("Edit a Kitchen")

conn = util.get_connection()
val_search_review_id = st.number_input(
    "Kitchen ID:", step=1)
val_name = st.text_input("New Kitchen Name: ")
val_pricing = st.text_input("New Pricing: ")
val_address = st.text_input("New Address: ")
val_appliances = st.text_input("New Appliances (comma separated): ")
val_description = st.text_input("New Description: ")

# Kitchen_availability
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
val_date = st.date_input("New Date Available: ", (today, tomorrow))

# Kitchen_image
val_images = st.file_uploader(
    "New images of the kitchen: ", accept_multiple_files=True)
is_new_images = st.checkbox("Replace Existing Images", value=False)

# A query to get the current review details as a preview
preview_results = conn.query(
    'SELECT k.id, name, pricing, address, appliances, description, start_date || " - " || end_date AS availability_range\
        FROM kitchen AS k\
        INNER JOIN kitchen_availability AS ka ON k.id = ka.kitchen_id\
        WHERE k.id = :val_search_review_id',
    params=dict(val_search_review_id=val_search_review_id)
)
st.write("Current Kitchen Details:")
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
        f"UPDATE kitchen SET name = :val_name, pricing = :val_pricing, address = :val_address, appliances = :val_appliances, description = :val_description WHERE id = :val_search_review_id",
        dict(val_name=val_name, val_pricing=val_pricing, val_address=val_address, val_appliances=val_appliances,
             val_description=val_description, val_search_review_id=val_search_review_id)
    )
    conn._instance.execute(
        f"UPDATE kitchen_availability SET start_date = :val_start_date, end_date = :val_end_date WHERE kitchen_id = :val_search_review_id",
        dict(val_start_date=val_date[0], val_end_date=val_date[1],
             val_search_review_id=val_search_review_id)
    )
    if is_new_images:
        conn._instance.execute(
            f"DELETE FROM kitchen_image WHERE kitchen_id = :val_search_review_id",
            dict(val_search_review_id=val_search_review_id)
        )
    for image in val_images:
        conn._instance.execute(
            f"insert into kitchen_image (kitchen_id, image) values (?, ?)",
            [val_search_review_id, image.getvalue()],
        )

    results_df = conn.query(
        'SELECT k.id, name, pricing, address, appliances, description, start_date || " - " || end_date AS availability_range\
        FROM kitchen AS k\
        INNER JOIN kitchen_availability AS ka ON k.id = ka.kitchen_id\
        WHERE k.id = :val_search_review_id',
        params=dict(val_search_review_id=val_search_review_id)
    )
    st.write(f'User Review: {val_search_review_id} has been updated')
    st.dataframe(
        results_df,
        use_container_width=True,
        hide_index=True,
    )
