import streamlit as st
import pandas as pd

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
    background-color: #f0f0f0;
}
.stApp {
    background-color: #f0f0f0;
}
.stSidebar {
    background-color: #34C759;
}
.stSidebar .stSidebarHeader {
    background-color: #34C759;
}
.stSidebar .stSidebarHeader .stSidebarHeaderText {
    color: #FFFFFF;
}
.stButton {
    background-color: #34C759;
    color: #FFFFFF;
}
.stButton:hover {
    background-color: #2E865F;
    color: #FFFFFF;
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
@st.cache
def load_data():
    data = {"Date": [], "Description": [], "Amount": [], "Category": []}
    return pd.DataFrame(data)

df = load_data()

# Save the data to the dataframe when the form is submitted
if submit:
    new_row = {"Date": [date], "Description": [description], "Amount": [amount], "Category": [category]}
    new_df = pd.DataFrame(new_row)
    df = pd.concat([df, new_df], ignore_index=True)
    st.write(df)

# Create a button to save the data to a CSV file
if st.button("Save to CSV"):
    df.to_csv("transactions.csv", index=False)
    st.write("Data saved to transactions.csv")
