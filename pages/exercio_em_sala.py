import streamlit as st

col1, col2, col3=st.columns(3)

with col1:
    col1.header("Coluna1")

with col2:
    col2.header("Coluna2")

with col3:
    col3.header("Coluna3")    

with col1:
    col1.text("Coluna1")

with col2:
    col2.text("Coluna2")
   

with col3:
    col3.text("Coluna3") 