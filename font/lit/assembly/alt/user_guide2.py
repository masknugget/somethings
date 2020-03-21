'''
marks
mark_area()
mark_bar()
mark_circle()
mark_geoshape()
mark_image()
mark_line()
mark_point()
mark_rect()
mark_rule()
mark_text()
mark_boxplot()
mark_errorband()
mark_errorbar()
'''


# ---
import altair as alt
from vega_datasets import data

url = data.cars.url

alt.Chart(url).mark_circle(
    color='red',
    opacity=0.3
).encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q'
)

# ---
import altair as alt
import pandas as pd

source = pd.DataFrame.from_records([
      {"x": 0.5, "y": 0.5, "img": "https://vega.github.io/vega-datasets/data/ffox.png"},
      {"x": 1.5, "y": 1.5, "img": "https://vega.github.io/vega-datasets/data/gimp.png"},
      {"x": 2.5, "y": 2.5, "img": "https://vega.github.io/vega-datasets/data/7zip.png"}
])

alt.Chart(source).mark_image(
    width=50,
    height=50
).encode(
    x='x',
    y='y',
    url='img'
)

# ---
import altair as alt
from vega_datasets import data

source = data.population.url

alt.Chart(source).mark_boxplot().encode(
    y='people:Q'
).properties(
    width=200,
    height=300
)


# ---
import altair as alt
from vega_datasets import data

source = data.population.url

alt.Chart(source).mark_boxplot().encode(
    x='age:O',
    y='people:Q'
)

# ===
import altair as alt
from vega_datasets import data

source = data.population.url

alt.Chart(source).mark_boxplot(extent=3.0).encode(
    x='age:O',
    y='people:Q'
)

# ---
import altair as alt
from vega_datasets import data

source = data.population.url

alt.Chart(source).mark_boxplot(extent='min-max').encode(
    x='age:O',
    y='people:Q'
)

#
#Bindings, Selections, Conditions: Making Charts Interactive
#

import altair as alt
from vega_datasets import data

cars = data.cars.url

alt.Chart(cars).mark_point().encode(
    x='Miles_per_Gallon:Q',
    y='Horsepower:Q',
    color='Origin:N'
)

brush = alt.selection_interval()  # selection of type "interval"

alt.Chart(cars).mark_point().encode(
    x='Miles_per_Gallon:Q',
    y='Horsepower:Q',
    color='Origin:N'
).add_selection(
    brush
)

alt.Chart(cars).mark_point().encode(
    x='Miles_per_Gallon:Q',
    y='Horsepower:Q',
    color=alt.condition(brush, 'Origin:N', alt.value('lightgray'))
).add_selection(
    brush
)


chart = alt.Chart(cars).mark_point().encode(
    y='Horsepower:Q',
    color=alt.condition(brush, 'Origin:N', alt.value('lightgray'))
).properties(
    width=250,
    height=250
).add_selection(
    brush
)

chart.encode(x='Acceleration:Q') | chart.encode(x='Miles_per_Gallon:Q')

###
brush = alt.selection_interval(encodings=['x'])

chart = alt.Chart(cars).mark_point().encode(
    y='Horsepower:Q',
    color=alt.condition(brush, 'Origin:N', alt.value('lightgray'))
).properties(
    width=250,
    height=250
).add_selection(
    brush
)

chart.encode(x='Acceleration:Q') | chart.encode(x='Miles_per_Gallon:Q')



## simple types
def make_example(selector):
    cars = data.cars.url

    return alt.Chart(cars).mark_rect().encode(
        x="Cylinders:O",
        y="Origin:N",
        color=alt.condition(selector, 'count()', alt.value('lightgray'))
    ).properties(
        width=300,
        height=180
    ).add_selection(
        selector
    )

interval = alt.selection_interval()
make_example(interval)

interval_x = alt.selection_interval(encodings=['x'], empty='none')
make_example(interval_x)


##---
scales = alt.selection_interval(bind='scales')

alt.Chart(cars).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color='Origin:N'
).add_selection(
    scales
)

# --- Single Selections
single = alt.selection_single()
make_example(single)

single_nearest = alt.selection_single(on='mouseover', nearest=True)
make_example(single_nearest)


multi = alt.selection_multi()
make_example(multi)

multi_mouseover = alt.selection_multi(on='mouseover', toggle=False, empty='none')
make_example(multi_mouseover)

# --- Composing Multiple Selections
alex = alt.selection_interval(
    on="[mousedown[event.altKey], mouseup] > mousemove",
    name='alex'
)
morgan = alt.selection_interval(
    on="[mousedown[event.shiftKey], mouseup] > mousemove",
    mark=alt.BrushConfig(fill="#fdbb84", fillOpacity=0.5, stroke="#e34a33"),
    name='morgan'
)

alt.Chart(cars).mark_rect().encode(
    x='Cylinders:O',
    y='Origin:O',
    color=alt.condition(alex | morgan, 'count()', alt.ColorValue("grey"))
).add_selection(
    alex, morgan
).properties(
    width=300,
    height=180
)

## --- Selection Targets: Fields and Encodings
selection = alt.selection_multi(fields=['Origin'])
color = alt.condition(selection,
                      alt.Color('Origin:N', legend=None),
                      alt.value('lightgray'))

scatter = alt.Chart(cars).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color=color,
    tooltip='Name:N'
)

legend = alt.Chart(cars).mark_point().encode(
    y=alt.Y('Origin:N', axis=alt.Axis(orient='right')),
    color=color
).add_selection(
    selection
)

scatter | legend


###########
selection = alt.selection_multi(fields=['Origin', 'Cylinders'])
color = alt.condition(selection,
                      alt.Color('Origin:N', legend=None),
                      alt.value('lightgray'))

scatter = alt.Chart(cars).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color=color,
    tooltip='Name:N'
)

legend = alt.Chart(cars).mark_rect().encode(
    y=alt.Y('Origin:N', axis=alt.Axis(orient='right')),
    x='Cylinders:O',
    color=color
).add_selection(
    selection
)

scatter | legend

# Input Element Binding
input_dropdown = alt.binding_select(options=['Europe','Japan','USA'])
selection = alt.selection_single(fields=['Origin'], bind=input_dropdown, name='Country of ')
color = alt.condition(selection,
                    alt.Color('Origin:N', legend=None),
                    alt.value('lightgray'))

alt.Chart(cars).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color=color,
    tooltip='Name:N'
).add_selection(
    selection
)


###

input_dropdown = alt.binding_select(options=['Europe','Japan','USA'])
selection = alt.selection_single(fields=['Origin'], bind=input_dropdown, name='Country of ')
color = alt.condition(selection,
                    alt.Color('Origin:N', legend=None),
                    alt.value('lightgray'))

alt.Chart(cars).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color='Origin:N',
    tooltip='Name:N'
).add_selection(
    selection
).transform_filter(
    selection
)



# scale binding
selection = alt.selection_interval(bind='scales')

alt.Chart(cars).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color='Origin:N',
    tooltip='Name:N'
).add_selection(
    selection
)

### Selection Values in Expressions

import altair as alt
import pandas as pd
import numpy as np

rand = np.random.RandomState(42)

df = pd.DataFrame({
    'xval': range(100),
    'yval': rand.randn(100).cumsum()
})

slider = alt.binding_range(min=0, max=100, step=1, name='cutoff:')
selector = alt.selection_single(name="SelectorName", fields=['cutoff'],
                                bind=slider, init={'cutoff': 50})

alt.Chart(df).mark_point().encode(
    x='xval',
    y='yval',
    color=alt.condition(
        alt.datum.xval < selector.cutoff,
        alt.value('red'), alt.value('blue')
    )
).add_selection(
    selector
)

