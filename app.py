import dash
from dash import html, dcc
import dash_table
from scrape import get_courses
import pandas as pd
#import base64
# NOTE: We need to add pandas to the requirements.txt

# Initialize App
app = dash.Dash(__name__)

courses = get_courses()
n = courses.header.next

data_list = []
while n != courses.header: 
    data_list.append(n.element)
    n = n.next

df_courses = pd.DataFrame(data_list)

# NOTE: Put dropdown in readme
app.layout = html.Div([
    html.H1("CS Course List"),
    # dcc.Dropdown("Dropdown",
    #     id='drop',
    #     options=[
    #         {'label': 'Option 1', 'value': 'OPT1'},
    #         {'label': 'Option 2', 'value': 'OPT2'},
    #         {'label': 'Option 3', 'value': 'OPT3'}
    #     ],
    #     value='OPT1'
    # ),
    # html.Div(id='drop')
    dash_table.DataTable(
        id='CS Classes',
        columns=[{"name": i, "id": i} for i in df_courses.columns],
        data=df_courses.to_dict('records'),
        style_table={'height': '300px', 'overflowY': 'auto'},
    )
])

if __name__ == '__main__':
    app.run(debug=True)