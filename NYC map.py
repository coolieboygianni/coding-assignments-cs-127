import folium
import pandas as pd

cuny = pd.read_csv('City_University_of_New_York__CUNY__University_Campus_Locations_20231113')

map = folium.Map(location=[40.75, -74.125])

map.save(outfile='nycMap.html')