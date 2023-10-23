import itertools
import pandas as pd
data = {
    ('Paragraph', '1.1'): {'25%': True, '33%': True, '50% V': True, '50% H': True, '67%': True, '100%': True},
    ('Paragraph', '1.2'): {'25%': False, '33%': True, '50% V': True, '50% H': True, '67%': True, '100%': True},
    ('Paragraph', '1.3'): {'25%': False, '33%': False, '50% V': True, '50% H': True, '67%': True, '100%': True},
    ('Paragraph', '1.4'): {'25%': False, '33%': False, '50% V': False, '50% H': True, '67%': True, '100%': False},
    ('Paragraph', '1.5'): {'25%': False, '33%': False, '50% V': False, '50% H': False, '67%': True, '100%': False},
    ('Bullet Point (Headings Only)', '2a.1.L'): {'25%': True, '33%': True, '50% V': True, '50% H': True, '67%': True, '100%': True},
    ('Bullet Point (Headings Only)', '2a.2.L'): {'25%': False, '33%': True, '50% V': True, '50% H': False, '67%': True, '100%': False},
    ('Bullet Point (Headings Only)', '2a.1.G'): {'25%': False, '33%': True, '50% V': True, '50% H': True, '67%': True, '100%': False},
    ('Bullet Point (Headings Only)', '2a.2.G'): {'25%': False, '33%': False, '50% V': True, '50% H': True, '67%': True, '100%': False},
    ('Bullet Point (Headings Only)', '2a.3.G'): {'25%': False, '33%': False, '50% V': False, '50% H': False, '67%': True, '100%': False},
    ('Bullet Point (Headings Only)', '2a.4.G'): {'25%': False, '33%': False, '50% V': False, '50% H': False, '67%': True, '100%': False},
    ('Bullet Point (Heading + Body)', '2b.1.L'): {'25%': True, '33%': True, '50% V': True, '50% H': True, '67%': True, '100%': True},
    ('Bullet Point (Heading + Body)', '2b.2.L'): {'25%': False, '33%': True, '50% V': True, '50% H': False, '67%': True, '100%': False},
    ('Bullet Point (Heading + Body)', '2b.1.G'): {'25%': False, '33%': True, '50% V': True, '50% H': True, '67%': True, '100%': False},
    ('Bullet Point (Heading + Body)', '2b.2.G'): {'25%': False, '33%': False, '50% V': True, '50% H': True, '67%': True, '100%': False},
    ('Bullet Point (Heading + Body)', '2b.3.G'): {'25%': False, '33%': False, '50% V': False, '50% H': False, '67%': False, '100%': True},
    ('Image', '3.1'): {'25%': False, '33%': True, '50% V': True, '50% H': True, '67%': True, '100%': False},
    ('Image', '3.2'): {'25%': False, '33%': False, '50% V': True, '50% H': True, '67%': True, '100%': False},
    ('Image', '3.3'): {'25%': False, '33%': False, '50% V': False, '50% H': True, '67%': True, '100%': False},
    ('Image', '3.4'): {'25%': False, '33%': False, '50% V': False, '50% H': False, '67%': True, '100%': False},
    ('Quote', '6.1'): {'25%': True, '33%': True, '50% V': True, '50% H': True, '67%': True, '100%': True},
    ('Quote', '6.2'): {'25%': False, '33%': True, '50% V': True, '50% H': False, '67%': True, '100%': False},
    ('Quote', '6.3'): {'25%': False, '33%': True, '50% V': True, '50% H': False, '67%': True, '100%': False},
    ('List', '7.1'): {'25%': False, '33%': True, '50% V': True, '50% H': True, '67%': True, '100%': False},
    ('List', '7.2'): {'25%': False, '33%': False, '50% V': True, '50% H': True, '67%': True, '100%': False},
    ('List', '7.3'): {'25%': False, '33%': False, '50% V': False, '50% H': True, '67%': True, '100%': False},
    ('List', '7.4'): {'25%': False, '33%': False, '50% V': False, '50% H': False, '67%': True, '100%': False},
}

# Create a MultiIndex from the tuple keys
index = pd.MultiIndex.from_tuples(data.keys(), names=["Element", "Subset"])

# Create the DataFrame
df = pd.DataFrame(data.values(), index=index)


data = {
    "Weights": [0.5, 0.5, 0.5, 0.5, 0.5, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.6, 0.6, 0.6, 0.6, 0.6, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.7],
    "Combined Weight": [0.25, 0.25, 0.25, 0.4, 0.5, 0.15, 0.3, 0.12, 0.18, 0.18, 0.3, 0.3, 0.6, 0.3, 0.42, 0.6, 0.16, 0.24, 0.36, 0.36, 0.2, 0.2, 0.28, 0.36, 0.36, 0.48, 0.6, 0.35, 0.49, 0.63, 0.7],
    "subset": ["1.1", "1.2", "1.3", "1.4", "1.5", "2a.1.L", "2a.2.L", "2a.1.G", "2a.2.G", "2a.3.G", "2a.4.G", "2b.1.L", "2b.2.L", "2b.1.G", "2b.2.G", "2b.3.G", "3.1", "3.2", "3.3", "3.4", "4.1", "4.2", "4.3", "4.4", "6.1", "6.2", "6.3", "7.1", "7.2", "7.3", "7.4"]
}

# Convert the dictionary to a pandas DataFrame
df_2 = pd.DataFrame(data)

import itertools


def recommend_grids(df, df_2, user_inputs):
    user_subsets = [t[1] for t in user_inputs]
    user_rows = df.loc[user_inputs]
    available_percentages = [row.index[row].tolist() for _, row in user_rows.iterrows()]
    all_combinations = list(itertools.product(*available_percentages))

    valid_combinations = [combo for combo in all_combinations if
                          sum(int(percent.split('%')[0]) for percent in combo) == 100]

    if len(valid_combinations) > 0:
        return valid_combinations
    else:
        if len(user_subsets) == 1:
            return [(user_subsets[0], '100%')]
        else:
            subset_weights = df_2[df_2['subset'].isin(user_subsets)]['Combined Weight']
            highest_weight_element = subset_weights.idxmax()
            a = df_2['subset'][highest_weight_element]
            # result = print(f'For {a}, the recommended grid is 100%')
            result = st.subheader(f"""For {a}, the recommended grid is 100% """)

            other = [t for t in user_inputs if t[1] != a]
            result = recommend_grids(df, df_2, other)
            return result

    # Define the Streamlit app
import streamlit as st
import itertools
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



# Define user_inputs here
user_inputs = []

# Define the Streamlit app
def main():
    st.title("Grid Recommendation App")

    # User input section
    st.sidebar.header("User Input")

    # Multi-select for selecting elements
    selected_elements = st.sidebar.multiselect(
        "Select Elements",
        df.index.get_level_values('Element').unique(),
        default=[]  # Initially, no elements are selected
    )

    user_inputs = []  # Initialize an empty list for user inputs

    # Display selected elements
    st.sidebar.header("Selected Elements")
    for element in selected_elements:
        st.sidebar.write(f"Element: {element}")

    # For each selected element, allow selection of subsets
    for element in selected_elements:
        available_subsets = df.loc[element].index.tolist()
        subset = st.sidebar.selectbox(f"Select Subset for {element}", available_subsets)
        user_inputs.append((element, subset))

    # Display user inputs
    st.sidebar.header("Selected Inputs")
    for user_input in user_inputs:
        st.sidebar.write(f"Element: {user_input[0]}, Subset: {user_input[1]}")

    if st.sidebar.button("Get Recommendations"):
        recommendations = recommend_grids(df, df_2, user_inputs)

    # Display recommendations
        st.header("Recommended Grids")
        if len(recommendations) == 0:
            st.error("No valid recommendations found.")

        else:
            st.success("Recommended Grids:")
            for i, recommendation in enumerate(recommendations, start=1):
                 st.subheader(f"Recommendation {i}")            
            
            # Display the recommendation
                 display_grid(recommendation)
            
# Function to display the recommended grid
def display_grid(recommendation):
    fig, ax = plt.subplots(figsize=(6, 4))

    percentages = [int(percent.split('%')[0]) for percent in recommendation]
    labels = [f"{percent}" for percent in recommendation]

    # Create a pie chart
    ax.pie(percentages, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig)

if __name__ == "__main__":
    main()






