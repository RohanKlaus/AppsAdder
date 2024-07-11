import streamlit as st
import pandas as pd

FILENAME = 'quickbooks_data.csv'

# Function to load existing data or create an empty DataFrame
def load_data(filename):
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Customer Name', 'Invoice Amount', 'Expense Category', 'Expense Amount'])
    return df

# Function to save data
def save_data(df, filename):
    df.to_csv(filename, index=False)

# File path and data loading
FILENAME = 'quickbooks_data.csv'
data = load_data(FILENAME)

# App layout and components
st.title('QuickBooks Demo with Data Saving')
st.write('Welcome to the demo of QuickBooks accounting software! Entries will be saved and can be accessed anytime.')

st.sidebar.title('Demo Sections')
app_mode = st.sidebar.selectbox('Choose a demo section',
                                ['Dashboard', 'Invoices', 'Expenses'])

if app_mode == 'Dashboard':
    st.subheader('Dashboard Overview')
    st.write('Display any summary or saved data here.')

elif app_mode == 'Invoices':
    st.subheader('Create Invoice')

    customer_name = st.text_input('Customer Name:')
    invoice_amount = st.number_input('Invoice Amount:', min_value=0.0)

    if st.button('Create Invoice'):
        new_entry = {'Customer Name': customer_name, 'Invoice Amount': invoice_amount,
                     'Expense Category': '', 'Expense Amount': 0.0}  # Ensure all columns are defined
        data = data.append(new_entry, ignore_index=True)
        save_data(data, FILENAME)
        st.success(f'Invoice created for {customer_name} for ${invoice_amount}')

elif app_mode == 'Expenses':
    st.subheader('Track Expenses')

    expense_category = st.selectbox('Select Expense Category',
                                    ['Office Supplies', 'Travel', 'Utilities'])
    expense_amount = st.number_input('Expense Amount:', min_value=0.0)

    if st.button('Track Expense'):
        new_entry = {'Customer Name': '', 'Invoice Amount': 0.0,  # Ensure all columns are defined
                     'Expense Category': expense_category, 'Expense Amount': expense_amount}
        data = data.append(new_entry, ignore_index=True)
        save_data(data, FILENAME)
        st.success(f'Expense of ${expense_amount} recorded for {expense_category}')
