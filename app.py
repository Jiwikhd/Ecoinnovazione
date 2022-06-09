from dash import Dash, dcc, State, html, Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container
import plotly.express as px
import plotly.graph_objects as go

import pandas as pd

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

colors = {
    'background': '#b3cde0'
}


Ecoinnovazione_logo = "https://www.emiliaromagnastartup.it/sites/default/files/ecoinnovazione.jpg"
Hydro_logo = "http://www.clairfield.com/wp-content/uploads/hydro_logo_horizontal_aluminium-300x124.png"
df = pd.read_csv('https://raw.githubusercontent.com/Jiwikhd/Ecoinnovazione/main/CFTool.csv')

app.layout = html.Div([

    
dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=Ecoinnovazione_logo, height="100px")),
                        dbc.Col(html.Img(src=Hydro_logo, height="100px", style={"margin-left": "810px"})),
                    ],
                    align="center",
                    className="g-0",
                ),
                style={"textDecoration": "none", 'color': 'dark'},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            
        ]
    ),
    color="white",
    dark=False,
),

 dbc.ListGroupItem("An Interactive Dashboard for Calculating Environmental Footprint", active=True, style ={'text_align':'center'} ),
    html.Br(),
    
    
        
        
    html.Div([
        html.H4([" ", dbc.Badge("Billets", pill=True, color="primary", className="border me-1")  ], style={"margin-left": "10px"}),
        dbc.Table([
        html.Thead(html.Tr([html.Th("Billet Type"), html.Th("Percentage")])),    
        html.Tr([html.Td(['Reduxa']), dbc.Input(id='num-multi',type='number',min = 0, max = 100, value=0,step = 10  )]),
        html.Tr([html.Td(['Circal']), dbc.Input(id='num-multi2',type='number',min = 0, max = 100, value=0,step = 10  )]),
        html.Tr([html.Td(['Hydro Europe']), dbc.Input(id='num-multi3',type='number',min = 0, max = 100, value=0,step = 10  )]),
        html.Tr([html.Td(['Speedline']), dbc.Input(id='num-multi4',type='number',min = 0, max = 100, value=0,step = 10  )]),
        html.Tr([html.Td(['Average billet consumed in Europe']), dbc.Input(id='num-multi5',type='number',min = 0, max = 100, value=0,step = 10  )]),
        html.Tr([html.Td(['Average billet produced in Europe']), dbc.Input(id='num-multi6',type='number',min = 0, max = 100, value=0,step = 10  )]),
        html.Tr([html.Td(['Average billet consumed by Hydro-Nenzing']), dbc.Input(id='num-multi7',type='number',min = 0, max = 100, value=0,step = 10  )]),
            
    ], bordered=True),
        dbc.Alert(id="alertmsg"),
        html.Div([
        dcc.Graph(id='indicator-graphic')], style={'backgroundColor': colors['background']}),
        
        


html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card([
    dbc.CardHeader("Total Emissions"),
    dbc.CardBody(
        [
            html.H5(id = "result", className="card-title"),
            html.P(
                "CO2 equivalent",
                className="card-text",
            ),
        ]
    ),
], color="primary", inverse=True)),
                
            ],
            className="mb-4"),
    ])
        
        ], style={'width': '38%', 'display': 'inline-block',"margin-left": "10px"}),
    
    

    
 
#----------------------------------------------------------------------------    
    
     html.Div([
        html.H4([" ", dbc.Badge("Extrusion", pill=True, color="primary", className="border me-1") ]),
        dcc.Dropdown(
                ['Hydro-Nenzing extrusion', 'Average European extrusion', 'Generic - based on extrusion by Hydro-Nenzing', 'Mix' ],
                'Hydro-Nenzing extrusion',
                id='xaxis-column'
                    ),
        html.Div([ 
        html.Table([
        html.Tr([html.Td(["Percentage of Extrusion performed in Nenzing: (only in case of Mix)"]), dbc.Input(id='num-multi8',type='number',min = 0, max = 100, value=0,step = 10, size="sm", style={"margin-left": "35px", 'display': 'inline-block'})]),
                  ])]),
         
        html.H4([" ", dbc.Badge("Fabrication", id='fabtitle', pill=True , className="border me-1") ]),
        dcc.Dropdown(
                ['Hydro-Nenzing fabrication (87,4% Nenzing and 12,6% external)', 'Hydro-Nenzing fabrication (100% Nenzing)', 'Generic - based on fabrication by Hydro-Nenzing', 'Mix', 'No Fabrication' ],
                'Hydro-Nenzing fabrication (87,4% Nenzing and 12,6% external)',
                id='xaxisss-column'
                    ),
        html.Table([
        html.Tr([html.Td(["Percentage of Fabrication performed in Nenzing: (only in case of Mix)"]), dbc.Input(id='num-multi91',type='number',min = 0, max = 100, value=0,step = 10, size="sm", style={"margin-left": "30px"})]),
                  ]),
         
        html.H4([" ", dbc.Badge("Anodizing", id='anotitle', pill=True, className="border me-1") ]),
        dcc.Dropdown(
                ['Average anodizing for Hydro-Nenzing (85% by Collini)', 'Generic anodizing', 'Generic anodizing (Insert surface area)','No Anodizing'],
                'Average anodizing for Hydro-Nenzing (85% by Collini)',
                id='ano-column'
                    ),
        html.Table([
        html.Tr([html.Td(["Surface area to be treated for kg of profile (m2/kg):"]), dbc.Input(id='num-multi92',type='number', value=0, size="sm", style={"margin-left": "45px"})]),
                  ]),
         
        html.H4([" ", dbc.Badge("Painting", id='paintitle', pill=True, className="border me-1") ]),
        dcc.Dropdown(
                ['Yes', 'Yes (Insert primary data)', 'No Painting'],
                'Yes',
                id='paint-column'
                    ),
        html.Table([
        html.Tr([html.Td(["Surface area to be treated for kg of profile (m2/kg):"]),
                 dbc.Input(id='num-multi93',type='number', value=0, size="sm", style={"margin-left": "20px"})]),

        html.Tr([html.Td(["Thickness of the painting applied on the surface area (μm)"]), dbc.Input(id='num-multi94',type='number', value=0, size="sm", style={"margin-left": "20px"})]),
                  ]),
         
        html.Br(),
        html.Br(),
        
        html.Div([
        html.H4([" ", dbc.Badge("Distribution", id='distitle', pill=True, className="border me-1") ]),
        dcc.Dropdown(
                ['Yes', 'No Distribution'],
                'Yes',
                id='dist-column'
                    )], style={'width': '38%', 'display': 'inline-block'}),
         
         html.Div([
         html.H4([" ", dbc.Badge("EoL", id='EoLtitle', pill=True, className="border me-1") ]),
         dcc.Dropdown(
                ['Yes', 'No EoL'],
                'Yes',
                id='EoL-column'
                    )], style={'width': '38%' , 'float': 'right', 'display': 'inline-block'}),
         
         html.Br(),
         html.Br(),
         
         
          html.Div([
        
        dbc.Table([
        html.Thead(html.Tr([html.Th("Life Cycle stage"), html.Th("CF (CO2e.q.)")])),    
        html.Tr([html.Td(['Upstream']), html.Td(id='upout')]),
        html.Tr([html.Td(['Extrusion']), html.Td(id='exout')]),
        html.Tr([html.Td(['Fabrication']), html.Td(id='fabout')]),
        html.Tr([html.Td(['Anodizing']), html.Td(id='anout')]),
        html.Tr([html.Td(['Painting']), html.Td(id='painout')]),
        html.Tr([html.Td(['Downstream']), html.Td(id='downout')]),
            
    ], bordered=True)]),

            
        ], style={'width': '42%', 'float': 'right', 'display': 'inline-block',"margin-right": "10px"}),
    

], style={'backgroundColor': colors['background']})







@app.callback(
    Output(component_id='indicator-graphic', component_property='figure'),
    Output(component_id='upout', component_property='children'),
    Output(component_id='exout', component_property='children'),
    Output(component_id='fabout', component_property='children'),
    Output(component_id='anout', component_property='children'),
    Output(component_id='painout', component_property='children'),
    Output(component_id='downout', component_property='children'),
    Output(component_id='alertmsg', component_property='children'),
    Output(component_id='alertmsg', component_property='color'),
    Output(component_id='fabtitle', component_property='color'),
    Output(component_id='anotitle', component_property='color'),
    Output(component_id='paintitle', component_property='color'),
    Output(component_id='distitle', component_property='color'),
    Output(component_id='EoLtitle', component_property='color'),
    Output(component_id='result', component_property='children'),
    Input(component_id='num-multi', component_property='value'),
    Input(component_id='num-multi2', component_property='value'),
    Input(component_id='num-multi3', component_property='value'),
    Input(component_id='num-multi4', component_property='value'),
    Input(component_id='num-multi5', component_property='value'),
    Input(component_id='num-multi6', component_property='value'),
    Input(component_id='num-multi7', component_property='value'),
    Input(component_id='num-multi8', component_property='value'),
    Input(component_id='xaxis-column', component_property='value'),
    Input(component_id='xaxisss-column', component_property='value'),
    Input(component_id='ano-column', component_property='value'),
    Input(component_id='num-multi91', component_property='value'),
    Input(component_id='num-multi92', component_property='value'),
    Input(component_id='paint-column', component_property='value'),
    Input(component_id='num-multi93', component_property='value'),
    Input(component_id='num-multi94', component_property='value'),
    Input(component_id='dist-column', component_property='value'),
    Input(component_id='EoL-column', component_property='value'))
def update_output_div(input_1, input_2, input_3, input_4, input_5, input_6, input_7, input_8, input_ext, input_fab, input_ano, input_91, input_92, input_pain, input_93, input_94, input_dis, input_EoL):
    red_df = df.loc[(df['Name'] == 'Reduxa')]['CF'].values*input_1*0.01
    circ_df = df.loc[(df['Name'] == 'Circal')]['CF'].values*input_2*0.01
    hyeu_df = df.loc[(df['Name'] == 'Hydro Europe')]['CF'].values*input_3*0.01
    sp_df = df.loc[(df['Name'] == 'Speedline')]['CF'].values*input_4*0.01
    avcs_df = df.loc[(df['Name'] == 'Average billet consumed in Europe')]['CF'].values*input_5*0.01
    avpr_df = df.loc[(df['Name'] == 'Average billet produced in Europe')]['CF'].values*input_6*0.01
    avnen_df = df.loc[(df['Name'] == 'Average billet consumed by Hydro-Nenzing')]['CF'].values*input_7*0.01

    
    
    if input_ext == 'Mix':
        extr_df1 = df.loc[(df['Name'] == 'Hydro-Nenzing extrusion')]['CF'].values[0]*input_8*0.01
        extr_df2 = df.loc[(df['Name'] == 'Average European extrusion')]['CF'].values[0]*(100-input_8)*0.01
        extr_df = extr_df1 + extr_df2
    else:
        extr_df = df.loc[(df['Name'] == input_ext)]['CF'].values[0]*1
        
        
    
    if input_fab == 'Mix':
        fab_df1 = df.loc[(df['Name'] == 'Hydro-Nenzing fabrication (100% Nenzing)')]['CF'].values[0]*input_91*0.01
        fab_df2 = df.loc[(df['Name'] == 'Generic - based on fabrication by Hydro-Nenzing')]['CF'].values[0]*(100-input_91)*0.01
        fab_df = fab_df1 + fab_df2
    else:
        fab_df = df.loc[(df['Name'] == input_fab)]['CF'].values[0]*1

    if input_ano == 'Generic anodizing (Insert surface area)':
        ano_df1 = df.loc[(df['Name'] == 'Generic anodizing (excluded pack and transport)')]['CF'].values[0]*input_92*0.5
        ano_df2 = df.loc[(df['Name'] == 'Packaging and transport to/from Nenzing')]['CF'].values[0]*1
        ano_df = ano_df1 + ano_df2
    else:
        ano_df = df.loc[(df['Name'] == input_ano)]['CF'].values[0]*1
    
    if input_pain == 'Yes (Insert primary data)':
        pain_df = df.loc[(df['Name'] == 'Average painting for Hydro-Nenzing')]['CF'].values[0]/(0.000095*0.31)*input_93*(input_94/1000000)
    elif input_pain == 'Yes':
        pain_df = df.loc[(df['Name'] == 'Average painting for Hydro-Nenzing')]['CF'].values[0]*1
    else:
        pain_df = 0
        
    
    if ((input_dis == 'Yes') & (input_pain != 'No Painting') ):
        dis_df = df.loc[(df['Name'] == 'Road transport + packaging - only in case of painted profile')]['CF'].values[0]*1
    elif ((input_dis == 'Yes') & (input_pain == 'No Painting') ):
        dis_df = df.loc[(df['Name'] == 'Road transport + packaging')]['CF'].values[0]*1
    else:
        dis_df = 0
    

    if ((input_EoL == 'Yes') & (input_pain != 'No Painting') ):
        EoL_df = df.loc[(df['Name'] == 'End of life  - only in case of painted profile')]['CF'].values[0]*1
    elif ((input_EoL == 'Yes') & (input_pain == 'No Painting') ):
        EoL_df = df.loc[(df['Name'] == 'End of life ')]['CF'].values[0]*1
    else:
        EoL_df = 0
    
    

    carbon= round(red_df[0] + circ_df[0] + hyeu_df[0] + sp_df[0] + avcs_df[0] + avpr_df[0] + avnen_df[0] , 3)
    carbon_footprint_ext = round(extr_df,3)
    carbon_footprint_fab = round(fab_df, 3)
    carbon_footprint_ano = round(ano_df, 3)
    carbon_footprint_pain = round(pain_df, 3)
    carbon_footprint_dis = round(dis_df, 3)
    carbon_footprint_EoL = round(EoL_df, 3)
    carbon_footprint_Down = round(dis_df + EoL_df , 3)
    
    carbon_footprint = carbon + carbon_footprint_ext + carbon_footprint_fab + carbon_footprint_ano + carbon_footprint_pain + carbon_footprint_dis + carbon_footprint_EoL
    total = round(carbon_footprint, 3)
    
    
    if input_1 + input_2 + input_3 + input_4 + input_5 + input_6 + input_7 == 100:
        msg = "You are all set!"
        clr = "success"
    else:
        msg = "The sum should be 100%"
        clr = "danger"
        
        
    if input_fab == 'No Fabrication':
        clr2 = "secondary"
    else:
        clr2 = "primary"
        
    if input_ano == 'No Anodizing':
        clr3 = "secondary"
    else:
        clr3 = "primary"
        
    if input_pain == 'No Painting':
        clr4 = "secondary"
    else:
        clr4 = "primary"
        
    if input_dis == 'No Distribution':
        clr5 = "secondary"
    else:
        clr5 = "primary"
        
    if input_EoL == 'No EoL':
        clr6 = "secondary"
    else:
        clr6 = "primary"
        
        

    jiwi = pd.DataFrame({
    "Stage" : ["Upstream","Extrusion", "Fabrication", "Anodizing", "Painting" ,"Distribution","EoL"],
    "Environmental Footprint" : [carbon, carbon_footprint_ext, carbon_footprint_fab, carbon_footprint_ano, carbon_footprint_pain, carbon_footprint_dis,carbon_footprint_EoL]
    })
    #fig = px.bar(jiwi, x="Stage", y="Environmental Footprint", title='Environmental Footprint', color="Stage")
    fig = px.pie(jiwi, names="Stage", values="Environmental Footprint", color="Stage", hole=.3)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    #labels = ["Upstream","Extrusion", "Fabrication", "Anodizing", "Painting" ,"Distribution","EoL","Total"],
    #values = [carbon, carbon_footprint_ext, carbon_footprint_fab, carbon_footprint_ano, carbon_footprint_pain, carbon_footprint_dis,carbon_footprint_EoL, carbon_footprint ]
    fig.update_layout(
    title_text="Carbon footprint for 1kg of profile", paper_bgcolor= '#b3cde0',
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='CF', x=0.5, y=0.5, font_size=20, showarrow=False)])
    
    #fig = go.Pie(labels = labels, values = values, name = "CO2 Emissions")

    return fig, carbon, carbon_footprint_ext, carbon_footprint_fab, carbon_footprint_ano, carbon_footprint_pain, carbon_footprint_Down, msg, clr, clr2, clr3, clr4, clr5, clr6, total

if __name__ == '__main__':
    app.run_server(debug=False)
