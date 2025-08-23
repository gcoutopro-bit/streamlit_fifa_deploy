# Importa as bibliotecas necessárias
import streamlit as st          # Para criar a interface web
import webbrowser               # Para abrir links externos no navegador
import pandas as pd             # Para manipulação de dados
from datetime import datetime   # Para trabalhar com datas

# Configura a página principal do Streamlit
st.set_page_config(
    page_title='FIFA',   # Título da aba do navegador
    layout='wide',       # Layout mais largo (aproveita a tela toda)
)

# Título principal da página
st.markdown("# FIFA23 OFFICIAL DATASET! ⚽")

# Texto na barra lateral
st.sidebar.markdown("Desenvolvido por Gabriel Martins Couto")

# Botão para acessar o dataset no Kaggle
btn = st.button("Acesse os dados no Kaggle!")

# Se o botão for clicado, abre o link do Kaggle em uma nova aba
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database")
    
    
# Texto descritivo sobre o dataset
st.markdown(
    """
    O conjunto de dados
    de jogadores de futebol de 2017 a 2023 fornece informações 
    abrangentes sobre jogadores de futebol profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos 
    do jogador, características físicas, estatísticas de jogo, detalhes do contrato e 
    afiliações de clubes. 
    
    Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para 
    analistas de futebol, pesquisadores e entusiastas interessados em explorar vários 
    aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de 
    desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e 
    desenvolvimento do jogador ao longo do tempo.
"""
)

# Verifica se os dados já foram carregados no session_state
if "data" not in st.session_state:
    # Lê o dataset CSV e define a primeira coluna como índice
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    
    # Filtra os jogadores cujo contrato é válido a partir do ano atual
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    
    # Remove jogadores que não possuem valor de mercado
    df_data = df_data[df_data["Value(£)"] > 0]
    
    # Ordena os jogadores pelo "Overall" de forma crescente
    df_data = df_data.sort_values(by="Overall", ascending=True)
    
    # Salva o dataframe processado no session_state para reutilização em outras páginas
    st.session_state["data"] = df_data
