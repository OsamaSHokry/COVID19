import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

sns.set()
import plotly.express as px



st.markdown("<h2 style='text-align: Left; color: #0066CC	;'> Countries where COVID-19 has spread </h1>", unsafe_allow_html=True)

st.markdown("""The data collection and publication of the number of COVID-19 cases and deaths worldwide have been discontinued.
228 Countries and Territories around the world have reported a total of 635,156,038 confirmed cases of the coronavirus COVID-19 that originated from Wuhan, China, and a death toll of 6,592,890 deaths.
""")

df = pd.read_csv("owid-covid-data200.csv")
data = df[['continent', 'location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'population']]
data = data.drop_duplicates()

st.markdown("<h3 style='text-align: Left; color: #0066CC	;'> Top 10 countries have infection cases.  </h3>",
            unsafe_allow_html=True)

data_without_continent = data[
    (data['location'] != 'World')&(data['location'] != 'High income')&(data['location'] != 'Europe')&(
                data['location'] != 'Asia')&(data['location'] != 'European Union')&(
                data['location'] != 'Upper middle income')&(data['location'] != 'North America')&(
                data['location'] != 'Lower middle income')&(data['location'] != 'South America')&(
                data['location'] != 'Africa')&((data['location'] != 'North Korea'))]
data_without_continent_g = data_without_continent.groupby(['location'])['new_cases'].sum().nlargest(10)

data_without_continent_figure = px.bar(data_without_continent_g, height=650, width=1000, text='value',
                                       labels={'location': 'Countries', 'value': 'Number of Cases'}, color='value',
                                       color_discrete_map="identity")
data_without_continent_figure.update_layout(
    title={'text': 'Top 10 countries have infection cases', 'font': {'size': 21}}, title_x=.5)
data_without_continent_figure
st.markdown("""---""")

st.markdown("<h3 style='text-align: Left; color: #0066CC	;'> Bottom 10 countries have infection cases. </h3>",
            unsafe_allow_html=True)
data_without_continent_x_0 = data_without_continent[
    (data_without_continent['new_cases'] >= 1)&(data_without_continent['location'] != 'North Korea')]
data_without_continent_x_01 = data_without_continent_x_0.groupby(['location'])['new_cases'].sum().nsmallest(10)
data_without_continent_x_01_fig = px.bar(data_without_continent_x_01, text='value', height=650, width=1000,
                                         labels={'location': 'Countries', 'value': 'Number of Cases'}, color='value',
                                         color_discrete_map="identity")
data_without_continent_x_01_fig.update_layout(
    title={'text': 'Bottom 10 countries have infection cases', 'font': {'size': 21}}, title_x=.5)
data_without_continent_x_01_fig

st.markdown("""---""")
st.markdown("<h3 style='text-align: Left; color: #0066CC	;'>Top 10 countries have deaths </h3>",
            unsafe_allow_html=True)
top_10_deaths = data_without_continent
top_10_deaths_g = top_10_deaths.groupby('location')['new_deaths'].sum().nlargest(10)
top_10_deaths_g_figure = px.bar(top_10_deaths_g, text='value', height=650, width=1000,
                                labels={'location': 'Countries', 'value': 'Number of Cases'},
                                color_discrete_sequence=['#993999'])
top_10_deaths_g_figure.update_layout(title={'text': 'Top 10 countries have deaths', 'font': {'size': 21}},
                                     title_x=.5)
top_10_deaths_g_figure

st.markdown("""---""")

st.markdown("<h3 style='text-align: Left; color: #0066CC	;'>The bottom 10 countries have infection cases </h3>",
            unsafe_allow_html=True)
top_10_deaths_g_x_0 = top_10_deaths[top_10_deaths['new_deaths'] >= 1]
top_10_deaths_g_x_0 = top_10_deaths_g_x_0.groupby('location')['new_deaths'].sum().nsmallest(10)
top_10_deaths_g_x_0_figure = px.bar(top_10_deaths_g_x_0, text = 'value', height=650, width=1000,
                                labels={'location': 'Countries', 'value': 'Number of Cases'},
                                color_discrete_sequence=['#993999'])
top_10_deaths_g_x_0_figure.update_layout(title={'text': 'Bottom 10 countries have deaths', 'font': {'size': 21}},
                                     title_x=.5)
top_10_deaths_g_x_0_figure


st.markdown("""---""")
st.markdown("<h3 style='text-align: Left; color: #0066CC	;'>The cases vs. deaths for the top 10 countries </h3>",
            unsafe_allow_html=True)


data_without_continent_g = data_without_continent.groupby(['location'])['new_cases'].sum().nlargest(10)
top_10_deaths_g = top_10_deaths.groupby('location')['new_deaths'].sum().nlargest(10)
new_df = data_without_continent.groupby('location')[['new_cases','new_deaths']].sum().nlargest(n = 10, columns= 'new_cases')
top_ten = data_without_continent[(data_without_continent['location'] == 'United States') | (data_without_continent['location'] == 'India') &(data_without_continent['location'] == 'France')  | (data_without_continent['location'] == 'Germany') | (data_without_continent['location'] == 'Brazil')  | (data_without_continent['location'] == 'South Korea') | (data_without_continent['location'] == 'Italy')  | (data_without_continent['location'] == 'United Kingdom')  | (data_without_continent['location'] == 'Japan')  | (data_without_continent['location'] == 'Russia')| (data_without_continent['location'] == 'India')| (data_without_continent['location'] == 'France')]
top_ten_g = top_ten.groupby('location')[['new_cases', 'new_deaths']].sum().nlargest(n = 10 , columns = 'new_cases')
top_ten_fig = px.bar(top_ten_g,text = 'value', height=650, width=1000,
                                labels={'location': 'Countries', 'value': 'Number of cases & deaths'})
top_ten_fig.update_layout(title={'text': 'Cases vs Deaths for top 10 countries', 'font': {'size': 21}},
                                     title_x=.5)
top_ten_fig

st.markdown("""---""")
st.markdown("<h3 style='text-align: Left; color: #0066CC;'>The cases vs. deaths for the top 10 countries | Line chart</h3>", unsafe_allow_html=True)
import matplotlib.pyplot as plt

import seaborn as sns

sns.set(rc={'figure.figsize':(14,9)})

sns.lineplot(data=new_df.new_cases, color="g")

ax2 = plt.twinx()

sns.lineplot(data=new_df.new_deaths, color="b", ax=ax2)

ax=plt.twinx()
ax.figure

st.markdown("""---""")
st.markdown("<h3 style='text-align: Left; color: #0066CC;'> Deaths for 100 infected | for top 10 countries </h3>", unsafe_allow_html=True)
relation_top_ten = (top_ten.groupby('location')['new_deaths'].sum() / top_ten.groupby('location')['new_cases'].sum()) *100
relation_top_ten = round(relation_top_ten,2)
relation_top_ten_fig = px.bar(relation_top_ten, text = 'value', height=650, width=1000,
                                labels={'location': 'Countries', 'value': 'deaths vs cases'},orientation="h", color = 'value')
relation_top_ten_fig.update_layout(title={'text': 'Cases vs Deaths for top 10 countries', 'font': {'size': 21}},
                                     title_x=.5)
relation_top_ten_fig


# st.markdown("""---""")

# st.markdown("<h3 style='text-align: Left; color: #0066CC;'> Getting the highest 10 countries to have cases vs. deaths percentage </h3>", unsafe_allow_html=True)
data_test = data_without_continent
data_test = data_test[(data_test['new_cases'] >= 1) & (data_test['location'] != 'North Korea')]
data_test_d = data_test[(data_test['new_deaths'] >= 1) & (data_test['location'] != 'North Korea')]
total_cases_per_location = data_test.groupby('location')['new_cases'].sum().sort_values()
total_deaths_per_location = data_test_d.groupby('location')['new_deaths'].sum().sort_values()
s = total_deaths_per_location /  total_cases_per_location
testicooo =  total_deaths_per_location /  total_cases_per_location * 100
testicooo = round(testicooo.nlargest(10), 2)
testicooo_fig = px.bar(testicooo , text = 'value', height=650, width=1000,
                                labels={'location': 'Countries', 'value': 'deaths vs cases'},color_discrete_sequence=['#62054D'])
testicooo_fig.update_layout(title={'text': 'Highest percentage across world', 'font': {'size': 21}},
                                     title_x=.5)
# testicooo_fig





st.markdown("""---""")

ques = st.sidebar.radio(

    "Top or Lowest 10 countries | Deaths vs Cases",

    ('Top','Lowest'))



#specifying what should be display when the radio button is selected

if ques == 'Top':

    st.markdown(
        "<h3 style='text-align: Left; color: #0066CC;'> Getting the highest 10 countries to have cases vs. deaths percentage </h3>",
        unsafe_allow_html=True)
    data_test = data_without_continent
    data_test = data_test[(data_test['new_cases'] >= 1)&(data_test['location'] != 'North Korea')]
    data_test_d = data_test[(data_test['new_deaths'] >= 1)&(data_test['location'] != 'North Korea')]
    total_cases_per_location = data_test.groupby('location')['new_cases'].sum().sort_values()
    total_deaths_per_location = data_test_d.groupby('location')['new_deaths'].sum().sort_values()
    s = total_deaths_per_location / total_cases_per_location
    testicooo = total_deaths_per_location / total_cases_per_location * 100
    testicooo = round(testicooo.nlargest(10), 2)
    testicooo_fig = px.bar(testicooo, text='value', height=650, width=1000,
                           labels={'location': 'Countries', 'value': 'deaths vs cases'},
                           color_discrete_sequence=['#62054D'])
    testicooo_fig.update_layout(title={'text': 'Highest percentage across world', 'font': {'size': 21}},
                                title_x=.5)
    testicooo_fig

else:
    st.markdown(
        "<h3 style='text-align: Left; color: #0066CC;'> The lowest 10 countries to have Deaths vs Cases percentage </h3>",
        unsafe_allow_html=True)
    testicooo_s = (total_deaths_per_location / total_cases_per_location) * 100
    testicooo_s = round(testicooo_s.nsmallest(10), 2)
    # print(round(testicooo_s,2))
    last_bar_fig = px.bar(testicooo_s, text='value', height=650, width=1000,
                          labels={'location': 'Countries', 'value': 'deaths vs cases'},
                          color_discrete_sequence=['#62054D'])
    last_bar_fig.update_layout(title={'text': 'Highest percentage across world', 'font': {'size': 21}},
                               title_x=.5)
    last_bar_fig

