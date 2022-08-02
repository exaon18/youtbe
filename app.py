from asyncore import write
from pytube import YouTube
import time
import os
import streamlit as st
os.system('clear')

link = st.text_input("Enter the video url (link)")
yt = YouTube(link)
st.write("title: "+ yt.title)
st.write("veiws : " + str(yt.views))
st.write("channel id :"+ str(yt.channel_id))
ui= st.button("")
if ui==1:

   yd =yt.streams.get_highest_resolution()
   path='C:\\Users\\Exaon\\Desktop'
   yd.download(path)
   prog = yd.on_progress()
   comp = yd.on_complete()
   print(prog)
   print(comp)
elif ui==2:
  yd=yt.streams.get_lowest_resolution()
  path1='C:\\Users\\Exaon\\Desktop'
  yd.download(path1) 
  prog1 = yd.on_progress()
  comp1 = yd.on_complete()
  print(prog1)
  print(comp1)
else:
  print("please choose the correct option","red","on_green")