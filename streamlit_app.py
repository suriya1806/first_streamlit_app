import streamlit

streamlit.title('My parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('  🥣 Omega 3 and Blueberry oat meal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Bolied  Free Range Egg')
streamlit.text('🥑🍞 Avocada Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
