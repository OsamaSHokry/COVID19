import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns

# get_ipython().run_line_magic('matplotlib', 'inline')
# sns.set()
import plotly.express as px
import streamlit as st
from PIL import Image

st.title("COVID-19")

image = Image.open('Coronavirus-COVID-19.png')
st.image(image, caption='COVID-19', width=900)

# st.markdown(""" <img class="center"> """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: Left; color: Blue;'> Data from Jan 2020 till NOW </h1>", unsafe_allow_html=True)

# st.markdown("# ")
st.markdown("<h2 style='text-align: Left; color: #990000;'> COVID-19 (Corona Virus Disease 2019) </h1>", unsafe_allow_html=True)
st.markdown("""- Caused by a SARS-COV-2 corona virus.
- First identified in Wuhan, Hubei, China. Earliest reported symptoms reported in November 2019.
- First cases were linked to contact with the Huanan Seafood Wholesale Market, which sold live animals.
- On 30 January the WHO declared the outbreak to be a Public Health Emergency of International Concern"
""")
st.markdown("<h2 style='text-align: Left; color: #990000;'> Dataset Features </h1>", unsafe_allow_html=True)
st.markdown("""
* **continent**   -- >   The name of continent of record or row
* **location**    -- > The country of row or record
* **date**        -- > The date of observation
* **total_cases** -- > Total cases (infections) till the date of row
* **new_cases**   -- > The new cases of date
* **total_deaths**-- > Total deaths till the date of row
* **new_deaths**  -- > The new deaths of date
* **population**  -- > The population of country
""")

st.markdown("<h2 style='text-align: Left; color: #990000;'> Important Questions </h1>", unsafe_allow_html=True)
st.markdown("""
* How many infections per continents?
* How many deaths per continents?
* What the percentage between infection cases and deaths per continents?
* Which the top 10 countries have infections cases?
* Which the bottom 10 countries have infection cases?
* Which the top 10 countries have deaths?
* Which the bottom 10 countries have deaths?
* What the percentage between deaths and infections for the top 10 countries have infections?
* What the percentage between deaths and infections for the top 10 countries have Deaths?
* Why did we eliminate the data of north Korea?
* Why the data has missing in continent column?


""")


image = Image.open('bqq6_h675_220127.jpg')
st.image(image, caption='COVID-19', width=500)








