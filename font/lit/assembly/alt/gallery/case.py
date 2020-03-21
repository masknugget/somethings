import altair as alt
from vega_datasets import data

source = data.anscombe()

alt.Chart(source).mark_circle().encode(
    alt.X('X', scale=alt.Scale(zero=False)),
    alt.Y('Y', scale=alt.Scale(zero=False)),
    alt.Facet('Series', columns=2),
).properties(
    width=180,
    height=180,
)


##
import altair as alt
from vega_datasets import data

source = data.co2_concentration.url

base = alt.Chart(
    source,
    title="Carbon Dioxide in the Atmosphere"
).transform_calculate(
    year="year(datum.Date)"
).transform_calculate(
    decade="floor(datum.year / 10)"
).transform_calculate(
    scaled_date="(datum.year % 10) + (month(datum.Date)/12)"
).transform_window(
    first_date='first_value(scaled_date)',
    last_date='last_value(scaled_date)',
    sort=[{"field": "scaled_date", "order": "ascending"}],
    groupby=['decade'],
    frame=[None, None]
).transform_calculate(
  end="datum.first_date === datum.scaled_date ? 'first' : datum.last_date === datum.scaled_date ? 'last' : null"
).encode(
    x=alt.X(
        "scaled_date:Q",
        axis=alt.Axis(title="Year into Decade", tickCount=11)
    ),
    y=alt.Y(
        "CO2:Q",
        title="CO2 concentration in ppm",
        scale=alt.Scale(zero=False)
    )
)

line = base.mark_line().encode(
    color=alt.Color(
        "decade:O",
        scale=alt.Scale(scheme="magma"),
        legend=None
    )
)

text = base.encode(text="year:N")

start_year = text.transform_filter(
  alt.datum.end == 'first'
).mark_text(baseline="top")

end_year = text.transform_filter(
  alt.datum.end == 'last'
).mark_text(baseline="bottom")

(line + start_year + end_year).configure_text(
    align="left",
    dx=1,
    dy=3
).properties(width=600, height=375)


##
import altair as alt
from vega_datasets import data

source = data.barley()

alt.Chart(source, title="The Morris Mistake").mark_point().encode(
    alt.X(
        'yield:Q',
        title="Barley Yield (bushels/acre)",
        scale=alt.Scale(zero=False),
        axis=alt.Axis(grid=False)
    ),
    alt.Y(
        'variety:N',
        title="",
        sort='-x',
        axis=alt.Axis(grid=True)
    ),
    color=alt.Color('year:N', legend=alt.Legend(title="Year")),
    row=alt.Row(
        'site:N',
        title="",
        sort=alt.EncodingSortField(field='yield', op='sum', order='descending'),
    )
).properties(
    height=alt.Step(20)
).configure_view(stroke="transparent")



###
import altair as alt
from vega_datasets import data

# Since these data are each more than 5,000 rows we'll import from the URLs
airports = data.airports.url
flights_airport = data.flights_airport.url

states = alt.topo_feature(data.us_10m.url, feature="states")

# Create mouseover selection
select_city = alt.selection_single(
    on="mouseover", nearest=True, fields=["origin"], empty="none"
)

# Define which attributes to lookup from airports.csv
lookup_data = alt.LookupData(
    airports, key="iata", fields=["state", "latitude", "longitude"]
)

background = alt.Chart(states).mark_geoshape(
    fill="lightgray",
    stroke="white"
).properties(
    width=750,
    height=500
).project("albersUsa")

connections = alt.Chart(flights_airport).mark_rule(opacity=0.35).encode(
    latitude="latitude:Q",
    longitude="longitude:Q",
    latitude2="lat2:Q",
    longitude2="lon2:Q"
).transform_lookup(
    lookup="origin",
    from_=lookup_data
).transform_lookup(
    lookup="destination",
    from_=lookup_data,
    as_=["state", "lat2", "lon2"]
).transform_filter(
    select_city
)

points = alt.Chart(flights_airport).mark_circle().encode(
    latitude="latitude:Q",
    longitude="longitude:Q",
    size=alt.Size("routes:Q", scale=alt.Scale(range=[0, 1000]), legend=None),
    order=alt.Order("routes:Q", sort="descending"),
    tooltip=["origin:N", "routes:Q"]
).transform_aggregate(
    routes="count()",
    groupby=["origin"]
).transform_lookup(
    lookup="origin",
    from_=lookup_data
).transform_filter(
    (alt.datum.state != "PR") & (alt.datum.state != "VI")
).add_selection(
    select_city
)

(background + connections + points).configure_view(stroke=None)

###
import altair as alt

source = "https://frdata.wikimedia.org/donationdata-vs-day.csv"

alt.Chart(source).mark_line().encode(
    alt.X('monthdate(date):T', title='Month', axis=alt.Axis(format='%B')),
    alt.Y('max(ytdsum):Q', title='Cumulative Donations', stack=None),
    alt.Color('year(date):O', legend=alt.Legend(title='Year')),
    alt.Order('year(data):O')
)

############
import altair as alt

source = [
      {"year": "1875", "population": 1309},
      {"year": "1890", "population": 1558},
      {"year": "1910", "population": 4512},
      {"year": "1925", "population": 8180},
      {"year": "1933", "population": 15915},
      {"year": "1939", "population": 24824},
      {"year": "1946", "population": 28275},
      {"year": "1950", "population": 29189},
      {"year": "1964", "population": 29881},
      {"year": "1971", "population": 26007},
      {"year": "1981", "population": 24029},
      {"year": "1985", "population": 23340},
      {"year": "1989", "population": 22307},
      {"year": "1990", "population": 22087},
      {"year": "1991", "population": 22139},
      {"year": "1992", "population": 22105},
      {"year": "1993", "population": 22242},
      {"year": "1994", "population": 22801},
      {"year": "1995", "population": 24273},
      {"year": "1996", "population": 25640},
      {"year": "1997", "population": 27393},
      {"year": "1998", "population": 29505},
      {"year": "1999", "population": 32124},
      {"year": "2000", "population": 33791},
      {"year": "2001", "population": 35297},
      {"year": "2002", "population": 36179},
      {"year": "2003", "population": 36829},
      {"year": "2004", "population": 37493},
      {"year": "2005", "population": 38376},
      {"year": "2006", "population": 39008},
      {"year": "2007", "population": 39366},
      {"year": "2008", "population": 39821},
      {"year": "2009", "population": 40179},
      {"year": "2010", "population": 40511},
      {"year": "2011", "population": 40465},
      {"year": "2012", "population": 40905},
      {"year": "2013", "population": 41258},
      {"year": "2014", "population": 41777}
    ]

source2 = [{
            "start": "1933",
            "end": "1945",
            "event": "Nazi Rule"
          },
          {
            "start": "1948",
            "end": "1989",
            "event": "GDR (East Germany)"
          }]


source = alt.pd.DataFrame(source)
source2 = alt.pd.DataFrame(source2)


line = alt.Chart(source).mark_line(color='#333').encode(
    alt.X('year:T', axis=alt.Axis(format='%Y')),
    y='population'
).properties(
    width=500,
    height=300
)

point = line.mark_point(color='#333')

rect = alt.Chart(source2).mark_rect().encode(
    x='start:T',
    x2='end:T',
    color='event:N'
)

rect + line + point


###
import altair as alt
from vega_datasets import data

source = data.gapminder_health_income.url

alt.Chart(source).mark_circle().encode(
    alt.X('income:Q', scale=alt.Scale(type='log')),
    alt.Y('health:Q', scale=alt.Scale(zero=False)),
    size='population:Q'
)
