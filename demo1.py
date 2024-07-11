import streamlit as st
import pandas as pd
import numpy as np

# Create a title for the app
st.title('Quickbooks Accounting App Demo')

# Create a sidebar with navigation options
st.sidebar.title('Navigation')
pages = ['Dashboard', 'Invoices', 'Expenses', 'Reports']
page = st.sidebar.selectbox('Select a page', pages)

# Create a dashboard page
if page == 'Dashboard':
    st.header('Dashboard')
    st.write('Welcome to Quickbooks Accounting App Demo!')
    st.image('quickbooks_logo.png', width=200)

# Create an invoices page
elif page == 'Invoices':
    st.header('Invoices')
    st.write('Manage your invoices here')
    st.image('invoices_screenshot.png', width=400)

    # Add a button to navigate to the next page
    if st.button('Create a new invoice'):
        st.write('You are now on the create invoice page')
        st.image('create_invoice_screenshot.png', width=400)

# Create an expenses page
elif page == 'Expenses':
    st.header('Expenses')
    st.write('Track your expenses here')
    st.image('expenses_screenshot.png', width=400)

    # Add a button to navigate to the next page
    if st.button('Add a new expense'):
        st.write('You are now on the add expense page')
        st.image('add_expense_screenshot.png', width=400)

# Create a reports page
elif page == 'Reports':
    st.header('Reports')
    st.write('View your financial reports here')
    st.image('reports_screenshot.png', width=400)

    # Add a button to navigate to the next page
    if st.button('Generate a new report'):
        st.write('You are now on the generate report page')
        st.image('generate_report_screenshot.png', width=400)

# Run the app
if __name__ == '__main__':
    st.write('This is the Quickbooks Accounting App Demo')
    st.image('quickbooks_logo.png', width=200)
