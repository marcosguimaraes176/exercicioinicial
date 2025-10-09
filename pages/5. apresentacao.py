import streamlit as st
import time
import pandas as pd
import numpy as np
import openpyxl
st.title("Programa Música na Rede")
#st.header("Escolas, Estudantes, Projetos")
st.markdown(
    """
    <h1 style='font-size:20px; color:#000080;'>
        Dados por Escolas, Estudantes e Projetos:
    </h1>
    """,
    unsafe_allow_html=True
)
col1, col2=st.columns([0.50,0.50])

with st.sidebar:
    st.markdown("[Coluna1](#projetos)")
with st.container (border=1):
    with col1:
        #st.subheader("Bandas nas Escolas")
        st.markdown(
        """
        <h1 style='font-size:20px; color:#808000;'>
            Projeto Bandas nas Escolas
        </h1>
        """,
        unsafe_allow_html=True
    )
        st.image("fotos/bandas.jpeg", caption="bandas")
        with st.container(border=True,horizontal=True):
            st.text("Quantidade de Escolas Bandas:")
            st.text("Quantidade de Estudantes Bandas:")
        

with col2:
    #st.subheader("Orquestra de Violões nas Escolas")
    st.markdown(
    """
    <h1 style='font-size:20px; color:#808000;'>
        Projeto Orquestra de Violões nas Escolas
    </h1>
    """,
    unsafe_allow_html=True
)
    st.image("fotos/violões.jpeg", caption="violões")
    with st.container(border=True,horizontal=True):
     st.text("Quantidade de Escolas Violões:")
     st.text("Quantidade de Estudantes Violões:")

col3, col4=st.columns([0.50,0.50])

with col3:
    #col3.subheader("Projeto Corais nas Escolas")
    st.markdown(
    """
    <h1 style='font-size:20px; color:#808000;'>
        Projeto Corais nas Escolas
    </h1>
    """,
    unsafe_allow_html=True
)
    st.image("fotos/coral.jpeg", caption="coral")
    with st.container(border=True,horizontal=True):
     st.text("Quantidade de Escolas Corais:")
     st.text("Quantidade de Estudantes Corais:")

with col4:
       #col4.subheader("Projeto Orquestra Sinfônica Jovem")
       st.markdown(
    """
    <h1 style='font-size:20px; color:#808000;'>
        Projeto Orquestra Sinfônica Jovem
    </h1>
    """,
    unsafe_allow_html=True
)
       st.image("fotos/sinfônica.jpeg", caption="sinfônica")
       with st.container(border=True,horizontal=True):
        st.text("Quantidade de Escolas Sinfônica:")
        st.text("Quantidade de Estudantes Sinfônica:")