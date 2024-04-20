import streamlit as st
import pandas as pd


st.subheader('UpLoading CSV Files : ')
df = st.file_uploader('Upload your CSV file', type = ['csv' , 'xlsx'])

st.subheader('Loading CSV Files : ')
df = pd.read_csv(r"C:\Users\Satyam\Desktop\Data_Science\Data Analytics\Streamlit\Products.csv")
if df is not None:
    st.table(df.head(10))

st.subheader('Dealing with Images Directly : ')
st.image(r"C:\Users\Satyam\Desktop\Data_Science\Data Analytics\Streamlit\img.png")

st.subheader('Dealing with Images via Uploading : ')

img_file = st.file_uploader('Upload your image', type = ['jpg' , 'png'])

if img_file is not None:
    st.image(img_file)


st.subheader('Dealing with Videos :')

video_file = st.file_uploader('Upload your video', type = ['mp4' , 'mkv'])
if video_file is not None:
    st.video(video_file)

st.subheader('Dealing with Audio :')

audio_file = st.file_uploader('Upload your audio', type = ['mp3' , 'wav'])
if audio_file is not None:
    st.audio(audio_file)