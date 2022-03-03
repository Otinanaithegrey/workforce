import streamlit as st
from PIL import Image



imagebus = Image.open('busca.png')
imagebus = imagebus.resize((180, 180))
imagepapa = Image.open('papa.jpg')
imagepapa = imagepapa.resize((180, 180))
imgerrani = Image.open('erani.jpg')
imgerrani = imgerrani.resize((180, 180))
imgfried = Image.open('fried.jpg')
imgfried = imgfried.resize((180, 180))
sasimage = Image.open('sas.jpg')
sasimage = sasimage.resize((180, 180))
imgkenin = Image.open('kenin.jpg')
imgkenin = imgkenin.resize((180, 180))
imgapo = Image.open('apo.jpg')
imgapo = imgapo.resize((180, 180))

if st.button("hello"):
  st.write('hello')
  
workdf = f'# WTA Factory\n ## Owner'
st.markdown(workdf)
st.image(imagepapa,"Sergio 'papa giorgi' Giorgi")
st.markdown('## CEO')
st.image(imgkenin, 'Alex Kenin')
st.markdown('## Communications Manager')
st.image(imgapo, "Apostolos 'Tsitsidad' Tsitsipas")
st.markdown('\n## Workforce\n### Supervisor')
st.image(sasimage, 'Sasnovich Aliaksandra')
st.markdown('### Workers')
sasimage2 = st.image([imgerrani, imgfried, imagebus], ['Errani Sara','Friedsam Anna-Lena', 'Bucsa Cristina'])

