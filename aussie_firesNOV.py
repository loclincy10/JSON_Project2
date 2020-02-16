import csv 
import plotly as py
import plotly.graph_objs as go
#from datetime import datetime 

open_file = open("MODIS_C6_Australia_NewZealand_MCD14DL_NRT_2019331.txt", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

for index,column_header in enumerate(header_row):
    print(index, column_header)

brights,lons,lats,hover_texts = [],[],[],[]

""" for row in csv_file:
    try:
        bright = int(row[header_row.index("brightness")]) 
        lon = int(row[header_row.index("longitude")])
        lat = int(row[header_row.index("latitude")])
    except ValueError:
        print("Missing data")

    else:
        brights.append(bright)
        lons.append(lon)
        lats.append(lat)
        hover_texts.append(hover_texts) """


for row in csv_file:
    bright =  float(row[header_row.index("brightness")]) 
    lon = float(row[header_row.index("longitude")])
    lat = float(row[header_row.index("latitude")])
    brights.append(bright)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(hover_texts)

print(brights[:10])





from plotly.graph_objs import Scattergeo,Layout
from plotly import offline as go

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker':{
        'size':[.04*bright for bright in brights],
        'color': brights,
        'colorscale': 'Viridis',
        'reversescale':True,
        'colorbar':{'title': 'Brightness'}
              
    },
}]


my_layout = Layout(title="Australian Fires- November 2019")

fig = {'data': data, 'layout':my_layout}

go.plot(fig,filename='aussie_firesNOV.html')
