'''
chart.save('chart.png')
chart.save('chart.svg')

chart.save('chart.png', webdriver='firefox')
chart.save('chart.png', scale_factor=2.0)

chart.save('chart.html')
chart.save('chart.html', embed_options={'renderer':'svg'})

'''


import altair as alt
from vega_datasets import data

chart = alt.Chart(data.cars.url).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color='Origin:N'
)

chart.save('chart.json')


# Customizing Visualizations
import altair as alt
from vega_datasets import data
cars = data.cars.url

alt.Chart(cars).mark_point().encode(
    x='Acceleration:Q',
    y='Horsepower:Q'
)


alt.Chart(cars).mark_point().encode(
    x='Acceleration:Q',
    y='Horsepower:Q'
).configure_mark(
    opacity=0.2,
    color='red'
)

alt.Chart(cars).mark_point(opacity=0.2, color='red').encode(
    x='Acceleration:Q',
    y='Horsepower:Q'
)


## Encoding

alt.Chart(cars).mark_point().encode(
    x='Acceleration:Q',
    y='Horsepower:Q',
    opacity=alt.value(0.2),
    color=alt.value('red')
)

##
import altair as alt
from vega_datasets import data

cars = data.cars.url

alt.Chart(cars).mark_point().encode(
    x='Acceleration:Q',
    y='Horsepower:Q'
)

#
alt.Chart(cars).mark_point().encode(
    alt.X('Acceleration:Q',
        scale=alt.Scale(zero=False)
    ),
    y='Horsepower:Q'
)

# ---
alt.Chart(cars).mark_point().encode(
    alt.X('Acceleration:Q',
        scale=alt.Scale(domain=(5, 20))
    ),
    y='Horsepower:Q'
)


#---
alt.Chart(cars).mark_point(clip=True).encode(
    alt.X('Acceleration:Q',
        scale=alt.Scale(domain=(5, 20))
    ),
    y='Horsepower:Q'
)



# ---
alt.Chart(cars).mark_point().encode(
    alt.X('Acceleration:Q',
        scale=alt.Scale(
            domain=(5, 20),
            clamp=True
        )
    ),
    y='Horsepower:Q'
).interactive()


# --- Adjusting Axis Labels
import pandas as pd
df = pd.DataFrame({'x': [0.03, 0.04, 0.05, 0.12, 0.07, 0.15],
                   'y': [10, 35, 39, 50, 24, 35]})

alt.Chart(df).mark_circle().encode(
    x='x',
    y='y'
)

alt.Chart(df).mark_circle().encode(
    x=alt.X('x', axis=alt.Axis(format='%', title='percentage')),
    y=alt.Y('y', axis=alt.Axis(format='$', title='dollar amount'))
)



# --- adjusting the legend ---

import altair as alt
from vega_datasets import data

iris = data.iris()

alt.Chart(iris).mark_point().encode(
    x='petalWidth',
    y='petalLength',
    color='species'
)


# ---
import altair as alt
from vega_datasets import data

iris = data.iris()

alt.Chart(iris).mark_point().encode(
    x='petalWidth',
    y='petalLength',
    color=alt.Color('species', legend=alt.Legend(title="Species by color"))
)


# ---
import altair as alt
from vega_datasets import data

iris = data.iris()

alt.Chart(iris).mark_point().encode(
    x='petalWidth',
    y='petalLength',
    color=alt.Color('species', legend=alt.Legend(orient="left")),
)


# ---
import altair as alt
from vega_datasets import data

iris = data.iris()

alt.Chart(iris).mark_point().encode(
    x='petalWidth',
    y='petalLength',
    color=alt.Color('species', legend=None),
)


# ---
import altair as alt
from vega_datasets import data

iris = data.iris()

alt.Chart(iris).mark_point().encode(
    x='petalWidth',
    y='petalLength',
    color='species'
)


# ---
import altair as alt
from vega_datasets import data

iris = data.iris()

alt.Chart(iris).mark_point().encode(
    x='petalWidth',
    y='petalLength',
    color='species'
).configure_axis(
    grid=False
)


# ---
import altair as alt
from vega_datasets import data

iris = data.iris()

alt.Chart(iris).mark_point().encode(
    x='petalWidth',
    y='petalLength',
    color='species'
).configure_axis(
    grid=False
).configure_view(
    strokeWidth=0
)


# ---
import altair as alt
from vega_datasets import data

iris = data.iris()

alt.Chart(iris).mark_point().encode(
    alt.X('petalWidth', axis=None),
    alt.Y('petalLength', axis=None),
    color='species'
).configure_axis(
    grid=False
).configure_view(
    strokeWidth=0
)


# --
import altair as alt
from vega_datasets import data

iris = data.iris()

alt.Chart(iris).mark_point().encode(
    x='petalWidth',
    y='petalLength',
    color=alt.Color('species', scale=alt.Scale(scheme='dark2'))
)


# ----
import altair as alt
from vega_datasets import data

iris = data.iris()
domain = ['setosa', 'versicolor', 'virginica']
range_ = ['red', 'green', 'blue']

alt.Chart(iris).mark_point().encode(
    x='petalWidth',
    y='petalLength',
    color=alt.Color('species', scale=alt.Scale(domain=domain, range=range_))
)


# raw color values
import pandas as pd
import altair as alt

data = pd.DataFrame({
    'x': range(6),
    'color': ['red', 'steelblue', 'chartreuse', '#F4D03F', '#D35400', '#7D3C98']
})

alt.Chart(data).mark_point(
    filled=True,
    size=100
).encode(
    x='x',
    color=alt.Color('color', scale=None)
)



# -- adjust
import altair as alt
import pandas as pd

data = pd.DataFrame({'name': ['a', 'b'], 'value': [4, 10]})

alt.Chart(data).mark_bar(size=10).encode(
    x='name:O',
    y='value:Q'
)

alt.Chart(data).mark_bar(size=30).encode(
    x='name:O',
    y='value:Q'
)

alt.Chart(data).mark_bar(size=30).encode(
    x='name:O',
    y='value:Q'
).properties(width=200)


alt.Chart(data).mark_bar(size=30).encode(
    x='name:N',
    y='value:Q'
).properties(width=alt.Step(100))


# adjust chart size

import altair as alt
from vega_datasets import data

cars = data.cars()

alt.Chart(cars).mark_bar().encode(
    x='Origin',
    y='count()'
).properties(
    width=200,
    height=150
)


alt.Chart(cars).mark_bar().encode(
    x='Origin',
    y='count()',
    column='Cylinders:Q'
).properties(
    width=100,
    height=100
)


alt.Chart(cars).mark_bar().encode(
    x='Origin',
    y='count()',
).properties(
    width='container',
    height=200
)

# --- Times and Dates in Altair
import altair as alt
import pandas as pd

df = pd.DataFrame({'local': ['2018-01-01T00:00:00'],
                   'utc': ['2018-01-01T00:00:00Z']})

alt.Chart(df).transform_calculate(
    compliant="hours(datum.local) != hours(datum.utc) ? true : false",
).mark_text(size=20, baseline='middle').encode(
    text=alt.condition('datum.compliant', alt.value('OK'), alt.value('not OK')),
    color=alt.condition('datum.compliant', alt.value('green'), alt.value('red'))
).properties(width=80, height=50)


###
import altair as alt
from vega_datasets import data

temps = data.seattle_temps()
temps.head()


#
temps = temps[temps.date < '2010-01-15']

alt.Chart(temps).mark_line().encode(
    x='date:T',
    y='temp:Q'
)


###########
alt.Chart(temps).mark_rect().encode(
    alt.X('hoursminutes(date):O', title='hour of day'),
    alt.Y('monthdate(date):O', title='date'),
    alt.Color('temp:Q', title='temperature (F)')
)


##
temps['date_pacific'] = temps['date'].dt.tz_localize('US/Pacific')
temps.dtypes


##########
alt.Chart(temps).mark_rect().encode(
    alt.X('hoursminutes(date_pacific):O', title='hour of day'),
    alt.Y('monthdate(date_pacific):O', title='date'),
    alt.Color('temp:Q', title='temperature (F)')
)



### utc time
alt.Chart(temps).mark_rect().encode(
    alt.X('utchoursminutes(date_pacific):O', title='UTC hour of day'),
    alt.Y('utcmonthdate(date_pacific):O', title='UTC date'),
    alt.Color('temp:Q', title='temperature (F)')
)


##
temps['date_utc'] = temps['date'].dt.tz_localize('UTC')

alt.Chart(temps).mark_rect().encode(
    alt.X('utchoursminutes(date_utc):O', title='hour of day'),
    alt.Y('utcmonthdate(date_utc):O', title='date'),
    alt.Color('temp:Q', title='temperature (F)')
)

