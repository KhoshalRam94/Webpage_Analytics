import streamlit as st
import streamlit-analytics

with streamlit_analytics.track():
  st.write("Write your Name.")
  st.checkbox("Which is your favourite",["DS","DE","AI","ML"])
  st.button("Click me")
