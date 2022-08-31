import folium
import pandas as pd

vol_data = pd.read_csv("volcano_db.csv", encoding='latin-1')
lat=list(vol_data["Latitude"])
lon = list(vol_data["Longitude"])
nm=list(vol_data["Volcano Name"])
elev = list(vol_data["Elev"])


html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=Volcano%%20%%22%s%%22"
target="_blank">%s</a><br>
Height: %s m
"""

def color_prod(ev):
    if ev<-3000:
        return 'beige'
    elif -3000<=ev<0:
        return 'orange'
    elif 0<=ev<2000:
        return 'lightred'
    elif 2000<=ev<4000:
        return 'red'
    else:
        return 'darkred'



map = folium.Map(location = [38.5,-99], zoom_start=3, tiles="Stamen Terrain")
fg= folium.FeatureGroup(name="My Map")

for lt, ln, vnm, ev  in zip(lat, lon,nm, elev):
    #txt= "Name: "+vnm+"<br>Elevation: "+str(ev) + " m"
    #popup = folium.Popup(txt, max_width=200, min_width = 100)
    iframe = folium.IFrame(html=html % (vnm, vnm, ev), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=color_prod(ev))))
map.add_child(fg)
map.save("Map1.html")
