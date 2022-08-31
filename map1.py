import folium
import pandas as pd

vol_data = pd.read_csv("volcano_db.csv", encoding='latin-1')
lat=list(vol_data["Latitude"])
lon = list(vol_data["Longitude"])
nm=list(vol_data["Volcano Name"])
elev = list(vol_data["Elev"])
map = folium.Map(location = [38.5,-99], zoom_start=6, tiles="Stamen Terrain")
fg= folium.FeatureGroup(name="My Map")

for lt, ln, vnm, ev  in zip(lat, lon,nm, elev):
    txt= "Name: "+vnm+"<br>Elevation: "+str(ev) + " m"
    popup = folium.Popup(txt, max_width=200, min_width = 100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=popup, icon=folium.Icon(color="red")))
map.add_child(fg)
map.save("Map1.html")
