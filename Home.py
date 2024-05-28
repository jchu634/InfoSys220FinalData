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

st.header('Use Case 5: Manage billing enquiries')
st.subheader("Add Transaction")
st.write("`Add_Transaction`: Add a transaction to the database.")

st.subheader("Edit Transaction")
st.write("`Edit_Transaction`: Edit a transaction in the database.")

st.subheader("Get Transaction")
st.write("`Get_Transaction`: Get transactions from the database. Can be filtered using various parameters.")
