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
            wdml_load = USWDML.objects.create(**wdml_data)
            message = {
                 "message": "New item(s) added to database"
            }
        return JsonResponse(message, status=201)


class Graph(TemplateView):
    template_name = 'graph.html'
    def get_context_data(self, **kwargs):
        latitude = []
        longitude = []
        mapbox_access_token = 'pk.eyJ1IjoiYXl1c2gzNyIsImEiOiJja3M0MGlmMjcyajA0MzFvN3g4cTZubGJhIn0.K9YaewuQsdcroDuCrQpyNw'
        WM_data = USWDML.objects.all()
        for x in WM_data:
            latitude.append(x.y_lat)
            longitude.append(x.x_long)
        context = super(Graph, self).get_context_data(**kwargs)
        fig = go.Figure(go.Scattermapbox(
            lat=latitude,lon=longitude,
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=9
            ),
            text=["The coffee bar","Bistro Bohem"],
        ))

        fig.update_layout(
            autosize=True,
            hovermode='closest',
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=0,
                center=dict(
                    lat= 35.088993,
                    lon= -118.352219
                ),
                pitch=0,
                zoom=10
        ),
    )
        div = opy.plot(fig, auto_open=False, output_type='div')
        context['graph'] = div
        return context
