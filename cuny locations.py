#Name: Gianni Russell
#Date: November 13, 2023
import folium
import pandas as pd

nyc_center = [40.75, -74.125]

map = folium.Map(location=nyc_center)

data = pd.read_csv('cunycampuses.csv')

folium.Marker([data['Latitude'][0], data['Longitude'][0]], popup='Hunter College').add_to(map)

map.save('nycMap.html')