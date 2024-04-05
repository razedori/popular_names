import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title('Popular Name Trends')

url = "https://github.com/esnt/Data/raw/main/Names/popular_names.csv"
df = pd.read_csv(url)

name = st.text_input('Enter a name', value='John')
name_df = df[df['name'] == name]

st.header(f'{name} Over Time')

# Add radio buttons to choose between female and male plots
gender = st.radio("Select gender:", ('Female', 'Male'))

plot_df = name_df[name_df['sex'] == gender[0]]  # Selecting rows based on the first character of gender (F/M)
if not plot_df.empty:
    plt.plot(plot_df['year'], plot_df['n'], marker='o')
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.title(f'{name} - {gender}')
    st.pyplot()
else:
    st.write(f"No data available for {name} - {gender}")

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
