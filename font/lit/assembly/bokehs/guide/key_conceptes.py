'''
Application
BokehJS
Documents
Embedding
Glyphs
Models
Server
Widgets

'''
from bokeh.models import Rect
from bokeh.plotting import figure, output_file, show

output_file("output.html")

p = figure()
p.line(x=[1, 2, 3], y=[4,6,2])

show(p)

from bokeh.plotting import figure, curdoc

p = figure()
p.line(x=[1, 2, 3], y=[4,6,2])
curdoc().add_root(p)

# properties can be configured when a model object is initialized
glyph = Rect(x="x", y="y2", w=10, h=20, line_color=None)

# or by assigning values to attributes on the model later
glyph.fill_alpha = 0.5
glyph.fill_color = "navy"


####
from bokeh.plotting import figure, output_file, show

# create a Figure object
p = figure(plot_width=300, plot_height=300, tools="pan,reset,save")

# add a Circle renderer to this figure
p.circle([1, 2.5, 3, 2], [2, 3, 1, 1.5], radius=0.3, alpha=0.5)

# specify how to output the plot(s)
output_file("foo.html")

# display the figure
show(p)
