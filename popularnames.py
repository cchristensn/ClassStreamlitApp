import plotly.express as px
import pandas as pd
import streamlit as st

st.title('Popular Names')

url ='https://github.com/esnt/Data/raw/main/Names/popular_names.csv'
df = pd.read_csv(url)

name = st.text_input('Enter a name', value='John')
name_df = df[df['name']==name]
#name_df = name_df.groupby('year')['n'].sum().reset_index()
tab1, tab2 = st.tabs(['Female', 'Male'])

with tab1:
    plotF_df = name_df[name_df['sex']=='F']
    figF = px.line(data_frame=plotF_df, x = 'year', y='n')
    st.header(f'{name} over time')
    st.plotly_chart(figF)

with tab2:
    plotM_df = name_df[name_df['sex']=='M']
    figM = px.line(data_frame=plotM_df, x = 'year', y='n')
    st.header(f'{name} over time')
    st.plotly_chart(figM)


with st.sidebar:
    year = st.slider('Chose a year', 1910, 2021)
    st.header(f'Top names by {year}')
    year_df =df[df['year']==year]

    girls_names = year_df[year_df.sex == 'F'].head().reset_index()
    boys_names = year_df[year_df.sex == 'M'].head().reset_index()

    newDF =pd.DataFrame({"Girls": girls_names['name'],
                         'Boys': boys_names['name']})
    
    newDF = newDF.set_index(pd.Series([1, 2, 3, 4, 5]))

    st.dataframe(newDF)
