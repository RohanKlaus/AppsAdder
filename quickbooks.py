import streamlit as st
import pandas as pd
import io
import os

# Set the page config
st.set_page_config(
    page_title="QuickBooks Demo",
    page_icon=":moneybag:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Set the theme colors
st.markdown("""
<style>
body {
    background-color: #C6F7D0; /* light green */
}
.stApp {
    background-color: #C6F7D0; /* light green */
}
.stSidebar {
    background-color: #FFFFFF; /* white */
}
.stSidebar.stSidebarHeader {
    background-color: #FFFFFF; /* white */
}
.stSidebar.stSidebarHeader.stSidebarHeaderText {
    color: #34C759; /* dark green */
}
.stButton {
    background-color: #34C759; /* dark green */
    color: #FFFFFF; /* white */
}
.stButton:hover {
    background-color: #2E865F; /* darker green */
    color: #FFFFFF; /* white */
}
</style>
""", unsafe_allow_html=True)

# Create a sidebar
st.sidebar.header("QuickBooks Demo")
st.sidebar.write("This is a demo of an accounting application called QuickBooks.")

# Create a form to enter data
st.title("Enter Transaction Data")
form = st.form("transaction_form")
date = form.date_input("Date")
description = form.text_input("Description")
amount = form.number_input("Amount")
category = form.selectbox("Category", ["Income", "Expense"])
submit = form.form_submit_button("Submit")

# Create a dataframe to store the data
def load_data():
    if os.path.exists("transactions.csv"):
        return pd.read_csv("transactions.csv")
    else:
        data = {"Date": [], "Description": [], "Amount": [], "Category": []}
        return pd.DataFrame(data)

df = load_data()

# Display the dataframe
st.write(df)

# Save the data to the dataframe when the form is submitted
if submit:
    new_row = {"Date": [date], "Description": [description], "Amount": [amount], "Category": [category]}
    new_df = pd.DataFrame(new_row)
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv("transactions.csv", index=False)

# Create a button to download the data to a CSV file
buffer = io.StringIO()
df.to_csv(buffer, index=False)
st.download_button(
    label="Download CSV",
    data=buffer.getvalue(),
    file_name="transactions.csv",
    mime="text/csv"
)

# Create a button to clear the entries
if st.button("Clear Entries"):
    os.remove("transactions.csv")
    st.write("Entries cleared!")
    st.stop()
