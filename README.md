# Sistema Bancário Interativo: Reforçando POO em Python

Este projeto consiste em um sistema bancário completo desenvolvido para consolidar conceitos avançados de Programação Orientada a Objetos (POO) e integração com bancos de dados relacionais, utilizando uma interface moderna e funcional.

## Objetivo do Projeto
O objetivo principal foi aplicar na prática os pilares da POO (Abstração, Encapsulamento, Herança e Polimorfismo) na construção de um software funcional. O sistema simula operações bancárias reais, garantindo a persistência dos dados e uma experiência de usuário técnica através de um dashboard de controle.

## Arquitetura do Sistema

### Diagrama de Classes
O diagrama abaixo ilustra as relações entre as principais classes do sistema:

```mermaid
classDiagram
    class 
    Cliente {
        +String nome
        +String cpf
    }
    class Conta {
        +String number
        +float saldo
        +Cliente cliente
        +sacar(valor)
        +depositar(valor)
        +transferir(destino, valor)
    }
    class Banco {
        +ClienteRepository cliente_repo
        +ContaRepository conta_repo
        +cadastrar_cliente(nome, cpf)
        +criar_conta(cpf, numero, saldo)
    }
    class ContaRepository {
        +busca_conta_por_cpf(cpf)
        +atualizar_saldo(conta)
    }

    Conta o-- Cliente : possui
    Banco ..> Conta : gerencia
    Banco ..> Cliente : gerencia
    Banco --> ContaRepository : utiliza
    Banco --> ClienteRepository : utiliza
```
## Resumo do que foi feito
* **Arquitetura em Camadas**: Separação clara entre a lógica de negócio (Conta, Cliente), a camada de persistência (Repositórios) e a interface de usuário.
* **Persistência com SQLite**: Implementação de um sistema de banco de dados para garantir que as informações de clientes e saldos sejam mantidas após o fechamento da aplicação.
* **Operações Atômicas**: Desenvolvimento de lógica de transferência bancária garantindo a consistência dos saldos entre contas de origem e destino.
* **Interface com Streamlit**: Criação de um dashboard interativo com autenticação de administrador, geração de dados em massa com a biblioteca Faker e feedbacks visuais de progresso.
* **Tratamento de Exceções**: Implementação de erros personalizados (ex: SaldoInsuficienteError) para garantir a robustez do sistema contra operações inválidas.



[Image of the Model-View-Controller (MVC) architectural pattern]


## Como clonar e rodar o projeto

### Pré-requisitos
* Python 3.8 ou superior instalado.
* Git instalado.

### Passo a Passo
1. **Clone o repositório**:
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
   cd nome-do-repositorio

2. **Crie um ambiente virtual** 
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No Linux/Mac:
    source venv/bin/activate

3. **Instale as dependências**
    pip install -r requirements.txt

4. **Executar a aplicação** 
    cd SistemaBancário
    streamlit run interface.py
