import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Web App URL: <https://geospatial-application.onrender.com>
GitHub Repository: <https://github.com/Aman-Ja1n/Geospatial-Applications.git>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

# Customize page title
st.title("Geospatial Applications")

st.markdown(
    """
    Geospatial applications involve the use of geographic information and location-based data to solve various problems and improve decision-making in a wide range of fields. These applications leverage technologies such as Geographic Information Systems (GIS), Global Positioning Systems (GPS), remote sensing, and more.
    """
)

st.header("Instructions")

markdown = """
1. For the [GitHub repository](https://github.com/Aman-Ja1n/Geospatial-Applications.git).
2. Customize the sidebar by changing the sidebar text and logo in each Python files.

"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
