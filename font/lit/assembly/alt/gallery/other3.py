import altair as alt
from vega_datasets import data

source = data.barley()

points = alt.Chart(source).mark_point(
    filled=True,
    color='black'
).encode(
    x=alt.X('mean(yield)', title='Barley Yield'),
    y=alt.Y(
        'variety',
        sort=alt.EncodingSortField(
            field='yield',
            op='mean',
            order='descending'
        )
    )
).properties(
    width=400,
    height=250
)

error_bars = points.mark_rule().encode(
    x='ci0(yield)',
    x2='ci1(yield)',
)

points + error_bars

##########
import altair as alt
import pandas as pd
import numpy as np

np.random.seed(42)

# Generating random data
source = pd.DataFrame({'samples': np.random.normal(50, 15, 100).astype(int).astype(str)})

# Splitting stem and leaf
source['stem'] = source['samples'].str[:-1]
source['leaf'] = source['samples'].str[-1]

source = source.sort_values(by=['stem', 'leaf'])

# Determining leaf position
source['position'] = source.groupby('stem').cumcount().add(1)

# Creating stem and leaf plot
alt.Chart(source).mark_text(
    align='left',
    baseline='middle',
    dx=-5
).encode(
    alt.X('position:Q', title='',
          axis=alt.Axis(ticks=False, labels=False, grid=False)
          ),
    alt.Y('stem:N', title='', axis=alt.Axis(tickSize=0)),
    text='leaf:N',
).configure_axis(
    labelFontSize=20
).configure_text(
    fontSize=20
)

##
import altair as alt
from vega_datasets import data

source = data.cars()

# Configure common options
base = alt.Chart(source).transform_aggregate(
    num_cars='count()',
    groupby=['Origin', 'Cylinders']
).encode(
    alt.X('Cylinders:O', scale=alt.Scale(paddingInner=0)),
    alt.Y('Origin:O', scale=alt.Scale(paddingInner=0)),
)

# Configure heatmap
heatmap = base.mark_rect().encode(
    color=alt.Color('num_cars:Q',
                    scale=alt.Scale(scheme='viridis'),
                    legend=alt.Legend(direction='horizontal')
                    )
)

# Configure text
text = base.mark_text(baseline='middle').encode(
    text='num_cars:Q',
    color=alt.condition(
        alt.datum.num_cars > 100,
        alt.value('black'),
        alt.value('white')
    )
)

# Draw the chart
heatmap + text

##
import altair as alt
from vega_datasets import data

alt.Chart(data.cars()).transform_density(
    'Miles_per_Gallon',
    as_=['Miles_per_Gallon', 'density'],
    extent=[5, 50],
    groupby=['Origin']
).mark_area(orient='horizontal').encode(
    y='Miles_per_Gallon:Q',
    color='Origin:N',
    x=alt.X(
        'density:Q',
        stack='center',
        impute=None,
        title=None,
        axis=alt.Axis(labels=False, values=[0], grid=False, ticks=True),
    ),
    column=alt.Column(
        'Origin:N',
        header=alt.Header(
            titleOrient='bottom',
            labelOrient='bottom',
            labelPadding=0,
        ),
    )
).properties(
    width=100
).configure_facet(
    spacing=0
).configure_view(
    stroke=None
)

##
import altair as alt
import pandas as pd

source = pd.DataFrame(
    {"data": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              2, 2, 2,
              3, 3,
              4, 4, 4, 4, 4, 4]
     }
)

alt.Chart(source).mark_circle(opacity=1).transform_window(
    id='rank()',
    groupby=['data']
).encode(
    alt.X('data:O'),
    alt.Y('id:O',
          axis=None,
          sort='descending')
).properties(height=100)
