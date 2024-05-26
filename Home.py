import streamlit as st

st.set_page_config(
    page_title="INFOSYS220 Group 45 Data App",
)

st.header("INFOSYS220 Group 45 Data App")

st.subheader("Create or view tables")
st.write("`Create_or_view_tables`: Create or see tables with the option to reset them.")
st.write("\n")

st.subheader("Drop and Recreate tables")
st.write("`Drop_And_Recreate_Tables`: Destroy previous table and recreate a fresh copy in its place.")
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
st.write("`Add_Kitchen`: Add a Kitchen to the database.")

st.subheader("Update Kitchen Details")
st.write("`Update_Kitchen_Details`: Update Kitchen details in the database.")

st.subheader("Add Images to Kitchen")
st.write("`Add_Images_To_Kitchen`: Add images to a Kitchen in the database.")

st.header('Use Case 4: Manage billing')
st.subheader("Toggle User Auto Payments")
st.write("`Toggle_User_Auto_Payments`: Enable/Disable user's auto payment flag in the database.")

st.subheader("Update User Bank Info")
st.write("`Update_User_Bank_Info`: Update user's bank number in the database.")

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
