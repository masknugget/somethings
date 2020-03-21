import altair as alt
from vega_datasets import data

source = data.flights_5k()

brush = alt.selection_interval(encodings=['x'])

base = alt.Chart(source).transform_calculate(
    time="hours(datum.date) + minutes(datum.date) / 60"
).mark_bar().encode(
    y='count():Q'
).properties(
    width=600,
    height=100
)

alt.vconcat(
  base.encode(
    alt.X('time:Q',
      bin=alt.Bin(maxbins=30, extent=brush),
      scale=alt.Scale(domain=brush)
    )
  ),
  base.encode(
    alt.X('time:Q', bin=alt.Bin(maxbins=30)),
  ).add_selection(brush)
)


##

import altair as alt
from vega_datasets import data

source = data.movies.url

base = alt.Chart(source)

bar = base.mark_bar().encode(
    x=alt.X('IMDB_Rating:Q', bin=True, axis=None),
    y='count()'
)

rule = base.mark_rule(color='red').encode(
    x='mean(IMDB_Rating):Q',
    size=alt.value(5)
)

bar + rule


#########################
##############################


import pandas as pd
import altair as alt
import numpy as np
np.random.seed(42)

# Generating Data
source = pd.DataFrame({
    'Trial A': np.random.normal(0, 0.8, 1000),
    'Trial B': np.random.normal(-2, 1, 1000),
    'Trial C': np.random.normal(3, 2, 1000)
})

alt.Chart(source).transform_fold(
    ['Trial A', 'Trial B', 'Trial C'],
    as_=['Experiment', 'Measurement']
).mark_area(
    opacity=0.3,
    interpolate='step'
).encode(
    alt.X('Measurement:Q', bin=alt.Bin(maxbins=100)),
    alt.Y('count()', stack=None),
    alt.Color('Experiment:N')
)


######
###################
import altair as alt
from vega_datasets import data

source = data.cars()

alt.Chart(source).mark_bar().encode(
    alt.X("Horsepower:Q", bin=True),
    y='count()',
    row='Origin'
)

