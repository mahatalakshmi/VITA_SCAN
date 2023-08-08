import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image


st.set_page_config(
    page_title="Visualization",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title('Pneumoina_Visualization')

st.header('1.NORMAL CHEST X-RAY:') 
st.write('The Chest X-ray is probably one of the most commonly seen plain films, and is one of the most difficult to master.  There are many ways to evaluate the chest. A systematic approach is usually the best. One method is described here.')
img = Image.open('1.jpeg')
st.image(img)

st.header('2.Right Middle Lobe Consolidation')
img = Image.open('2.jpeg')
st.image(img)
st.header('3.Right Middle Lobe Pneumonia')
img = Image.open('3.jpeg')
st.image(img)
img = Image.open('4.jpeg')
st.header('4.Right Lower Lobe Pneumonia')
st.image(img)
img = Image.open('5.jpeg')
st.header('5.Right Lower Lobe Pneumonia, Anterior Segment')
st.image(img)
img = Image.open('6.jpeg')
st.header('6.Right Lower Lobe Pneumonia, Superior Segment')
st.image(img)


