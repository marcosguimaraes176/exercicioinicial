import streamlit as st
import time
import pandas as pd
import numpy as np
import openpyxl

st.set_page_config(page_title="Programa Música na Rede", layout="wide")

# --- CSS para centralização e estilização dos títulos ---
# Usamos o st.markdown com a flag unsafe_allow_html=True
st.markdown(
    """
    <style>
    /* Estilo para o título principal */
    .central-title {
        text-align: center;
        font-family: Georgia, serif;
        font-size: 36px !important; /* Tamanho 36 */
        color: #8B0000; /* Cor Vermelho Escuro (Borgonha) */
        padding-bottom: 5px; /* Espaço entre o título e o subtítulo */
    }

    /* Estilo para o subtítulo */
    .central-subtitle {
        text-align: center;
        font-family: Georgia, serif;
        font-size: 20px; /* Mantendo o tamanho 20 para o subtítulo */
        color: #4682B4; /* Cor Azul Aço */
        margin-top: 0; /* Remove margem superior padrão */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Aplicação dos títulos usando as classes CSS ---

# Título Principal (com ícone e estilo centralizado)
st.markdown(
    '<div class="central-title">🎵 Programa Música na Rede</div>',
    unsafe_allow_html=True
)

# Subtítulo
st.markdown(
    '<p class="central-subtitle">Dados por Escolas, Estudantes e Projetos</p>',
    unsafe_allow_html=True
)

st.markdown("---")

# Exemplo de conteúdo abaixo dos títulos
st.write("Bem-vindo ao painel de controle do projeto de violão.")


# Configuração da página
#st.title("Programa Música na Rede")
#st.header("Escolas, Estudantes, Projetos")
#st.markdown(
   # """
    #<h1 style='font-size:20px; color:#000080;'>
        #Dados por Escolas, Estudantes e Projetos:
    #</h1>
    #""",
    #unsafe_allow_html=True
#)




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