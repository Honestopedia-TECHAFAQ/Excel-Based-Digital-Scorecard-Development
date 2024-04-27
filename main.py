import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def upload_file():
    file = st.file_uploader("Upload Excel File", type=["xlsx"])
    if file is not None:
        global df
        df = pd.read_excel(file)
        display_scorecard()

def display_scorecard():
    st.write(df)
    st.subheader("Visualizations")
    selected_columns = st.multiselect("Select columns for visualization", df.columns)

    if selected_columns:
        for column in selected_columns:
            if column in df.columns:
                data = df[column].dropna()
                plt.figure(figsize=(12, 6))
                sns.histplot(data, kde=True)
                plt.title(f'Histogram of {column}')
                st.pyplot()
                plt.figure(figsize=(12, 6))
                sns.boxplot(y=data)
                plt.title(f'Box Plot of {column}')
                st.pyplot()
                if 'Category2' in df.columns:
                    plt.figure(figsize=(12, 6))
                    sns.scatterplot(x='Category2', y=column, data=df)
                    plt.title(f'Scatter Plot of {column}')
                    st.pyplot()

            else:
                st.write(f"Column '{column}' not found in the DataFrame.")
    st.subheader("Summary Statistics")
    st.write(df.describe())
st.title("Digital Scorecard")
upload_file()
