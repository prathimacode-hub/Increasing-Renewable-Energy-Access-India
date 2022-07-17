from pathlib import Path

import folium
import geopandas as gpd
import pandas as pd
import plotly_express as px
import streamlit as st
from streamlit_folium import folium_static

#import altair as alt
import datetime
import geopy
import json
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import osmnx as ox
import plotly.io as pio
import plotly.offline as pyo
import requests
import seaborn as sns

# from folium.features import DivIcon
# from googletrans import Translator
# from PIL import Image
# from shapely.geometry import Point, LineString
# from spacy import displacy
# from spacy_streamlit import visualize_ner
# from folium.plugins import MarkerCluster

# import streamlit.components.v1 as components
# import os
# from pylocator.positionstackfuns import latlonpositionstack

#from turfpy.measurement import bbox
#from functools import reduce

PAGE_TITLE = "Visualizations"

st.sidebar.header("Visualizations")

st.subheader("Mapping Of Global Horizontal Irradiance Locations")
fig2=Figure(width=550,height=350)

m2=folium.Map(location=[20.0504188,64.4139099], zoom_start=3)
fig2.add_child(m2)
folium.TileLayer('Stamen Terrain').add_to(m2)
folium.TileLayer('Stamen Toner').add_to(m2)
folium.TileLayer('Stamen Water Color').add_to(m2)
folium.TileLayer('cartodbpositron').add_to(m2)
folium.TileLayer('cartodbdark_matter').add_to(m2)
folium.LayerControl().add_to(m2)

df = pd.read_csv('Solar_GHI.csv') #global horizontal irradiance

df['latitude'] = pd.to_numeric(df.latitude, errors='coerce')
df['longitude'] = pd.to_numeric(df.longitude, errors='coerce')# drop rows with missing lat and lon

df.dropna(subset=['latitude', 'longitude'], inplace=True)# convert from string to int

from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl

map_1 = KeplerGl(height=800)
map_1.add_data(data=df, name="global-horizontal-irradiance-map-of-india")
keplergl_static(map_1)




st.subheader("Mapping Of Direct Normal Irradiance Locations")

fig2=Figure(width=550,height=350)

m2=folium.Map(location=[20.0504188, 64.4139099], zoom_start=3)
fig2.add_child(m2)
folium.TileLayer('Stamen Terrain').add_to(m2)
folium.TileLayer('Stamen Toner').add_to(m2)
folium.TileLayer('Stamen Water Color').add_to(m2)
folium.TileLayer('cartodbpositron').add_to(m2)
folium.TileLayer('cartodbdark_matter').add_to(m2)
folium.LayerControl().add_to(m2)

df = pd.read_csv('Solar_DNI.csv') #direct normal irradiance

df['latitude'] = pd.to_numeric(df.latitude, errors='coerce')
df['longitude'] = pd.to_numeric(df.longitude, errors='coerce')# drop rows with missing lat and lon

df.dropna(subset=['latitude', 'longitude'], inplace=True)# convert from string to int

from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl

map_1 = KeplerGl(height=800)
map_1.add_data(data=df, name="direct-normal-irradiance-map-of-india")
keplergl_static(map_1)




st.subheader("Monthly Temperatures")

fig2=Figure(width=550,height=350)

m2=folium.Map(location=[20.0504188, 64.4139099], zoom_start=3)
fig2.add_child(m2)
folium.TileLayer('Stamen Terrain').add_to(m2)
folium.TileLayer('Stamen Toner').add_to(m2)
folium.TileLayer('Stamen Water Color').add_to(m2)
folium.TileLayer('cartodbpositron').add_to(m2)
folium.TileLayer('cartodbdark_matter').add_to(m2)
folium.LayerControl().add_to(m2)

df = pd.read_csv('solar.csv') #direct normal irradiance

df['latitude'] = pd.to_numeric(df.latitude, errors='coerce')
df['longitude'] = pd.to_numeric(df.longitude, errors='coerce')# drop rows with missing lat and lon

df.dropna(subset=['latitude', 'longitude'], inplace=True)# convert from string to int

from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl

map_1 = KeplerGl(height=800)
map_1.add_data(data=df, name="monthly-temperatures-of-india")
keplergl_static(map_1)




# if "latitude" not in st.session_state.keys():
#     st.session_state["latitude"] = 20.0504188
# if "longitude" not in st.session_state.keys():
#     st.session_state["longitude"] = 64.4139099
# if "cityname" not in st.session_state.keys():
#     st.session_state["cityname"] = "New Delhi"

# st.title("Weather Map using Streamlit")

# st.markdown("""
#     Welcome to this weather map. To use this application, simply select the input 
#     type, which can be either the **city name** or the **latitude and longitude** 
#     of the place that you want, then click the **Search** button. The map 
#     will then change and show the weather of the place.
# """)

# st.markdown("---")

# selectope = st.selectbox("Select input type", ["City name", "Latitude and Longitude"])

# with st.form(key="location_input"):
#     if selectope == "City name":
#         locat = st.text_input("Type the city name below", value="New Delhi")
#     elif selectope == "Latitude and Longitude":
#         latinput = st.number_input("Latitude",value=20.0504188)
#         loninput = st.number_input("Longitude", value=64.4139099)
#     subbutton = st.form_submit_button("Search")

# if subbutton:
#     if selectope == "City name":

#         # Get the latitude and longitude
#         latdata, londata = latlonpositionstack(
#             os.environ.get("apipositionstack"),
#             locat)
#         st.session_state["latitude"] = latdata
#         st.session_state["longitude"] = londata

#     elif selectope == "Latitude and Longitude":
#         # Get the latitude and longitude
#         st.session_state["latitude"] = latinput
#         st.session_state["longitude"] = loninput

# latc = st.session_state["latitude"]
# lonc = st.session_state["longitude"]

# components.iframe(src=f"https://embed.windy.com/embed2.html?lat={latc}&lon={lonc}&detailLat={latc}&detailLon={lonc}&width=650&height=450&zoom=5&level=surface&overlay=wind&product=ecmwf&menu=&message=&marker=&calendar=now&pressure=&type=map&location=coordinates&detail=&metricWind=default&metricTemp=default&radarRange=-1",
#     height=500)



# fileNames = [ "n27_e076_1arc_v3.tif", "n27_e077_1arc_v3.tif" ]

# doc = aw.Document()
# builder = aw.DocumentBuilder(doc)

# shapes = [builder.insert_image(fileName) for fileName in fileNames]

# # Calculate the maximum width and height and update page settings 
# # to crop the document to fit the size of the pictures.
# pageSetup = builder.page_setup
# pageSetup.page_width = max(shape.width for shape in shapes)
# pageSetup.page_height = sum(shape.height for shape in shapes)
# pageSetup.top_margin = 0;
# pageSetup.left_margin = 0;
# pageSetup.bottom_margin = 0;
# pageSetup.right_margin = 0;

# doc.save("Output.jpg");




st.subheader("Energy Map Of India")

fig2=Figure(width=550,height=350)
#m2=folium.Map(location=[20.593684, 78.96288], zoom_start=4)
#m2=folium.Map(location=[28.7183, 77.2778], zoom_start=3)
#m2=folium.Map(location=[28.580874, 77.143854], zoom_start=3)
m2=folium.Map(location=[20.5937, 78.9629], zoom_start=3)
#m2=folium.Map(location=[20.0504188, 64.4139099], zoom_start=3)
fig2.add_child(m2)
folium.TileLayer('Stamen Terrain').add_to(m2)
folium.TileLayer('Stamen Toner').add_to(m2)
folium.TileLayer('Stamen Water Color').add_to(m2)
folium.TileLayer('cartodbpositron').add_to(m2)
folium.TileLayer('cartodbdark_matter').add_to(m2)
folium.LayerControl().add_to(m2)

df = pd.read_csv('energy_map_of_india.csv')

df['latitude'] = pd.to_numeric(df.latitude, errors='coerce')
df['longitude'] = pd.to_numeric(df.longitude, errors='coerce')# drop rows with missing lat and lon

midpoint = (np.average(df['latitude']), np.average(df['longitude']))

df.dropna(subset=['latitude', 'longitude'], inplace=True)# convert from string to int

# fig.update_geos(
#     # fitbounds="locations",
#     center_lon=64.4139099,
#     center_lat=20.0504188,
#     visible=False,
# )

# fig.update_geos(showcountries=False, showcoastlines=False,
#                 showland=False, fitbounds="locations",
#                 subunitcolor='white')
# fig.show()

from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl

map_1 = KeplerGl(height=800)
map_1.add_data(data=df, name="energy-map-of-india")
keplergl_static(map_1)



st.subheader("Solar Station Locations in India")

fig2=Figure(width=550,height=350)

m2=folium.Map(location=[20.0504188, 64.4139099], zoom_start=3)
fig2.add_child(m2)
folium.TileLayer('Stamen Terrain').add_to(m2)
folium.TileLayer('Stamen Toner').add_to(m2)
folium.TileLayer('Stamen Water Color').add_to(m2)
folium.TileLayer('cartodbpositron').add_to(m2)
folium.TileLayer('cartodbdark_matter').add_to(m2)
folium.LayerControl().add_to(m2)

df = pd.read_csv('solar_stations.csv') #solar stations

df['start_latitude'] = pd.to_numeric(df.start_latitude, errors='coerce')
df['start_longitude'] = pd.to_numeric(df.start_longitude, errors='coerce')

df['end_latitude'] = pd.to_numeric(df.end_latitude, errors='coerce')
df['end_longitude'] = pd.to_numeric(df.end_longitude, errors='coerce')# drop rows with missing lat and lon

df.dropna(subset=['start_latitude', 'start_longitude', 'end_latitude', 'end_longitude'], inplace=True)# convert from string to int

from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl

map_1 = KeplerGl(height=800)
map_1.add_data(data=df, name="solar-stations-in-world")
keplergl_static(map_1)

st.subheader("Know Our Renewable Energy Statistics")

INDIA_PROVINCES_URL = 'https://raw.githubusercontent.com/Subhash9325/GeoJson-Data-of-Indian-States/master/Indian_States.geojson'

SOLAR_GHI_PATH = Path('Solar_GHI.csv')

SOLAR_DNI_PATH = Path('Solar_DNI.csv')

fig2=Figure(width=550,height=350)

m = folium.Map(width=500,height=500,location=[20.0504188, 64.4139099], zoom_start=5)

fig2.add_child(m2)
folium.TileLayer('Stamen Terrain').add_to(m2)
folium.TileLayer('Stamen Toner').add_to(m2)
folium.TileLayer('Stamen Water Color').add_to(m2)
folium.TileLayer('cartodbpositron').add_to(m2)
folium.TileLayer('cartodbdark_matter').add_to(m2)
folium.LayerControl().add_to(m2)

#return folium_static(m)


