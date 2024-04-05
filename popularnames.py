import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title('Popular Name Trends')

url = "https://github.com/esnt/Data/raw/main/Names/popular_names.csv"
df = pd.read_csv(url)

name = st.text_input('Enter a name', value='John')
name_df = df[df['name'] == name]

selected_sex = st.selectbox('Select Sex', ['Female', 'Male'])

if selected_sex == 'Female':
    plot_df = name_df[name_df['sex'] == 'F']
    plt.plot(plot_df['year'], plot_df['n'])
    plt.title(f'{name} Over Time (Female)')
    plt.xlabel('Year')
    plt.ylabel('Frequency')
    st.pyplot()

elif selected_sex == 'Male':
    plot_df = name_df[name_df['sex'] == 'M']
    plt.plot(plot_df['year'], plot_df['n'])
    plt.title(f'{name} Over Time (Male)')
    plt.xlabel('Year')
    plt.ylabel('Frequency')
    st.pyplot()

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
