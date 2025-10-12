import streamlit as st
import pandas as pd

st.title("fonte de dados")

st.write("1. Site do Programa Música na Rede")
st.markdown("https://musicanarede.fames.es.gov.br/")

st.write("2. Sistema de Gestão:")
st.text("SEGES - Sistema Estadual de Gestão Escolar")

# --- Configuração da Página e Título (exemplo) ---
st.set_page_config(layout="wide")
st.title("📊 Análise Descritiva da Base de Dados")
st.markdown("---") # Linha divisória

# --- Carregar o DataFrame (usando o arquivo Excel) ---
# **Importante:** Certifique-se de que o arquivo "Projetos por Municípios.xlsx"
# esteja no mesmo diretório do seu script Streamlit, ou use o caminho completo.
try:
    df = pd.read_excel("data/Projetos por Municípios.xlsx", engine='openpyxl')
except FileNotFoundError:
    st.error("Erro: O arquivo 'Projetos por Municípios.xlsx' não foi encontrado. Verifique o caminho.")
    st.stop()
except Exception as e:
    st.error(f"Erro ao carregar o arquivo Excel: {e}")
    st.stop()

# --- Gerar a Tabela Descritiva usando .describe() ---
# O .describe() gera estatísticas apenas para colunas numéricas por padrão.
# Para incluir colunas de texto (como a contagem de municípios), use include='all'.
try:
    df_descritivo = df.describe(include='all').T  # .T para transpor a tabela (linhas viram colunas e vice-versa)

    # Opcional: Tratar o index para melhor visualização (nomes das colunas)
    df_descritivo.index.name = 'Variável'
    df_descritivo = df_descritivo.reset_index()
    
except Exception as e:
    st.warning(f"Ocorreu um erro ao gerar o describe() (pode ser problema de tipos de dados misturados): {e}")
    # Uma alternativa é usar o describe() apenas para colunas numéricas se a versão 'all' falhar.
    try:
        df_descritivo = df.describe().T
        df_descritivo.index.name = 'Variável'
        df_descritivo = df_descritivo.reset_index()
    except:
        st.error("Falha ao gerar o describe() mesmo para colunas numéricas.")
        st.stop()


# --- Exibir a Tabela no Streamlit ---
st.subheader("Tabela de Estatísticas Descritivas da Base de Dados")

# Usamos st.dataframe() para uma tabela interativa e bonita
st.dataframe(
    df_descritivo,
    use_container_width=True, # Usa a largura total do container
    hide_index=True          # Esconde o índice numérico
)

st.markdown("""
<style>
/* Estilo para ajustar a altura da tabela descritiva (opcional) */
.stDataFrame {
    height: 600px; 
}
</style>
""", unsafe_allow_html=True)