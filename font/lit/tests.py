import streamlit as st
import altair as alt
from vega_datasets import data
import pandas as pd

source=data.barley()

bars = alt.Chart(source, width=720, height=480).mark_bar().encode(
    x=alt.X('sum(yield):Q', stack='normalize'),
    y=alt.Y('variety:N'),
    color=alt.Color('site')
)

text = alt.Chart(source, width=720, height=480).mark_text(dx=-15, dy=3, color='white').encode(
    x=alt.X('sum(yield):Q', stack='normalize'),
    y=alt.Y('variety:N'),
    detail='site:N',
    text=alt.Text('sum(yield):Q', format='.1f')
)

c = bars + text


source = data.stocks()

stock_index = alt.Chart(source,  width=720, height=180).mark_area(
    color="lightblue",
    interpolate='step-after',
    line=True
).encode(
    x='date',
    y='price'
).transform_filter(alt.datum.symbol == 'GOOG')


st.altair_chart(stock_index)
st.markdown('---')
st.header('查询')
title = st.text_input('Movie title', 'Life of Brain')
st.write('The current movie title is', title)


st.markdown('---')
st.altair_chart(c)

df = pd.DataFrame({
    'code': list(range(100)),
    'name': list(range(100)),
    'industry': list(range(100)),
    'change_ratio': list(range(100)),
    'pe': list(range(100)),
    'ps': list(range(100)),
    'pb': list(range(100)),
})

select_industry = st.selectbox(
    'which industry?',
    ('all', None, 1, 2, 3, 4, 5)
)

if select_industry:
    if select_industry == 'all':
        st.write(df)
    st.dataframe(df[df.code == select_industry],
                 width=None, height=None)


