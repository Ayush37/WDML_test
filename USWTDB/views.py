from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from .models import USWDML
import plotly.offline as opy
import plotly.graph_objs as go
from django.views.generic import TemplateView
# Create your views here.
class WindMill(View):
    def wind_view(self):
        f = open('data.json',)
        data = json.load(f)
        for i in data['features']:
            case_id = int(i['properties']['case_id'])
            p_year = int(i['properties']['p_year'])
            p_tnum = int(i['properties']['p_tnum'])
            t_state = i['properties']['t_state'] 
            p_name = i['properties']['p_name']
            p_cap = i['properties']['p_cap']
            t_manu = i['properties']['t_manu']
            t_model = i['properties']['t_model']
            t_cap = i['properties']['t_cap']
            t_hh = i['properties']['t_hh']
            x_long = i['properties']['xlong']
            y_lat = i['properties']['ylat']
            
            wdml_data = {
                 'case_id' : case_id,
                 't_state' : t_state,
                 'p_name' : p_name,
                 'p_year' : p_year,
                 'p_tnum' : p_tnum,
                 'p_cap' : p_cap,
                 't_manu' : t_manu,
                 't_model' : t_model,
                 't_cap' : t_cap,
                 't_hh' : t_hh,
                 'x_long' : x_long,
                 'y_lat' : y_lat,
                 }         
            print ('****************')
            print (wdml_data)
            wdml_load = USWDML.objects.create(**wdml_data)

            message = {
                 "message": "New item(s) added to database"
            }
        return JsonResponse(message, status=201)


class Graph(TemplateView):
    template_name = 'graph.html'

    def get_context_data(self, **kwargs):
        mapbox_access_token = 'pk.eyJ1IjoiYXl1c2gzNyIsImEiOiJja3M0MGlmMjcyajA0MzFvN3g4cTZubGJhIn0.K9YaewuQsdcroDuCrQpyNw'
        
        context = super(Graph, self).get_context_data(**kwargs)

        fig = go.Figure(go.Scattermapbox(
            lat=['38.91427','38.91538','38.91458',
                 '38.92239','38.93222','38.90842',
                 '38.91931','38.93260','38.91368',
                 '38.88516','38.921894','38.93206',
                 '38.91275'],
            lon=['-77.02827','-77.02013','-77.03155',
                 '-77.04227','-77.02854','-77.02419',
                 '-77.02518','-77.03304','-77.04509',
                 '-76.99656','-77.042438','-77.02821',
                 '-77.01239'],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=9
            ),
            text=["The coffee bar","Bistro Bohem","Black Cat",
                 "Snap","Columbia Heights Coffee","Azi's Cafe",
                 "Blind Dog Cafe","Le Caprice","Filter",
                 "Peregrine","Tryst","The Coupe",
                 "Big Bear Cafe"],
        ))

        fig.update_layout(
            autosize=True,
            hovermode='closest',
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=0,
                center=dict(
                    lat=38.92,
                    lon=-77.07
                ),
                pitch=0,
                zoom=10
        ),
    )
        div = opy.plot(fig, auto_open=False, output_type='div')
        context['graph'] = div
        return context
