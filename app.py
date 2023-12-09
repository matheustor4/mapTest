from flask import Flask, render_template
import folium

app = Flask(__name__)

@app.route('/')
def index():
    # Create a Folium map centered on a location of your choice
    my_map = folium.Map(location=[-5.8, -38.5], zoom_start=6)

    # Embed the map directly in the HTML template
    map_html = my_map._repr_html_()

    return render_template('index.html', map_html=map_html)

if __name__ == '__main__':
    app.run(debug=True)