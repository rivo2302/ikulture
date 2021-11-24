from flask import  render_template, url_for
from webservice import app
import folium
@app.route('/', methods=['POST', 'GET'])
def home():
    start_coords = (46.9540700, 142.7360300)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    folium_map.save('webservice/templates/map.html')
    return render_template('index.html')







