#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd


# In[7]:

header = st.container()
data = st.container()
scoreboard = st.container()
display = st.container()

with header:
    st.title('The Its Always Sunny Ranker')
    
with data:
    st.title('Please enter episode details')
    ep_na = st.text_area("Enter Episode Name")
    se_nu = st.number_input("Enter Series Number", min_value=0, max_value=100, step=1)
    ep_nu = st.number_input("Enter Episode Number", min_value=0, max_value=100, step=1)
    pro = st.selectbox('Who was main character', ('Dennis', 'Charlie', 'Dee', 'Mac', 'Frank', 'Waitress', 'Cricket'))
    ra = st.number_input("Enter Rating", min_value=1, max_value=5, step=1)
    
    def get_data():
        return []
    if st.button("Add row"):
        get_data().append({'Epsiode name':episode_name, 'Series Number': series_number, 'Episode number': episode_number, 
        'Main Protagonist': main_pro, "Overall Rating": rating})

    st.write(pd.DataFrame(get_data()))
