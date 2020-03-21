import altair as alt
from vega_datasets import data

source = data.stocks()

alt.Chart(source).mark_area(
    color="lightblue",
    interpolate='step-after',
    line=True
).encode(
    x='date',
    y='price'
).transform_filter(alt.datum.symbol == 'GOOG')

##
import altair as alt
from vega_datasets import data

source = data.cars()

line = alt.Chart(source).mark_line().encode(
    x='Year',
    y='mean(Miles_per_Gallon)'
)

band = alt.Chart(source).mark_errorband(extent='ci').encode(
    x='Year',
    y=alt.Y('Miles_per_Gallon', title='Miles/Gallon'),
)

band + line




###
import altair as alt
from vega_datasets import data

source = data.stocks()

base = alt.Chart(source).properties(width=550)

line = base.mark_line().encode(
    x='date',
    y='price',
    color='symbol'
)

rule = base.mark_rule().encode(
    y='average(price)',
    color='symbol',
    size=alt.value(2)
)

line + rule

##########
import altair as alt
from vega_datasets import data

source = data.jobs.url

alt.Chart(source).mark_line().encode(
    alt.X('year:O'),
    alt.Y('perc:Q', axis=alt.Axis(format='%')),
    color='sex:N'
).transform_filter(
    alt.datum.job == 'Welder'
)



###
import altair as alt
import numpy as np
import pandas as pd

x = np.arange(100)
source = pd.DataFrame({
  'x': x,
  'f(x)': np.sin(x / 5)
})

alt.Chart(source).mark_line(point=True).encode(
    x='x',
    y='f(x)'
)



########
import altair as alt

source = alt.sequence(start=0, stop=12.7, step=0.1, as_='x')

alt.Chart(source).mark_line().transform_calculate(
    sin='sin(datum.x)',
    cos='cos(datum.x)'
).transform_fold(
    ['sin', 'cos']
).encode(
    x='x:Q',
    y='value:Q',
    color='key:N'
)

##
import altair as alt
from vega_datasets import data

source = data.wheat()

alt.Chart(source).mark_trail().encode(
    x='year:T',
    y='wheat:Q',
    size='wheat:Q'
)



##
import altair as alt
from vega_datasets import data

source = data.stocks()

alt.Chart(source).mark_line().encode(
    x='date',
    y='price',
    color='symbol'
)


##
import altair as alt
from vega_datasets import data

source = data.barley()

alt.Chart(source).mark_line().encode(
    x='year:O',
    y='median(yield)',
    color='site'
)


##
import altair as alt
from vega_datasets import data

source = data.stocks()

alt.Chart(source).mark_line(interpolate='step-after').encode(
    x='date',
    y='price'
).transform_filter(
    alt.datum.symbol == 'GOOG'
)

