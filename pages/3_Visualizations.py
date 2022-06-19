from pathlib import Path

import folium
import geopandas as gpd
import pandas as pd
import plotly_express as px
import streamlit as st
from streamlit_folium import folium_static

#import altair as alt
import datetime
#import folium
#import geopandas as gpd
import geopy
#import json
#import base64
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import osmnx as ox
#import pandas as pd
#import plotly_express as px
import plotly.io as pio
import plotly.offline as pyo
import requests
import seaborn as sns
#import streamlit as st
#import psycopg2

from folium.features import DivIcon
from googletrans import Translator
from PIL import Image
from shapely.geometry import Point, LineString
from spacy import displacy
from spacy_streamlit import visualize_ner
#from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

from branca.element import Figure
#from streamlit_folium import folium_static
from geopy.geocoders import Nominatim

#from turfpy.measurement import bbox
#from functools import reduce

PAGE_TITLE = "Visualizations"

st.sidebar.header("Solar Panel Mapping Locations")

st.subheader("Mapping Of Suitable Locations")

fig2=Figure(width=550,height=350)
#m2=folium.Map(location=[20.593684, 78.96288], zoom_start=4)
#m2=folium.Map(location=[28.7183, 77.2778], zoom_start=3)
#m2=folium.Map(location=[28.580874, 77.143854], zoom_start=3)
m2=folium.Map(location=[20.0504188, 64.4139099], zoom_start=3)
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


st.sidebar.header("Know Our Renewable Energy Statistics")

st.subheader("Generalized Statistics Of Renewable Energy Access")

