import streamlit, pandas

streamlit.title("My Parents New Healthy Diner")

streamlit.header("Breakfast Menu")
streamlit.header("Omega 3 & Blueberry Oatmeal")
streamlit.header("Kale, Spinach & Rocket Smoothie")
streamlit.header("Hard-Boiled Free-Range Egg")
streamlit.header("Avacado Toast")

streamlit.header("Build your Own Fruit Smoothie")
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruite_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avacado','Lemon'])
streamlit.dataframe(my_fruit_list)

