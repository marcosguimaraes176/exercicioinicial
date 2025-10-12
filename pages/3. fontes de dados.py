import streamlit as st
import pandas as pd
import io
import openpyxl

st.markdown("""
<style>
/* Zera o espaçamento abaixo dos subcabeçalhos (st.subheader) */
h3 {
    margin-bottom: 0px; 
    padding-top: 5px; 
}

/* Zera o espaçamento abaixo de st.dataframe (a tabela) */
.stDataFrame {
    margin-bottom: 0px; 
}

/* Zera o espaçamento abaixo de st.text (usado para o df.info) */
.stText {
    margin-bottom: 0px;
}

/* Ajusta a linha divisória (st.markdown("---")) */
hr {
    margin-top: 10px; 
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)


st.title("fonte de dados")

st.write("1. Site do Programa Música na Rede")
st.markdown("https://musicanarede.fames.es.gov.br/")

st.write("2. Sistema de Gestão:")
st.text("SEGES - Sistema Estadual de Gestão Escolar")

# --- Configuração da Página e Título (exemplo) ---
st.set_page_config(layout="wide")
st.title("📊 Análise Descritiva de Múltiplas Bases de Dados")
st.markdown("---")

# Nomes dos arquivos
FILE_PROJETOS = "data/Projetos por Municípios.xlsx"
FILE_MUSICA = "data/Relatório Música na Rede1.xlsx" # ATENÇÃO: Confirme este nome!

df_projetos = None
df_musica = None

# Carregamento da Primeira Tabela
try:
    st.info(f"Carregando {FILE_PROJETOS}...")
    df_projetos = pd.read_excel(FILE_PROJETOS)
except FileNotFoundError:
    st.error(f"🚨 Erro: O arquivo '{FILE_PROJETOS}' não foi encontrado.")
except Exception as e:
    st.error(f"🚨 Erro ao carregar {FILE_PROJETOS}: {e}")

# Carregamento da Segunda Tabela
try:
    st.info(f"Carregando {FILE_MUSICA}...")
    df_musica = pd.read_excel(FILE_MUSICA)
except FileNotFoundError:
    st.error(f"🚨 Erro: O arquivo '{FILE_MUSICA}' não foi encontrado.")
except Exception as e:
    st.error(f"🚨 Erro ao carregar {FILE_MUSICA}: {e}")


# --- 3. FUNÇÃO AUXILIAR PARA EXIBIR DADOS ---

def exibir_tabelas(df, titulo_principal):
    """
    Exibe as três visualizações (describe, head, info) para um dado DataFrame.
    """
    # Apenas exibe se o DataFrame foi carregado com sucesso
    if df is None:
        return
        
    st.header(f"Base: {titulo_principal}")

    # 1. Tabela Descritiva (describe)
    st.subheader("1. Estatísticas Descritivas (describe)")
    
    # Prepara o describe para exibir colunas numéricas e categóricas
    try:
        df_descritivo = df.describe(include='all').T 
    except Exception as e:
        st.warning(f"⚠️ Aviso: Não foi possível gerar o describe completo para **{titulo_principal}**. Exibindo apenas o numérico. Erro: {e}")
        df_descritivo = df.describe().T
        
    df_descritivo.index.name = 'Variável'
    
    st.dataframe(
        df_descritivo.reset_index(),
        use_container_width=True, 
        hide_index=True 
    )

    st.markdown("---") 

    # 2. Visualização do Head (Organização da Tabela Original)
    st.subheader("2. Visualização dos Dados Originais (Primeiras Linhas)")
    st.dataframe(df.head(), use_container_width=True)

    st.markdown("---") 

    # 3. Informações da Estrutura (info)
    st.subheader("3. Tipos de Dados e Contagem de Não-Nulos (info)")

    # Captura e exibe o df.info()
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)
    
    st.markdown("---") # Separador final entre as grandes seções


# --- 4. EXIBIÇÃO SEQUENCIAL DAS BASES ---

# Exibe a primeira base de dados
exibir_tabelas(df_projetos, "**Projetos por Municípios**")

# Adiciona um separador grande para diferenciar visualmente as duas bases
st.markdown("# 🔔 Início da Segunda Base de Dados")
st.markdown("---") 

# Exibe a segunda base de dados
exibir_tabelas(df_musica, "**Relatório Música na Rede** (Estudantes Atendidos)")

def exibir_analise_musica(df):
    """
    Combina o cálculo, o gráfico e a exibição das tabelas descritivas 
    da base Música na Rede em uma única chamada.
    """
    if df is None:
        return

    # A. CÁLCULO E GRÁFICO (Como definimos antes)
    st.header("Base: **Relatório Música na Rede** (Estudantes Atendidos)")
    
    # Colunas de interesse (ANOS)
    colunas_anos = ['2023', '2024', '2025']
    
    # --- CÁLCULO DO TOTAL GERAL ---
    try:
        total_geral = df[colunas_anos].sum().sum()
        st.subheader("📈 Análise de Atendimentos")
        st.metric(
            label="Total Geral de Estudantes Atendidos (2023-2025)", 
            value=f"{total_geral:,.0f}".replace(",", "_").replace(".", ",").replace("_", ".") # Formatação Brasileira
        )
        st.markdown("---")

    except KeyError:
        st.warning(f"⚠️ Aviso: Não foi possível calcular o Total Geral. Verifique se as colunas {colunas_anos} existem.")
    except Exception as e:
         st.warning(f"⚠️ Ocorreu um erro inesperado no cálculo: {e}")


    # --- GERAÇÃO DO GRÁFICO DE EVOLUÇÃO ---
    st.subheader("Evolução Anual de Atendimentos por Projeto")

    try:
        coluna_projeto = 'Projeto' if 'Projeto' in df.columns else df.columns[0]
        df_plot = df[[coluna_projeto] + colunas_anos].set_index(coluna_projeto).T 
        st.line_chart(df_plot)
        st.caption(f"Cada linha representa a evolução de um item da coluna: '{coluna_projeto}' ao longo dos anos.")
        st.markdown("---")

    except Exception as e:
        st.warning(f"⚠️ Não foi possível gerar o gráfico de linhas. Verifique as colunas.")

    
    # B. EXIBIÇÃO DAS TABELAS DESCRITIVAS (Agora dentro desta função, eliminando a chamada externa)

    # 1. Tabela Descritiva (describe)
    st.subheader("1. Estatísticas Descritivas (describe)")
    
    # ... [O restante do código de exibição do describe, head e info, que já estava em exibir_tabelas, viria aqui]
    
    # Para ser conciso, usaremos a função 'exibir_tabelas' para o restante das visualizações
    # NOTE: Isso pressupõe que você só quer o gráfico/cálculo ANTES das 3 tabelas
    # Se você quiser o gráfico/cálculo no MEIO das 3 tabelas, o código seria diferente.

    # 1. Tabela Descritiva (describe)
    st.subheader("1. Estatísticas Descritivas (describe)")
    # ... [Código do Describe]
    
    # 2. Visualização do Head (Organização da Tabela Original)
    st.subheader("2. Visualização dos Dados Originais (Primeiras Linhas)")
    # ... [Código do Head]
    
    # 3. Informações da Estrutura (info)
    st.subheader("3. Tipos de Dados e Contagem de Não-Nulos (info)")
    # ... [Código do Info]


# --- 4. EXIBIÇÃO SEQUENCIAL DAS BASES (FINAL) ---
# ... (Este é o bloco que fica no fim do seu script, chamando as funções)
# exibir_tabelas(df_projetos, "**Projetos por Municípios**")
# st.markdown("#") 
# st.markdown("---") 
# exibir_analise_musica(df_musica) # Chamada única!