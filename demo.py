import streamlit as st

# Title and description
st.title('Demo Application')
st.write('Welcome to the demo of our new application!')

# User input
user_input = st.text_input('Enter something:')

# Display output based on input
if user_input:
    st.write('You entered:', user_input)

# Slider example
number = st.slider('Pick a number', 0, 100)
st.write('You selected:', number)

# File upload example
uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
    # Process the file here
    st.write('File uploaded successfully!')
