import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from matplotlib.ticker import FuncFormatter
sns.set(style='dark')

def get_total_rented(df):
    return df['cnt'].sum()

def get_workingday_group(df):
    return df.groupby('workingday')['cnt'].sum()

def get_weathersit_group(df):
    return df.groupby('weathersit')['cnt'].sum()

def show_workingday_group(df):
    # Buat bar chart menggunakan Seaborn
    plt.figure(figsize=(8, 5))
    ax = sns.barplot(x=df.index, y=df.values, palette='pastel')

    # Set formatter untuk sumbu y tanpa notasi ilmiah
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))

    plt.title('Total Counts Based on Workingday Category')
    plt.xlabel('Workingday')
    plt.ylabel('Total Count (Sum of cnt)')
    plt.xticks(ticks=[0, 1], labels=['Not Workingday', 'Workingday'])
    plt.show()
    st.pyplot(plt)

def show_weathersit_group(df):
    # Buat bar chart menggunakan Seaborn
    plt.figure(figsize=(8, 5))
    ax = sns.barplot(x=df.index, y=df.values, palette='pastel')

    # Set formatter untuk sumbu y tanpa notasi ilmiah
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))

    plt.title('Total Counts Based on WeatherSit Category')
    plt.xlabel('Weather Situation')
    plt.ylabel('Total Count (Sum of cnt)')
    plt.xticks(ticks=[0, 1, 2], labels=['1', '2', '3'])
    plt.show()
    st.pyplot(plt)
    st.write('1: Clear, Few clouds, Partly cloudy, Partly cloudy')
    st.write('2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist')
    st.write('3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds')
    st.write('4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog')

wumbo = 0
with st.sidebar:
    st.write('Ingin menampilkan berdasarkan apa?')
    if st.button('Berdasarkan hari kerja'):
        subhead = 'Pengaruh Hari Kerja pada Bike Sharing'
        main_df = pd.read_csv('all_data.csv')
        main_df['cnt'] = main_df['cnt'].astype(int)  # Ensure data type is integer
        total_rented = get_total_rented(main_df)
        workingday_group = get_workingday_group(main_df)
        wumbo = 1
    if st.button('Berdasarkan cuaca'):
        subhead = 'Pengaruh Cuaca pada Bike Sharing'
        main_df = pd.read_csv('all_data.csv')
        main_df['cnt'] = main_df['cnt'].astype(int)  # Ensure data type is integer
        total_rented = get_total_rented(main_df)
        workingday_group = get_weathersit_group(main_df)
        wumbo = 2

st.header('Analisis data pada bike sharing dataset :sparkles:')
if wumbo == 1:
    st.subheader(subhead)
    st.metric("Total orders", value=total_rented)
    st.subheader(subhead)
    show_workingday_group(workingday_group)
elif wumbo == 2:
    st.subheader(subhead)
    st.metric("Total orders", value=total_rented)
    st.subheader(subhead)
    show_weathersit_group(workingday_group)