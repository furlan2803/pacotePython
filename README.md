# 1. Package CNPJ e DATASUS

Este pacote é dedicado ao tratamento e envio para a AWS S3 de dados relacionados aos CNPJs e ao DATASUS, selecionados para atender às necessidades do projeto. Seu objetivo principal é facilitar o processamento e análise desses dados, garantindo uma integração suave com as ferramentas da AWS. As instruções abaixo guiarão você no uso adequado deste pacote, desde a execução dos notebooks Jupyter até a realização de testes do código.

## 1.1 Arquivos do pacote

Este é um breve guia sobre os arquivos contidos neste pacote Python.

- **.env.tmpl**: Arquivo de configuração de ambiente. Contém as keys da AWS Lab. 

- **.gitignore**: Arquivo de configuração do Git para ignorar o arquivo  ``.env.tmpl`` durante o versionamento.

- **.ipynb_checkpoints**: Diretório que armazena checkpoints automáticos de notebooks Jupyter.

- **.pytest_cache**: Diretório que armazena cache e dados temporários do Pytest.

- **build**: Diretório gerado durante o processo de construção do pacote. Contém arquivos intermediários.

- **arquivos_csv**: Diretório para armazenar arquivos CSV relacionados ao projeto.

- **inteli.ipynb**: Jupyter Notebook principal do projeto, que contém todo o processo de tratamento dos dados CSV.

- **intelidata**: Pacote Python principal.

  - **__init__.py**: Arquivo necessário para que o diretório seja tratado como um pacote Python.
  
  - **lib.py**: Módulo Python contendo funcionalidades específicas. Aqui são definidas todas as funções de processamento utilizadas no `inteli.ipynb`.

- **intelidata.egg-info**: Informações sobre o pacote, geradas durante a construção.

- **requirements.txt**: Lista de dependências necessárias para executar o projeto.

- **send_s3.ipynb**: Jupyter Notebook onde os arquivos CSV, após o processamento, são encaminhados aos buckets da AWS S3.

- **setup.py**: Script de configuração para instalar o pacote.

- **temp.csv**: Arquivo temporário.

- **tests**: Diretório contendo testes para o pacote.

  - **test_lib.py**: Arquivo de teste do módulo.
  
- **README.md**: Este arquivo, fornecendo informações sobre o pacote.

## 1.2 Executando o Pacote

Antes de executar os arquivos, certifique-se de ter instalado todas as dependências do projeto. 

### 1.2.1 Notebooks Jupyter

Para executar os processos principais do projeto, utilize os seguintes notebooks Jupyter:

- **inteli.ipynb**: Este notebook contém o fluxo principal de tratamento dos dados CSV. Basta abrir o notebook e executar suas células para processar e analisar os dados.

- **send_s3.ipynb**: Utilize este notebook para o envio dos dados processados para o Amazon S3. Abra o notebook e execute suas células para encaminhar os arquivos CSV aos buckets da AWS S3.

### 1.2.2 Testes

A pasta "tests" contém testes para garantir a integridade do pacote. Para executar os testes, recomenda-se o uso do Windows Subsystem for Linux (WLS) ou de um terminal Linux. Utilize o seguinte comando no terminal:

```bash
pytest tests
```

## 1.3 Licença

Este pacote é distribuído sob a licença [Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
