import altair as alt
from vega_datasets import data

source = data.movies.url

alt.Chart(source).mark_circle().encode(
    alt.X('IMDB_Rating:Q', bin=True),
    alt.Y('Rotten_Tomatoes_Rating:Q', bin=True),
    size='count()'
)

##
import altair as alt
from vega_datasets import data

source = data.cars()

# Brush for selection
brush = alt.selection(type='interval')

# Scatter Plot
points = alt.Chart(source).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color=alt.condition(brush, 'Cylinders:O', alt.value('grey'))
).add_selection(brush)

# Base chart for data tables
ranked_text = alt.Chart(source).mark_text().encode(
    y=alt.Y('row_number:O', axis=None)
).transform_window(
    row_number='row_number()'
).transform_filter(
    brush
).transform_window(
    rank='rank(row_number)'
).transform_filter(
    alt.datum.rank < 20
)

# Data Tables
horsepower = ranked_text.encode(text='Horsepower:N').properties(title='Horsepower')
mpg = ranked_text.encode(text='Miles_per_Gallon:N').properties(title='MPG')
origin = ranked_text.encode(text='Origin:N').properties(title='Origin')
text = alt.hconcat(horsepower, mpg, origin)  # Combine data tables

# Build chart
alt.hconcat(
    points,
    text
).resolve_legend(
    color="independent"
)

##
import altair as alt
from vega_datasets import data

source = data.cars()

alt.Chart(source).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    size='Acceleration'
)

##
import altair as alt
from vega_datasets import data

source = data.driving()

alt.Chart(source).mark_line(point=True).encode(
    alt.X('miles', scale=alt.Scale(zero=False)),
    alt.Y('gas', scale=alt.Scale(zero=False)),
    order='year'
)

##
import altair as alt
from vega_datasets import data

source = data.cars()

# Configure the options common to all layers
brush = alt.selection(type='interval')
base = alt.Chart(source).add_selection(brush)

# Configure the points
points = base.mark_point().encode(
    x=alt.X('Miles_per_Gallon', title=''),
    y=alt.Y('Horsepower', title=''),
    color=alt.condition(brush, 'Origin', alt.value('grey'))
)

# Configure the ticks
tick_axis = alt.Axis(labels=False, domain=False, ticks=False)

x_ticks = base.mark_tick().encode(
    alt.X('Miles_per_Gallon', axis=tick_axis),
    alt.Y('Origin', title='', axis=tick_axis),
    color=alt.condition(brush, 'Origin', alt.value('lightgrey'))
)

y_ticks = base.mark_tick().encode(
    alt.X('Origin', title='', axis=tick_axis),
    alt.Y('Horsepower', axis=tick_axis),
    color=alt.condition(brush, 'Origin', alt.value('lightgrey'))
)

# Build the chart
y_ticks | (points & x_ticks)

##
import altair as alt
from vega_datasets import data

source = data.iris()

alt.Chart(source).mark_circle().encode(
    alt.X('sepalLength', scale=alt.Scale(zero=False)),
    alt.Y('sepalWidth', scale=alt.Scale(zero=False, padding=1)),
    color='species',
    size='petalWidth'
)

##
import numpy as np
import pandas as pd
import altair as alt

# Generate some random data
rng = np.random.RandomState(1)
x = rng.rand(40) ** 2
y = 10 - 1.0 / (x + 0.1) + rng.randn(40)
source = pd.DataFrame({"x": x, "y": y})

# Define the degree of the polynomial fits
degree_list = [1, 3, 5]

base = alt.Chart(source).mark_circle(color="black").encode(
    alt.X("x"), alt.Y("y")
)

polynomial_fit = [
    base.transform_regression(
        "x", "y", method="poly", order=order, as_=["x", str(order)]
    )
        .mark_line()
        .transform_fold([str(order)], as_=["degree", "y"])
        .encode(alt.Color("degree:N"))
    for order in degree_list
]

alt.layer(base, *polynomial_fit)

##
import altair as alt
from vega_datasets import data

source = data.normal_2d.url

base = alt.Chart(source).transform_quantile(
    'u',
    step=0.01,
    as_=['p', 'v']
).transform_calculate(
    uniform='quantileUniform(datum.p)',
    normal='quantileNormal(datum.p)'
).mark_point().encode(
    alt.Y('v:Q')
)

base.encode(x='uniform:Q') | base.encode(x='normal:Q')

##
import altair as alt
from vega_datasets import data

source = data.cars()

alt.Chart(source).mark_circle().encode(
    alt.X(alt.repeat("column"), type='quantitative'),
    alt.Y(alt.repeat("row"), type='quantitative'),
    color='Origin:N'
).properties(
    width=150,
    height=150
).repeat(
    row=['Horsepower', 'Acceleration', 'Miles_per_Gallon'],
    column=['Miles_per_Gallon', 'Acceleration', 'Horsepower']
).interactive()

##
import altair as alt
from vega_datasets import data

source = data.cars()

alt.Chart(source).transform_calculate(
    url='https://www.google.com/search?q=' + alt.datum.Name
).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color='Origin:N',
    href='url:N',
    tooltip=['Name:N', 'url:N']
)

##
import altair as alt
from vega_datasets import data

source = data.seattle_weather()

line = alt.Chart(source).mark_line(
    color='red',
    size=3
).transform_window(
    rolling_mean='mean(temp_max)',
    frame=[-15, 15]
).encode(
    x='date:T',
    y='rolling_mean:Q'
)

points = alt.Chart(source).mark_point().encode(
    x='date:T',
    y=alt.Y('temp_max:Q',
            axis=alt.Axis(title='Max Temp'))
)

points + line

###
import altair as alt
import pandas as pd
import numpy as np

# generate some data points with uncertainties
np.random.seed(0)
x = [1, 2, 3, 4, 5]
y = np.random.normal(10, 0.5, size=len(x))
yerr = 0.2

# set up data frame
source = pd.DataFrame({"x": x, "y": y, "yerr": yerr})

# the base chart
base = alt.Chart(source).transform_calculate(
    ymin="datum.y-datum.yerr",
    ymax="datum.y+datum.yerr"
)

# generate the points
points = base.mark_point(
    filled=True,
    size=50,
    color='black'
).encode(
    x=alt.X('x', scale=alt.Scale(domain=(0, 6))),
    y=alt.Y('y', scale=alt.Scale(domain=(10, 11)))
)

# generate the error bars
errorbars = base.mark_errorbar().encode(
    x="x",
    y="ymin:Q",
    y2="ymax:Q"
)

points + errorbars

###########
###################
import altair as alt
import pandas as pd

source = pd.DataFrame({
    'x': [1, 3, 5, 7, 9],
    'y': [1, 3, 5, 7, 9],
    'label': ['A', 'B', 'C', 'D', 'E']
})

points = alt.Chart(source).mark_point().encode(
    x='x:Q',
    y='y:Q'
)

text = points.mark_text(
    align='left',
    baseline='middle',
    dx=7
).encode(
    text='label'
)

points + text

###############################
###################
###########
import altair as alt
from vega_datasets import data

source = data.movies.url

stripplot = alt.Chart(source, width=40).mark_circle(size=8).encode(
    x=alt.X(
        'jitter:Q',
        title=None,
        axis=alt.Axis(values=[0], ticks=True, grid=False, labels=False),
        scale=alt.Scale(),
    ),
    y=alt.Y('IMDB_Rating:Q'),
    color=alt.Color('Major_Genre:N', legend=None),
    column=alt.Column(
        'Major_Genre:N',
        header=alt.Header(
            labelAngle=-90,
            titleOrient='top',
            labelOrient='bottom',
            labelAlign='right',
            labelPadding=3,
        ),
    ),
).transform_calculate(
    # Generate Gaussian jitter with a Box-Muller transform
    jitter='sqrt(-2*log(random()))*cos(2*PI*random())'
).configure_facet(
    spacing=0
).configure_view(
    stroke=None
)

stripplot

######
import altair as alt
from vega_datasets import data

source = data.github.url

alt.Chart(source).mark_circle().encode(
    x='hours(time):O',
    y='day(time):O',
    size='sum(count):Q'
)

##
import altair as alt
from vega_datasets import data

source = data.cars()

alt.Chart(source).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    row='Origin:N'
)
