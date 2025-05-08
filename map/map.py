import folium
import geopandas as gpd
import pandas as pd

gdf = gpd.read_file('regions.geojson')
m = folium.Map(location=[50.4501, 30.5234], zoom_start=10)
data = pd.read_json('responses/courts_by_regions.json')
gdf = gdf.merge(data, left_on="name", right_on="name")
print(data)

folium.Choropleth(
    geo_data=gdf,
    name="choropleth",
    data=gdf,
    columns=["name", "number of courts"],
    key_on="feature.properties.name",
    fill_color="PuBu",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Кількість судів в областях"
).add_to(m)

for _, row in gdf.iterrows():
    folium.Marker(
        location=[row.geometry.centroid.y, row.geometry.centroid.x],
        popup=f"{row['name']}: {row['number of courts']} судів"
    ).add_to(m)

m.save("diagram/district_courts.html")