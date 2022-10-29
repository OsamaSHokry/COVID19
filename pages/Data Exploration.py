import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

sns.set()
import plotly.express as px

st.markdown("<h2 style='text-align: Left; color: #990000;'> COVID-19 (Corona Virus Disease 2019) </h1>",
            unsafe_allow_html=True)

df = pd.read_csv("owid-covid-data200.csv")

st.markdown("<h2 style='text-align: Left; color: #333399	;'> Data Exploration </h1>", unsafe_allow_html=True)
st.markdown("""Data exploration definition: Data exploration refers to the initial step in data analysis in which data analysts use data visualization and statistical techniques to describe dataset characterizations, such as size, quantity, and accuracy, in order to better understand the nature of the data.

Data exploration techniques include both manual analysis and automated data exploration software solutions that visually explore and identify relationships between different data variables, the structure of the dataset, the presence of outliers, and the distribution of data values in order to reveal patterns and points of interest, enabling data analysts to gain greater insight into the raw data.

Data is often gathered in large, unstructured volumes from various sources and data analysts must first understand and develop a comprehensive view of the data before extracting relevant data for further analysis, such as univariate, bivariate, multivariate, and principal components analysis.
""")

st.markdown("<h2 style='text-align: Left; color: #990000;'> Quick Look </h1>", unsafe_allow_html=True)

image_2 = Image.open('01.png')
st.image(image_2, caption='COVID-19', width=700)

# The Data with useful columns
data = df[['continent', 'location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'population']]

choice = st.sidebar.selectbox("SubMenu", ["Data Info", "Data cleaning & preparing"])
if choice == "Data Info":
    st.markdown("<h3 style='text-align: Left; color: #333399	;'> Data Describe: </h3>", unsafe_allow_html=True)
    st.write(data.describe())
    st.markdown("""---""")
    st.markdown("<h3 style='text-align: Left; color: #333399	;'> Last 10 Rows: </h3>", unsafe_allow_html=True)
    st.table(data.tail(10))
    st.markdown("""---""")

elif choice == "Data cleaning & preparing":
    st.markdown("<h2 style='text-align: Left; color: #660000;'> Data cleaning & preparing </h2>",
                unsafe_allow_html=True)
    data['date'] = pd.to_datetime(data['date'])
    data = data.drop_duplicates()

    # check the count of missing values in dataset
    data.isnull().values.sum()

    # Get the percentage of missing values in dataset more 0
    null_data = data.isnull().sum()
    null_data = null_data[null_data >= 1]

    # check the percentage of missing values in dataset per coloums
    null_values = data.isnull().values.sum()
    null_percentage = round(((data.isnull().sum() / data.shape[0]) * 100), 2)

    null_df = pd.DataFrame({'Column Name': data.columns, 'Null Count': null_values, 'null_percentage': null_percentage})
    null_df.reset_index(drop=True, inplace=True)

    null_df.sort_values(by='null_percentage', ascending=False)
    st.markdown("<h3 style='text-align: Left; color: #333399;'> The percentage of missing data per feature </h3>",
                unsafe_allow_html=True)
    st.write(null_df)
    st.markdown("""---""")
    st.markdown("<h3 style='text-align: Left; color: #333399;'> Funnel chart for missing data </h3>",
                unsafe_allow_html=True)
    missing_plot = data.isnull().sum()
    missing_plot = missing_plot[data.isnull().sum() >= 1]
    missing_plot_fig = px.funnel(missing_plot, text='value', labels={'index': 'Features'}, width=825, height=650)
    missing_plot_fig.update_layout(title={'text': 'Missing value per features', 'font': {'size': 21}}, title_x=.5)
    missing_plot_fig
    st.markdown("""---""")
    st.markdown("<h3 style='text-align: Left; color: #CC0000;'> Why are missing continents ? </h3>",
                unsafe_allow_html=True)

    st.text("Check the data has missing continents values")
    missin_contienent = data[pd.isnull(data["continent"])]
    st.write(missin_contienent.head())
    st.text("Locations have missing values in contienent")
    # st.write(missin_contienent["location"].unique())
    missing_location = pd.DataFrame(missin_contienent["location"].unique())
    st.table(missing_location)
    st.markdown("""---""")

    st.markdown("<h3 style='text-align: Left; color: #333399;'> Create a data set without continents </h3>",
                unsafe_allow_html=True)
    data_without_continent = data[data['continent'].notna()]
    st.write(data_without_continent.tail())

    st.markdown("<h3 style='text-align: Left; color: #333399;'> Chart after decreasing missing values </h3>",
                unsafe_allow_html=True)
    missing_plot_without_continent = data_without_continent.isnull().sum()
    missing_plot_without_continent = missing_plot_without_continent[data_without_continent.isnull().sum() >= 1]
    missing_plot_without_continent_fig = px.funnel(missing_plot_without_continent, text='value',
                                                   labels={'index': 'Features'}, width=825, height=650)
    missing_plot_without_continent_fig.update_layout(title={'text': 'Missing value per features', 'font': {'size': 21}},
                                                     title_x=.5)
    missing_plot_without_continent_fig

image = Image.open('001.png')
st.image(image, caption='To be ...', width=500)
