<div align="center">
  <h1>
    <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Spiral%20Calendar.png" alt="Calendário" width="45" height="45" />
    Agenda de Contatos em Python
    <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Man%20Technologist.png" alt="Tecnólogo" width="45" height="45" />
  </h1>
</div>

<p align="center">
  <img alt="Linguagem Principal" src="https://img.shields.io/github/languages/top/vrsmarcos26/Agenda-Simples-em-Python?style=for-the-badge&color=3776AB">
  <img alt="Último Commit" src="https://img.shields.io/github/last-commit/vrsmarcos26/Agenda-Simples-em-Python?style=for-the-badge&color=green">
</p>

<p align="center">
  Um projeto simples de agenda de contatos, desenvolvido em Python para demonstrar operações de CRUD (Create, Read, Update, Delete) e manipulação de arquivos CSV.
</p>

<p align="center">
  <a href="#-funcionalidades">Funcionalidades</a> •
  <a href="#-tecnologias-utilizadas">Tecnologias</a> •
  <a href="#-como-rodar-o-projeto">Como Rodar</a> •
  <a href="#-estrutura-do-código">Estrutura</a> •
  <a href="#-contribuições">Contribuições</a> •
  <a href="#-licença">Licença</a>
</p>

---

### 🚀 Funcionalidades

O sistema oferece as seguintes funcionalidades para gerenciamento de contatos:

-   **Listar Contatos:** Exibe todos os contatos registrados na agenda.
-   **Buscar Contato:** Permite a busca de um contato específico pelo nome.
-   **Adicionar Contato:** Inclui um novo contato com nome, telefone, e-mail e endereço.
-   **Editar Contato:** Modifica as informações de um contato já existente.
-   **Excluir Contato:** Remove um contato da agenda.
-   **Exportar para CSV:** Salva a lista de contatos em um arquivo `.csv` customizado.
-   **Importar de CSV:** Carrega contatos a partir de um arquivo `.csv`.
-   **Salvar e Sair:** Salva todas as alterações no arquivo `database.csv` e encerra o programa.

---

### 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando as seguintes tecnologias:

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
</p>

-   A biblioteca nativa `csv` do Python foi utilizada para a manipulação de dados.

---

### ⚙️ Como Rodar o Projeto

Você precisará ter o **Python 3** instalado em sua máquina.

1.  **Clone o Repositório**
    ```bash
    git clone [https://github.com/vrsmarcos26/Agenda-Simples-em-Python.git
    cd NOME_DO_REPOSITORIO
    ```

2.  **Execute a Aplicação**
    Rode o script principal para iniciar a agenda no seu terminal.
    ```bash
    python agenda.py
    ```

3.  **Interaja com o Menu**
    Após a execução, um menu interativo será exibido no terminal. Digite o número da opção desejada para usar a agenda.

    ```
    -- AGENDA --
    1- Mostrar todos os contatos
    2- Buscar contato
    3- Incluir contato
    4- Editar contato
    5- Excluir contato
    6- Exportar contatos para CSV
    7- Importar contatos CSV
    8- Salvar e fechar
    ```

---

### 💻 Estrutura do Código

O código é organizado da seguinte forma:

-   **`AGENDA` (Dicionário):** Estrutura de dados principal que armazena os contatos em memória durante a execução.
-   **Funções Modulares:** Cada funcionalidade do menu é implementada em uma função específica para manter o código limpo e organizado.
    -   `mostrar_contatos()`: Exibe todos os contatos.
    -   `buscar_contato()`: Busca um contato.
    -   `incluir_editar_contato()`: Adiciona ou edita um contato.
    -   `excluir_contato()`: Remove um contato.
    -   `exportar_contatos()`: Exporta para um arquivo CSV.
    -   `importar_contato()`: Importa de um arquivo CSV.
-   **Persistência de Dados:**
    -   `carregar()`: Carrega os contatos do arquivo `database.csv` para a memória ao iniciar.
    -   `salvar()`: Salva o estado atual da agenda no arquivo `database.csv` ao fechar.

---

### 🤝 Contribuições

Sinta-se à vontade para contribuir com este projeto. Se você encontrar algum problema ou tiver sugestões de melhoria, por favor, abra uma **Issue** ou envie um **Pull Request**.

---

### 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

<hr>

<p align="center">
  Desenvolvido por <b>vrsmarcos26</b>
</p>
