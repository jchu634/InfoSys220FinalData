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
