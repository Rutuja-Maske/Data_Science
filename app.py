import streamlit as st
import pandas as pd

# Title and text
st.title("My First Streamlit App")
st.write("This is a simple Streamlit app")

# Create a sample dataframe
df = pd.DataFrame({
    'column1': [1, 2, 3, 4],
    'column2': [10, 20, 30, 40]
})

# Display the dataframe
st.write(df)

# Add a slider
number = st.slider('Pick a number', 1, 10)
st.write(f'You selected: {number}')
