#https://bokeh.pydata.org/en/latest/docs/user_guide/examples/interaction_data_table.html

from datetime import date
from random import randint

from bokeh.io import output_file, show
from bokeh.layouts import widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn
from bokeh.plotting import figure, output_file, show
from bokeh.models import Span

output_file("./data/data_table.html")

data = dict(
        dates=[date(2014, 3, i+1) for i in range(10)],
        downloads=[randint(0, 100) for i in range(10)],
        stocks=['xx'+str(randint(0, 100)) for i in range(10)]
    )
source = ColumnDataSource(data)

columns = [
        TableColumn(field="SOMA_ENTRA", title="SOMA_ENTRA", formatter=DateFormatter()),
        TableColumn(field="SOMA_SAI", title="SOMA_SAI"),
        TableColumn(field="STOCK", title="STOCK"),
    ]
data_table = DataTable(source=source, columns=columns, width=400, height=280)

#show(widgetbox(data_table))

p = figure(plot_width=640, plot_height=360, x_axis_type="datetime")
source = ColumnDataSource(data)

p.vbar(x='STOCK', top='STOCK', width=0.5, source=source, fill_alpha=0.4, color='paleturquoise')
#p.vbar(x='SOMA_ENTRA', top='SOMA_ENTRA', width=0.5, source=source, fill_alpha=0.8, color='seagreen')
#p.vbar(x='SOMA_SAI', top='SOMA_SAI', width=0.5, source=source, fill_alpha=0.8, color='crimson')

hline = Span(location=0, line_alpha=0.4, dimension='width', line_color='gray', line_width=3)
p.renderers.extend([hline])

show(p)
