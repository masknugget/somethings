import altair as alt
import pandas as pd
from vega_datasets import data

source = data.wheat()
threshold = pd.DataFrame([{"threshold": 90}])

bars = alt.Chart(source).mark_bar().encode(
    x="year:O",
    y="wheat:Q",
)

highlight = alt.Chart(source).mark_bar(color="#e45755").encode(
    x='year:O',
    y='baseline:Q',
    y2='wheat:Q'
).transform_filter(
    alt.datum.wheat > 90
).transform_calculate("baseline", "90")

rule = alt.Chart(threshold).mark_rule().encode(
    y='threshold:Q'
)

(bars + highlight + rule).properties(width=600)


##
import altair as alt
from vega_datasets import data

source = data.barley.url

alt.Chart(source).mark_point().encode(
    alt.X('median(yield):Q', scale=alt.Scale(zero=False)),
    y='variety:O',
    color='year:N',
    facet=alt.Facet('site:O', columns=2),
).properties(
    width=200,
    height=100,
)



## ---
import altair as alt
from vega_datasets import data

source = data.movies.url

alt.Chart(source).mark_rect().encode(
    alt.X('IMDB_Rating:Q', bin=alt.Bin(maxbins=60)),
    alt.Y('Rotten_Tomatoes_Rating:Q', bin=alt.Bin(maxbins=40)),
    alt.Color('count(IMDB_Rating):Q', scale=alt.Scale(scheme='greenblue'))
)



## ---

import altair as alt
from vega_datasets import data

source = data.population.url

alt.Chart(source).mark_boxplot().encode(
    x='age:O',
    y='people:Q'
)

# ---

import altair as alt
import pandas as pd

source = pd.DataFrame(
[
      {
        "date": "2009-06-01",
        "open": 28.7,
        "high": 30.05,
        "low": 28.45,
        "close": 30.04,
        "signal": "short",
        "ret": -4.89396411092985
      },
      {
        "date": "2009-06-02",
        "open": 30.04,
        "high": 30.13,
        "low": 28.3,
        "close": 29.63,
        "signal": "short",
        "ret": -0.322580645161295
      },
      {
        "date": "2009-06-03",
        "open": 29.62,
        "high": 31.79,
        "low": 29.62,
        "close": 31.02,
        "signal": "short",
        "ret": 3.68663594470045
      },
      {
        "date": "2009-06-04",
        "open": 31.02,
        "high": 31.02,
        "low": 29.92,
        "close": 30.18,
        "signal": "short",
        "ret": 4.51010886469673
      },
      {
        "date": "2009-06-05",
        "open": 29.39,
        "high": 30.81,
        "low": 28.85,
        "close": 29.62,
        "signal": "short",
        "ret": 6.08424336973478
      },
      {
        "date": "2009-06-08",
        "open": 30.84,
        "high": 31.82,
        "low": 26.41,
        "close": 29.77,
        "signal": "short",
        "ret": 1.2539184952978
      },
      {
        "date": "2009-06-09",
        "open": 29.77,
        "high": 29.77,
        "low": 27.79,
        "close": 28.27,
        "signal": "short",
        "ret": -5.02431118314424
      },
      {
        "date": "2009-06-10",
        "open": 26.9,
        "high": 29.74,
        "low": 26.9,
        "close": 28.46,
        "signal": "short",
        "ret": -5.46623794212217
      },
      {
        "date": "2009-06-11",
        "open": 27.36,
        "high": 28.11,
        "low": 26.81,
        "close": 28.11,
        "signal": "short",
        "ret": -8.3743842364532
      },
      {
        "date": "2009-06-12",
        "open": 28.08,
        "high": 28.5,
        "low": 27.73,
        "close": 28.15,
        "signal": "short",
        "ret": -5.52763819095477
      },
      {
        "date": "2009-06-15",
        "open": 29.7,
        "high": 31.09,
        "low": 29.64,
        "close": 30.81,
        "signal": "long",
        "ret": 3.4920634920635
      },
      {
        "date": "2009-06-16",
        "open": 30.81,
        "high": 32.75,
        "low": 30.07,
        "close": 32.68,
        "signal": "short",
        "ret": 0.155038759689914
      },
      {
        "date": "2009-06-17",
        "open": 31.19,
        "high": 32.77,
        "low": 30.64,
        "close": 31.54,
        "signal": "short",
        "ret": 5.82822085889571
      },
      {
        "date": "2009-06-18",
        "open": 31.54,
        "high": 31.54,
        "low": 29.6,
        "close": 30.03,
        "signal": "short",
        "ret": 8.17610062893082
      },
      {
        "date": "2009-06-19",
        "open": 29.16,
        "high": 29.32,
        "low": 27.56,
        "close": 27.99,
        "signal": "short",
        "ret": 8.59872611464968
      },
      {
        "date": "2009-06-22",
        "open": 30.4,
        "high": 32.05,
        "low": 30.3,
        "close": 31.17,
        "signal": "short",
        "ret": 15.4907975460123
      },
      {
        "date": "2009-06-23",
        "open": 31.3,
        "high": 31.54,
        "low": 27.83,
        "close": 30.58,
        "signal": "short",
        "ret": 11.7370892018779
      },
      {
        "date": "2009-06-24",
        "open": 30.58,
        "high": 30.58,
        "low": 28.79,
        "close": 29.05,
        "signal": "long",
        "ret": -10.4234527687296
      },
      {
        "date": "2009-06-25",
        "open": 29.45,
        "high": 29.56,
        "low": 26.3,
        "close": 26.36,
        "signal": "long",
        "ret": 0
      },
      {
        "date": "2009-06-26",
        "open": 27.09,
        "high": 27.22,
        "low": 25.76,
        "close": 25.93,
        "signal": "long",
        "ret": 0
      },
      {
        "date": "2009-06-29",
        "open": 25.93,
        "high": 27.18,
        "low": 25.29,
        "close": 25.35,
        "signal": "long",
        "ret": 5.26315789473684
      },
      {
        "date": "2009-06-30",
        "open": 25.36,
        "high": 27.38,
        "low": 25.02,
        "close": 26.35,
        "signal": "long",
        "ret": 6.73758865248228
      }
    ]
)
open_close_color = alt.condition("datum.open < datum.close",
                                 alt.value("#06982d"),
                                 alt.value("#ae1325"))

rule = alt.Chart(source).mark_rule().encode(
    alt.X(
        'yearmonthdate(date):T',
        scale=alt.Scale(domain=[{"month": 5, "date": 31, "year": 2009},
                                {"month": 7, "date": 1, "year": 2009}]),
        axis=alt.Axis(format='%m/%d', title='Date in 2009')
    ),
    alt.Y(
        'low',
        title='Price',
        scale=alt.Scale(zero=False),
    ),
    alt.Y2('high'),
    color=open_close_color
)

bar = alt.Chart(source).mark_bar().encode(
    x='yearmonthdate(date):T',
    y='open',
    y2='close',
    color=open_close_color
)

rule + bar



#########
import altair as alt
from vega_datasets import data

source = data.barley()

error_bars = alt.Chart(source).mark_errorbar(extent='stdev').encode(
  x=alt.X('yield:Q', scale=alt.Scale(zero=False)),
  y=alt.Y('variety:N')
)

points = alt.Chart(source).mark_point(filled=True, color='black').encode(
  x=alt.X('yield:Q', aggregate='mean'),
  y=alt.Y('variety:N'),
)

error_bars + points



########
import altair as alt
from vega_datasets import data

source = data.barley()

error_bars = alt.Chart(source).mark_errorbar(extent='ci').encode(
  x=alt.X('yield:Q', scale=alt.Scale(zero=False)),
  y=alt.Y('variety:N')
)

points = alt.Chart(source).mark_point(filled=True, color='black').encode(
  x=alt.X('yield:Q', aggregate='mean'),
  y=alt.Y('variety:N'),
)

error_bars + points

