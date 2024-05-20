import streamlit as st

st.title("title goes here")

st.write("Generally, every component change results in the page re-running")
st.warning("You can get fancy with how to display text and data")
st.info("Explore some basic components below")

with st.expander("inputting and outputting values"):
    st.write("here is some text")

    inputted_text = st.text_input("text input")
    st.write(inputted_text)

    checkbox_result = st.checkbox("here is a checkbox")
    st.write(checkbox_result)

    selectbox_result = st.selectbox("here is a selectbox", ["option1", "option2", "option3"])
    st.write(selectbox_result)

with st.expander("using forms"):
    with st.form("form"):
        inputted_number = st.number_input("choose a number")
        submitted = st.form_submit_button("submit form")

    if submitted:
        st.write(inputted_number)
    else:
        st.write("form not yet submitted")


with st.expander("displaying data"):
    code = """some_data = [1, 2, 3, 4]"""
    st.code(code)
    some_data = [1, 2, 3, 4]

    st.write("as a table")
    st.table(some_data)
    st.write("as a dataframe")
    st.dataframe(some_data, hide_index=True)

with st.expander("displaying tabular data"):
    code = """some_data = [[1, "a"], [2, "b"], [3, "c"], [4, "d"]]"""
    st.code(code)
    some_data = [[1, "a"], [2, "b"], [3, "c"], [4, "d"]]

    st.write("as a table")
    st.table(some_data)
    st.write("as a dataframe")
    st.dataframe(some_data, hide_index=True)

with st.expander("displaying tabular data with column names"):
    code = """some_data = [
    {"col1": 1, "col2": "a", "col3": 0},
    {"col1": 2, "col2": "b", "col3": 0},
    {"col1": 3, "col2": "c", "col3": 0},
    {"col1": 4, "col2": "d", "col3": 0},
]"""
    st.code(code)
    some_data = [
        {"col1": 1, "col2": "a", "col3": 0},
        {"col1": 2, "col2": "b", "col3": 0},
        {"col1": 3, "col2": "c", "col3": 0},
        {"col1": 4, "col2": "d", "col3": 0},
    ]

    st.write("as a table")
    st.table(some_data)
    st.write("as a dataframe")
    st.dataframe(some_data, hide_index=True)

with st.expander("displaying json"):
    code = """some_data = [
    {"col1": 1, "col2": "a", "col3": 0},
    {"col1": 2, "col2": "b", "col3": 0},
    {"col1": 3, "col2": "c", "col3": 0},
    {"col1": 4, "col2": "d", "col3": 0},
]"""
    st.code(code)
    some_data = [
        {"col1": 1, "col2": "a", "col3": 0},
        {"col1": 2, "col2": "b", "col3": 0},
        {"col1": 3, "col2": "c", "col3": 0},
        {"col1": 4, "col2": "d", "col3": 0},
    ]

    st.write("as json")
    st.write(some_data)
