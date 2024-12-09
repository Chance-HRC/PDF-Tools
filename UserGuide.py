# --------------------------------------------------------------------------------
# Imports
import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
import io

# --------------------------------------------------------------------------------
#sidebar 
st.sidebar.title("IF THERE ARE ANY BUGS PLEASE CONTACT")
st.sidebar.markdown("@ChanceDehar@hotmail.com")
st.sidebar.image("airport.png")
# --------------------------------------------------------------------------------
#website explanation 
st.title("PDF Tool Helper")
st.divider()
st.write("This website it for ease of access in order to help navigate and alter PDF documents")
st.divider()
st.write("It offers a multitude of tools (located on the left page navigator)")
st.divider()
st.write("It is brower-based meaning all information entered isnt sent anywhere leading to being fully confidential")
st.divider()

# --------------------------------------------------------------------------------