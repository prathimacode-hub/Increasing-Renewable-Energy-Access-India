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

#https://media.istockphoto.com/photos/engineer-standing-in-solar-power-station-looking-sunrise-picture-id1318137351?s=612x612

st.header("Renewable Energy Access in India")

#IMG_URL = 'https://media.istockphoto.com/photos/engineer-standing-in-solar-power' \
#          '-station-looking-sunrise-picture-id1318137351?s=612x612/'

#https://news.stanford.edu/2015/11/23/plan-energy-storage-112315/
    
#IMG_URL = 'https://etimg.etb2bimg.com/thumb/msid-79151507,width-700,resizemode-4/.jpg'

IMG_URL = 'https://bsmedia.business-standard.com/_media/bs/img/article/2021-12/28/full/1640711472-4731.jpg?im=Resize,width=480'

#IMG_URL = 'https://news.stanford.edu/news/2015/november/images/15891-plan_news.jpg/'

response = requests.get(IMG_URL)
img = Image.open(BytesIO(response.content))

col1, col2 = st.columns(2)
with col1:
    st.subheader('Increasing Our Renewable Energy Access Throughout India using AI')
    st.markdown("""
    India has vast land reserves and is geographically favourable for solar power projects, but there is still scope to improve the electricity 
    production that relies on coal.
    
    This initiative is taken to use satellite data in conjunction with other relevant datasets to identify sites that are most suitable for 
    solar panel installations as a greener energy source through machine learning and coverage analysis.
    
    The aim is to help connect and encourage organisations to use AI tools to understand and plan in transition for green energy. We also 
    hope to encourage citizen science by open sourcing the dataset and code.
    """)
with col2:
    st.image(img.resize((500, 600)))
    
