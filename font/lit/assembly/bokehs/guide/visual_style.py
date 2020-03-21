from bokeh.io import output_file, show
from bokeh.plotting import figure

# We set-up a standard figure with two lines
p = figure(plot_width=500, plot_height=200, tools='')
visible_line = p.line([1, 2, 3], [1, 2, 1], line_color="blue")
invisible_line = p.line([1, 2, 3], [2, 1, 2], line_color="pink")

# We hide the xaxis, the xgrid lines, and the pink line
invisible_line.visible = False
p.xaxis.visible = False
p.xgrid.visible = False

output_file("styling_visible_property.html")

show(p)

##########
from bokeh.io import output_file, show
from bokeh.layouts import layout
from bokeh.models import BoxAnnotation, Toggle
from bokeh.plotting import figure

output_file("styling_visible_annotation_with_interaction.html")

p = figure(plot_width=600, plot_height=200, tools='')
p.line([1, 2, 3], [1, 2, 1], line_color="blue")
pink_line = p.line([1, 2, 3], [2, 1, 2], line_color="pink")

green_box = BoxAnnotation(left=1.5, right=2.5, fill_color='green', fill_alpha=0.1)
p.add_layout(green_box)

# Use js_link to connect button active property to glyph visible property

toggle1 = Toggle(label="Green Box", button_type="success", active=True)
toggle1.js_link('active', green_box, 'visible')

toggle2 = Toggle(label="Pink Line", button_type="success", active=True)
toggle2.js_link('active', pink_line, 'visible')

show(layout([p], [toggle1, toggle2]))

#######

# dimensions

from bokeh.plotting import figure, output_file, show

output_file("dimensions.html")

# create a new plot with specific dimensions
p = figure(plot_width=700)
p.plot_height = 300

p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

show(p)

## title
from bokeh.plotting import figure, output_file, show

output_file("title.html")

p = figure(plot_width=400, plot_height=400, title="Some Title")
p.title.text_color = "olive"
p.title.text_font = "times"
p.title.text_font_style = "italic"

p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

show(p)

## background
from bokeh.plotting import figure, output_file, show

output_file("background.html")

p = figure(plot_width=400, plot_height=400)
p.background_fill_color = "beige"
p.background_fill_alpha = 0.5

p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

show(p)

# boarder
from bokeh.plotting import figure, output_file, show

output_file("border.html")

p = figure(plot_width=400, plot_height=400)
p.border_fill_color = "whitesmoke"
p.min_border_left = 80

p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

show(p)

## outline

from bokeh.plotting import figure, output_file, show

output_file("outline.html")

p = figure(plot_width=400, plot_height=400)
p.outline_line_width = 7
p.outline_line_alpha = 0.3
p.outline_line_color = "navy"

p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

show(p)

## Glyphs
from bokeh.plotting import figure, output_file, show

output_file("axes.html")

p = figure(plot_width=400, plot_height=400)
r = p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7])

glyph = r.glyph
glyph.size = 60
glyph.fill_alpha = 0.2
glyph.line_color = "firebrick"
glyph.line_dash = [6, 3]
glyph.line_width = 2

show(p)

## select

from bokeh.io import output_file, show
from bokeh.models import Circle
from bokeh.plotting import figure

output_file("styling_selections.html")

plot = figure(plot_width=400, plot_height=400, tools="tap", title="Select a circle")
renderer = plot.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=50)

selected_circle = Circle(fill_alpha=1, fill_color="firebrick", line_color=None)
nonselected_circle = Circle(fill_alpha=0.2, fill_color="blue", line_color="firebrick")

renderer.selection_glyph = selected_circle
renderer.nonselection_glyph = nonselected_circle

show(plot)

##
from bokeh.io import output_file, show
from bokeh.plotting import figure

output_file("styling_selections.html")

plot = figure(plot_width=400, plot_height=400, tools="tap", title="Select a circle")
renderer = plot.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=50,

                       # set visual properties for selected glyphs
                       selection_color="firebrick",

                       # set visual properties for non-selected glyphs
                       nonselection_fill_alpha=0.2,
                       nonselection_fill_color="blue",
                       nonselection_line_color="firebrick",
                       nonselection_line_alpha=1.0)

show(plot)

### Hover Inspections

from bokeh.models import HoverTool
from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.glucose import data

output_file("styling_hover.html")

subset = data.loc['2010-10-06']

x, y = subset.index.to_series(), subset['glucose']

# Basic plot setup
plot = figure(plot_width=600, plot_height=300, x_axis_type="datetime", tools="",
              toolbar_location=None, title='Hover over points')

plot.line(x, y, line_dash="4 4", line_width=1, color='gray')

cr = plot.circle(x, y, size=20,
                 fill_color="grey", hover_fill_color="firebrick",
                 fill_alpha=0.05, hover_alpha=0.3,
                 line_color=None, hover_line_color="white")

plot.add_tools(HoverTool(tooltips=None, renderers=[cr], mode='hline'))

show(plot)

### Tool Overlays
import numpy as np

from bokeh.models import BoxSelectTool, BoxZoomTool, LassoSelectTool
from bokeh.plotting import figure, output_file, show

output_file("styling_tool_overlays.html")

x = np.random.random(size=200)
y = np.random.random(size=200)

# Basic plot setup
plot = figure(plot_width=400, plot_height=400, title='Select and Zoom',
              tools="box_select,box_zoom,lasso_select,reset")

plot.circle(x, y, size=5)

select_overlay = plot.select_one(BoxSelectTool).overlay

select_overlay.fill_color = "firebrick"
select_overlay.line_color = None

zoom_overlay = plot.select_one(BoxZoomTool).overlay

zoom_overlay.line_color = "olive"
zoom_overlay.line_width = 8
zoom_overlay.line_dash = "solid"
zoom_overlay.fill_color = None

plot.select_one(LassoSelectTool).overlay.line_dash = [10, 10]

show(plot)

### ToolBar Autohide
from bokeh.plotting import figure, output_file, show

output_file("styling_toolbar_autohide.html")

# Basic plot setup
plot = figure(width=400, height=400, title='Toolbar Autohide')
plot.line([1, 2, 3, 4, 5], [2, 5, 8, 2, 7])

# Set autohide to true to only show the toolbar when mouse is over plot
plot.toolbar.autohide = True

show(plot)

####### ---
from bokeh.plotting import figure, output_file, show

output_file("axes.html")

p = figure(plot_width=400, plot_height=400)
p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

# change just some things about the x-axes
p.xaxis.axis_label = "Temp"
p.xaxis.axis_line_width = 3
p.xaxis.axis_line_color = "red"

# change just some things about the y-axes
p.yaxis.axis_label = "Pressure"
p.yaxis.major_label_text_color = "orange"
p.yaxis.major_label_orientation = "vertical"

# change things on all axes
p.axis.minor_tick_in = -3
p.axis.minor_tick_out = 6

show(p)

## Labels
from bokeh.plotting import figure, output_file, show

output_file("bounds.html")

p = figure(plot_width=400, plot_height=400)
p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

p.xaxis.axis_label = "Lot Number"
p.xaxis.axis_label_text_color = "#aa6666"
p.xaxis.axis_label_standoff = 30

p.yaxis.axis_label = "Bin Count"
p.yaxis.axis_label_text_font_style = "italic"

show(p)

## bounds
from bokeh.plotting import figure, output_file, show

output_file("bounds.html")

p = figure(plot_width=400, plot_height=400)
p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

p.xaxis.bounds = (2, 4)

show(p)

## --- FixedTicker
from bokeh.plotting import figure
from bokeh.models.tickers import FixedTicker

p = figure()

# no additional tick locations will be displayed on the x-axis
p.xaxis.ticker = FixedTicker(ticks=[10, 20, 37.4])

from bokeh.plotting import figure, output_file, show

output_file("fixed_ticks.html")

p = figure(plot_width=400, plot_height=400)
p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

p.xaxis.ticker = [2, 3.5, 4]

show(p)

# --- Tick Lines---

from bokeh.plotting import figure, output_file, show

output_file("axes.html")

p = figure(plot_width=400, plot_height=400)
p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

p.xaxis.major_tick_line_color = "firebrick"
p.xaxis.major_tick_line_width = 3
p.xaxis.minor_tick_line_color = "orange"

p.yaxis.minor_tick_line_color = None

p.axis.major_tick_out = 10
p.axis.minor_tick_in = -3
p.axis.minor_tick_out = 8

show(p)

###########
from bokeh.models import NumeralTickFormatter
from bokeh.plotting import figure, output_file, show

output_file("gridlines.html")

p = figure(plot_width=400, plot_height=400)
p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

p.xaxis[0].formatter = NumeralTickFormatter(format="0.0%")
p.yaxis[0].formatter = NumeralTickFormatter(format="$0.00")

show(p)

##
from bokeh.models import PrintfTickFormatter
from bokeh.plotting import figure, output_file, show

output_file("gridlines.html")

p = figure(plot_width=400, plot_height=400)
p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

p.xaxis[0].formatter = PrintfTickFormatter(format="%4.1e")
p.yaxis[0].formatter = PrintfTickFormatter(format="%5.3f mu")

show(p)

from bokeh.models import FuncTickFormatter
from bokeh.plotting import figure, output_file, show

output_file("formatter.html")

p = figure(plot_width=500, plot_height=500)
p.circle([0, 2, 4, 6, 8, 10], [6, 2, 4, 10, 8, 0], size=30)

p.yaxis.formatter = FuncTickFormatter(code="""
    return Math.floor(tick) + " + " + (tick % 1).toFixed(2)
""")

show(p)

### Tick Label Orientation
from math import pi

from bokeh.plotting import figure, output_file, show

output_file("gridlines.html")

p = figure(plot_width=400, plot_height=400)
p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

p.xaxis.major_label_orientation = pi / 4
p.yaxis.major_label_orientation = "vertical"

show(p)

#####
from bokeh.plotting import figure, output_file, show

output_file("gridlines.html")

p = figure(plot_width=400, plot_height=400)
p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

# change just some things about the x-grid
p.xgrid.grid_line_color = None

# change just some things about the y-grid
p.ygrid.grid_line_alpha = 0.5
p.ygrid.grid_line_dash = [6, 4]

show(p)

## Minor Lines
from bokeh.plotting import figure, output_file, show

output_file("minorgridlines.html")

p = figure(plot_width=400, plot_height=400)
p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

# change just some things about the y-grid
p.ygrid.minor_grid_line_color = 'navy'
p.ygrid.minor_grid_line_alpha = 0.1

show(p)

####### Bands
from bokeh.plotting import figure, output_file, show

output_file("grid_band_fill.html")

p = figure(plot_width=400, plot_height=400)
p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

# change just some things about the x-grid
p.xgrid.grid_line_color = None

# change just some things about the y-grid
p.ygrid.band_fill_alpha = 0.1
p.ygrid.band_fill_color = "navy"

show(p)

#########
from bokeh.io import output_file, show
from bokeh.plotting import figure

output_file("grid_band_hatch.html")

p = figure(plot_height=250, plot_width=600, x_range=(0, 10), tools="", toolbar_location=None)
p.line(x=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
       y=[1, 3, 4, 3, 1, 2, 6, 5, 2, 3, 4])

p.ygrid.grid_line_color = None

ticks = [0, 2, 4, 6, 8, 10]
p.xaxis[0].ticker = ticks
p.xgrid[0].ticker = ticks

p.xgrid.band_hatch_pattern = "/"
p.xgrid.band_hatch_alpha = 0.6
p.xgrid.band_hatch_color = "lightgrey"
p.xgrid.band_hatch_weight = 0.5
p.xgrid.band_hatch_scale = 10

show(p)

## bounds

from bokeh.plotting import figure, output_file, show

output_file("bounds.html")

p = figure(plot_width=400, plot_height=400)
p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

p.grid.bounds = (2, 4)

show(p)

## Legends

import numpy as np

from bokeh.plotting import figure, output_file, show

x = np.linspace(0, 4 * np.pi, 100)
y = np.sin(x)

output_file("legend_labels.html")

p = figure()

p.circle(x, y, legend_label="sin(x)")
p.line(x, y, legend_label="sin(x)")

p.line(x, 2 * y, legend_label="2*sin(x)",
       line_dash=[4, 4], line_color="orange", line_width=2)

p.square(x, 3 * y, legend_label="3*sin(x)", fill_color=None, line_color="green")
p.line(x, 3 * y, legend_label="3*sin(x)", line_color="green")

p.legend.location = "bottom_left"

show(p)

### Outside the Plot Area

import numpy as np

from bokeh.models import Legend
from bokeh.plotting import figure, output_file, show

x = np.linspace(0, 4 * np.pi, 100)
y = np.sin(x)

output_file("legend_labels.html")

p = figure(toolbar_location="above")

r0 = p.circle(x, y)
r1 = p.line(x, y)

r2 = p.line(x, 2 * y, line_dash=[4, 4], line_color="orange", line_width=2)

r3 = p.square(x, 3 * y, fill_color=None, line_color="green")
r4 = p.line(x, 3 * y, line_color="green")

legend = Legend(items=[
    ("sin(x)", [r0, r1]),
    ("2*sin(x)", [r2]),
    ("3*sin(x)", [r3, r4]),
], location="center")

p.add_layout(legend, 'right')

show(p)

### title
import pandas as pd

from bokeh.palettes import Spectral4
from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT

output_file("styling_legend_title.html", title="styling_legend_title.py example")

p = figure(plot_width=800, plot_height=250, x_axis_type="datetime")

for data, name, color in zip([AAPL, IBM, MSFT, GOOG], ["AAPL", "IBM", "MSFT", "GOOG"], Spectral4):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    p.line(df['date'], df['close'], line_width=2, color=color, legend_label=name)

p.legend.location = "top_left"
p.legend.title = 'Stock'
p.legend.title_text_font_style = "bold"
p.legend.title_text_font_size = "15pt"

show(p)

## orientation
import numpy as np

from bokeh.plotting import figure, output_file, show

x = np.linspace(0, 4 * np.pi, 100)
y = np.sin(x)

output_file("legend_labels.html")

p = figure()

p.circle(x, y, legend_label="sin(x)")
p.line(x, y, legend_label="sin(x)")

p.line(x, 2 * y, legend_label="2*sin(x)",
       line_dash=[4, 4], line_color="orange", line_width=2)

p.square(x, 3 * y, legend_label="3*sin(x)", fill_color=None, line_color="green")
p.line(x, 3 * y, legend_label="3*sin(x)", line_color="green")

p.legend.orientation = "horizontal"

show(p)

### Label Text
import numpy as np

from bokeh.plotting import figure, output_file, show

x = np.linspace(0, 4 * np.pi, 100)
y = np.sin(x)

output_file("legend_labels.html")

p = figure()

p.circle(x, y, legend_label="sin(x)")
p.line(x, y, legend_label="sin(x)")

p.line(x, 2 * y, legend_label="2*sin(x)",
       line_dash=[4, 4], line_color="orange", line_width=2)

p.square(x, 3 * y, legend_label="3*sin(x)", fill_color=None, line_color="green")
p.line(x, 3 * y, legend_label="3*sin(x)", line_color="green")

p.legend.label_text_font = "times"
p.legend.label_text_font_style = "italic"
p.legend.label_text_color = "navy"

show(p)

### boarder
import numpy as np

from bokeh.plotting import figure, output_file, show

x = np.linspace(0, 4 * np.pi, 100)
y = np.sin(x)

output_file("legend_border.html")

p = figure()

p.circle(x, y, legend_label="sin(x)")
p.line(x, y, legend_label="sin(x)")

p.line(x, 2 * y, legend_label="2*sin(x)",
       line_dash=[4, 4], line_color="orange", line_width=2)

p.square(x, 3 * y, legend_label="3*sin(x)", fill_color=None, line_color="green")
p.line(x, 3 * y, legend_label="3*sin(x)", line_color="green")

p.legend.border_line_width = 3
p.legend.border_line_color = "navy"
p.legend.border_line_alpha = 0.5

show(p)

######### Background
import numpy as np

from bokeh.plotting import figure, output_file, show

x = np.linspace(0, 4 * np.pi, 100)
y = np.sin(x)

output_file("legend_background.html")

p = figure()

p.circle(x, y, legend_label="sin(x)")
p.line(x, y, legend_label="sin(x)")

p.line(x, 2 * y, legend_label="2*sin(x)",
       line_dash=[4, 4], line_color="orange", line_width=2)

p.square(x, 3 * y, legend_label="3*sin(x)", fill_color=None, line_color="green")
p.line(x, 3 * y, legend_label="3*sin(x)", line_color="green")

#  3*sin(x) curve should be under this legend at initial viewing, so
# we can see that the legend is transparent
p.legend.location = "bottom_right"
p.legend.background_fill_color = "navy"
p.legend.background_fill_alpha = 0.5

show(p)

###
import numpy as np

from bokeh.plotting import figure, output_file, show

x = np.linspace(0, 4 * np.pi, 100)
y = np.sin(x)

output_file("legend_labels.html")

p = figure()

p.circle(x, y, legend_label="sin(x)")
p.line(x, y, legend_label="sin(x)")

p.line(x, 2 * y, legend_label="2*sin(x)",
       line_dash=[4, 4], line_color="orange", line_width=2)

p.square(x, 3 * y, legend_label="3*sin(x)", fill_color=None, line_color="green")
p.line(x, 3 * y, legend_label="3*sin(x)", line_color="green")

p.legend.label_standoff = 5
p.legend.glyph_width = 50
p.legend.spacing = 10
p.legend.padding = 50
p.legend.margin = 50

show(p)
