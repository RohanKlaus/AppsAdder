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
    st.image('images/invoices_screenshot.png', width=400)

    # Add a button to navigate to the next page
    if st.button('Create a new invoice'):
        st.write('You are now on the create invoice page')
        st.image('images/create_invoice_screenshot.png', width=400)

# Create an expenses page
elif page == 'Expenses':
    st.header('Expenses')
    st.write('Track your expenses here')
    st.image('images/expenses_screenshot.png', width=400)

    # Add a button to navigate to the next page
    if st.button('Add a new expense'):
        st.write('You are now on the add expense page')
        st.image('images/add_expense_screenshot.png', width=400)

# Create a reports page
elif page == 'Reports':
    st.header('Reports')
    st.write('View your financial reports here')
    st.image('https://www.google.com/search?sca_esv=551c7f8375920942&sca_upv=1&rlz=1C1OPNX_enIN1092IN1092&sxsrf=ADLYWIJbCqIXcLemiz5xH6f9ChWdOCMANg:1720664679272&q=quickbooks&udm=2&fbs=AEQNm0AeMNWKf4PpcKMI-eSa16lJoRPMIuyspCxWO6iZW9F1Nu5UXlEfGU2YX1CrW9Nmm9Q3JIJZUqyMsLxos5tPU_UnqJ9Yac9VVJRGWfC4j5Vo8iVdmp0yHcykFiMIS9jUiQbN_U_vVDhXuiv9WtRFP3w1xyEfuag4hZCMtDiWR5yvDhV6r1V8aWdr2pDV3Csi4oLpFhod-EYWrnzWwrB0T8SfNvjCyg&sa=X&sqi=2&ved=2ahUKEwjE9_C3952HAxVSxzgGHfKIBRwQtKgLegQIDBAB&biw=1536&bih=695&dpr=1.25#vhid=jc9z2xSvfBWXrM&vssid=mosaic', width=400)

    # Add a button to navigate to the next page
    if st.button('Generate a new report'):
        st.write('You are now on the generate report page')
        st.image('images/generate_report_screenshot.png', width=400)

# Run the app
if __name__ == '__main__':
    st.write('This is the Quickbooks Accounting App Demo')
    st.image('quickbooks_logo.png', width=200)
