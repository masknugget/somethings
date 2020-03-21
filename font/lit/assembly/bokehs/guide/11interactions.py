from bokeh.layouts import column
from bokeh.models import ColumnDataSource, CustomJS, Slider
from bokeh.plotting import Figure, output_file, show

output_file("js_on_change.html")

x = [x*0.005 for x in range(0, 200)]
y = x

source = ColumnDataSource(data=dict(x=x, y=y))

plot = Figure(plot_width=400, plot_height=400)
plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

callback = CustomJS(args=dict(source=source), code="""
    var data = source.data;
    var f = cb_obj.value
    var x = data['x']
    var y = data['y']
    for (var i = 0; i < x.length; i++) {
        y[i] = Math.pow(x[i], f)
    }
    source.change.emit();
""")

slider = Slider(start=0.1, end=4, value=1, step=.1, title="power")
slider.js_on_change('value', callback)

layout = column(slider, plot)

show(layout)


##
from bokeh.models.callbacks import CustomJS

callback = CustomJS(code="""
// the event that triggered the callback is cb_obj:
// The event type determines the relevant attributes
console.log('Tap event occurred at x-position: ' + cb_obj.x)
""")

p = figure()
# execute a callback whenever the plot canvas is tapped
p.js_on_event('tap', callback)



#####
""" Demonstration of how to register event callbacks using an adaptation
of the color_scatter example from the bokeh gallery
"""
import numpy as np

from bokeh import events
from bokeh.io import output_file, show
from bokeh.layouts import column, row
from bokeh.models import Button, CustomJS, Div
from bokeh.plotting import figure


def display_event(div, attributes=[], style = 'float:left;clear:left;font_size=10pt'):
    "Build a suitable CustomJS to display the current event in the div model."
    return CustomJS(args=dict(div=div), code="""
        var attrs = %s; var args = [];
        for (var i = 0; i<attrs.length; i++) {
            args.push(attrs[i] + '=' + Number(cb_obj[attrs[i]]).toFixed(2));
        }
        var line = "<span style=%r><b>" + cb_obj.event_name + "</b>(" + args.join(", ") + ")</span>\\n";
        var text = div.text.concat(line);
        var lines = text.split("\\n")
        if (lines.length > 35)
            lines.shift();
        div.text = lines.join("\\n");
    """ % (attributes, style))

x = np.random.random(size=4000) * 100
y = np.random.random(size=4000) * 100
radii = np.random.random(size=4000) * 1.5
colors = ["#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50+2*x, 30+2*y)]

p = figure(tools="pan,wheel_zoom,zoom_in,zoom_out,reset")
p.scatter(x, y, radius=np.random.random(size=4000) * 1.5,
          fill_color=colors, fill_alpha=0.6, line_color=None)

div = Div(width=400, height=p.plot_height, height_policy="fixed")
button = Button(label="Button", button_type="success")
layout = column(button, row(p, div))

## Events with no attributes
button.js_on_event(events.ButtonClick, display_event(div)) # Button click
p.js_on_event(events.LODStart, display_event(div))         # Start of LOD display
p.js_on_event(events.LODEnd, display_event(div))           # End of LOD display

## Events with attributes
point_attributes = ['x', 'y', 'sx', 'sy']                  # Point events
wheel_attributes = point_attributes + ['delta']            # Mouse wheel event
pan_attributes = point_attributes + ['delta_x', 'delta_y'] # Pan event
pinch_attributes = point_attributes + ['scale']            # Pinch event

point_events = [
    events.Tap, events.DoubleTap, events.Press, events.PressUp,
    events.MouseMove, events.MouseEnter, events.MouseLeave,
    events.PanStart, events.PanEnd, events.PinchStart, events.PinchEnd,
]

for event in point_events:
    p.js_on_event(event, display_event(div, attributes=point_attributes))

p.js_on_event(events.MouseWheel, display_event(div, attributes=wheel_attributes))
p.js_on_event(events.Pan,        display_event(div, attributes=pan_attributes))
p.js_on_event(events.Pinch,      display_event(div, attributes=pinch_attributes))

output_file("js_events.html", title="JS Events Example")
show(layout)

## CustomJS for Widgets
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, CustomJS, Slider
from bokeh.plotting import figure, output_file, show

output_file("callback.html")

x = [x*0.005 for x in range(0, 200)]
y = x

source = ColumnDataSource(data=dict(x=x, y=y))

plot = figure(plot_width=400, plot_height=400)
plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

callback = CustomJS(args=dict(source=source), code="""
        var data = source.data;
        var f = cb_obj.value
        var x = data['x']
        var y = data['y']
        for (var i = 0; i < x.length; i++) {
            y[i] = Math.pow(x[i], f)
        }
        source.change.emit();
    """)

slider = Slider(start=0.1, end=4, value=1, step=.1, title="power")
slider.js_on_change('value', callback)

layout = column(slider, plot)

show(layout)

######
from random import random

from bokeh.layouts import row
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.plotting import figure, output_file, show

output_file("callback.html")

x = [random() for x in range(500)]
y = [random() for y in range(500)]

s1 = ColumnDataSource(data=dict(x=x, y=y))
p1 = figure(plot_width=400, plot_height=400, tools="lasso_select", title="Select Here")
p1.circle('x', 'y', source=s1, alpha=0.6)

s2 = ColumnDataSource(data=dict(x=[], y=[]))
p2 = figure(plot_width=400, plot_height=400, x_range=(0, 1), y_range=(0, 1),
            tools="", title="Watch Here")
p2.circle('x', 'y', source=s2, alpha=0.6)

s1.selected.js_on_change('indices', CustomJS(args=dict(s1=s1, s2=s2), code="""
        var inds = cb_obj.indices;
        var d1 = s1.data;
        var d2 = s2.data;
        d2['x'] = []
        d2['y'] = []
        for (var i = 0; i < inds.length; i++) {
            d2['x'].push(d1['x'][inds[i]])
            d2['y'].push(d1['y'][inds[i]])
        }
        s2.change.emit();
    """)
)

layout = row(p1, p2)

show(layout)



############
from random import random

from bokeh.models import ColumnDataSource, CustomJS
from bokeh.plotting import figure, output_file, show

output_file("callback.html")

x = [random() for x in range(500)]
y = [random() for y in range(500)]
color = ["navy"] * len(x)

s = ColumnDataSource(data=dict(x=x, y=y, color=color))
p = figure(plot_width=400, plot_height=400, tools="lasso_select", title="Select Here")
p.circle('x', 'y', color='color', size=8, source=s, alpha=0.4)

s2 = ColumnDataSource(data=dict(x=[0, 1], ym=[0.5, 0.5]))
p.line(x='x', y='ym', color="orange", line_width=5, alpha=0.6, source=s2)

s.selected.js_on_change('indices', CustomJS(args=dict(s=s, s2=s2), code="""
    const inds = s.selected.indices;
    const d = s.data;
    var ym = 0

    if (inds.length == 0)
        return;

    for (var i = 0; i < d['color'].length; i++) {
        d['color'][i] = "navy"
    }
    for (var i = 0; i < inds.length; i++) {
        d['color'][inds[i]] = "firebrick"
        ym += d['y'][inds[i]]
    }

    ym /= inds.length
    s2.data['ym'] = [ym, ym]

    s.change.emit();
    s2.change.emit();
"""))

show(p)



#####
import numpy as np

from bokeh.layouts import row
from bokeh.models import ColumnDataSource, CustomJS, Rect
from bokeh.plotting import figure, output_file, show

output_file('range_update_callback.html')

N = 4000

x = np.random.random(size=N) * 100
y = np.random.random(size=N) * 100
radii = np.random.random(size=N) * 1.5
colors = [
    "#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50+2*x, 30+2*y)
]

source = ColumnDataSource({'x': [], 'y': [], 'width': [], 'height': []})

jscode = """
    const data = source.data
    const start = cb_obj.start
    const end = cb_obj.end
    data[%r] = [start + (end - start) / 2]
    data[%r] = [end - start]
    source.change.emit()
"""

p1 = figure(title='Pan and Zoom Here', x_range=(0, 100), y_range=(0, 100),
            tools='box_zoom,wheel_zoom,pan,reset', plot_width=400, plot_height=400)
p1.scatter(x, y, radius=radii, fill_color=colors, fill_alpha=0.6, line_color=None)

xcb = CustomJS(args=dict(source=source), code=jscode % ('x', 'width'))
ycb = CustomJS(args=dict(source=source), code=jscode % ('y', 'height'))

p1.x_range.js_on_change('start', xcb)
p1.x_range.js_on_change('end', xcb)
p1.y_range.js_on_change('start', ycb)
p1.y_range.js_on_change('end', ycb)

p2 = figure(title='See Zoom Window Here', x_range=(0, 100), y_range=(0, 100),
            tools='', plot_width=400, plot_height=400)
p2.scatter(x, y, radius=radii, fill_color=colors, fill_alpha=0.6, line_color=None)

rect = Rect(x='x', y='y', width='width', height='height', fill_alpha=0.1,
            line_color='black', fill_color='black')
p2.add_glyph(source, rect)

layout = row(p1, p2)

show(layout)

## CustomJS for Tools
from bokeh.events import SelectionGeometry
from bokeh.models import ColumnDataSource, CustomJS, Rect
from bokeh.plotting import figure, output_file, show

output_file("box_select_tool_callback.html")

source = ColumnDataSource(data=dict(x=[], y=[], width=[], height=[]))

callback = CustomJS(args=dict(source=source), code="""
    const geometry = cb_obj['geometry']
    const data = source.data

    // calculate Rect attributes
    const width = geometry['x1'] - geometry['x0']
    const height = geometry['y1'] - geometry['y0']
    const x = geometry['x0'] + width/2
    const y = geometry['y0'] + height/2

    // update data source with new Rect attributes
    data['x'].push(x)
    data['y'].push(y)
    data['width'].push(width);
    data['height'].push(height)

    // emit update of data source
    source.change.emit()
""")

p = figure(plot_width=400, plot_height=400, tools="box_select",
           title="Select Below", x_range=(0, 1), y_range=(0, 1))

rect = Rect(x='x', y='y', width='width', height='height',
            fill_alpha=0.3, fill_color='#009933')

p.add_glyph(source, rect, selection_glyph=rect, nonselection_glyph=rect)

p.js_on_event(SelectionGeometry, callback)

show(p)



## hover
from bokeh.models import ColumnDataSource, CustomJS, HoverTool
from bokeh.plotting import figure, output_file, show

output_file("hover_callback.html")

# define some points and a little graph between them
x = [2, 3, 5, 6, 8, 7]
y = [6, 4, 3, 8, 7, 5]
links = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1, 4],
    4: [1, 3],
    5: [2, 3, 4]
}

p = figure(plot_width=400, plot_height=400, tools="", toolbar_location=None, title='Hover over points')

source = ColumnDataSource({'x0': [], 'y0': [], 'x1': [], 'y1': []})
sr = p.segment(x0='x0', y0='y0', x1='x1', y1='y1', color='olive', alpha=0.6, line_width=3, source=source, )
cr = p.circle(x, y, color='olive', size=30, alpha=0.4, hover_color='olive', hover_alpha=1.0)

# Add a hover tool, that sets the link data for a hovered circle
code = """
const links = %s
const data = {'x0': [], 'y0': [], 'x1': [], 'y1': []}
const indices = cb_data.index.indices
for (var i = 0; i < indices.length; i++) {
    const start = indices[i]
    for (var j = 0; j < links[start].length; j++) {
        const end = links[start][j]
        data['x0'].push(circle.data.x[start])
        data['y0'].push(circle.data.y[start])
        data['x1'].push(circle.data.x[end])
        data['y1'].push(circle.data.y[end])
    }
}
segment.data = data
""" % links

callback = CustomJS(args={'circle': cr.data_source, 'segment': sr.data_source}, code=code)
p.add_tools(HoverTool(tooltips=None, callback=callback, renderers=[cr]))

show(p)



## openurl
from bokeh.models import ColumnDataSource, OpenURL, TapTool
from bokeh.plotting import figure, output_file, show

output_file("openurl.html")

p = figure(plot_width=400, plot_height=400,
           tools="tap", title="Click the Dots")

source = ColumnDataSource(data=dict(
    x=[1, 2, 3, 4, 5],
    y=[2, 5, 8, 2, 7],
    color=["navy", "orange", "olive", "firebrick", "gold"]
    ))

p.circle('x', 'y', color='color', size=20, source=source)

# use the "color" column of the CDS to complete the URL
# e.g. if the glyph at index 10 is selected, then @color
# will be replaced with source.data['color'][10]
url = "http://www.colors.commutercreative.com/@color/"
taptool = p.select(type=TapTool)
taptool.callback = OpenURL(url=url)

show(p)

