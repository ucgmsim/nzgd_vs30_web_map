from flask import Flask, render_template, request
import geopandas as gpd
from pathlib import Path
import pandas as pd
import rasterio
from rasterio.plot import reshape_as_image

import folium
from folium.plugins import MarkerCluster

app = Flask(__name__)

@app.route('/map', methods=['POST'])
def map():
    query = request.form.get('query')

    load_dir = Path("/home/arr65/data/nzgd/resources")
    info_df = gpd.read_file(load_dir / "vs30_from_data.geojson")
    info_df = info_df.iloc[0:1000]

    if query:
        info_df = info_df[info_df["record_name"] == query]

    fmap = folium.Map(location=[-41.2728,173.2994], tiles="OpenStreetMap", zoom_start=6)

    # Create a MarkerCluster object
    marker_cluster = MarkerCluster().add_to(fmap)

    for row_index, row in info_df.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            name=row["record_name"]
        ).add_to(marker_cluster)

    folium_map_render: str = fmap.get_root()._repr_html_()
    # The following replace removes the erroneous request to trust the notebook.
    return folium_map_render.replace(
        '<span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span>',
        "",
    )

@app.route('/')
def index():  # put application's code here
    return render_template('index.html', title='VS30 Map')

if __name__ == '__main__':
    app.run()