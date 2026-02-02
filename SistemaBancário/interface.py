import streamlit as st

from cliente import * 
from conta import *
from banco import*
from main import banco
import base64
import os

directorio_atual = os.path.dirname (os.path.abspath (__file__ ))
caminho = os.path.join (directorio_atual, "fundo.jpg")


def criar_card_animado(titulo, corpo, delay=0):
    # CSS com efeito de vidro para maior contraste
    style = f"""
    <style>
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .card-animado-{delay} {{
            animation: fadeIn 1.5s ease-out forwards;
            animation-delay: {delay}s;
            opacity: 0;
            background: #1E1EE1E /* Fundo escuro para ler sobre a foto */
            backdrop-filter: none;    /* Efeito de vidro fosco */
            padding: 25px;
            border-radius: 15px;
            border: 1px solid;
            margin-bottom: 20px;
            color: white;
        }}
    </style>
    <div class="card-animado-{delay}">
        <h2 style="color: #00c0f2; margin-top:0;">{titulo}</h2>
        <p style="font-size: 1.1em; line-height: 1.6;">{corpo}</p>
    </div>
    """
    return st.markdown(style, unsafe_allow_html=True)
def get_base64 (bin_file) :
    with open (bin_file, "rb") as f :
        data = f.read ()
    return base64.b64encode (data).decode () 

def set_background (png_file) :
    bin_str = get_base64 (png_file)
    page_bg_img = f'''
<style>
.stApp {{
    background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), 
                url("data:image/jpeg;base64,{bin_str}");
    background-size: cover;
    background-attachment: fixed;
}}
</style>
'''
    st.markdown (page_bg_img, unsafe_allow_html = True)

def cliente_form () : 
    with st.form ("form_cliente") :
        try :
            st.subheader ("Cadastro de Cliente")
            nome = st.text_input ("Nome do Cliente")
            cpf = st.text_input ("CPF do Cliente")
            enviar = st.form_submit_button ("Cadastrar Cliente")
            if enviar :
                return nome , cpf , True 
        except Exception as e :
            st.error (f"Erro ao cadastrar cliente: {e}")
            return None , None ,False
    return None , None , False
        
set_background (caminho)

st.set_page_config ("​​💰​Sistema_Bancário_Interativo")
with st.sidebar :
    st.title ("Navegação")
    opção = st.radio("Ir para" , ["​​​🧬​​Início" , " ​🙎🏻‍♂️​Cliente" , "​​​📈​Conta" , "​​​​💳​Banco"])
if opção == "​​​🧬​​Início" :
    criar_card_animado ("  ​​💰​Sistema Bancário Interativo  ", "Projeto feito para consolidar conhecimentos em POO ", delay=1)

    texto_boas_vindas = """ 
    Este é um projeto de sistema bancário utilizando programação orientada a objetos (POO) em Python com o intuito de demonstrar conceitos fundamentais de POO, como classes, objetos, encapsulamento, herança e polimorfismo.
              
    Você poderá navegar entre as seções para explorar as funcionalidades do sistema bancário, incluindo a criação de clientes, contas e operações bancárias básicas.""" 

    criar_card_animado("Seja bem-vindo!", texto_boas_vindas, delay=1) 

              
    sobre_mim = """Olá! Meu nome é Bruno Raphael, sou estudante de Engenharia da Computação na UEMA e tenho paixão por análise de dados e desenvolvimento de software. Este projeto é uma demonstração dos meus conhecimentos em programação orientada a objetos e desenvolvimento de sistemas bancários. Espero que você aproveite a experiência!"""

    criar_card_animado("Sobre o Desenvolvedor", sobre_mim, delay=2)

    
    col1 , col2 , col3 = st.columns (3)
    with col1 : 
        st.badge("Linkedln", color = "blue")
        st.link_button ("Acessar", "https://www.linkedin.com/in/bruno-raphael-andrade-48816b334/")
    with col2 :
        st.badge ("GitHub", color = "blue")
        st.link_button ("Veja aqui", "https://github.com/BrunoAndrade-dev")
    with col3 :
        st.badge ("Portifólio", color = "blue")
        st.link_button ("Veja aqui", "https://portifolioapp-hwdouyi2fhao77txs4b5da.streamlit.app")

if opção == " ​🙎🏻‍♂️​Cliente" :
    texto_aba_cliente = """
     Nesta seção você poderá gerenciar informações dos clientes do banco, incluindo a criação de novos clientes, visualização de detalhes e atualização de informações pessoais.

     """
    criar_card_animado (" ​🙎🏻‍♂️​Cliente  ", texto_aba_cliente,  delay=1)

    op_cliente , op_cliente2 = st.columns(2)
    with op_cliente :
        botao_cliente = st.button ("Cadastrar Novo Cliente")
        if botao_cliente :
            nome, cpf, enviar = cliente_form ()
            if enviar : 
                try :
                    banco.cadastrar_cliente (nome , cpf)
                    st.success (f"Cliente {nome} cadastrado com sucesso!")
                except Exception as e :
                    st.error(f"Erro ao cadastrar cliente: {e}")
if opção == "​​​📈​Conta" :
    texto_aba_conta = """
    Nesta seção você poderá gerenciar as contas bancárias dos clientes, incluindo a criação de novas contas, visualização de detalhes das contas existentes e atualização de saldos.
    """
    criar_card_animado ("​​​📈​Conta  ", texto_aba_conta, delay=1)

            



