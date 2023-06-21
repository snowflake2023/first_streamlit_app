import streamlit, pandas

streamlit.title("My Parents New Healthy Diner")

streamlit.header("Breakfast Menu")
streamlit.header("Omega 3 & Blueberry Oatmeal")
streamlit.header("Kale, Spinach & Rocket Smoothie")
streamlit.header("Hard-Boiled Free-Range Egg")
streamlit.header("Avacado Toast")

streamlit.header("Build your Own Fruit Smoothie")
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
default_fruits = list(my_fruit_list.index)[:2]

fruits_selected = streamlit.multiselect("Pick some fruits:",options=list(my_fruit_list.index),default=default_fruits)
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

