import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="QuickBooks Demo",
    page_icon=":money_with_wings:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Set background color and text color
st.markdown(
    """
    <style>
    body {
        color: black;
        background-color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and description
st.title('QuickBooks Demo')
st.markdown('<style>h1{color: #8bc34a;}</style>', unsafe_allow_html=True)
st.write('Welcome to the demo of QuickBooks accounting software!')

# Sidebar navigation
st.sidebar.title('Demo Sections')
st.sidebar.markdown('<style>h2{color: #8bc34a;}</style>', unsafe_allow_html=True)
app_mode = st.sidebar.selectbox('Choose a demo section',
                                ['Dashboard', 'Invoices', 'Expenses'])

# Simulate dashboard
if app_mode == 'Dashboard':
    st.subheader('Dashboard Overview')
    st.markdown('<style>h3{color: #8bc34a;}</style>', unsafe_allow_html=True)

    # Simulated data
    total_sales = 100000
    total_expenses = 50000
    net_profit = total_sales - total_expenses

    st.write(f'Total Sales: ${total_sales}')
    st.write(f'Total Expenses: ${total_expenses}')
    st.write(f'Net Profit: ${net_profit}')

# Simulate invoices
elif app_mode == 'Invoices':
    st.subheader('Create Invoice')
    st.markdown('<style>h3{color: #8bc34a;}</style>', unsafe_allow_html=True)

    customer_name = st.text_input('Customer Name:')
    invoice_amount = st.number_input('Invoice Amount:', min_value=0.0)

    if st.button('Create Invoice'):
        st.success(f'Invoice created for {customer_name} for ${invoice_amount}')

# Simulate expenses
elif app_mode == 'Expenses':
    st.subheader('Track Expenses')
    st.markdown('<style>h3{color: #8bc34a;}</style>', unsafe_allow_html=True)

    expense_category = st.selectbox('Select Expense Category',
                                    ['Office Supplies', 'Travel', 'Utilities'])
    expense_amount = st.number_input('Expense Amount:', min_value=0.0)

    if st.button('Track Expense'):
        st.success(f'Expense of ${expense_amount} recorded for {expense_category}')
