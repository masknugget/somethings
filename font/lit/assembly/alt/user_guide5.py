import pandas as pd
data = pd.DataFrame({'a': list('CCCDDDEEE'),
                     'b': [2, 7, 4, 1, 2, 6, 8, 4, 7]})

import altair as alt
chart = alt.Chart(data)

alt.Chart(data).mark_point()

alt.Chart(data).mark_point().encode(
    x='a',
)
alt.Chart(data).mark_point().encode(
    x='a',
    y='b'
)



## Data Transformation: Aggregation
alt.Chart(data).mark_point().encode(
    x='a',
    y='average(b)'
)


alt.Chart(data).mark_bar().encode(
    x='a',
    y='average(b)'
)

alt.Chart(data).mark_bar().encode(
    y='a',
    x='average(b)'
)

chart = alt.Chart(data).mark_bar().encode(
    x='a',
    y='average(b)',
)
print(chart.to_json())

y = alt.Y('average(b):Q')
print(y.to_json())
y = alt.Y(field='b', type='quantitative', aggregate='average')
print(y.to_json())

alt.Chart(data).mark_bar().encode(
    alt.Y('a', type='nominal'),
    alt.X('b', type='quantitative', aggregate='average')
)


alt.Chart(data).mark_bar(color='firebrick').encode(
    alt.Y('a', title='category'),
    alt.X('average(b)', title='avg(b) by category')
)


