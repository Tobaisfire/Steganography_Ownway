import streamlit as st
from PIL import Image
from stream_func import *
import cv2
import numpy as np
st.set_page_config(layout="wide")
st.title('Steganography')
st.caption('A program to encode Text data into Image data !!!')
st.caption(f'Working directory: D:\keval\study\Python_exp\stream_stegano')
col1, col2, col3 = st.columns(3)
val = False
vald = False
with col1:
    txt = st.text_area('Text to analyze', '')
    st.write('Text prompt :  \n', txt)

    if st.button('Encode'):
        val = True
  

    
with col2:

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        st.image(uploaded_file)


        
    if st.button('Decode'):
        vald = True


with col3:
   if val == True:
    if len(txt) < 1 :
        st.error('Please enter some text')
    elif uploaded_file is None:
        st.error('Please upload img')

    else:
        result = encode(txt,uploaded_file)
        result = convert_to_img(result[0],result[1])
        # result.save('Encoded.png')
        st.image(result)
        st.success('Encoded Completed')
        from io import BytesIO
        buf = BytesIO()
        result.save(buf, format="png")
        byte_im = buf.getvalue()

        btn = st.download_button(
            label="Download image",
            data=byte_im,
            file_name="flower.png",
            mime="image/png"
          )
      
   if vald == True:
    if uploaded_file is None:
        st.error('Please input img')
    else:
        with open('D:\keval\study\Python_exp\stream_stegano\Key.txt') as f:
            lines = f.readlines()
            tx = int(lines[0])
        resulti = decode(uploaded_file,tx)
        st.success(resulti)



