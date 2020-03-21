import altair as alt
import pandas as pd

data = pd.DataFrame({'x': ['A', 'B', 'C', 'D', 'E'],
                     'y': [5, 3, 6, 7, 2]})
alt.Chart(data).mark_bar().encode(
    x='x',
    y='y',
)


#
import altair as alt

data = alt.Data(values=[{'x': 'A', 'y': 5},
                        {'x': 'B', 'y': 3},
                        {'x': 'C', 'y': 6},
                        {'x': 'D', 'y': 7},
                        {'x': 'E', 'y': 2}])

chart = alt.Chart(data).mark_bar().encode(
    x='x:O',  # specify ordinal data
    y='y:Q',  # specify quantitative data
)

chart.serve('localhost', 8888)


# ---

import altair as alt
from vega_datasets import data
url = data.cars.url

alt.Chart(url).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q'
)

# --- Including Index Data
import numpy as np
rand = np.random.RandomState(0)

data = pd.DataFrame({'value': rand.randn(100).cumsum()},
                    index=pd.date_range('2018', freq='D', periods=100))
data.head()

alt.Chart(data.reset_index()).mark_line().encode(
    x='index:T',
    y='value:Q'
)


# --- Long-form vs. Wide-form Data

wide_form = pd.DataFrame({'Date': ['2007-10-01', '2007-11-01', '2007-12-01'],
                          'AAPL': [189.95, 182.22, 198.08],
                          'AMZN': [89.15, 90.56, 92.64],
                          'GOOG': [707.00, 693.00, 691.48]})
print(wide_form)

long_form = pd.DataFrame({'Date': ['2007-10-01', '2007-11-01', '2007-12-01',
                                   '2007-10-01', '2007-11-01', '2007-12-01',
                                   '2007-10-01', '2007-11-01', '2007-12-01'],
                          'company': ['AAPL', 'AAPL', 'AAPL',
                                      'AMZN', 'AMZN', 'AMZN',
                                      'GOOG', 'GOOG', 'GOOG'],
                          'price': [189.95, 182.22, 198.08,
                                     89.15,  90.56,  92.64,
                                    707.00, 693.00, 691.48]})
print(long_form)

alt.Chart(long_form).mark_line().encode(
  x='Date:T',
  y='price:Q',
  color='company:N'
)

wide_form.melt('Date', var_name='company', value_name='price')
long_form.pivot(index='Date', columns='company', values='price').reset_index()

alt.Chart(wide_form).transform_fold(
    ['AAPL', 'AMZN', 'GOOG'],
    as_=['company', 'price']
).mark_line().encode(
    x='Date:T',
    y='price:Q',
    color='company:N'
)

# --- Sequence Generator
import altair as alt

# Note that the following generator is functionally similar to
# data = pd.DataFrame({'x': np.arange(0, 10, 0.1)})
data = alt.sequence(0, 10, 0.1, as_='x')

alt.Chart(data).transform_calculate(
    y='sin(datum.x)'
).mark_line().encode(
    x='x:Q',
    y='y:Q',
)

# --- Graticule Generator

import altair as alt

data = alt.graticule(step=[15, 15])

alt.Chart(data).mark_geoshape(stroke='black').project(
    'orthographic',
    rotate=[0, -45, 0]
)

# --- Sphere Generator
import altair as alt

sphere_data = alt.sphere()
grat_data = alt.graticule(step=[15, 15])

background = alt.Chart(sphere_data).mark_geoshape(fill='aliceblue')
lines = alt.Chart(grat_data).mark_geoshape(stroke='lightgrey')

alt.layer(background, lines).project('naturalEarth1')


######## ---------
#
# Encodings

import altair as alt
from vega_datasets import data
cars = data.cars()

alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
    shape='Origin'
)

alt.Chart(cars).mark_point().encode(
    x='Acceleration:Q',
    y='Miles_per_Gallon:Q',
    color='Origin:N'
)

alt.Chart(cars).mark_point().encode(
    alt.X('Acceleration', type='quantitative'),
    alt.Y('Miles_per_Gallon', type='quantitative'),
    alt.Color('Origin', type='nominal')
)


base = alt.Chart(cars).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
).properties(
    width=150,
    height=150
)

alt.vconcat(
   base.encode(color='Cylinders:Q').properties(title='quantitative'),
   base.encode(color='Cylinders:O').properties(title='ordinal'),
   base.encode(color='Cylinders:N').properties(title='nominal'),
)


# ---

pop = data.population.url

base = alt.Chart(pop).mark_bar().encode(
    alt.Y('mean(people):Q', title='total population')
).properties(
    width=200,
    height=200
)

alt.hconcat(
    base.encode(x='year:Q').properties(title='year=quantitative'),
    base.encode(x='year:O').properties(title='year=ordinal')
)

base.encode(
    alt.X('year:Q',
        scale=alt.Scale(zero=False)
    )
)


##
############
alt.Chart(cars).mark_bar().encode(
    alt.X('Horsepower', bin=True),
    y='count()'
    # could also use alt.Y(aggregate='count', type='quantitative')
)

alt.Chart(cars).mark_point().encode(
    alt.X('Horsepower', bin=True),
    alt.Y('Miles_per_Gallon', bin=True),
    size='count()',
)

alt.Chart(cars).mark_circle().encode(
    alt.X('Horsepower', bin=True),
    alt.Y('Miles_per_Gallon', bin=True),
    size='count()',
    color='average(Acceleration):Q'
)


import altair as alt
from vega_datasets import data

barley = data.barley()

alt.Chart(barley).mark_bar().encode(
    x='variety:N',
    y='sum(yield):Q',
    color='site:N',
    order=alt.Order("site", sort="ascending")
)

import altair as alt
from vega_datasets import data

barley = data.barley()

alt.Chart(barley).mark_bar().encode(
    x='variety:N',
    y='sum(yield):Q',
    color='site:N',
    order=alt.Order("site", sort="descending")
)

import altair as alt
from vega_datasets import data

barley = data.barley()

alt.Chart(barley).mark_area().encode(
    x='variety:N',
    y='sum(yield):Q',
    color='site:N',
    order=alt.Order("site", sort="ascending")
)

import altair as alt
from vega_datasets import data

driving = data.driving()

alt.Chart(driving).mark_line(point=True).encode(
    alt.X('miles', scale=alt.Scale(zero=False)),
    alt.Y('gas', scale=alt.Scale(zero=False)),
    order='year'
)

############################################
####

import altair as alt
from vega_datasets import data

barley = data.barley()

base = alt.Chart(barley).mark_bar().encode(
    y='mean(yield):Q',
    color=alt.Color('mean(yield):Q', legend=None)
).properties(width=100, height=100)

# Sort x in ascending order
ascending = base.encode(
    alt.X(field='site', type='nominal', sort='ascending')
).properties(
    title='Ascending'
)

# Sort x in descending order
descending = base.encode(
    alt.X(field='site', type='nominal', sort='descending')
).properties(
    title='Descending'
)

# Sort x in an explicitly-specified order
explicit = base.encode(
    alt.X(field='site', type='nominal',
          sort=['Duluth', 'Grand Rapids', 'Morris',
                'University Farm', 'Waseca', 'Crookston'])
).properties(
    title='Explicit'
)

# Sort according to encoding channel
sortchannel = base.encode(
    alt.X(field='site', type='nominal',
          sort='y')
).properties(
    title='By Channel'
)

# Sort according to another field
sortfield = base.encode(
    alt.X(field='site', type='nominal',
          sort=alt.EncodingSortField(field='yield', op='mean'))
).properties(
    title='By Yield'
)

alt.concat(
    ascending, descending, explicit,
    sortchannel, sortfield,
    columns=3
)

#
####
###############

import altair as alt
from vega_datasets import data

barley = data.barley()
base = alt.Chart(barley).mark_point().encode(
    y='yield:Q',
).properties(width=200)

# Sort according to encoding channel
sortchannel = base.encode(
    alt.X(field='site', type='nominal',
          sort='y')
).properties(
    title='By Channel'
)

# Sort according to another field
sortfield = base.encode(
    alt.X(field='site', type='nominal',
          sort=alt.EncodingSortField(field='yield', op='min'))
).properties(
    title='By Min Yield'
)
sortchannel | sortfield


#####
## sort legends

alt.Chart(barley).mark_rect().encode(
    alt.X('mean(yield):Q', sort='ascending'),
    alt.Y('site:N', sort='descending'),
    alt.Color('site:N',
        sort=['Morris', 'Duluth', 'Grand Rapids',
              'University Farm', 'Waseca', 'Crookston']
    )
)

