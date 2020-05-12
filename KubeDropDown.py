import pandas as pd     #(version 1.0.0)
import plotly           #(version 4.5.4) pip install plotly==4.5.4
import plotly.express as px

import dash             #(version 1.9.1) pip install dash==1.9.1
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import ListingPods

ListingPods.list_all_pods()

app = dash.Dash(__name__)

#---------------------------------------------------------------
#Taken from https://opendata.cityofnewyork.us/
df = pd.read_csv("ListingPods.csv")

#---------------------------------------------------------------
app.layout = html.Div([

    html.Div([
        dcc.Graph(id='our_graph')
    ],className='nine columns'),

    html.Div([

        html.Br(),
        html.Div(id='output_data'),
        html.Br(),

        html.Label(['Choose column:'],style={'font-weight': 'bold', "text-align": "center"}),

        dcc.Dropdown(id='kube_dropdown',
            options=[
                     {'label': 'NAMESPACE', 'value': 'NAMESPACE'},
                     {'label': 'POD IP', 'value': 'POD_IP'},
                     {'label': 'HOST IP', 'value': 'HOST_IP'},
                     {'label': 'NODE NAME', 'value': 'NODE_NAME'},
                     {'label': 'POD NAME', 'value': 'POD_NAME'}
            ],
            optionHeight=35,                    #height/space between dropdown options
            value='NAMESPACE',                    #dropdown value selected automatically when page loads
            disabled=False,                     #disable dropdown value selection
            multi=False,                        #allow multiple dropdown values to be selected
            searchable=True,                    #allow user-searching of dropdown values
            search_value='',                    #remembers the value searched in dropdown
            placeholder='Please select...',     #gray, default text shown when no option is selected
            clearable=True,                     #allow user to removes the selected value
            style={'width':"100%"},             #use dictionary to define CSS styles of your dropdown
            # className='select_box',           #activate separate CSS document in assets folder
            # persistence=True,                 #remembers dropdown value. Used with persistence_type
            # persistence_type='memory'         #remembers dropdown value selected until...
            ),                                  #'memory': browser tab is refreshed
                                                #'session': browser tab is closed
                                                #'local': browser cookies are deleted
    ],className='three columns'),

])

#---------------------------------------------------------------
# Connecting the Dropdown values to the graph
@app.callback(
    Output(component_id='our_graph', component_property='figure'),
    [Input(component_id='kube_dropdown', component_property='value')]
)

def build_graph(column_chosen):
    dff=df
    fig = px.pie(dff,names=column_chosen)
    fig.update_traces(textinfo='percent+label')
    fig.update_layout(title={'text':'Kubernetes Resources',
                      'font':{'size':28},'x':0.5,'xanchor':'center'})
    return fig

#---------------------------------------------------------------
# For tutorial purposes to show the user the search_value

@app.callback(
    Output(component_id='output_data', component_property='children'),
    [Input(component_id='kube_dropdown', component_property='search_value')]
)

def build_graph(data_chosen):
    return ('Search value was: " {} "'.format(data_chosen))
#---------------------------------------------------------------

if __name__ == '__main__':
    app.run_server(host='0.0.0.0',port=8050,debug=True)
