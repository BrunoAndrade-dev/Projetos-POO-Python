import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px

def extracao_info (df) :  
    col1, col2 = st.columns(2)
    with col1 : 
        st.metric (label = "Total de Clientes" , value= df.shape[0])
    with col2 : 
        st.metric (label = "Total de colunas", value= df.shape[1])

    st.divider()

    st.subheader("📚​ Resumo Estatístico dos Saldos")
    metricas = df.describe()

    c1,c2,c3 = st.columns(3)
    c1.metric ("Saldo  Médio", f"R$ {metricas.loc['mean', 'saldo']:.2f}")
    c2.metric ("Saldo  Mínimo", f"R$ {metricas.loc['min', 'saldo']:.2f}")
    c3.metric ("Saldo  Máximo", f"R$ {metricas.loc['max', 'saldo']:.2f}")

def concentracao (df) : 
    df_ordenado_saldo = df.sort_values(by = 'saldo', ascending=False)
    aum_tot = df['saldo'].sum()

    top_10_percent = int(len(df_ordenado_saldo )* (0.1))
    saldo_top_10 = df_ordenado_saldo.iloc[:top_10_percent]['saldo'].sum()
    saldo_restante = aum_tot - saldo_top_10
     
    porcentagem = (saldo_top_10 / aum_tot ) * 100
    st.subheader (" 💰 Existe Concentração de capital no banco ?")
    
    # Construção da figura 
    dados_grafico = {
        "Grupo" : ["Top 10 % Clientes" , "Restante (90%)"], "Valor" : [saldo_top_10, saldo_restante]
    }
    fig = px.pie (
        dados_grafico, values = 'Valor', names = 'Grupo', hole = 0.5, color_discrete_sequence = ['#00CC96', '#636EFA']
    )

    fig.update_traces(textposition = 'inside', textinfo ='percent+label')

    st.plotly_chart (fig, use_container_width=True) 
    st.info (f"Os 10 % melhores clientes detêm ** {porcentagem:.2f} ** do capital total ")


def Aum (df) : 
    tot = df['saldo'].sum()
    return st.metric (label = " O Assetes Under Management (AUM)", value =f"{tot:.2f}", help= "Soma total de todos os saldos de clientes no banco")

def divisao_saldo(df) : 
    bins = [0  , 1200 , 5000, 14000, float('inf')]
    labels = ['Silver ' ,  'Platine ' , 'Gold' , 'Diamante ']
    intervalos = ['Até R$ 1.200 ', 'R$ 1.200 a R$ 5.000', 'R$ 5.000 a R$ 14.000', 'Acima de R$ 14.000']

    df_legenda = pd.DataFrame({
        'Categoria' : labels,
        'Critério de Saldo' : intervalos
    })
    st.dataframe = df_legenda

    df['Faixa_saldo'] = pd.cut(df['saldo'] , bins = bins , labels= labels)

    distribuicao = df['Faixa_saldo'].value_counts().reindex(labels)

    return distribuicao, st.dataframe


def plot_3_bar (distribuicao) : 
    fig, ax = plt.subplots(figsize=(10,6))
    sns.barplot(x=distribuicao.index, y=distribuicao.values, palette='viridis', ax=ax)
    plt.title("Distribuição por faixa de saldo")
    
    st.pyplot(fig) 

def plot_3_dif(dist) : 
    df_plot = dist.reset_index()
    df_plot.columns = ['Classificação de faixa', 'Quantidade de clientes']

    fig, ax = plt.subplots(figsize=(10,6))
    sns.set_theme(style='darkgrid')
    sns.pointplot(data=df_plot, x='Classificação de faixa', y='Quantidade de clientes', ax=ax) 

    st.pyplot(fig)

