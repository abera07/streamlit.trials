# -*- coding: utf-8 -*-
"""GradeApp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vF5WV7z2003cJzAtzYy1lqLDQtdHNgWW
"""

!pip install streamlit

!touch app.py

#!streamlit --help

#!streamlit hello

#!streamlit run app.py#not_working

"""**For and text or title:** """

! pip install pyngrok

from pyngrok import ngrok

!ngrok authtoken 1ybNwF3mL6lryRbmuk2EzEvmzjc_52DNfFKvvyM5ijrgqYUft

!streamlit run app.py &>/dev/null&

public_url=ngrok.connect('8501')

public_url

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# from PIL import Image
# import streamlit as st
# PAGE_CONFIG = {"page_title":"GradeCalc.io","page_icon":":star:","layout":"centered"}
# st.set_page_config(**PAGE_CONFIG)
# st.markdown("<h1 style='text-align: center; color: green;'>Grade Calculation</h1>", unsafe_allow_html=True)
# st.title("Messing around in Streamlit.")
# col1, col2, col3 = st.columns([1,1,1])
# img=Image.open("kiit.png")
# 
# with col1:
#   st.write("")
# 
# with col2:
#   st.image(img,width=300)
# 
# with col3:
#   st.write("")
# 
# st.header("Dummy CGPA calculation App.")
# st.subheader("Ankita Bera, Final year, 1828229.")
# st.text("I am a student KIIT DU.")
# st.info("Calculating your CGPA:")
# cgpa = st.slider("Input Your CGPA:",0.0,10.0)
# st.markdown("## Result below:")
# if cgpa>=8.0:
#   st.success("You have a great cgpa!")
# elif cgpa>7.0 and cgpa<8.0:
#   st.warning("Nice work, you can do better.")
# else:
#   st.error("You have to work harder!")
# 
# 
#

!pgrep streamlit

!kill 608

ngrok.kill()
