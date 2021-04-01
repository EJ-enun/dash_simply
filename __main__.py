import os
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

#Generic View Objects
class ViewObject():
	def __init__(self):
		self.title = None
	
	#Reusable Graph.
	def new_graph(id_):
		return dbc.Col(children=[dbc.Card(dbc.Col(children=[dcc.Graph(id=id_),html.Br()])),])

	def graph(id_, figure_, layout_, margin_, width_, height_):
		return dbc.Col(children=[dbc.Card(dbc.Col(children=[dcc.Graph(id=id_, figure=figure_,layout=layout_, margin=margin_, style={'width':width_, 'height':height_}),html.Br()])),])
	#Reusable Uploader object.
	def upload(id_, text_, width_='100%', height_='60px'):
		return dbc.Col(children=[dcc.Upload([
			text_,
			html.A('Select a File')
			], id=id_, style={
			'width': width_,
			'height': height_,
			'lineHeight': '60px',
			'borderWidth': '1px',
			'borderStyle': 'dashed',
			'borderRadius': '5px',
			'textAlign': 'center'
			})
		])

	def dropdown(id_, text_, dict_, value_, multi_= False):
		return dbc.FormGroup([
			html.H4(text_),
			dcc.Dropdown(id=id_, value=value_, multi = multi_, options=[{'label':x,'value':x} for x in dict_])
		])
	def progress_bar(id_, id_int_, n_interval, interval):
		return html.Div([dcc.Interval(id=id_int_, n_intervals = n_interval, interval = interval), dbc.Progress(id=id_)])

	def radio_item(id_, dict_, value_, label_style_dict_= {'display': 'inline-block'}):
		return dcc.RadioItems(id=id_, options=dict_, value=value_,labelStyle=label_style_dict_)
	
	def checklist(id_, dict_, value_, label_style_dict_= {'display': 'inline-block'}):
		return dcc.Checklist(id=id_, options=dict_, value=value_, labelStyle=label_style_dict_ )
	#labelStyle=label_style_dict_
	def slider(id_, min_, max_, step_, value_):
		return html.Div([dcc.Slider(id=id_, min=min_, max=max_, step=step_, value=value_)])

	def marks_slider(id_, min_, max_, marks_, value_):
		return html.Div([dcc.Slider(id=id_, min=min_, max=max_, marks={i:i for i in range(marks_)}, value=value_)])

	def range_slider(id_, count_,  min_, max_, step_, value_):
		return html.Div([dcc.RangeSlider(id=id_, count = count_, min=min_, max=max_, step=step_, value=value_)])

	def range_marks_slider(id_, count_,  min_, max_, marks_, value_):
		return html.Div([dcc.RangeSlider(id=id_, count = count_, min=min_, max=max_, marks={i:i for i in range(marks_)}, value=value_)])

	def text_input(id_, type_, placeholder_, value_):
		return html.Div([dcc.Input(id= id_, type = type_, placeholder = placeholder_, value=value_)])

	def audio(src_, controls_=True):
		return html.Div([html.Audio(src=src_, controls=controls_ )])
	
	def textarea(id_,  placeholder_, value_, width_, height_):
		return html.Div([dcc.Textarea(id=id_, value=value_, style={'width':width_, 'height':height_}, placeholder=placeholder_)])

	def button(id_, btn_name, width_, height_, n_clicks_= 0):
		return html.Button(btn_name, id=id_, n_clicks=n_clicks_, style={'width':width_, 'height':height_})

	def date_picker_single(id_, date_):
		return html.Div([dcc.DatePickerSingle(id=id_, date = date_)])

	def date_picker_range(id_, start_date_, end_placeholder_text_):
		return html.Div([dcc.DatePickerRange(id=id_, start_date = date_, end_date_placeholder_text=end_placeholder_text_)])
	
	def markdown():
		return html.Div([dcc.Markdown()])

	def tabs(no_of_tabs_, id_, value_):
		tabs = [dcc.Tab(label="Tab {}".format(x)) for x in range(0, no_of_tabs_)]
		return dcc.Tabs(id=id_, value=value_, children=[tabs])

	def loading(id_, child_id_, value_, type_="default"):
		return html.Div([dcc.Loading(id=id_, type=type_, value=value_, children=html.Div(id=child_id_))])

	def confirm_dialog_provider(id_, btn_name_, message_):
		return html.Div([dcc.ConfirmDialogProvider(id=id_, message=message_, children=[html.Button(btn_name_)])])

	def confirm_dialog(id_, message_):
		return html.Div([dcc.ConfirmDialog(id=id_, message=message_)])

	def store(id_, storage_type_):
		return html.Div([dcc.Store(id=id_, storage_type=storage_type_)

if __name__ == "__main__":
    ViewObject()