# Agenda Simples em Python

Este é um projeto de uma agenda de contatos simples, desenvolvido em Python. A agenda permite ao usuário adicionar, editar, excluir e buscar contatos, além de importar e exportar dados em formato CSV. O objetivo deste projeto é criar uma aplicação funcional para gerenciar contatos, utilizando operações básicas de manipulação de dados.

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

1. **Mostrar todos os contatos da agenda**: Exibe todos os contatos registrados.
2. **Buscar contato**: Permite buscar um contato específico pelo nome.
3. **Incluir contato**: Adiciona um novo contato à agenda.
4. **Editar contato**: Edita um contato já existente.
5. **Excluir contato**: Remove um contato da agenda.
6. **Exportar contatos para CSV**: Exporta a lista de contatos para um arquivo CSV.
7. **Importar contatos de CSV**: Importa contatos de um arquivo CSV.
8. **Salvar dados**: Salva a agenda em um arquivo CSV local.
9. **Fechar agenda**: Encerra o programa.

## Como Usar

### Requisitos

Este projeto foi desenvolvido em Python 3. Para rodar o código, você precisa ter o Python instalado em sua máquina. Para verificar a instalação do Python, use o comando:

```python --version```

Se não tiver o Python instalado, você pode baixá-lo aqui.

### Instruções

1. Clone o repositório:

```git clone https://github.com/seu-usuario/nome-do-repositorio.git```
```cd nome-do-repositorio```

3. Execute o programa:

Basta rodar o arquivo Python para iniciar o programa de agenda:

```python agenda.py```

4. Interaja com o menu:
O programa exibirá um menu com as opções numeradas. Basta digitar o número correspondente à ação desejada.

5. Arquivos CSV:
Para exportar os contatos para um arquivo CSV, escolha a opção 6 e digite o nome do arquivo.
Para importar contatos de um arquivo CSV, escolha a opção 7 e forneça o caminho para o arquivo CSV.


### Exemplo de Uso

1- Mostrar todos os contatos da agenda
2- Buscar contato
3- Incluir contato
4- Editar contato
5- Excluir contato
6- Exportar contatos para CSV
7- Importar Contatos CSV
8- Salvar
0- Fechar agenda

Escolha a opção que deseja utilizar, digite o número correspondente e siga as instruções.

### Estrutura do Código
Agenda: O dicionário AGENDA armazena os contatos com seus respectivos detalhes (telefone, email, CEP).
Funções principais:
mostrar_contatos(): Exibe todos os contatos.
buscar_contato(): Busca um contato pelo nome.
incluir_editar_contato(): Adiciona ou edita um contato na agenda.
excluir_contato(): Remove um contato.
exportar_contatos(): Exporta os contatos para um arquivo CSV.
importar_contato(): Importa contatos de um arquivo CSV.
salvar(): Salva os contatos no arquivo database.csv.
carregar(): Carrega os contatos do arquivo database.csv para a memória.

### Tecnologias Utilizadas
Python 3
Manipulação de arquivos CSV

### Contribuições
Sinta-se à vontade para contribuir para este projeto. Se você encontrar algum erro ou tiver sugestões de melhorias, abra uma issue ou envie um pull request.
