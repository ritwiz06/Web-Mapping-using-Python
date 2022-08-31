import folium
import pandas as pd

vol_data = pd.read_csv("volcano_db.csv", encoding='latin-1')
lat=list(vol_data["Latitude"])
lon = list(vol_data["Longitude"])
nm=list(vol_data["Volcano Name"])
elev = list(vol_data["Elev"])


html = """
Volcano name:
<a href="https://www.google.com/search?q=Volcano%%20%%22%s%%22"
target="_blank">%s</a><br>
Height: %s m
"""

def color_prod(ev):
    if ev<-2000:
        return 'yellow'
    elif -2000<=ev<1000:
        return 'orange'
    elif 1000<=ev<3500:
        return 'red'
    else:
        return 'maroon'



map = folium.Map(location = [38.5,-99], zoom_start=3, tiles="Stamen Terrain")
fgp= folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'orange' if x['properties']['POP2005'] < 10000000
else 'red' if 10000000<=x['properties']['POP2005']< 20000000 else 'purple'}))
map.add_child(fgp)
fgv= folium.FeatureGroup(name="Volcano")
for lt, ln, vnm, ev  in zip(lat, lon,nm, elev):
    #txt= "Name: "+vnm+"<br>Elevation: "+str(ev) + " m"
    #popup = folium.Popup(txt, max_width=200, min_width = 100)
    iframe = folium.IFrame(html=html % (vnm, vnm, ev), width=200, height=75)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe,max_width=300, min_width = 100), radius=6, fill=True, fill_color=color_prod(ev), color='grey', fill_opacity=0.75))


map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("index.html")
