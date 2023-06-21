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
default_fruits = my_fruite_list.sample(2)
streamlit.write(default_fruits,' ',type(default_fruits))
streamlit.multiselect("Pick some fruits:",options=list(my_fruit_list.index),default=list(default_fruits))
streamlit.dataframe(my_fruit_list)

