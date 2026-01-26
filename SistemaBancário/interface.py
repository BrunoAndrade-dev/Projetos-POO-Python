import streamlit as st
from cliente import * 
from conta import *
from banco import*

st.set_page_config ("​​💰​Sistema_Bancário_Interativo")

st.header ("​​💰​Sistema Bancário Interativo")

st.subheader (""" Seja bem-vindo! 
Este é um projeto de sistema bancário utilizando programação orientada a objetos (POO) em Python com o intuito de demonstrar conceitos fundamentais de POO, como classes, objetos, encapsulamento, herança e polimorfismo.
              
Você poderá navegar entre as seções para explorar as funcionalidades do sistema bancário, incluindo a criação de clientes, contas e operações bancárias básicas.
              
""")

st.subheader (""" Sobre o Desenvolvedor
Olá! Meu nome é Bruno Raphael, sou estudante de Engenharia da Computação na UEMA e tenho paixão por análise de dados e desenvolvimento de software. Este projeto é uma demonstração dos meus conhecimentos em programação orientada a objetos e desenvolvimento de sistemas bancários. Espero que você aproveite a experiência!

    Contato
    # email : brunorafha4@gmail.com 
    # Linkedin : https://www.linkedin.com/in/bruno-raphael-andrade-48816b334/ 
    # GitHub : https://github.com/BrunoAndrade-dev """)
    

with st.sidebar :
    st.title ("Navegação")
    opção = st.radio("Ir para" , ["​​​🧬​​Início" , " ​🙎🏻‍♂️​Cliente" , "​​​📈​Conta" , "​​​​💳​Banco"])

