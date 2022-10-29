import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
sns.set()
import plotly.express as px

st.markdown("<h2 style='text-align: Left; color: #0066CC	;'> Data of entire world </h1>", unsafe_allow_html=True)

st.markdown("""The data collection and publication of the number of COVID-19 cases and deaths worldwide have been discontinued.

Please refer to the World Health Organization (WHO) data on COVID-19 and the WHO Weekly Epidemiological and Weekly Operational Updates page for the non-EU/EEA countries. .

ECDC will continue providing weekly updates for EU/EEA Member States and report on an ad-hoc basis about significant events related to COVID-19 globally.

ECDC has been collecting data on the number of COVID-19 cases and deaths for all countries in the EU/EEA and globally for more than two years. The data collected by ECDC will continue to be available in an archived format.""")

df = pd.read_csv("owid-covid-data200.csv")
data = df[['continent', 'location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'population']]
data = data.drop_duplicates()

continents_data = data[
    (data['location'] == 'Europe')|(data['location'] == 'Asia')|(data['location'] == 'North America')|(
                data['location'] == 'South America')|(data['location'] == 'Oceania')|(data['location'] == 'Africa')]


continents_cases_2 = continents_data.groupby('location')[['new_cases','new_deaths']].sum()



st.markdown("<h2 style='text-align: Left; color: #0066CC	;'> World and Continents </h1>", unsafe_allow_html=True)

image_2 = Image.open('9267.jpg')
st.image(image_2, caption='COVID-19', width=700)

st.markdown("""---""")

st.markdown("<h2 style='text-align: Left; color: #0066CC	;'> World and Continents </h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: Left; color: #0066CC	;'> List of continents and the infection number </h3>", unsafe_allow_html=True)
continents_data = data[
    (data['location'] == 'Europe')|(data['location'] == 'Asia')|(data['location'] == 'North America')|(
                data['location'] == 'South America')|(data['location'] == 'Oceania')|(data['location'] == 'Africa')]
continents_cases = continents_data.groupby('location')['new_cases'].sum().nlargest(10)
continents_cases_df = pd.DataFrame(continents_cases)
continents_cases_df = continents_cases_df.reset_index()
continents_cases_df = continents_cases_df.rename(columns = {'location':'Continent', 'new_cases':'New Cases'})
st.write(continents_cases_df)

st.markdown("<h3 style='text-align: Left; color: #0066CC	;'> Chart of continents and the infection number </h3>", unsafe_allow_html=True)

continents_cases_fig = px.bar(continents_cases, text='value', width= 950  , height= 675, labels = {'value': 'Numbers', 'location': 'Contents'}, color_discrete_sequence= ['#0066CC'])
continents_cases_fig.update_layout(title={'text': 'Infection per continent', 'font': {'size': 21}}, title_x=.5)
st.write(continents_cases_fig)

st.markdown("""---""")

st.markdown("<h3 style='text-align: Left; color: #0066CC	;'> List of continents and the number of the deaths </h3>", unsafe_allow_html=True)
continents_deaths = continents_data.groupby('location')['new_deaths'].sum().nlargest(10)
continents_deaths_df = pd.DataFrame(continents_deaths)
continents_deaths_df = continents_deaths_df.reset_index()
continents_deaths_df = continents_deaths_df.rename(columns = {'location': 'Continent', 'new_deaths': 'Number of Deaths'})
continents_deaths_df
st.markdown("<h3 style='text-align: Left; color: #0066CC	;'> Chart of continents and the number of the deaths </h3>", unsafe_allow_html=True)
continents_deaths_fig = px.bar(continents_deaths, text='value', width= 950  , height= 675, labels = {'value': 'Numbers', 'location': 'Contents'}, color_discrete_sequence= ['#0066CC'])
continents_deaths_fig.update_layout(title={'text': 'Deaths per continent', 'font': {'size': 21}}, title_x=.5)

st.write(continents_deaths_fig)

st.markdown("""---""")


image = Image.open('t.png')
st.image(image, width=500)

# st.subheader('Cases vs Deaths | Per continents')
#continents_cases_2 = continents_data.groupby('location')[['new_cases', 'new_deaths']].sum()
# st.write(continents_cases_2)
st.markdown("<h3 style='text-align: Left; color: #0066CC	;'> Chart shows the relationships between cases and deaths </h3>", unsafe_allow_html=True)
continents_cases_2_fig = px.bar(continents_cases_2, text = 'value', labels = {'location':'Contintents', 'value':'Numbers' })

continents_cases_2_fig.update_layout(
    autosize=False,
    width=950,
    height=650
    )
continents_cases_2_fig
st.markdown("""---""")

# st.subheader("Two charts")
# st.write(continents_cases_fig)
# st.write(continents_deaths_fig)

continents_cases_2 = continents_data.groupby('location')[['new_cases','new_deaths']].sum()
# continents_cases_2

st.markdown("<h3 style='text-align: Left; color: #0066CC	;'> Curves for each metric </h3>", unsafe_allow_html=True)


import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize':(14,9)})
from matplotlib.pyplot import figure

figure(figsize=(8, 6), dpi=120)

sns.lineplot(data=continents_cases_2.new_cases, color="g")
ax2 = plt.twinx()
sns.lineplot(data=continents_cases_2.new_deaths, color="b", ax=ax2)
ax = plt.twinx()
ax.figure
st.markdown("""---""")

# st.subheader('Cases vs Deaths | Per continents')
#continents_cases_2 = continents_data.groupby('location')[['new_cases', 'new_deaths']].sum()
# st.write(continents_cases_2)
# st.markdown("<h3 style='text-align: Left; color: #0066CC	;'> Chart shows the relationships between cases and deaths </h3>", unsafe_allow_html=True)
continents_cases_2_fig = px.bar(continents_cases_2, text = 'value', labels = {'location':'Contintents', 'value':'Numbers' })

continents_cases_2_fig.update_layout(
    autosize=False,
    width=950,
    height=650
    )
# continents_cases_2_fig
# st.markdown("""---""")


st.markdown("<h3 style='text-align: Left; color: #0066CC	;'> Chart of Cases vs. Deaths | Per continents </h3>", unsafe_allow_html=True)

percentage_vs_deaths_continents = round(continents_data.groupby('location')['new_deaths'].sum() / continents_data.groupby('location')['new_cases'].sum(), 4) *100
percentage_vs_deaths_continents_fig = px.bar(percentage_vs_deaths_continents, text = 'value', labels = {'location':'Contintents', 'value':'Numbers' },width = 950, height = 675, color="value", color_discrete_sequence= px.colors.sequential.ice_r,orientation="h")
percentage_vs_deaths_continents_fig.update_layout(title={'text': 'Number of deaths per 100 infection', 'font': {'size': 21}}, title_x=.5)
percentage_vs_deaths_continents_fig


st.markdown("""---""")

choice = st.sidebar.selectbox("Contintents", ["World","Africa", "Europe","North America","South America", "Asia","Oceania"])
if choice == "World":
    st.markdown(
        "<h2 style='text-align: Left; color: #0066CC	;'> Time serious for the entire world</h2>",
        unsafe_allow_html=True)

    st.markdown("""---""")
    world_line_data = data[data['location'] == 'World']
    world_line_data = world_line_data[['date', 'new_cases', 'total_cases','new_deaths','total_deaths']]
    world_line_data['date'] = pd.to_datetime(world_line_data['date'])
    ###

    test_plotly = px.line(world_line_data, x = world_line_data['date'] , y =  world_line_data['total_cases'] , width=950, height=675,
                                   color_discrete_sequence=['#0066CC'], labels= {'date':'Date','total_cases':'Total number of cases'}, template = 'seaborn')
    test_plotly.update_layout(title={'text': 'Time Series for cumulative total cases', 'font': {'size': 21}}, title_x=.5)
    test_plotly

    test_plotly_2 = px.line(world_line_data, x = world_line_data['date'] , y =  world_line_data['new_cases'] , width=950, height=675,
                                   color_discrete_sequence=['#0066CC'],labels= {'date':'Date','new_cases':'New Cases'}, template = 'seaborn')
    test_plotly_2.update_layout(title={'text': 'Time series of new cases in entire world', 'font': {'size': 21}}, title_x=.5)
    test_plotly_2
    ###
    test_plotly_d = px.line(world_line_data, x = world_line_data['date'] , y =  world_line_data['total_deaths'] , width=950, height=675,
                                   color_discrete_sequence=['#0066CC'], labels= {'date':'Date','total_deaths':'Total number of Deaths'}, template = 'seaborn')
    test_plotly_d.update_layout(title={'text': 'Time Series for cumulative total deaths', 'font': {'size': 21}}, title_x=.5)
    test_plotly_d
    ###
    test_plotly_2d = px.line(world_line_data, x = world_line_data['date'] , y =  world_line_data['new_deaths'] , width=950, height=675,
                                   color_discrete_sequence=['#0066CC'],labels= {'date':'Date','new_deaths':'New deaths'}, template = 'seaborn')
    test_plotly_2d.update_layout(title={'text': 'Time series of new deaths in entire world', 'font': {'size': 21}}, title_x=.5)
    test_plotly_2d

    ###

elif choice == "Africa":
    st.markdown(
        "<h2 style='text-align: Left; color: #0066CC	;'> Time serious for the entire Africa</h2>",
        unsafe_allow_html=True)
    st.markdown("""---""")

    Africa = continents_data[continents_data['location'] == 'Africa']
    Africa = Africa[['date', 'total_cases', 'new_cases','new_deaths','total_deaths']]
    Africa['date'] = pd.to_datetime(Africa['date'])

    test_plotly_A = px.line(Africa, x = Africa['date'] , y =  Africa['total_cases'] , width=950, height=675,
                                   color_discrete_sequence=['#0066CC'], labels= {'date':'Date','total_cases':'Total number of cases'}, template = 'seaborn')
    test_plotly_A.update_layout(title={'text': 'Time Series for cumulative total cases', 'font': {'size': 21}}, title_x=.5)
    test_plotly_A

    ###
    test_plotly_2_A = px.line(Africa, x = Africa['date'] , y =  Africa['new_cases'] , width=950, height=675,
                                   color_discrete_sequence=['#0066CC'],labels= {'date':'Date','new_cases':'New Cases'}, template = 'seaborn')
    test_plotly_2_A.update_layout(title={'text': 'Time series of new cases in Africa', 'font': {'size': 21}}, title_x=.5)
    test_plotly_2_A
    ###
    test_plotly_d_A = px.line(Africa, x = Africa['date'] , y =  Africa['total_deaths'] , width=950, height=675,
                                   color_discrete_sequence=['#0066CC'], labels= {'date':'Date','total_deaths':'Total number of Deaths'}, template = 'seaborn')
    test_plotly_d_A.update_layout(title={'text': 'Time Series for cumulative total deaths', 'font': {'size': 21}}, title_x=.5)
    test_plotly_d_A
    ###
    test_plotly_2d_A = px.line(Africa, x = Africa['date'] , y =  Africa['new_deaths'] , width=950, height=675,
                                   color_discrete_sequence=['#0066CC'],labels= {'date':'Date','new_deaths':'New deaths'}, template = 'seaborn')
    test_plotly_2d_A.update_layout(title={'text': 'Time series of new deaths in Africa', 'font': {'size': 21}}, title_x=.5)
    test_plotly_2d_A


elif choice == "Europe":
    st.markdown(
        "<h2 style='text-align: Left; color: #0066CC	;'> Time serious for the entire Europe</h2>",
        unsafe_allow_html=True)
    st.markdown("""---""")

    Europe = continents_data[continents_data['location'] == 'Europe']
    Europe = Europe[['date', 'total_cases', 'new_cases','new_deaths','total_deaths']]
    Europe['date'] = pd.to_datetime(Europe['date'])

    test_plotly_e = px.line(Europe, x = Europe['date'] , y =  Europe['total_cases'] , width=950, height=675,
                                   color_discrete_sequence=['#0066CC'], labels= {'date':'Date','total_cases':'Total number of cases'}, template = 'seaborn')
    test_plotly_e.update_layout(title={'text': 'Time Series for cumulative total cases', 'font': {'size': 21}}, title_x=.5)
    test_plotly_e

    ###
    test_plotly_2_e = px.line(Europe, x = Europe['date'] , y =  Europe['new_cases'] , width=950, height=675,
                                   color_discrete_sequence=['#0066CC'],labels= {'date':'Date','new_cases':'New Cases'}, template = 'seaborn')
    test_plotly_2_e.update_layout(title={'text': 'Time series of new cases in Europe', 'font': {'size': 21}}, title_x=.5)
    test_plotly_2_e
    ###
    test_plotly_d_e = px.line(Europe, x = Europe['date'] , y =  Europe['total_deaths'] , width=950, height=675,
                                   color_discrete_sequence=['#0066CC'], labels= {'date':'Date','total_deaths':'Total number of Deaths'}, template = 'seaborn')
    test_plotly_d_e.update_layout(title={'text': 'Time Series for cumulative total deaths', 'font': {'size': 21}}, title_x=.5)
    test_plotly_d_e
    ###
    test_plotly_2d_e = px.line(Europe, x = Europe['date'] , y =  Europe['new_deaths'] , width=950, height=675,
                                   color_discrete_sequence=['#0066CC'],labels= {'date':'Date','new_deaths':'New deaths'}, template = 'seaborn')
    test_plotly_2d_e.update_layout(title={'text': 'Time series of new deaths in Europe', 'font': {'size': 21}}, title_x=.5)
    test_plotly_2d_e

elif choice == "North America":
    st.markdown(
        "<h2 style='text-align: Left; color: #0066CC	;'> Time serious for the entire North America </h2>",
        unsafe_allow_html=True)
    st.markdown("""---""")

    North_America = continents_data[continents_data['location'] == 'North America']
    North_America = North_America[['date', 'total_cases', 'new_cases','new_deaths','total_deaths']]
    North_America['date'] = pd.to_datetime(North_America['date'])

    test_plotly_NA = px.line(North_America, x = North_America['date'] , y =  North_America['total_cases'] , width=950, height=675,
                                   color_discrete_sequence=['#0066CC'], labels= {'date':'Date','total_cases':'Total number of cases'}, template = 'seaborn')
    test_plotly_NA.update_layout(title={'text': 'Time Series for cumulative total cases', 'font': {'size': 21}}, title_x=.5)
    test_plotly_NA

    ###
    test_plotly_2_NA = px.line(North_America, x = North_America['date'] , y =  North_America['new_cases'] , width=950, height=675,
                                   color_discrete_sequence=['#0066CC'],labels= {'date':'Date','new_cases':'New Cases'}, template = 'seaborn')
    test_plotly_2_NA.update_layout(title={'text': 'Time series of new cases in North America', 'font': {'size': 21}}, title_x=.5)
    test_plotly_2_NA
    ###
    test_plotly_d_NA = px.line(North_America, x = North_America['date'] , y =  North_America['total_deaths'] , width=950, height=675,
                                   color_discrete_sequence=['#0066CC'], labels= {'date':'Date','total_deaths':'Total number of Deaths'}, template = 'seaborn')
    test_plotly_d_NA.update_layout(title={'text': 'Time Series for cumulative total deaths', 'font': {'size': 21}}, title_x=.5)
    test_plotly_d_NA
    ###
    test_plotly_2d_NA = px.line(North_America, x = North_America['date'] , y =  North_America['new_deaths'] , width=950, height=675,
                                   color_discrete_sequence=['#0066CC'],labels= {'date':'Date','new_deaths':'New deaths'}, template = 'seaborn')
    test_plotly_2d_NA.update_layout(title={'text': 'Time series of new deaths in North America', 'font': {'size': 21}}, title_x=.5)
    test_plotly_2d_NA


elif choice == "South America":
    st.markdown(
        "<h2 style='text-align: Left; color: #0066CC	;'> Time serious for the entire South America </h2>",
        unsafe_allow_html=True)
    st.markdown("""---""")

    South_America = continents_data[continents_data['location'] == 'South America']
    South_America = South_America[['date', 'total_cases', 'new_cases','new_deaths','total_deaths']]
    South_America['date'] = pd.to_datetime(South_America['date'])

    test_plotly_SA = px.line(South_America, x = South_America['date'] , y =  South_America['total_cases'] , width=950, height=675,
                                   color_discrete_sequence=['#0066CC'], labels= {'date':'Date','total_cases':'Total number of cases'}, template = 'seaborn')
    test_plotly_SA.update_layout(title={'text': 'Time Series for cumulative total cases', 'font': {'size': 21}}, title_x=.5)
    test_plotly_SA

    ###
    test_plotly_2_SA = px.line(South_America, x = South_America['date'] , y =  South_America['new_cases'] , width=950, height=675,
                                   color_discrete_sequence=['#0066CC'],labels= {'date':'Date','new_cases':'New Cases'}, template = 'seaborn')
    test_plotly_2_SA.update_layout(title={'text': 'Time series of new cases in South America', 'font': {'size': 21}}, title_x=.5)
    test_plotly_2_SA
    ###
    test_plotly_d_SA = px.line(South_America, x = South_America['date'] , y =  South_America['total_deaths'] , width=950, height=675,
                                   color_discrete_sequence=['#0066CC'], labels= {'date':'Date','total_deaths':'Total number of Deaths'}, template = 'seaborn')
    test_plotly_d_SA.update_layout(title={'text': 'Time Series for cumulative total deaths', 'font': {'size': 21}}, title_x=.5)
    test_plotly_d_SA
    ###
    test_plotly_2d_SA = px.line(South_America, x = South_America['date'] , y =  South_America['new_deaths'] , width=950, height=675,
                                   color_discrete_sequence=['#0066CC'],labels= {'date':'Date','new_deaths':'New deaths'}, template = 'seaborn')
    test_plotly_2d_SA.update_layout(title={'text': 'Time series of new deaths in South America', 'font': {'size': 21}}, title_x=.5)
    test_plotly_2d_SA

elif choice == "Asia":
    st.subheader("Asia")
elif choice == "Oceania":
    st.subheader("Oceania")





