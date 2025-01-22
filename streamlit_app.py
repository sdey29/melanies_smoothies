# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize your Smoothie! :cup_with_straw:")
st.write(
    """Choose the fruits you want in your custom Smoothie!
    """
)

name_on_order = st.text_input('Name on Smoothie:')
st.write('The name on your smoothie will be:', name_on_order)

#from snowflake.snowpark.functions import col

cnx=st.connection("snowflake")
session=cnx.session()
#session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select (col('FRUIT_NAME'))


ingredients_list=st.multiselect('Choose upto5 ingeredients:', my_dataframe,max_selections=5)



if ingredients_list:

    #st.write(ingredients_list)
    #st.text(ingredients_list)
    ingredients_string=''   
    for fruits_chosen in ingredients_list:
        ingredients_string+=fruits_chosen + ' '

    #st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','"""+name_on_order+"""')"""
    
    #st.write(my_insert_stmt)
    #st.stop()
        
    time_to_insert=st.button('Submit Order')
   
    
    if time_to_insert:
     session.sql(my_insert_stmt).collect()
     st.success('Your Smoothie is ordered!', icon="✅")

import requests
smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
st.text(smoothiefroot_response)

