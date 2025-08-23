import streamlit as st

df_data = st.session_state["data"]


clubes = df_data["Club"].unique()
club = st.sidebar.selectbox(
    "Club",
    options=clubes
)

df_players = df_data[df_data['Club'] == club]

players = df_players["Name"].unique()
player = st.sidebar.selectbox(
    "Jogador",
    options=players
)

player_stats = df_data[df_data['Name'] == player].iloc[0]
st.image(player_stats["Photo"])
st.title(player_stats["Name"])

st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

idade, altura, peso, col4 = st.columns(4) 
idade.markdown(f"**Idade:** {player_stats['Age']}")
altura.markdown(f"**Altura:** {player_stats['Height(cm.)']}")
peso.markdown(f"**Peso:** {player_stats['Weight(lbs.)']}")

st.divider()

st.subheader(f'Overall {player_stats["Overall"]}')

st.progress(int(player_stats['Overall']))

col1, col2, col3 = st.columns(3)
col1.metric(label='Valor de Mercado', value=f'£ {player_stats["Value(£)"]}')
col2.metric(label='Remuneração Semanal', value=f'£ {player_stats["Wage(£)"]}')
col3.metric(label='Cláusula de Rescisão', value=f'£ {player_stats["Release Clause(£)"]}')