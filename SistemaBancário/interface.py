import streamlit as st

from cliente import * 
from conta import *
from banco import *
from main import banco
import base64
import os
from faker import Faker
import pandas as pd
from repository.dp import get_connect
import random 
import time 
from logica import *
directorio_atual = os.path.dirname (os.path.abspath (__file__ ))
caminho = os.path.join (directorio_atual, "fundo.jpg")
df = pd.read_csv("data/clean_data.csv")

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
            backdrop-filter: none;    /* Efeito de vidro fosco */;
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
    opção = st.radio("Ir para" , ["​​​🧬​​Início" ,"​🚨​Informações",  " ​🙎🏻‍♂️​Cliente" , "​​​📈​Conta" , "​​​​💳​Banco", "😎​Administrador" , "📊​​Dashboard", "📠 ​IA investimentos"])
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

if opção == "​🚨​Informações" :
    criar_card_animado("​🚨​Informações do Projeto", "Detalhes sobre o sistema bancário e instruções de uso.", delay=1)

    info_projeto_clientes = (" ​Na aba clientes você pode cadastrar novos clientes e listar os ja existentes ")
    criar_card_animado("🙎🏻‍♂️Cliente", info_projeto_clientes, delay=1)

    info_projeto_contas = (" Na aba contas você pode acessar detalhes de contas vinculadas a um CPF, realizar depósitos, saques e transferências ")
    criar_card_animado("📈Conta", info_projeto_contas, delay=2)

    info_projeto_banco = (" Na aba banco você pode criar novas contas vinculadas a um CPF já cadastrado ")
    criar_card_animado("💳Banco", info_projeto_banco, delay=3)

    info_projeto_administrador = (" Espaço dedicado apenas ao criador do projeto, onde é possível gerar clientes e contas de forma automatizada para testes ")
    criar_card_animado("😎Administrador", info_projeto_administrador, delay=4)

    info_projeto_dashboard = ("📊 Na aba dashboard você tem acesso a análises sobre a base de clientes do banco, incluindo distribuição de saldos e o Asset Under Management (AUM) ")
    criar_card_animado("📊Dashboard", info_projeto_dashboard, delay=5)

    info_projeto_IA = (" Na aba IA investimentos você pode testar um modelo de machine learning que classifica o perfil de investimento do cliente com base no saldo disponível em conta ")
    criar_card_animado("📠IA Investimentos", info_projeto_IA, delay=6)
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
    if "confirmacao_pendente" not in st.session_state:
        st.session_state.confirmacao_pendente = False

    with st.form("identificacao_cliente"):
        st.write("### 🔍 Identificação de Correntista")
        cpf_input = st.text_input("Digite o CPF do cliente", placeholder="000.000.000-00")
        submeteu = st.form_submit_button("Verificar CPF")

        if submeteu:
            if cpf_input and banco.cliente_repo.cpf_existe(cpf_input):
                st.session_state.cliente_localizado = True
                st.session_state.cpf_atual = cpf_input
                st.rerun() 
            else:
                st.error("❌ CPF não encontrado ou inválido.")

    
    if st.session_state.cliente_localizado:
        
        cliente_data = banco.cliente_repo.buscar_por_cpf(st.session_state.cpf_atual)
        conta_data = banco.conta_repo.busca_conta_por_cpf(st.session_state.cpf_atual)

        if conta_data:
            st.success(f"✅ Cliente localizado: {cliente_data.nome}")
            
            col1, col2 = st.columns([1, 2])
            with col1:
                st.metric("Status da Conexão", "Ativa", delta="Disponível")
            with col2:
                st.metric("Número da Conta", conta_data.number)
                
                if conta_data.saldo >= 0:
                    st.metric("Saldo Atual", f"R$ {conta_data.saldo:.2f}", delta="Positivo")
                else:
                    st.metric("Saldo Atual", f"R$ {conta_data.saldo:.2f}", delta="Negativo", delta_color="inverse")

            with st.expander("💸 Realizar Transações Financeiras", expanded=True):
                tab_deposito, tab_saque, tab_transferir = st.tabs(["💰 Depósito", "🏧 Saque", "🔄 Transferência"])

                with tab_deposito:
                    st.write("### 💰 Área de Depósito")

    
                    if "confirmar_deposito" not in st.session_state:
                        st.session_state.confirmar_deposito = False
                    if "valor_preparado" not in st.session_state:
                        st.session_state.valor_preparado = 0.0

    
                    with st.form("form_valor_deposito"):
                        valor_digitado = st.number_input("Quanto deseja depositar?", min_value=0.01, step=50.0)
                        if st.form_submit_button("Preparar Depósito"):
                            st.session_state.valor_preparado = valor_digitado
                            st.session_state.confirmar_deposito = True
            

    
                    if st.session_state.confirmar_deposito:
                        st.warning(f"⚠️ **Atenção:** Você está prestes a depositar **R$ {st.session_state.valor_preparado:.2f}** na conta {conta_data.number}. Confirma?")
        
                        col_c1, col_c2 = st.columns(2)
        
                        with col_c1:
                            if st.button("✅ Confirmar Agora", use_container_width=True):
                                try:
                    
                                    conta_data.depositar(st.session_state.valor_preparado)
                                    banco.conta_repo.atualizar_saldo(conta_data)
                    
                                    st.success("Depósito realizado com sucesso!")
                    
                    
                                    st.session_state.confirmar_deposito = False
                                    st.session_state.valor_preparado = 0.0
                                    st.rerun()
                                except Exception as e:
                                    st.error(f"Erro ao depositar: {e}")

                        with col_c2:
                            if st.button("❌ Cancelar", use_container_width=True):
                                st.session_state.confirmar_deposito = False
                                st.session_state.valor_preparado = 0.0
                                st.rerun()

                with tab_saque:
                    st.write("### 🏧 Área de Saque")
                    with st.form("executar_saque"):
                        valor_s = st.number_input("Quanto deseja sacar?", min_value=0.01, step=50.0)
                        if st.form_submit_button("Confirmar Saque"):
                            try:
                                conta_data.sacar(valor_s)
                                banco.conta_repo.atualizar_saldo(conta_data)
                                st.success("Saque realizado!")
                                st.rerun()
                            except Exception as e:
                                st.error(f"Erro: {e}")

                with tab_transferir:
                    st.write("### 🔄Área de Transferência")

                    with st.form (" 🚀​transferir") : 
                        cpf_d = st.text_input("CPF do Destinatário" ,placeholder = "000.000.000-00" )
                        valor_d = st.number_input ("Valor da transferência", placeholder = "000,00")
                        
                        if st.form_submit_button ("transferir") :
                            try : 
                                conta_destino = banco.conta_repo.busca_conta_por_cpf(cpf_d)
                                if not conta_destino : 

                                    st.error (" ❌​ ERRO AO ENCONTRAR DESTINATÁRIO")

                                elif conta_destino == st.session_state.cpf_atual :

                                    st.warning (" ​⚠️​ Não pode transferir para você mesmo")

                                else : 
                                    conta_data.transferir(conta_destino, valor_d)
                                    banco.conta_repo.atualizar_saldo (conta_data)
                                    banco.conta_repo.atualizar_saldo(conta_destino)
                                    progresso_bar = st.progress(0)
                                    
                                    
                                for i in range (20) : 
                                    time.sleep(0.1)
                                    progresso_bar.progress(i + 1)

                                st.success(f"✅ Transferência de R$ {valor_d:.2f} realizada!")
                                st.rerun()
                            except Exception as e : 
                                st.error(f" ERRO AO PROCESSAR TRANSFERÊNCIA {e}")
                                
                    
                    

        if st.button("🔍 Buscar outro CPF"):
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


if opção == "📊​​Dashboard": 
    criar_card_animado("📊 Dashboard de Análise", "Visão geral da saúde financeira do banco.", delay=1)
    
    
    extracao_info(df)

    st.divider()

    col_aum, col_legenda = st.columns([1.5, 1])

    with col_aum: 
        Aum(df) 

    with col_legenda: 
        dist, legenda = divisao_saldo(df)
        st.write("### 🔍 Regras de Negócio")
        st.table(legenda)

    st.divider()

    
    st.subheader("📈 Distribuição e Tendência de Saldo")
    plot_3_dif(dist)
    st.caption("Este gráfico demonstra a densidade de clientes por faixa salarial.")

    st.divider()

if opção == "📠 ​IA investimentos" :
    criar_card_animado("📠 IA para Recomendação de Investimentos", "Previsão de perfil de investimento com base no saldo do cliente.", delay=3)
    modelo = carregar_modelo_ia()

    st.subheader("🔮 Previsão de Perfil de Investimento")

    with st.container() : 
        coluna1 , coluna2 = st.columns (2)

        with coluna1 : 
            saldo_teste = st.number_input("Digite o saldo em R$ do cliente para a previsão" , placeholder= "000,00")
        with coluna2 : 
            st.caption ("O modelo de IA classifica os clientes em categorias de investimento com base no saldo disponível. Insira o saldo para obter a recomendação de perfil de investimento.")

        st.divider()
    if st.button (" ​🧿​ Realizar Previsão") : 
        with st.spinner("Processando previsão..."):
            resultado, f_num = realizar_predicao(modelo, saldo_teste)
            
            st.divider()

            dist, legenda = divisao_saldo(df)

            res1, res2 = st.columns(2)
            res1.metric("Categoria", "Verifique abaixo")
            st.table(legenda)
            
            res2.metric("Faixa Numérica", f_num)

            if resultado == "Diamante":
                st.success(f"💎 O cliente com saldo de R$ {saldo_teste:,.2f} é um investidor de elite!")
            else:
                st.info(f"✅ O modelo classificou o perfil como: **{resultado}**")
            
            st.balloons()
        
        

    
    

    
    
    
