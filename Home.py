import osmnx as ox
import plotly.offline as pyo
import streamlit as st
from io import BytesIO
import requests

from PIL import Image


ox.config(use_cache=True, log_console=True)
pyo.init_notebook_mode(connected=True)
st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(
    page_title="Renewable Energy Access in India - NewDelhi Chapter",
    layout="wide",
    initial_sidebar_state="expanded",
)
https://media.istockphoto.com/photos/engineer-standing-in-solar-power-station-looking-sunrise-picture-id1318137351?s=612x612
st.header("Renewable Energy Access in India")

IMG_URL = 'https://media.istockphoto.com/photos/engineer-standing-in-solar-power' \
          '-station-looking-sunrise-picture-id1318137351?s=612x612/'

response = requests.get(IMG_URL)
img = Image.open(BytesIO(response.content))

col1, col2 = st.columns(2)
with col1:
    st.subheader('Increasing Our Renewable Energy Access Throughout India using AI')
    st.markdown("""
    efnfnkdnfkdnfkdnfk.
    """)
with col2:
    st.image(img.resize((500, 600)))
    
