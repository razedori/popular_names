import plotly.express as px
import pandas as pd
import streamlit as st

st.title('Popular Name Trends')

url = "https://github.com/esnt/Data/raw/main/Names/popular_names.csv"
df = pd.read_csv(url)

name = st.text_input('Enter a name', value='John')
name_df = df[df['name'] == name]

st.header(f'{name} Over Time')
tab1, tab2 = st.columns(2)

with tab1:
    plot_df_female = name_df[name_df['sex'] == 'F']
    if not plot_df_female.empty:
        fig_female = px.line(data_frame=plot_df_female, x='year', y='n', title=f'{name} Over Time (Female)')
        st.plotly_chart(fig_female)
    else:
        st.write("No data available for female.")

with tab2:
    plot_df_male = name_df[name_df['sex'] == 'M']
    if not plot_df_male.empty:
        fig_male = px.line(data_frame=plot_df_male, x='year', y='n', title=f'{name} Over Time (Male)')
        st.plotly_chart(fig_male)
    else:
        st.write("No data available for male.")

with st.sidebar:
    year = st.slider('Choose a year', 1910, 2021)
    st.header(f'Top names by {year}')
    year_df = df[df['year'] == year]

    girls_names = year_df[year_df.sex == 'F'].sort_values('n', ascending=False).head(5)['name']
    boys_names = year_df[year_df.sex == 'M'].sort_values('n', ascending=False).head(5)['name']

    top_names = pd.concat([girls_names.reset_index(drop=True), boys_names.reset_index(drop=True)],
                          ignore_index=True, axis=1)
    top_names.columns = ['Girls', 'Boys']
    top_names.index = [1, 2, 3, 4, 5]
    st.dataframe(top_names)
