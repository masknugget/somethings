# layers
import altair as alt
from altair.expr import datum

from vega_datasets import data
stocks = data.stocks.url

base = alt.Chart(stocks).encode(
    x='date:T',
    y='price:Q',
    color='symbol:N'
).transform_filter(
    datum.symbol == 'GOOG'
)

base.mark_line() + base.mark_point()


alt.layer(
  base.mark_line(),
  base.mark_point(),
  base.mark_rule()
).interactive()



## order of layers

import altair as alt
from vega_datasets import data

source = data.movies.url

heatmap = alt.Chart(source).mark_rect().encode(
    alt.X('IMDB_Rating:Q', bin=True),
    alt.Y('Rotten_Tomatoes_Rating:Q', bin=True),
    alt.Color('count()', scale=alt.Scale(scheme='greenblue'))
)

points = alt.Chart(source).mark_circle(
    color='black',
    size=5,
).encode(
    x='IMDB_Rating:Q',
    y='Rotten_Tomatoes_Rating:Q',
)

heatmap + points

points + heatmap


## ---
## Horizontal Concatenation

import altair as alt
from vega_datasets import data

iris = data.iris.url

chart1 = alt.Chart(iris).mark_point().encode(
    x='petalLength:Q',
    y='petalWidth:Q',
    color='species:N'
).properties(
    height=300,
    width=300
)

chart2 = alt.Chart(iris).mark_bar().encode(
    x='count()',
    y=alt.Y('petalWidth:Q', bin=alt.Bin(maxbins=30)),
    color='species:N'
).properties(
    height=300,
    width=100
)

chart1 | chart2
alt.hconcat(chart1, chart2)



#########

import altair as alt
from vega_datasets import data
sp500 = data.sp500.url

brush = alt.selection(type='interval', encodings=['x'])

upper = alt.Chart(sp500).mark_area().encode(
    x=alt.X('date:T', scale=alt.Scale(domain=brush)),
    y='price:Q'
).properties(
    width=600,
    height=200
)

lower = upper.properties(
    height=60
).add_selection(brush)

alt.vconcat(upper, lower)

#### Repeated Charts
import altair as alt
from vega_datasets import data

iris = data.iris.url

base = alt.Chart().mark_point().encode(
    color='species:N'
).properties(
    width=200,
    height=200
).interactive()

chart = alt.vconcat(data=iris)
for y_encoding in ['petalLength:Q', 'petalWidth:Q']:
    row = alt.hconcat()
    for x_encoding in ['sepalLength:Q', 'sepalWidth:Q']:
        row |= base.encode(x=x_encoding, y=y_encoding)
    chart &= row
chart



####--------
import altair as alt
from vega_datasets import data
iris = data.iris.url

alt.Chart(iris).mark_point().encode(
    alt.X(alt.repeat("column"), type='quantitative'),
    alt.Y(alt.repeat("row"), type='quantitative'),
    color='species:N'
).properties(
    width=200,
    height=200
).repeat(
    row=['petalLength', 'petalWidth'],
    column=['sepalLength', 'sepalWidth']
).interactive()

### Faceted Charts
import altair as alt
from altair.expr import datum
from vega_datasets import data
iris = data.iris.url

base = alt.Chart(iris).mark_point().encode(
    x='petalLength:Q',
    y='petalWidth:Q',
    color='species:N'
).properties(
    width=160,
    height=160
)

chart = alt.hconcat()
for species in ['setosa', 'versicolor', 'virginica']:
    chart |= base.transform_filter(datum.species == species)
chart

alt.Chart(iris).mark_point().encode(
    x='petalLength:Q',
    y='petalWidth:Q',
    color='species:N'
).properties(
    width=180,
    height=180
).facet(
    column='species:N'
)


alt.Chart(iris).mark_point().encode(
    x='petalLength:Q',
    y='petalWidth:Q',
    color='species:N',
    column='species:N'
).properties(
    width=180,
    height=180
)

#####

hover = alt.selection_single(on='mouseover', nearest=True, empty='none')

base = alt.Chart(iris).encode(
    x='petalLength:Q',
    y='petalWidth:Q',
    color=alt.condition(hover, 'species:N', alt.value('lightgray'))
).properties(
    width=180,
    height=180,
)

points = base.mark_point().add_selection(
    hover
)

text = base.mark_text(dy=-5).encode(
    text = 'species:N',
    opacity = alt.condition(hover, alt.value(1), alt.value(0))
)

alt.layer(points, text).facet(
    'species:N',
)

#########
# Scale and Guide Resolution


import altair as alt
from vega_datasets import data

source = data.cars()

base = alt.Chart(source).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q'
).properties(
    width=200,
    height=200
)

alt.concat(
    base.encode(color='Origin:N'),
    base.encode(color='Cylinders:O')
)

alt.concat(
    base.encode(color='Origin:N'),
    base.encode(color='Cylinders:O')
).resolve_scale(
    color='independent'
)

