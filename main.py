import pandas as pd 
import plotly.express as px 
import streamlit as st

#streamlit run main.py
# ler dataset
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

#alterando o nome das colunas
df = df.rename(columns={'newDeaths': 'Novos óbitos', 'newCases': 'Novos Casos', 'deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes', 'totalCases_per_100k_inhabitants': 'Casos por 100 mil habitantes'})

#selecionando o estado
#state = 'MG'
estados = list(df['state'].unique())
state = st.sidebar.selectbox('Informe o nome do estado',estados)

#selecionando dados da coluna
#column = 'Casos por 100 mil habitantes'
colunas = ['Novos óbitos','Novos Casos','Óbitos por 100 mil habitantes','Casos por 100 mil habitantes']
column = st.sidebar.selectbox('Qual é a informação desejada',colunas)

#selecionando as linhas que pertecem ao estado 
df = df[df['state'] == state]

fig = px.line(df, x = "date", y =column, title = column + ' - ' + state)
fig.update_layout(xaxis_title = 'Data', yaxis_title = column.upper(),title = {'x':0.5})

st.title('DADOS COVID - BRASIL')
st.write('Informações sobre a covid 19, aqui o usuário pode selecionar as informações desejadas de acordo com as opções disponíveis. Para isso utilize o menu na lateral esquerda')

st.plotly_chart(fig, use_container_width=True)
st.caption('Os dados foram obtidos do site : https://github.com/wcota/covid19br')