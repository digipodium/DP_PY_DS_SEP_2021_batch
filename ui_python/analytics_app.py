import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

@st.cache
def load_and_process():
    data = pd.read_excel('../data analysis/Canada.xlsx',
                            skiprows=20,
                            skipfooter=2)
    data.drop(columns=['Type','AREA','REG','DEV'], inplace=True)
    data.rename({
        'OdName':'Country',
        'AreaName':'Continent',
        'RegName' : 'Region',
        'DevName' : 'Status'
    }, axis=1, inplace=True)
    data['Total'] = data[range(1980,2014)].sum(axis=1)
    data.set_index('Country', inplace=True)
    return data

df = load_and_process()
# st.write(df)
def show_comparison():
    countries = df.index.unique()
    sel_countries = st.multiselect("select a few countries",countries)
    graph = st.radio("choose graph style",['line','area','bar'])
    years=list(range(1980,2014))
    fig, ax = plt.subplots(figsize=(20,7))
    df.loc[sel_countries,years].T.plot(kind=graph,ax=ax)
    st.pyplot(fig)

ops= ['show timeline','compare countries','some other thing']
choice = st.selectbox("select an option",ops)
if choice == ops[0]:
    years=list(range(1980,2014))
    countries = df.index.unique()
    country = st.selectbox('select a country',countries)
    startyear = st.slider("select start year",min_value=years[0],max_value=years[-2])
    graph = st.radio("choose graph style",['line','area','bar'])
    c = st.color_picker("select a color")
    fig, ax = plt.subplots(figsize=(20,7))
    year_start = years.index(startyear)
    df.loc[country,years[year_start:]].plot(kind=graph,ax=ax,color=c)
    st.pyplot(fig)

if choice == ops[1]:
    show_comparison()