import streamlit as st
import time
st.title("Layouts")
st.header("Testando Layouts")

col1, col2, col3=st.columns([0.50,0.25,0.25])

with st.sidebar:
    st.markdown("[Coluna1](#coluna1)")
with col1:
    st.header("Coluna 1")
    with st.container(border=True,horizontal=True):
        st.text("container-content1")
        st.text("container-comtemnt2")
    

with col2:
       col2.header("Coluna 2")
       st.image("/workspaces/exercicioinicial/fotos/foto 1.jpeg", caption="Foto 1")
  

with col3:
    col3.header("Coluna 3")
    st.image("/workspaces/exercicioinicial/fotos/foto 2.jpeg", caption="Foto 1")