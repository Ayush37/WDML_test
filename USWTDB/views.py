from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import USWDML
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
