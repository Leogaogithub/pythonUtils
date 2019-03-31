#https://stackoverflow.com/questions/52351801/bokeh-add-a-grid-of-information-below-a-plot#52351801
#https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Bokeh_Cheat_Sheet.pdf
from bokeh.plotting import figure, output_file, show
from bokeh.io import output_file, show
from bokeh.layouts import widgetbox
from bokeh.models import ColumnDataSource, LabelSet
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn
from bokeh.plotting import figure, output_file, show
from bokeh.models import Span
from datetime import date
from random import randint
from bokeh.layouts import layout

data = dict(
        dates=[date(2014, 3, i+1) for i in range(10)],
        downloads=[i for i in range(10)],
        stocks=['xx'+str(randint(0, 100)) for i in range(10)],
        uploads=[i-10 for i in range(10)],
    )
source = ColumnDataSource(data)
plot = figure(plot_width=300, plot_height=300)
plot.vbar(x='dates', width=0.5, bottom=0, top='downloads', source=source, fill_alpha=0.4, color="#CAB2D6")
plot.vbar(x='dates', width=0.5, bottom=0, top='uploads', source=source, fill_alpha=0.8, color='seagreen')

hline = Span(location=0, line_alpha=0.4, dimension='width', line_color='gray', line_width=3)
labels = LabelSet(x='dates', y='uploads', text='stocks', level='glyph',
      source=source, render_mode='canvas')

plot.add_layout(labels)
plot.renderers.extend([hline])
#show(plot)
productInfo = dict(
    unit_cost=[30],
unit_cost2=[30],
unit_cost3=[30],
unit_cost4=[30],
unit_cost5=[30],

    lead_time=[date(2014, 3, 10)]
)
source2 = ColumnDataSource(productInfo)
columns = [

        TableColumn(field="unit_cost", title="78888888888888888888888"),
    TableColumn(field="unit_cost2", title="unit_cost2"),
    TableColumn(field="unit_cost3", title="unit_cost2"),
    TableColumn(field="unit_cost4", title="unit_cost2"),
    TableColumn(field="unit_cost5", title="4"),
TableColumn(field="lead_time", title="Date", formatter=DateFormatter()),
    ]
data_table = DataTable(source=source2, columns=columns,fit_columns=True, height=280, sortable=False, selectable=False)

columns2 = [

        TableColumn(field="unit_cost", title="78888888888888888888888"),
    TableColumn(field="unit_cost2", title="unit_cost2"),
    TableColumn(field="unit_cost3", title="unit_cost2"),
    TableColumn(field="unit_cost4", title="unit_cost2"),
    TableColumn(field="unit_cost5", title="4"),
TableColumn(field="lead_time", title="Date", formatter=DateFormatter()),
    ]
data_table2 = DataTable(source=source2, columns=columns2,fit_columns=True, height=280, sortable=False, selectable=False)

l = layout([
  [plot],
  [widgetbox(data_table)],
[widgetbox(data_table2)],
], sizing_mode='stretch_both')

show(l)
