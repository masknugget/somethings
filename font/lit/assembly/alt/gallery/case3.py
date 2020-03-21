import altair as alt
from vega_datasets import data

source = data.disasters.url

alt.Chart(source).mark_circle(
    opacity=0.8,
    stroke='black',
    strokeWidth=1
).encode(
    alt.X('Year:O', axis=alt.Axis(labelAngle=0)),
    alt.Y('Entity:N'),
    alt.Size('Deaths:Q',
        scale=alt.Scale(range=[0, 4000]),
        legend=alt.Legend(title='Annual Global Deaths')
    ),
    alt.Color('Entity:N', legend=None)
).properties(
    width=450,
    height=320
).transform_filter(
    alt.datum.Entity != 'All natural disasters'
)


##
import altair as alt
from vega_datasets import data

# Since the data is more than 5,000 rows we'll import it from a URL
source = data.zipcodes.url

alt.Chart(source).transform_calculate(
    "leading digit", alt.expr.substring(alt.datum.zip_code, 0, 1)
).mark_circle(size=3).encode(
    longitude='longitude:Q',
    latitude='latitude:Q',
    color='leading digit:N',
    tooltip='zip_code:N'
).project(
    type='albersUsa'
).properties(
    width=650,
    height=400
)


##
import altair as alt
from vega_datasets import data

# Since the data is more than 5,000 rows we'll import it from a URL
source = data.seattle_temps.url

alt.Chart(
    source,
    title="2010 Daily High Temperature (F) in Seattle, WA"
).mark_rect().encode(
    x='date(date):O',
    y='month(date):O',
    color=alt.Color('max(temp):Q', scale=alt.Scale(scheme="inferno")),
    tooltip=[
        alt.Tooltip('monthdate(date):T', title='Date'),
        alt.Tooltip('max(temp):Q', title='Max Temp')
    ]
).properties(width=550)


##
import altair as alt
from vega_datasets import data

source = data.seattle_weather()

scale = alt.Scale(domain=['sun', 'fog', 'drizzle', 'rain', 'snow'],
                  range=['#e7ba52', '#a7a7a7', '#aec7e8', '#1f77b4', '#9467bd'])
color = alt.Color('weather:N', scale=scale)

# We create two selections:
# - a brush that is active on the top panel
# - a multi-click that is active on the bottom panel
brush = alt.selection_interval(encodings=['x'])
click = alt.selection_multi(encodings=['color'])

# Top panel is scatter plot of temperature vs time
points = alt.Chart().mark_point().encode(
    alt.X('monthdate(date):T', title='Date'),
    alt.Y('temp_max:Q',
        title='Maximum Daily Temperature (C)',
        scale=alt.Scale(domain=[-5, 40])
    ),
    color=alt.condition(brush, color, alt.value('lightgray')),
    size=alt.Size('precipitation:Q', scale=alt.Scale(range=[5, 200]))
).properties(
    width=550,
    height=300
).add_selection(
    brush
).transform_filter(
    click
)

# Bottom panel is a bar chart of weather type
bars = alt.Chart().mark_bar().encode(
    x='count()',
    y='weather:N',
    color=alt.condition(click, color, alt.value('lightgray')),
).transform_filter(
    brush
).properties(
    width=550,
).add_selection(
    click
)

alt.vconcat(
    points,
    bars,
    data=source,
    title="Seattle Weather: 2012-2015"
)


import altair as alt
import pandas as pd
from vega_datasets import data

source = data.us_employment()
presidents = pd.DataFrame([
    {
        "start": "2006-01-01",
        "end": "2009-01-19",
        "president": "Bush"
    },
    {
        "start": "2009-01-20",
        "end": "2015-12-31",
        "president": "Obama"
    }
])

bars = alt.Chart(
    source,
    title="The U.S. employment crash during the Great Recession"
).mark_bar().encode(
    x=alt.X("month:T", title=""),
    y=alt.Y("nonfarm_change:Q", title="Change in non-farm employment (in thousands)"),
    color=alt.condition(
        alt.datum.nonfarm_change > 0,
        alt.value("steelblue"),
        alt.value("orange")
    )
)

rule = alt.Chart(presidents).mark_rule(
    color="black",
    strokeWidth=2
).encode(
    x='end:T'
).transform_filter(alt.datum.president == "Bush")

text = alt.Chart(presidents).mark_text(
    align='left',
    baseline='middle',
    dx=7,
    dy=-135,
    size=11
).encode(
    x='start:T',
    x2='end:T',
    text='president',
    color=alt.value('#000000')
)

(bars + rule + text).properties(width=600)


##
import altair as alt
from vega_datasets import data

source = data.movies.url

# Top 10 movies by IMBD rating
alt.Chart(
    source,
).mark_bar().encode(
    x=alt.X('Title:N', sort='-y'),
    y=alt.Y('IMDB_Rating:Q'),
    color=alt.Color('IMDB_Rating:Q')

).transform_window(
    rank='rank(IMDB_Rating)',
    sort=[alt.SortField('IMDB_Rating', order='descending')]
).transform_filter(
    (alt.datum.rank < 10)
)

##
import altair as alt
import pandas as pd
import numpy as np

# Excerpt from A Tale of Two Cities; public domain text
text = """
It was the best of times, it was the worst of times, it was the age of wisdom,
it was the age of foolishness, it was the epoch of belief, it was the epoch of
incredulity, it was the season of Light, it was the season of Darkness, it was
the spring of hope, it was the winter of despair, we had everything before us,
we had nothing before us, we were all going direct to Heaven, we were all going
direct the other way - in short, the period was so far like the present period,
that some of its noisiest authorities insisted on its being received, for good
or for evil, in the superlative degree of comparison only.
"""

source = pd.DataFrame(
    {'letters': np.array([c for c in text if c.isalpha()])}
)

alt.Chart(source).transform_aggregate(
    count='count()',
    groupby=['letters']
).transform_window(
    rank='rank(count)',
    sort=[alt.SortField('count', order='descending')]
).transform_filter(
    alt.datum.rank < 10
).mark_bar().encode(
    y=alt.Y('letters:N', sort='-x'),
    x='count:Q',
)



##
import altair as alt
from vega_datasets import data

source = data.movies.url

alt.Chart(source).mark_bar().encode(
    x=alt.X("aggregate_gross:Q", aggregate="mean", title=None),
    y=alt.Y(
        "ranked_director:N",
        sort=alt.Sort(op="mean", field="aggregate_gross", order="descending"),
        title=None,
    ),
).transform_aggregate(
    aggregate_gross='mean(Worldwide_Gross)',
    groupby=["Director"],
).transform_window(
    rank='row_number()',
    sort=[alt.SortField("aggregate_gross", order="descending")],
).transform_calculate(
    ranked_director="datum.rank < 10 ? datum.Director : 'All Others'"
).properties(
    title="Top Directors by Average Worldwide Gross",
)

