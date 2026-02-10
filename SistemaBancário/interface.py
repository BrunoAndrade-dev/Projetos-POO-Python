import streamlit as st

from cliente import * 
from conta import *
from banco import*
from main import banco
import base64
import os
from faker import Faker
import pandas as pd
from repository.dp import get_connect
import random 
directorio_atual = os.path.dirname (os.path.abspath (__file__ ))
caminho = os.path.join (directorio_atual, "fundo.jpg")

def gerar_clientes ( banco_instance , quantidade : int) : 
    faker = Faker ('pt_BR')
    sucesso = 0 
    st.progress (0)
    status_text = st.empty()
    for i in range(quantidade) : 
        nome = faker.name()
        cpf = faker.cpf()
        if banco_instance.cliente_repo.cpf_existe(cpf) : 
            continue
        banco_instance.cadastrar_cliente(nome, cpf)
        sucesso += 1
        if i % 10 == 0:
            st.progress ((i+1) / quantidade)
            status_text.text (f"Gerando clientes: {sucesso}/{quantidade}")
    status_text.text (f"Clientes gerados com sucesso: {sucesso}/{quantidade}")  
    return sucesso



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
    opção = st.radio("Ir para" , ["​​​🧬​​Início" , " ​🙎🏻‍♂️​Cliente" , "​​​📈​Conta" , "​​​​💳​Banco", "😎​Administrador"])
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
        st.link_button ("Acessar", "https://github.com/BrunoAndrade-dev")
    with col3 :
        st.badge ("Portifólio", color = "blue")
        st.link_button ("Acessar", "https://portifolioapp-hwdouyi2fhao77txs4b5da.streamlit.app")

if opção == " ​🙎🏻‍♂️​Cliente": 
    texto_aba_cliente = """
     Nesta seção você poderá gerenciar informações dos clientes do banco...
     """
    criar_card_animado(" ​🙎🏻‍♂️​Cliente  ", texto_aba_cliente, delay=1)

    
    if 'clicou_cadastrar' not in st.session_state:
        st.session_state.clicou_cadastrar = False

    
    
    
        
    if st.button("Cadastrar Novo Cliente"):
        st.session_state.clicou_cadastrar = True

    
    if st.session_state.clicou_cadastrar:
        st.write ("### 📝 Formulário ")
        nome, cpf, enviar = cliente_form()
        
        if enviar: 
            if nome and cpf:
                try:
                    banco.cadastrar_cliente(nome, cpf)
                    st.success(f"Cliente {nome} cadastrado com sucesso!")
                    
                    st.session_state.clicou_cadastrar = False 
                   
                except Exception as e:
                    st.error(f"Erro ao cadastrar cliente: {e}")
            else:
                st.warning("Por favor, preencha todos os campos.")
    
    if st.button("Listar Clientes com tabela") : 
        st.caption("Ok, você está prestes a listar clientes...")
        # Listar banco de dados com tabela
        df = pd.read_sql_query("SELECT * FROM clientes", get_connect())
        st.dataframe(df)
        st.caption("Clientes listados com sucesso!")

if opção == "​​​📈​Conta":
    texto_aba_conta = "Gerencie contas, visualize detalhes e atualize saldos."
    criar_card_animado("​​​📈​Conta", texto_aba_conta, delay=1)

    if "cliente_localizado" not in st.session_state:
        st.session_state.cliente_localizado = False
    if "cpf_atual" not in st.session_state:
        st.session_state.cpf_atual = ""

    with st.form("identificacao_cliente"):
        st.write("### 🔍 Identificação de Correntista")
        cpf_input = st.text_input("Digite o CPF do cliente", placeholder="000.000.000-00")
        submeteu = st.form_submit_button("Verificar CPF")

        if submeteu:
            if cpf_input:
                if banco.cliente_repo.cpf_existe(cpf_input):
                    st.session_state.cliente_localizado = True
                    st.session_state.cpf_atual = cpf_input
                else:
                    st.session_state.cliente_localizado = False
                    st.error("❌ CPF não encontrado no sistema.")
            else:
                st.warning("⚠️ Digite um CPF para pesquisar.")

    if st.session_state.cliente_localizado:
        st.success(f"✅ Cliente localizado: {st.session_state.cpf_atual}")
        cliente_data = banco.cliente_repo.buscar_por_cpf(st.session_state.cpf_atual)

        conta_data = banco.conta_repo.busca_conta_por_cpf(st.session_state.cpf_atual)

        col1, col2 = st.columns([1, 2])
        with col1:
             st.metric("Status da Conexão", "Ativa", delta="Disponível")
        if conta_data : 
            with col2:
                st.metric("Número da Conta", conta_data.number, )
                if conta_data.saldo >= 0 :
                    st.metric ("Saldo Atual", f"R$ {conta_data.saldo:.2f}", delta = "Positivo", delta_color="normal")
                else :
                    st.metric ("Saldo Atual", f"R$ {conta_data.saldo:.2f}", delta = "Negativo", delta_color="inverse")

            with st.expander("💸 Realizar Transações Financeiras", expanded = False ) : 
                tab_deposito, tab_saque, tab_transferir= st.tabs (["💰Depósito" , "🏧Saque"])

                with tab_deposito :
                    st.write ("### 💰 Área de Depósito")
                    pass
                with tab_saque :
                    st.write ("### 🏧 Área de Saque")
                    pass
                with tab_transferir : 
                    st.write ("### ")
                
        
        if st.button("Buscar outro CPF"):
            st.session_state.cliente_localizado = False
            st.session_state.cpf_atual = ""
            st.rerun() 

if opção == "​​​​💳​Banco" :
    texto_aba_banco = """
    Nesta seção você poderá gerenciar o banco, incluindo a criação de novas contas, visualização de detalhes das contas existentes e atualização de saldos.
    """
    criar_card_animado ("​​​​💳​Banco  ", texto_aba_banco, delay=1)

    if "Criar_Conta" not in st.session_state : 
        st.session_state.Criar_Conta = False
    if not st.session_state.Criar_Conta:
        if st.button("Criar Nova Conta ") : 
            st.session_state.Criar_Conta = True
    if st.session_state.Criar_Conta:
        with st.form("forma_nova_conta") : 
            st.write ("### 🏦 Criação de Nova Conta Bancária")
            numero = st.text_input(" Número da Conta")
            saldo = st.text_input("Saldo da Conta")
            cliente = st.text_input("CPF do Cliente")
            enviar = st.form_submit_button("Criar Conta")
            if enviar:
                if numero and saldo and cliente:
                    try:
                        banco.criar_conta(cliente, numero, saldo)
                        st.success("Conta criada com sucesso!")
                    except Exception as e:
                        st.error (f"Erro ao criar conta : {e}")
                else:
                    st.warning("Por favor, preencha todos os campos.")

if opção == "😎​Administrador" :
    texto_aba_administrador = """
    Aba exclusiva para o administrador do sistema.
    """
    criar_card_animado ("😎​Administrador  ", texto_aba_administrador, delay=1)

    if "clicou_senha" not in st.session_state : 
        st.session_state.clicou_senha = False

    def gerar_contas(banco_instance):
    # Agora usamos o método que você acabou de criar no repositório
        try:
            clientes = banco_instance.cliente_repo.buscar_todos_clientes()
        except Exception as e:
            st.error(f"Erro ao buscar clientes: {e}")
            return

        if not clientes:
            st.warning("Nenhum cliente encontrado no banco de dados.")
            return 

        sucesso = 0
    
        with st.status("Vinculando contas aos clientes...", expanded=True) as status: 
            for c in clientes: 
           
                numero_conta = random.randint(1000, 99999)
            
                saldo_inicial = round(random.uniform(10.0, 5000.0), 2)

                try: 
               
                    banco_instance.criar_conta(c.cpf, numero_conta, saldo_inicial)
                    sucesso += 1
                except Exception:  
                
                    continue

        status.update(label=f"Processo concluído! {sucesso} contas criadas.", state="complete")
    
        return sucesso

    if not st.session_state.clicou_senha:
        with st.form("form_admin"):
            st.write ("### 🔐 Acesso Restrito - Administrador")
            senha = st.text_input("Senha de Acesso", type="password")
            entrar = st.form_submit_button("Entrar")
            if entrar:
                if senha == '18052006':
                    st.session_state.clicou_senha = True
                    st.rerun()
                else:
                    st.error("Senha incorreta!")
    
    if st.session_state.clicou_senha:
        st.success("Logado como administrador!")
        
        
        col1, col2 = st.columns(2)
    
        with col1:
            if st.button("Gerar Clientes"): 
                st.caption("A processar carga de clientes...")
                gerar_clientes(banco, 1000)
                st.success("1000 Clientes gerados!")

        with col2:
            if st.button("Gerar Contas para Clientes"):
                st.caption("A vincular contas aos CPFs existentes...")
                gerar_contas(banco)
            
        st.divider() 
        
        if st.button("Logout"):
            st.session_state.clicou_senha = False
            st.rerun()
