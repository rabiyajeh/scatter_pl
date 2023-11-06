# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the title of the web application
st.title("Random Scatter Plot Generator")

# Create a user interface using Streamlit
num_points = st.number_input("Number of data points:", min_value=1, max_value=1000, value=100, key="num_points")

if st.button("Generate Scatter Plot", key="generate_button"):
    # Generate random data
    data = {
        'X': np.random.rand(num_points),
        'Y': np.random.rand(num_points)
    }
    df = pd.DataFrame(data)

    # Create scatter plot
    st.write("Scatter Plot:")
    fig, ax = plt.subplots()
    ax.scatter(df['X'], df['Y'])
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    st.pyplot(fig)

    # Display the data in a table
    st.write("Data Table:")
    st.dataframe(df)

# Add some instructions to the user
st.write("Enter the number of data points and click 'Generate Scatter Plot' to create a random scatter plot.")
