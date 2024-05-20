import streamlit as st
from data import util

table_name = "message"

############################################################################################################
st.title("Get Message(s) by Sender UID")
st.warning("If you see errors, ensure you've created the table(s) first using the `Create & read` pages.")

conn = util.get_connection()
value = st.number_input("Search via Sender UID", step=1)

result_df = conn.query(
    # change "person" to your columnname
    f"select * from {table_name} where sender_id = :value",
    params=dict(value=value),
    ttl=0,  # don't cache results so changes in the database are immediately retrieved
)

num_rows_found = len(result_df)
st.write(f'{num_rows_found} row{"" if num_rows_found ==
         1 else "s"} found for `{value}`')
st.dataframe(
    result_df,
    use_container_width=True,
    hide_index=True,
)

############################################################################################################
st.title("Get Message(s) by Recipient UID")
st.warning("If you see errors, ensure you've created the table(s) first using the `Create & read` pages.")

recipient_id = st.number_input("Search via Recipient UID", step=1)

result_df = conn.query(
    # change "person" to your columnname
    f"select * from {table_name} where recipient_id = :recipient_id",
    params=dict(recipient_id=recipient_id),
    ttl=0,  # don't cache results so changes in the database are immediately retrieved
)
num_rows_found = len(result_df)
st.write(f'{num_rows_found} row{"" if num_rows_found ==
         1 else "s"} found for `{recipient_id}`')
st.dataframe(
    result_df,
    use_container_width=True,
    hide_index=True,
)
