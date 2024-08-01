import streamlit as st
import streamlit_analytics

with streamlit_analytics.track():
  st.text_input("Write your Name.")
  st.selectbox("Which is your favourite",["DS","DE","AI","ML"])
  st.button("Click me")
