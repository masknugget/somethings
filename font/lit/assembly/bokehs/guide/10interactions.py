from bokeh.io import output_file, show
from bokeh.layouts import gridplot
from bokeh.plotting import figure

output_file("panning.html")

x = list(range(11))
y0 = x
y1 = [10-xx for xx in x]
y2 = [abs(xx-5) for xx in x]

# create a new plot
s1 = figure(plot_width=250, plot_height=250, title=None)
s1.circle(x, y0, size=10, color="navy", alpha=0.5)

# create a new plot and share both ranges
s2 = figure(plot_width=250, plot_height=250, x_range=s1.x_range, y_range=s1.y_range, title=None)
s2.triangle(x, y1, size=10, color="firebrick", alpha=0.5)

# create a new plot and share only one range
s3 = figure(plot_width=250, plot_height=250, x_range=s1.x_range, title=None)
s3.square(x, y2, size=10, color="olive", alpha=0.5)

p = gridplot([[s1, s2, s3]], toolbar_location=None)

# show the results
show(p)





#####
from bokeh.io import output_file, show
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

output_file("brushing.html")

x = list(range(-20, 21))
y0 = [abs(xx) for xx in x]
y1 = [xx**2 for xx in x]

# create a column data source for the plots to share
source = ColumnDataSource(data=dict(x=x, y0=y0, y1=y1))

TOOLS = "box_select,lasso_select,help"

# create a new plot and add a renderer
left = figure(tools=TOOLS, plot_width=300, plot_height=300, title=None)
left.circle('x', 'y0', source=source)

# create another new plot and add a renderer
right = figure(tools=TOOLS, plot_width=300, plot_height=300, title=None)
right.circle('x', 'y1', source=source)

p = gridplot([[left, right]])

show(p)


#########
from bokeh.layouts import column
from bokeh.models import Slider
from bokeh.plotting import figure, show

plot = figure(plot_width=400, plot_height=400)
r = plot.circle([1,2,3,4,5,], [3,2,5,6,4], radius=0.2, alpha=0.5)

slider = Slider(start=0.1, end=2, step=0.01, value=0.2)
slider.js_link('value', r.glyph, 'radius')

show(column(plot, slider))



######## Hiding Glyphs
import pandas as pd

from bokeh.palettes import Spectral4
from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT

p = figure(plot_width=800, plot_height=250, x_axis_type="datetime")
p.title.text = 'Click on legend entries to hide the corresponding lines'

for data, name, color in zip([AAPL, IBM, MSFT, GOOG], ["AAPL", "IBM", "MSFT", "GOOG"], Spectral4):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    p.line(df['date'], df['close'], line_width=2, color=color, alpha=0.8, legend_label=name)

p.legend.location = "top_left"
p.legend.click_policy="hide"

output_file("interactive_legend.html", title="interactive_legend.py example")

show(p)



## muting glyphs

import pandas as pd

from bokeh.palettes import Spectral4
from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT

p = figure(plot_width=800, plot_height=250, x_axis_type="datetime")
p.title.text = 'Click on legend entries to mute the corresponding lines'

for data, name, color in zip([AAPL, IBM, MSFT, GOOG], ["AAPL", "IBM", "MSFT", "GOOG"], Spectral4):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    p.line(df['date'], df['close'], line_width=2, color=color, alpha=0.8,
           muted_color=color, muted_alpha=0.2, legend_label=name)

p.legend.location = "top_left"
p.legend.click_policy="mute"

output_file("interactive_legend.html", title="interactive_legend.py example")

show(p)



##  Button
from bokeh.io import output_file, show
from bokeh.models import Button

output_file("button.html")

button = Button(label="Foo", button_type="success")

show(button)



from bokeh.io import output_file, show
from bokeh.models import CheckboxButtonGroup

output_file("checkbox_button_group.html")

checkbox_button_group = CheckboxButtonGroup(
        labels=["Option 1", "Option 2", "Option 3"], active=[0, 1])

show(checkbox_button_group)




##
from bokeh.io import output_file, show
from bokeh.models import CheckboxGroup

output_file("checkbox_group.html")

checkbox_group = CheckboxGroup(
        labels=["Option 1", "Option 2", "Option 3"], active=[0, 1])

show(checkbox_group)


## colorpicker
from bokeh.io import output_file, show
from bokeh.models import ColorPicker

output_file("color_picker.html")

color_picker = ColorPicker(color="#ff4466", title="Choose color:", width=200)

show(color_picker)




########
from datetime import date
from random import randint

from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, DataTable, DateFormatter, TableColumn

output_file("data_table.html")

data = dict(
        dates=[date(2014, 3, i+1) for i in range(10)],
        downloads=[randint(0, 100) for i in range(10)],
    )
source = ColumnDataSource(data)

columns = [
        TableColumn(field="dates", title="Date", formatter=DateFormatter()),
        TableColumn(field="downloads", title="Downloads"),
    ]
data_table = DataTable(source=source, columns=columns, width=400, height=280)

show(data_table)


###  DropdownMenu
from bokeh.io import output_file, show
from bokeh.models import Dropdown

output_file("dropdown.html")

menu = [("Item 1", "item_1"), ("Item 2", "item_2"), None, ("Item 3", "item_3")]
dropdown = Dropdown(label="Dropdown button", button_type="warning", menu=menu)

show(dropdown)


##
from bokeh.io import output_file, show
from bokeh.models import FileInput

output_file("file_input.html")

file_input = FileInput()

show(file_input)


## MultiSelect
from bokeh.io import output_file, show
from bokeh.models import MultiSelect

output_file("multi_select.html")

multi_select = MultiSelect(title="Option:", value=["foo", "quux"],
                           options=[("foo", "Foo"), ("bar", "BAR"), ("baz", "bAz"), ("quux", "quux")])

show(multi_select)

## RadioButtonGroup
from bokeh.io import output_file, show
from bokeh.models import RadioButtonGroup

output_file("radio_button_group.html")

radio_button_group = RadioButtonGroup(
        labels=["Option 1", "Option 2", "Option 3"], active=0)

show(radio_button_group)


## RadioGroup
from bokeh.io import output_file, show
from bokeh.models import RadioGroup

output_file("radio_group.html")

radio_group = RadioGroup(
        labels=["Option 1", "Option 2", "Option 3"], active=0)

show(radio_group)



### Select

from bokeh.io import output_file, show
from bokeh.models import Select

output_file("select.html")

select = Select(title="Option:", value="foo", options=["foo", "bar", "baz", "quux"])

show(select)


## Slider

from bokeh.io import output_file, show
from bokeh.models import Slider

output_file("slider.html")

slider = Slider(start=0, end=10, value=1, step=.1, title="Stuff")

show(slider)



## RangeSlider
from bokeh.io import output_file, show
from bokeh.models import RangeSlider

output_file("range_slider.html")

range_slider = RangeSlider(start=0, end=10, value=(1,9), step=.1, title="Stuff")

show(range_slider)


## tabs
from bokeh.io import output_file, show
from bokeh.models import Panel, Tabs
from bokeh.plotting import figure

output_file("slider.html")

p1 = figure(plot_width=300, plot_height=300)
p1.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)
tab1 = Panel(child=p1, title="circle")

p2 = figure(plot_width=300, plot_height=300)
p2.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=3, color="navy", alpha=0.5)
tab2 = Panel(child=p2, title="line")

tabs = Tabs(tabs=[ tab1, tab2 ])

show(tabs)




## TextAreaInput
from bokeh.io import output_file, show
from bokeh.models import TextAreaInput

output_file("text_input.html")

text_input = TextAreaInput(value="default", rows=6, title="Label:")

show(text_input)



## TextInput
from bokeh.io import output_file, show
from bokeh.models import TextInput

output_file("text_input.html")

text_input = TextInput(value="default", title="Label:")

show(text_input)


### ToggleButton
from bokeh.io import output_file, show
from bokeh.models import Toggle

output_file("toggle.html")

toggle = Toggle(label="Foo", button_type="success")

show(toggle)



## -- div ---
from bokeh.io import output_file, show
from bokeh.models import Div

output_file("div.html")

div = Div(text="""Your <a href="https://en.wikipedia.org/wiki/HTML">HTML</a>-supported text is initialized with the <b>text</b> argument.  The
remaining div arguments are <b>width</b> and <b>height</b>. For this example, those values
are <i>200</i> and <i>100</i> respectively.""",
width=200, height=100)

show(div)

# --- Paragraph ---
from bokeh.io import output_file, show
from bokeh.models import Paragraph

output_file("div.html")

p = Paragraph(text="""Your text is initialized with the 'text' argument.  The
remaining Paragraph arguments are 'width' and 'height'. For this example, those values
are 200 and 100 respectively.""",
width=200, height=100)

show(p)


## PreText
from bokeh.io import output_file, show
from bokeh.models import PreText

output_file("div.html")

pre = PreText(text="""Your text is initialized with the 'text' argument.

The remaining Paragraph arguments are 'width' and 'height'. For this example,
those values are 500 and 100 respectively.""",
width=500, height=100)

show(pre)
