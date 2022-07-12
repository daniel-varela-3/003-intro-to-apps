######### import libraries 

import dash
from dash import html
from dash import dcc
import plotly.graph_objs as go

########### Define your variables
weeks=[1,2,3,4,5,6]
confusion_values=[99, 90, 80, 60, 50, 40]
knowledge_values=[0, 5, 15, 5, 25, 45]
color1='red'
color2='green'
mytitle='Daniels Data Science Journey'

label1='Confusion'
label2='Coding knowledge'

########### Set up the chart



# create the data trace
def make_that_cool_linechart(weeks, confusion_values, knowledge_values, color1, color2, mytitle):
    confusion =go.Scatter(x=weeks,
                      y=confusion_values,
                      mode = 'lines',
                      marker={'color':color1},
                      name = 'confusion')
    knowledge =go.Scatter(x=weeks,
                      y=knowledge_values,
                      mode = 'lines',
                      marker={'color':color2},
                      name = 'knowledge')

    # combine into a figure
    coding_fig = go.Figure([confusion, knowledge])
    coding_fig
    return coding_fig


######### Run the function #######

if __name__ == '__main__':
    fig = make_that_cool_linechart(weeks, confusion_values, knowledge_values, color1, color2, mytitle)
    fig.write_html('docs/barchart_v2.html')
    print('We successfully updated the barchart!')
