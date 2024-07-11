import streamlit as st
import random
from googleapiclient.discovery import build
import requests
import os

# Set up your Google Custom Search API credentials
api_key = "YOUR_API_KEY"
cse_id = "YOUR_CSE_ID"

# Set up the search query
query = "quickbooks screenshots"

# Create the search service
service = build("customsearch", "v1", developerKey=api_key)

# Set up the search parameters
params = {
    "q": query,
    "cx": cse_id,
    "searchType": "image",
    "num": 10  # Return 10 results
}

# Perform the search
results = service.cse().list(**params).execute()

# Get the image URLs from the search results
image_urls = [result["link"] for result in results["items"]]

# Create a Streamlit app
st.title("Quickbooks Accounting App Demo")

# Create a sidebar with navigation options
st.sidebar.title("Navigation")
pages = ['Dashboard', 'Invoices', 'Expenses', 'Reports']
page = st.sidebar.selectbox('Select a page', pages)

# Create a dashboard page
if page == 'Dashboard':
    st.header('Dashboard')
    st.write('Welcome to Quickbooks Accounting App Demo!')
    random_image_url = random.choice(image_urls)
    response = requests.get(random_image_url)
    image_data = response.content
    with open("random_image.png", "wb") as f:
        f.write(image_data)
    st.image("random_image.png", width=400)

# Create an invoices page
elif page == 'Invoices':
    st.header('Invoices')
    st.write('Manage your invoices here')
    random_image_url = random.choice(image_urls)
    response = requests.get(random_image_url)
    image_data = response.content
    with open("random_image.png", "wb") as f:
        f.write(image_data)
    st.image("random_image.png", width=400)

    # Add a button to navigate to the next page
    if st.button('Create a new invoice'):
        st.write('You are now on the create invoice page')
        random_image_url = random.choice(image_urls)
        response = requests.get(random_image_url)
        image_data = response.content
        with open("random_image.png", "wb") as f:
            f.write(image_data)
        st.image("random_image.png", width=400)

# Create an expenses page
elif page == 'Expenses':
    st.header('Expenses')
    st.write('Track your expenses here')
    random_image_url = random.choice(image_urls)
    response = requests.get(random_image_url)
    image_data = response.content
    with open("random_image.png", "wb") as f:
        f.write(image_data)
    st.image("random_image.png", width=400)

    # Add a button to navigate to the next page
    if st.button('Add a new expense'):
        st.write('You are now on the add expense page')
        random_image_url = random.choice(image_urls)
        response = requests.get(random_image_url)
        image_data = response.content
        with open("random_image.png", "wb") as f:
            f.write(image_data)
        st.image("random_image.png", width=400)

# Create a reports page
elif page == 'Reports':
    st.header('Reports')
    st.write('View your financial reports here')
    random_image_url = random.choice(image_urls)
    response = requests.get(random_image_url)
    image_data = response.content
    with open("random_image.png", "wb") as f:
        f.write(image_data)
    st.image("random_image.png", width=400)

    # Add a button to navigate to the next page
    if st.button('Generate a new report'):
        st.write('You are now on the generate report page')
        random_image_url = random.choice(image_urls)
        response = requests.get(random_image_url)
        image_data = response.content
        with open("random_image.png", "wb") as f:
            f.write(image_data)
        st.image("random_image.png", width=400)

# Run the app
if __name__ == '__main__':
    st.write('This is the Quickbooks Accounting App Demo')
    random_image_url = random.choice(image_urls)
    response = requests.get(random_image_url)
    image_data = response.content
    with open("random_image.png", "wb") as f:
        f.write(image_data)
    st.image("random_image.png", width=200)
