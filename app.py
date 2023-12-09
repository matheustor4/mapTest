from flask import Flask, render_template
import folium

app = Flask(__name__)

# Sample data for cities
cities = [
    {'name': 'City A', 'location': [-3.71, -38.54], 'data': 'Population: 1 million'},
    {'name': 'City B', 'location': [-3.72, -38.55], 'data': 'Population: 800,000'},
    # Add more cities as needed
]

@app.route('/')
def index():
    # Create a Folium map centered on a location of your choice
    my_map = folium.Map(location=[-3.7172, -38.5433], zoom_start=6)

    for city in cities:
        popup_content = f"<strong>{city['name']}</strong><br>{city['data']}"
        folium.Marker(location=city['location'], popup=popup_content).add_to(my_map)


    # Embed the map directly in the HTML template
    map_html = my_map._repr_html_()

    return render_template('index.html', map_html=map_html)

if __name__ == '__main__':
    app.run(debug=True)