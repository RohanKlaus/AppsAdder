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
    background-color: #2E865F; /* dark green */
    color: #FFFFFF; /* white */
}
.stButton:hover {
    background-color: #1E5C3F; /* darker green */
    color: #FFFFFF; /* white */
}
</style>
""", unsafe_allow_html=True)

# Create a sidebar
st.sidebar.header("QuickBooks Demo")
st.sidebar.write("This is a demo of an accounting application called QuickBooks.")

# Create a form to enter data
st.title("Enter Transaction Data")
with st.form("transaction_form"):
    date = st.date_input("Date")
    description = st.text_input("Description")
    amount = st.number_input("Amount")
    category = st.selectbox("Category", ["Income", "Expense"])
    submit = st.form_submit_button("Submit")

# Create a dataframe to store the data
def load_data():
    if os.path.exists("transactions.csv"):
        return pd.read_csv("transactions.csv")
    else:
        data = {"Date": [], "Description": [], "Amount": [], "Category": []}
        return pd.DataFrame(data)

df = load_data()
history = [df.copy()]

# Display the dataframe
if submit:
    new_row = {"Date": [date], "Description": [description], "Amount": [amount], "Category": [category]}
    new_df = pd.DataFrame(new_row)
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv("transactions.csv", index=False)
    history.append(df.copy())

st.write(df)

# Create a button to download the data to a CSV file
buffer = io.StringIO()
df.to_csv(buffer, index=False)
st.download_button(
    label="Download CSV",
    data=buffer.getvalue(),
    file_name="transactions.csv",
    mime="text/csv"
)

# Create a button to delete the recent entry
if st.button("Delete Recent Entry"):
    if os.path.exists("transactions.csv"):
        df = pd.read_csv("transactions.csv")
        df.drop(df.tail(1).index, inplace=True)
        df.to_csv("transactions.csv", index=False)
        st.experimental_rerun()

# Create an "Undo" button to go back to the previous step
if st.button("Undo"):
    if len(history) > 1:
        history.pop()
        df = history[-1].copy()
        df.to_csv("transactions.csv", index=False)
        st.session_state.run = True

# Create a button to refresh the app
if st.button("Refresh"):
    if os.path.exists("transactions.csv"):
        os.remove("transactions.csv")
    st.experimental_rerun()
    st.sidebar.write("")  # Clear the sidebar
    st.write(load_data())  # Refresh the dataframe

if "run" not in st.session_state:
    st.session_state.run = False

if st.session_state.run:
    st.experimental_rerun()

# Add a chart to visualize the data
st.title("Transaction History")
chart_data = df.groupby("Category")["Amount"].sum()
st.bar_chart(chart_data)

# Add a filter to the dataframe
st.title("Filter Transactions")
category_filter = st.selectbox("Filter by Category", ["All", "Income", "Expense"])
if category_filter!= "All":
    filtered_df = df[df["Category"] == category_filter]
    st.write(filtered_df)
else:
    st.write(df)
