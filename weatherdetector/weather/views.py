# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import json
import urllib2

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=60cc346f02d05fbeca5f8cbe446daf9b').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity'])
        }
    else:
        city = ''
        data  = {}
    return render(request, 'index.html', {'city': city, 'data': data})