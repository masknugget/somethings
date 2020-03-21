import altair as alt
from vega_datasets import data

source = data.barley()

alt.Chart(source).mark_bar().encode(
    x='year:O',
    y='sum(yield):Q',
    color='year:N',
    column='site:N'
)


#
import altair as alt
from vega_datasets import data

source = data.barley()

bars = alt.Chart().mark_bar().encode(
    x='year:O',
    y=alt.Y('mean(yield):Q', title='Mean Yield'),
    color='year:N',
)

error_bars = alt.Chart().mark_errorbar(extent='ci').encode(
    x='year:O',
    y='yield:Q'
)

alt.layer(bars, error_bars, data=source).facet(
    column='site:N'
)



##
import altair as alt
from vega_datasets import data

source = data.wheat()

alt.Chart(source).mark_bar().encode(
    x='wheat:Q',
    y="year:O"
).properties(height=700)



##
import altair as alt
from vega_datasets import data

source = data.barley()

alt.Chart(source).mark_bar().encode(
    x='sum(yield):Q',
    y='year:O',
    color='year:N',
    row='site:N'
)


##
import altair as alt
from vega_datasets import data

source = data.barley()

alt.Chart(source).mark_bar().encode(
    x='sum(yield)',
    y='variety',
    color='site'
)

#
import altair as alt
from vega_datasets import data

source = data.iowa_electricity()

alt.Chart(source).mark_bar(opacity=0.7).encode(
    x='year:O',
    y=alt.Y('net_generation:Q', stack=None),
    color="source",
)

#
import altair as alt
from vega_datasets import data

source = data.barley()

alt.Chart(source).mark_bar().encode(
    x=alt.X('sum(yield)', stack="normalize"),
    y='variety',
    color='site'
)



##
import altair as alt
from vega_datasets import data

source = data.barley()

alt.Chart(source).mark_bar().encode(
    x='sum(yield):Q',
    y=alt.Y('site:N', sort='-x')
)

##
import altair as alt
from vega_datasets import data

source = data.barley()

alt.Chart(source).mark_bar().encode(
    x='variety',
    y='sum(yield)',
    color='site'
)

#
import altair as alt
from vega_datasets import data

source = data.barley()

alt.Chart(source).mark_bar().encode(
    x='sum(yield)',
    y='variety',
    color='site',
    order=alt.Order(
      # Sort the segments of the bars by this field
      'site',
      sort='ascending'
    )
)


##
import altair as alt
from vega_datasets import data

source=data.barley()

bars = alt.Chart(source).mark_bar().encode(
    x=alt.X('sum(yield):Q', stack='zero'),
    y=alt.Y('variety:N'),
    color=alt.Color('site')
)

text = alt.Chart(source).mark_text(dx=-15, dy=3, color='white').encode(
    x=alt.X('sum(yield):Q', stack='zero'),
    y=alt.Y('variety:N'),
    detail='site:N',
    text=alt.Text('sum(yield):Q', format='.1f')
)

bars + text



##
import altair as alt
from vega_datasets import data

source = data.barley()

alt.Chart(source).mark_bar().encode(
    column='year',
    x='yield',
    y='variety',
    color='site'
).properties(width=220)
