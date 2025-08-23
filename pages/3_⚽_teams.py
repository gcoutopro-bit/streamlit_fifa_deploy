import streamlit as st

df_data = st.session_state["data"]

clubes = df_data["Club"].unique()
clube = st.sidebar.selectbox(
    "Clube",
    clubes
)

clube_stats = df_data[(df_data['Club'] == clube)].set_index("Name")
st.title(clube_stats['Club'].iloc[0])

columns = ["Age", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)", 
           "Joined", "Height(cm.)", "Weight(lbs.)", "Contract Valid Until", "Release Clause(£)"
        ]

st.dataframe(clube_stats[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     'Overall',format="%d" ,min_value=0, max_value=100
                 ),
                 "Value(£)": st.column_config.NumberColumn(
                     'Value', format="euro", width="small"
                 ),
                 "Wage(£)": st.column_config.NumberColumn(
                     'Wage', format="euro", width="small"
                 ),
                 "Release Clause(£)": st.column_config.NumberColumn(
                     "Release Clause", format="euro"
                 ),
                 "Photo": st.column_config.ImageColumn(
                     'Photo'
                 ),
                 "Flag": st.column_config.ImageColumn(
                     "Flag"
                 )
             })