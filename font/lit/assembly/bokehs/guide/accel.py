import numpy as np

from bokeh.plotting import figure, show, output_file

N = 10000

x = np.random.normal(0, np.pi, N)
y = np.sin(x) + np.random.normal(0, 0.2, N)

output_file("scatter10k.html", title="scatter 10k points (no WebGL)")

p = figure(output_backend="canvas")
p.scatter(x, y, alpha=0.1)
show(p)

import numpy as np

from bokeh.plotting import figure, show, output_file

N = 10000

x = np.random.normal(0, np.pi, N)
y = np.sin(x) + np.random.normal(0, 0.2, N)

output_file("scatter10k.html", title="scatter 10k points (with WebGL)")

p = figure(output_backend="webgl")
p.scatter(x, y, alpha=0.1)
show(p)



import numpy as np

from bokeh.plotting import figure, show, output_file

N = 10000

x = np.linspace(0, 10*np.pi, N)
y = np.cos(x) + np.sin(2*x+1.25) + np.random.normal(0, 0.001, (N, ))

output_file("line10k.html", title="line10k.py example")

p = figure(title="A line consisting of 10k points", output_backend="webgl")
p.line(x, y, color="#22aa22", line_width=3)
show(p)

