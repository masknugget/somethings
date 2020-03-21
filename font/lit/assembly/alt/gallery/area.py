import altair as alt
from vega_datasets import data

source = data.movies.url

alt.Chart(source).transform_window(
    cumulative_count="count()",
    sort=[{"field": "IMDB_Rating"}],
).mark_area().encode(
    x="IMDB_Rating:Q",
    y="cumulative_count:Q"
)

##
import altair as alt
from vega_datasets import data

source = data.iris()

alt.Chart(source).transform_fold(
    ['petalWidth',
     'petalLength',
     'sepalWidth',
     'sepalLength'],
    as_ = ['Measurement_type', 'value']
).transform_density(
    density='value',
    bandwidth=0.3,
    groupby=['Measurement_type'],
    extent= [0, 8]
).mark_area().encode(
    alt.X('value:Q'),
    alt.Y('density:Q'),
    alt.Row('Measurement_type:N')
).properties(width=300, height=50)



###
import altair as alt
import pandas as pd

source = pd.DataFrame([
    {"x": 1,  "y": 28}, {"x": 2,  "y": 55},
    {"x": 3,  "y": 43}, {"x": 4,  "y": 91},
    {"x": 5,  "y": 81}, {"x": 6,  "y": 53},
    {"x": 7,  "y": 19}, {"x": 8,  "y": 87},
    {"x": 9,  "y": 52}, {"x": 10, "y": 48},
    {"x": 11, "y": 24}, {"x": 12, "y": 49},
    {"x": 13, "y": 87}, {"x": 14, "y": 66},
    {"x": 15, "y": 17}, {"x": 16, "y": 27},
    {"x": 17, "y": 68}, {"x": 18, "y": 16},
    {"x": 19, "y": 49}, {"x": 20, "y": 15}
])

area1 = alt.Chart(source).mark_area(
    clip=True,
    interpolate='monotone'
).encode(
    alt.X('x', scale=alt.Scale(zero=False, nice=False)),
    alt.Y('y', scale=alt.Scale(domain=[0, 50]), title='y'),
    opacity=alt.value(0.6)
).properties(
    width=500,
    height=75
)

area2 = area1.encode(
    alt.Y('ny:Q', scale=alt.Scale(domain=[0, 50]))
).transform_calculate(
    "ny", alt.datum.y - 50
)

area1 + area2


##
import altair as alt
from vega_datasets import data

source = data.sp500.url

brush = alt.selection(type='interval', encodings=['x'])

upper = alt.Chart(source).mark_area().encode(
    alt.X('date:T', scale=alt.Scale(domain=brush)),
    y='price:Q'
).properties(
    width=600,
    height=200
)

lower = upper.properties(
    height=60
).add_selection(brush)

upper & lower


##
import altair as alt
from vega_datasets import data

source = data.iowa_electricity()

alt.Chart(source).mark_area(opacity=0.3).encode(
    x="year:T",
    y=alt.Y("net_generation:Q", stack=None),
    color="source:N"
)



##
import altair as alt
from vega_datasets import data

source = data.iowa_electricity()

alt.Chart(source).mark_area().encode(
    x="year:T",
    y=alt.Y("net_generation:Q", stack="normalize"),
    color="source:N"
)

###
import altair as alt
from vega_datasets import data

source = data.iris()

alt.Chart(source).transform_fold(
    ['petalWidth',
     'petalLength',
     'sepalWidth',
     'sepalLength'],
    as_ = ['Measurement_type', 'value']
).transform_density(
    density='value',
    bandwidth=0.3,
    groupby=['Measurement_type'],
    extent= [0, 8],
    counts = True,
    steps=200
).mark_area().encode(
    alt.X('value:Q'),
    alt.Y('density:Q', stack='zero'),
    alt.Color('Measurement_type:N')
).properties(width=400, height=100)



###
import altair as alt
from vega_datasets import data

source = data.unemployment_across_industries.url

alt.Chart(source).mark_area().encode(
    alt.X('yearmonth(date):T',
        axis=alt.Axis(format='%Y', domain=False, tickSize=0)
    ),
    alt.Y('sum(count):Q', stack='center', axis=None),
    alt.Color('series:N',
        scale=alt.Scale(scheme='category20b')
    )
).interactive()



##
import altair as alt
from vega_datasets import data

source = data.iowa_electricity()

alt.Chart(source).mark_area().encode(
    x="year:T",
    y="net_generation:Q",
    color="source:N",
    row="source:N"
).properties(
    height=100
)



##
import altair as alt
from vega_datasets import data

source = data.stocks()

alt.Chart(source).transform_filter(
    alt.datum.symbol != 'GOOG'
).mark_area().encode(
    x='date:T',
    y='price:Q',
    color='symbol:N',
    row=alt.Row('symbol:N', sort=['MSFT', 'AAPL', 'IBM', 'AMZN'])
).properties(height=50, width=400)

import altair as alt
from vega_datasets import data

source = data.movies.url

alt.Chart(source).transform_window(
    cumulative_count="count()",
    sort=[{"field": "IMDB_Rating"}],
).mark_area().encode(
    x="IMDB_Rating:Q",
    y="cumulative_count:Q"
)

##
import altair as alt
from vega_datasets import data

source = data.iris()

alt.Chart(source).transform_fold(
    ['petalWidth',
     'petalLength',
     'sepalWidth',
     'sepalLength'],
    as_ = ['Measurement_type', 'value']
).transform_density(
    density='value',
    bandwidth=0.3,
    groupby=['Measurement_type'],
    extent= [0, 8]
).mark_area().encode(
    alt.X('value:Q'),
    alt.Y('density:Q'),
    alt.Row('Measurement_type:N')
).properties(width=300, height=50)



###
import altair as alt
import pandas as pd

source = pd.DataFrame([
    {"x": 1,  "y": 28}, {"x": 2,  "y": 55},
    {"x": 3,  "y": 43}, {"x": 4,  "y": 91},
    {"x": 5,  "y": 81}, {"x": 6,  "y": 53},
    {"x": 7,  "y": 19}, {"x": 8,  "y": 87},
    {"x": 9,  "y": 52}, {"x": 10, "y": 48},
    {"x": 11, "y": 24}, {"x": 12, "y": 49},
    {"x": 13, "y": 87}, {"x": 14, "y": 66},
    {"x": 15, "y": 17}, {"x": 16, "y": 27},
    {"x": 17, "y": 68}, {"x": 18, "y": 16},
    {"x": 19, "y": 49}, {"x": 20, "y": 15}
])

area1 = alt.Chart(source).mark_area(
    clip=True,
    interpolate='monotone'
).encode(
    alt.X('x', scale=alt.Scale(zero=False, nice=False)),
    alt.Y('y', scale=alt.Scale(domain=[0, 50]), title='y'),
    opacity=alt.value(0.6)
).properties(
    width=500,
    height=75
)

area2 = area1.encode(
    alt.Y('ny:Q', scale=alt.Scale(domain=[0, 50]))
).transform_calculate(
    "ny", alt.datum.y - 50
)

area1 + area2


##
import altair as alt
from vega_datasets import data

source = data.sp500.url

brush = alt.selection(type='interval', encodings=['x'])

upper = alt.Chart(source).mark_area().encode(
    alt.X('date:T', scale=alt.Scale(domain=brush)),
    y='price:Q'
).properties(
    width=600,
    height=200
)

lower = upper.properties(
    height=60
).add_selection(brush)

upper & lower


##
import altair as alt
from vega_datasets import data

source = data.iowa_electricity()

alt.Chart(source).mark_area(opacity=0.3).encode(
    x="year:T",
    y=alt.Y("net_generation:Q", stack=None),
    color="source:N"
)



##
import altair as alt
from vega_datasets import data

source = data.iowa_electricity()

alt.Chart(source).mark_area().encode(
    x="year:T",
    y=alt.Y("net_generation:Q", stack="normalize"),
    color="source:N"
)

###
import altair as alt
from vega_datasets import data

source = data.iris()

alt.Chart(source).transform_fold(
    ['petalWidth',
     'petalLength',
     'sepalWidth',
     'sepalLength'],
    as_ = ['Measurement_type', 'value']
).transform_density(
    density='value',
    bandwidth=0.3,
    groupby=['Measurement_type'],
    extent= [0, 8],
    counts = True,
    steps=200
).mark_area().encode(
    alt.X('value:Q'),
    alt.Y('density:Q', stack='zero'),
    alt.Color('Measurement_type:N')
).properties(width=400, height=100)



###
import altair as alt
from vega_datasets import data

source = data.unemployment_across_industries.url

alt.Chart(source).mark_area().encode(
    alt.X('yearmonth(date):T',
        axis=alt.Axis(format='%Y', domain=False, tickSize=0)
    ),
    alt.Y('sum(count):Q', stack='center', axis=None),
    alt.Color('series:N',
        scale=alt.Scale(scheme='category20b')
    )
).interactive()



##
import altair as alt
from vega_datasets import data

source = data.iowa_electricity()

alt.Chart(source).mark_area().encode(
    x="year:T",
    y="net_generation:Q",
    color="source:N",
    row="source:N"
).properties(
    height=100
)



##
import altair as alt
from vega_datasets import data

source = data.stocks()

alt.Chart(source).transform_filter(
    alt.datum.symbol != 'GOOG'
).mark_area().encode(
    x='date:T',
    y='price:Q',
    color='symbol:N',
    row=alt.Row('symbol:N', sort=['MSFT', 'AAPL', 'IBM', 'AMZN'])
).properties(height=50, width=400)

