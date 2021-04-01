dash-simply
 
Create dash objects easily with reusable methods. This library simplifies the creation of dash view objects by enclosing a wrapper over the dash view objects and form groups. it does so by creating functions which return an instance of any relevant view with most of the data structure already built-in. You only need to plug in the id, data and any other required parameter by each individual object. 


Examples:

Multiple dropdowns:
dropdown_1 = dash_simply.dropdown("d1", "Name", {'car':'white', 'airplane':'blue'}, 'Yellow')
	
dropdown_2 = dash_simply.dropdown("d2", "Object", {'car':'white', 'bike':'blue'}, 'Yellow')

Instance of a Graph Object:
graph_view = dash_simply.new_graph('map')

Tabs:		
tb = dash_simply.tabs(3, "tab", "Tab_z")
#Please note that tab functionality is currently in progress. Track the progress at: https://github.com/plotly/dash-core-components/issues/265

Radio Items:		
cl = dash_simply.radio_item('ido', [{'label': 'New York City', 'value': 'NYC'},{'label': 'Montréal', 'value': 'MTL'},{'label': 'San Francisco', 'value': 'SF'}], ['NYC', 'MTL'])

Upload View:		
uploader = dash_simply.upload('up','Drag or Drop, ')

Slider View:
slider = dash_simply.slider('sl', 0.0001, 0.1, 0.001, 0.001)

Button:		
button = dash_simply.button('but','Train', '100%', '60px' ) 
