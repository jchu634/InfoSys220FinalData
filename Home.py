import streamlit as st

st.set_page_config(
    page_title="INFOSYS220 Group 45 Data App",
)

st.header("INFOSYS220 Group 45 Data App")

st.subheader("Create & read tables")
st.write("`Create_&_read_tables`: Show rows from a table in a sqlite database.")
# st.info("You will modify this template as the Week 9 lab exercise.")
st.write("\n")

st.subheader("Seeding data")
st.write("`Seed_And_Reset_All_Tables`: Creates all the tables in database and seeds them with data.")
st.info("This needs to be run before all of functions below.")
st.write("\n")

st.subheader('View Table')
st.write("`View_Table`: View a table from the database.")

st.header('Use Case 1: Manage Inbox')
st.subheader("Add Message")
st.write("`Add_Message`: Add a message to the database.")

st.subheader("Get Message")
st.write("`Get_Message`: Get messages from the database.")

st.header('Use Case 2: Manage Review(s)/Rating(s)')
st.info("Note: The schema handles Ratings as a Review without a description.")

st.subheader("Add Review/Rating")
st.write("`Add_Rating`: Add a Review/Rating to the database.")

st.subheader("Edit Review/Rating")
st.write("`Edit_Rating`: Edit a Review/Rating in the database.")

st.subheader("Get Review/Rating")
st.write("`Get_Rating`: Get Review(s)/Rating(s) from the database. Can be filtered using various parameters.")

st.header('Use Case 3: Manage Listings')
st.subheader("Add Kitchen")

st.subheader("Update Kitchen Details")
st.subheader("Add Images to Kitchen")

st.subheader("Create Invoice")
st.subheader("Get Invoice")
st.subheader("Edit Invoice")
st.subheader
st.subheader
st.subheader


st.header("Legacy stuff from lab")
#### This is legacy code, Use as a reference only, delete when done ####


st.subheader("Read public gsheet")
st.write("`Read_public_gsheet`: Connect to a public Google Sheet and display its contents as a Streamlit dataframe.")
st.info("You will modify this template as the Week 9 lab exercise.")
st.write("\n")


def group_project_modify_info_footer():
    st.info("You can modify/reuse this code to suit your group project requirements.", icon="📄")
    st.write("\n")


st.subheader("Get by value")
st.write("`TEMPLATE_Get_by_value`: Get rows from `pet_owners` matching a specific value using a SQL WHERE clause.")
group_project_modify_info_footer()

st.subheader("Get by value (dynamic)")
st.write("`TEMPLATE_Get_by_value_(dynamic)`: Get rows from any table matching a specific value for any column.")
group_project_modify_info_footer()

st.subheader("Add row")
st.write("`TEMPLATE_Add_row`: Add a row to `pet_owners` by providing values.")
group_project_modify_info_footer()

st.subheader("Add row (dynamic)")
st.write("`TEMPLATE_Add_row_(dynamic)`: Add a row to any table.")
group_project_modify_info_footer()
