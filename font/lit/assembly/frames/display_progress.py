import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import time

my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete+1)


with st.spinner('wait for it ...'):
    time.sleep(5)

st.success('Done!')

st.balloons()
st.error('this is an error')
st.warning('this is a warning')
st.info('this is purely informational message!')
st.success('this is a success message!')

e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)

my_placeholder = st.empty()
my_placeholder.text("Hello world!")
# my_placeholder.image(my_image_bytes)


df1 = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20))
)

my_table = st.table(df1)

df2 = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20))
)

my_table.add_rows(df2)
# Now the table shown in the Streamlit app contains the data for
# df1 followed by the data for df2.

# Assuming df1 and df2 from the example above still exist...
my_chart = st.line_chart(df1)
my_chart.add_rows(df2)
# Now the chart shown in the Streamlit app contains the data for
# df1 followed by the data for df2.

my_chart = st.vega_lite_chart({
    'mark': 'line',
    'encoding': {'x': 'a', 'y': 'b'},
    'datasets': {
      'some_fancy_name': df1,  # <-- named dataset
     },
    'data': {'name': 'some_fancy_name'},
}),

my_chart.add_rows(some_fancy_name=df2)  # <-- name used as keyword

