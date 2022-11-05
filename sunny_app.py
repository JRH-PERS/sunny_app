#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st


# In[7]:

header = st.container()
data = st.container()
scoreboard = st.container()
display = st.container()

with header:
    st.title('The Its Always Sunny Ranker')
    
with data:
    st.title('Please enter episode details')
    episode_name = st.text_area("Enter Episode Name")
    series_number = st.number_input("Enter Series Number", min_value=0, max_value=100, step=1)
    episode_number = st.number_input("Enter Episode Number", min_value=0, max_value=100, step=1)
    main_pro = st.selectbox('Who was main character', ('Dennis', 'Charlie', 'Dee', 'Mac', 'Frank', 'Waitress', 'Cricket'))
    rating = st.number_input("Enter Rating", min_value=1, max_value=5, step=1)
    
    
data = {'Epsiode name':episode_name, 'Series Number': series_number, 'Episode number': episode_number, 
        'Main Protagonist': main_pro, "Overall Rating": rating}

