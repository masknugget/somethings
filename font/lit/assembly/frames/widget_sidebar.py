import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')


agree = st.checkbox('I agree')
if agree:
    st.write('Great!')


genre = st.radio(
    "what is your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary')
)

if genre == 'Comedy':
    st.write('you selected comedy.')
else:
    st.write('you didnt select comedy')


option = st.selectbox(
    'How would you like to contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)
st.write('You selected', option)

options = st.multiselect(
    'what are your favorite colors',
    ('Yellow', 'Red'),
    ('Green', 'Yellow', 'Red', 'Blue')
)

st.write('You selected: ', options)



## ---slider---

age = st.slider('How old are you?', 0, 130, 25)
st.write("i'am", age, 'years old')

values = st.slider(
    'select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

st.write('Values:', values)
title = st.text_input('Movie title', 'Life of Brain')
st.write('The current movie title is', title)

number = st.number_input('insert a number')
st.write('the current number is', number)

txt = st.text_area('text to analyze', '''
    it was the best of times, it was the worst of times, 
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
''')

import datetime
d = st.date_input(
    "When's your birthday",
    datetime.date(2019, 7, 6)
)

st.write('Your birthday is:', d)

t = st.time_input('Set an alarm for', datetime.time(8, 6))
st.write('Alarm is set for', t)

uploaded_file = st.file_uploader('choose a csv file ', type='csv')
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)


import streamlit as st
add_selectbox = st.sidebar.selectbox(
    'how would you like to be contactedd?',
    ('Email', 'Home phone', 'Mobile phone')
)

