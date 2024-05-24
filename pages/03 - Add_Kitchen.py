import datetime
import streamlit as st
from data import util
from io import StringIO

st.title("Add a kitchen to the database")
st.info("The schema treats appliances as a strings.  \nThe application is assumed to handle the conversion of strings to a list of strings.")
st.warning("If you see errors, ensure you've created the table(s) first using the `Seed and Reset All Tables` pages.")

conn = util.get_connection()

# Kitchen
val_name = st.text_input("Kitchen Name: ")
val_pricing = st.text_input("Pricing: ")
val_address = st.text_input("Address: ")
val_owner_uid = st.text_input("Owner's User ID (INT): ")
val_appliances = st.text_input("Appliances (comma separated): ")
val_description = st.text_input("(OPTIONAL) Description: ")
val_size = st.number_input("(OPTIONAL) Size (Square Meters)(INT): ", step=1)

# Kitchen_availability
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
val_date = st.date_input("Date Available: ", (today, tomorrow))

# Kitchen_image
val_images = st.file_uploader(
    "(OPTIONAL) Upload images of the kitchen: ", accept_multiple_files=True)

list_of_values = [
    val_name,
    val_pricing,
    val_address,
    val_owner_uid,
    val_appliances,
    val_description,
    val_size
]

# We use a form to control when the page is (re)loaded and hence when the row is attempted to be added.
with st.form("form"):
    submitted = st.form_submit_button("Add new kitchen")

if submitted:
    if not val_name or val_pricing or val_address or val_owner_uid or val_appliances or val_date:
        st.write("Please fill in necessary fields.")
        st.stop()
    result = conn._instance.execute(
        f"select max(id) from kitchen"
    )
    max_id = result.fetchone()[0]
    next_id = (max_id or 0) + 1
    list_of_values = [next_id] + list_of_values
    conn._instance.execute(
        f"insert into kitchen (id, name, pricing, address, owner_id, appliances, description, size) values (?,?, ?, ?, ?, ?, ?, ?)",
        list_of_values,
    )
    conn._instance.execute(
        f"insert into kitchen_availability (kitchen_id, start_date, end_date) values (?, ?, ?)",
        [next_id] + list(val_date),
    )
    for image in val_images:
        conn._instance.execute(
            f"insert into kitchen_image (kitchen_id, image) values (?, ?)",
            [next_id, StringIO(image.getvalue().decode("utf-8"))],
        )
    row_count = conn.query(
        f"select count(1) from kitchen",
        ttl=0,  # don't cache results so changes in the database are immediately retrieved
    )
    st.write(f"kitchen now has {row_count.iat[0, 0]} rows.")
