from flask import  render_template, url_for
import requests 
import folium
import json


from webservice import app
from  service import  *

API_URL = 'http://localhost:8000'
BASE_URL = 'http://localhost:5000'

@app.route('/map', methods=[ 'GET'])
def map():
    start_coords = (-18.89523134876237, 47.5418858782649)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    response = requests.get(f'{API_URL}/commune')
    data = json.loads(response.text)
    for donnee in data :
        folium.Marker([donnee[2], donnee[3]], popup= f"<a href={BASE_URL}/commune/{donnee[0]}>{donnee[1]}</a>", tooltip= f"{donnee[1]}").add_to(folium_map)
    folium_map.save('webservice/templates/map.html')
    return render_template('index.html')

@app.route('/commune/<string:id>')
def commune(id):
    response = requests.get(f'{API_URL}/commune/{id}')
    data = json.loads(response.text)
    weather = meteo(data[2])
    folium_map = folium.Map(location=(data[3], data[4]), zoom_start=14)
    folium.Marker([data[3], data[4]], popup= f"{data[1]}").add_to(folium_map)
    folium_map.save('webservice/templates/map.html')
    return render_template('commune.html', commune=data, meteo=weather)


