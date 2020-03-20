import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a','b','c']
)

st.line_chart(chart_data)


# ==

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'],
)

st.area_chart(chart_data)
st.bar_chart(chart_data)


# = pyplit

import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
plt.hist(arr, bins=20)
st.pyplot()


# altair_chart

import pandas as pd
import numpy as np
import altair as alt

df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b','c']
)

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c'
)

st.altair_chart(c, width=-1)


# vega_lite_chart

import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c']
)

st.vega_lite_chart(df, {
    'mark': 'circle',
    'encoding': {
        'x': {'field': 'a', 'type': 'quantitative'},
        'y': {'field': 'b', 'type': 'quantitative'},
        'size': {'field': 'c', 'type': 'quantitative'},
        'color': {'field': 'c', 'type': 'quantitative'},
    }
})


## ---
import plotly.figure_factory as ff
import numpy as np

x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

hist_data = [x1, x2, x3]

group_labels = ['Group1', 'Group2', 'Group3']
fig = ff.create_distplot(
    hist_data, group_labels, bin_size=[.1, .25, .5]
)

# plot!
st.plotly_chart(fig)

## ---
from bokeh.plotting import figure

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
    title='simple line example',
    x_axis_label='x',
    y_axis_label='y'
)
p.line(x, y, legend='Trend', line_width=2)
st.bokeh_chart(p)


## =====

df = pd.DataFrame(
    np.random.randn(1000, 2)/[50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=df,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))


st.deck_gl_chart(
    viewport={
        'latitude': 37.76,
        'longitude': -122.4,
        'zoom': 11,
        'pitch': 50,
    },
    layers=[{
        'type': 'HexagonLayer',
        'data': df,
        'radius': 200,
        'elevationScale': 4,
        'elevationRange': [0, 1000],
        'pickable': True,
        'extruded': True,
    }, {
        'type': 'ScatterplotLayer',
        'data': df,
    }])


import graphviz as graphviz

# Create a graphlib graph object
graph = graphviz.DiGraph()
graph.edge('run', 'intr')
graph.edge('intr', 'runbl')
graph.edge('runbl', 'run')
graph.edge('run', 'kernel')
graph.edge('kernel', 'zombie')
graph.edge('kernel', 'sleep')
graph.edge('kernel', 'runmem')
graph.edge('sleep', 'swap')
graph.edge('swap', 'runswap')
graph.edge('runswap', 'new')
graph.edge('runswap', 'runmem')
graph.edge('new', 'runmem')
graph.edge('sleep', 'runmem')

st.graphviz_chart(graph)

import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(1000, 2)/[50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)



## --image---

from PIL import Image
image = Image.open('sunrise.jpg')
st.image(image, caption='Sunrise by the mountains', use_column_width=True)


audio_file = open('myaudio.ogg', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes,format='audio/ogg')

# --video--

video_file = open('myvideo.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

