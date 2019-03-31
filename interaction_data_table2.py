import math

from bokeh.io import show
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval, GlyphRenderer, ColumnDataSource, MultiLine
from bokeh.palettes import Spectral8
from bokeh.plotting import figure

N = 8
node_indices = list(range(N))

plot = figure(title="Graph Layout Demonstration", x_range=(-1.1, 1.1), y_range=(-1.1, 1.1),
              plot_width=250, plot_height=250,
              tools="", toolbar_location=None)

node_ds = ColumnDataSource(data=dict(index=node_indices,
                                     color=Spectral8),
                           name="Node Renderer")
edge_ds = ColumnDataSource(data=dict(start=[0] * N,
                                     end=node_indices),
                           name="Edge Renderer")
### start of layout code
circ = [i * 2 * math.pi / 8 for i in node_indices]
x = [math.cos(i) for i in circ]
y = [math.sin(i) for i in circ]
graph_layout = dict(zip(node_indices, zip(x, y)))

graph = GraphRenderer(node_renderer=GlyphRenderer(glyph=Oval(height=0.1, width=0.2, fill_color="color"),
                                                  data_source=node_ds),
                      edge_renderer=GlyphRenderer(glyph=MultiLine(),
                                                  data_source=edge_ds),
                      layout_provider=StaticLayoutProvider(graph_layout=graph_layout))

plot.renderers.append(graph)

show(plot)