import altair as alt
from vega_datasets import data

states = alt.topo_feature(data.us_10m.url, 'states')
capitals = data.us_state_capitals.url

# US states background
background = alt.Chart(states).mark_geoshape(
    fill='lightgray',
    stroke='white'
).properties(
    title='US State Capitols',
    width=650,
    height=400
).project('albersUsa')

# Points and text
hover = alt.selection(type='single', on='mouseover', nearest=True,
                      fields=['lat', 'lon'])

base = alt.Chart(capitals).encode(
    longitude='lon:Q',
    latitude='lat:Q',
)

text = base.mark_text(dy=-5, align='right').encode(
    alt.Text('city', type='nominal'),
    opacity=alt.condition(~hover, alt.value(0), alt.value(1))
)

points = base.mark_point().encode(
    color=alt.value('black'),
    size=alt.condition(~hover, alt.value(30), alt.value(100))
).add_selection(hover)

background + points + text



###
import altair as alt
from vega_datasets import data

source = data.population.url

pink_blue = alt.Scale(domain=('Male', 'Female'),
                      range=["steelblue", "salmon"])

slider = alt.binding_range(min=1900, max=2000, step=10)
select_year = alt.selection_single(name="year", fields=['year'],
                                   bind=slider, init={'year': 2000})

alt.Chart(source).mark_bar().encode(
    x=alt.X('sex:N', title=None),
    y=alt.Y('people:Q', scale=alt.Scale(domain=(0, 12000000))),
    color=alt.Color('sex:N', scale=pink_blue),
    column='age:O'
).properties(
    width=20
).add_selection(
    select_year
).transform_calculate(
    "sex", alt.expr.if_(alt.datum.sex == 1, "Male", "Female")
).transform_filter(
    select_year
).configure_facet(
    spacing=8
)



#################
import altair as alt
from vega_datasets import data

source = data.population.url

slider = alt.binding_range(min=1850, max=2000, step=10)
select_year = alt.selection_single(name='year', fields=['year'],
                                   bind=slider, init={'year': 2000})

base = alt.Chart(source).add_selection(
    select_year
).transform_filter(
    select_year
).transform_calculate(
    gender=alt.expr.if_(alt.datum.sex == 1, 'Male', 'Female')
).properties(
    width=250
)


color_scale = alt.Scale(domain=['Male', 'Female'],
                        range=['#1f77b4', '#e377c2'])

left = base.transform_filter(
    alt.datum.gender == 'Female'
).encode(
    y=alt.Y('age:O', axis=None),
    x=alt.X('sum(people):Q',
            title='population',
            sort=alt.SortOrder('descending')),
    color=alt.Color('gender:N', scale=color_scale, legend=None)
).mark_bar().properties(title='Female')

middle = base.encode(
    y=alt.Y('age:O', axis=None),
    text=alt.Text('age:Q'),
).mark_text().properties(width=20)

right = base.transform_filter(
    alt.datum.gender == 'Male'
).encode(
    y=alt.Y('age:O', axis=None),
    x=alt.X('sum(people):Q', title='population'),
    color=alt.Color('gender:N', scale=color_scale, legend=None)
).mark_bar().properties(title='Male')

alt.concat(left, middle, right, spacing=5)



######
import altair as alt
from vega_datasets import data

source = data.population.url

alt.Chart(source).mark_area().encode(
    x='age:O',
    y=alt.Y(
        'sum(people):Q',
        title='Population',
        axis=alt.Axis(format='~s')
    ),
    facet=alt.Facet('year:O', columns=5),
).properties(
    title='US Age Distribution By Year',
    width=90,
    height=80
)



###########
################
import altair as alt
from vega_datasets import data


base_wheat = alt.Chart(data.wheat.url).transform_calculate(
    year_end="+datum.year + 5")

base_monarchs = alt.Chart(data.monarchs.url).transform_calculate(
    offset="((!datum.commonwealth && datum.index % 2) ? -1: 1) * 2 + 95",
    off2="((!datum.commonwealth && datum.index % 2) ? -1: 1) + 95",
    y="95",
    x="+datum.start + (+datum.end - +datum.start)/2"
)

bars = base_wheat.mark_bar(**{"fill": "#aaa", "stroke": "#999"}).encode(
    x=alt.X("year:Q", axis=alt.Axis(format='d', tickCount=5)),
    y=alt.Y("wheat:Q", axis=alt.Axis(zindex=1)),
    x2=alt.X2("year_end")
)

area = base_wheat.mark_area(**{"color": "#a4cedb", "opacity": 0.7}).encode(
    x=alt.X("year:Q"),
    y=alt.Y("wages:Q")
)

area_line_1 = area.mark_line(**{"color": "#000", "opacity": 0.7})
area_line_2 = area.mark_line(**{"yOffset": -2, "color": "#EE8182"})

top_bars = base_monarchs.mark_bar(stroke="#000").encode(
    x=alt.X("start:Q"),
    x2=alt.X2("end"),
    y=alt.Y("y:Q"),
    y2=alt.Y2("offset"),
    fill=alt.Fill("commonwealth:N", legend=None, scale=alt.Scale(range=["black", "white"]))
)

top_text = base_monarchs.mark_text(**{"yOffset": 14, "fontSize": 9, "fontStyle": "italic"}).encode(
    x=alt.X("x:Q"),
    y=alt.Y("off2:Q"),
    text=alt.Text("name:N")
)

(bars + area + area_line_1 + area_line_2 + top_bars + top_text).properties(
    width=900, height=400
).configure_axis(
    title=None, gridColor="white", gridOpacity=0.25, domain=False
).configure_view(
    stroke="transparent"
)



#################
############################
import altair as alt
import pandas as pd

source = pd.DataFrame(
    [
        {"team": "Germany", "matchday": 1, "point": 0, "diff": -1},
        {"team": "Germany", "matchday": 2, "point": 3, "diff": 0},
        {"team": "Germany", "matchday": 3, "point": 3, "diff": -2},
        {"team": "Mexico", "matchday": 1, "point": 3, "diff": 1},
        {"team": "Mexico", "matchday": 2, "point": 6, "diff": 2},
        {"team": "Mexico", "matchday": 3, "point": 6, "diff": -1},
        {"team": "South Korea", "matchday": 1, "point": 0, "diff": -1},
        {"team": "South Korea", "matchday": 2, "point": 0, "diff": -2},
        {"team": "South Korea", "matchday": 3, "point": 3, "diff": 0},
        {"team": "Sweden", "matchday": 1, "point": 3, "diff": 1},
        {"team": "Sweden", "matchday": 2, "point": 3, "diff": 0},
        {"team": "Sweden", "matchday": 3, "point": 6, "diff": 3},
    ]
)

color_scale = alt.Scale(
    domain=["Germany", "Mexico", "South Korea", "Sweden"],
    range=["#000000", "#127153", "#C91A3C", "#0C71AB"],
)

alt.Chart(source).mark_line().encode(
    x="matchday:O", y="rank:O", color=alt.Color("team:N", scale=color_scale)
).transform_window(
    rank="rank()",
    sort=[
        alt.SortField("point", order="descending"),
        alt.SortField("diff", order="descending"),
    ],
    groupby=["matchday"],
).properties(title="World Cup 2018: Group F Rankings")

