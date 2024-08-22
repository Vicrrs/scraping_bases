# scraping_bases
This is scraping from content documentation of winthor and qliksense.

### Explicações:

* src/: Diretório principal do código-fonte, onde ficam os scripts de scraping, parsing, utilidades, e pré-processamento.
* data/: Armazena os dados em diferentes estados: brutos (raw/), processados (processed/), e organizados para treinamento (datasets/).
* models/: Scripts para treinamento do modelo de linguagem e armazenamento de modelos pré-treinados.
* notebooks/: Notebooks Jupyter para análise exploratória dos dados e experimentos de pré-processamento.
* config/: Configurações usadas no projeto, como URLs para scraping e parâmetros de treinamento do LLM.
* tests/: Testes automatizados para garantir que cada componente funcione corretamente.
* scripts/: Scripts auxiliares para automatizar tarefas comuns, como iniciar o scraper ou o treinamento do LLM.


```tree
scraping_bases/
|
├── README.md                     # Descrição do projeto, instruções de uso, etc.
├── pyproject.toml                # Arquivo de configuração do Poetry com dependências
├── poetry.lock                   # Arquivo de bloqueio de dependências do Poetry
├── setup.cfg                     # Configurações adicionais (opcional)
├── .gitignore                    # Arquivos e diretórios a serem ignorados pelo Git
│
├── src/                          # Código-fonte do projeto
│   ├── __init__.py               # Torna src um módulo Python
│   ├── scraper.py                # Script principal de scraping
│   ├── parser.py                 # Funções para parsing e limpeza dos dados
│   ├── utils.py                  # Funções utilitárias (log, manipulação de arquivos, etc.)
│   └── data_preprocessing.py     # Script de pré-processamento dos dados para o LLM
│
├── data/                         # Dados extraídos e processados
│   ├── raw/                      # Dados brutos extraídos pelo scraper
│   │   └── winthor_docs.json     # Exemplo de arquivo com dados brutos
│   ├── processed/                # Dados processados e prontos para treinamento
│   │   └── winthor_docs_cleaned.json  # Dados após pré-processamento
│   └── datasets/                 # Conjuntos de treino, validação e teste para o LLM
│       ├── train.json
│       ├── val.json
│       └── test.json
│
├── models/                       # Scripts e modelos de treinamento do LLM
│   ├── train_llm.py              # Script de treinamento do LLM
│   ├── fine_tune.py              # Script para fine-tuning do modelo
│   └── pretrained/               # Diretório para armazenar modelos pré-treinados
│       └── model_name/           # Nome do modelo pré-treinado
│           ├── config.json
│           ├── pytorch_model.bin
│           └── tokenizer/
│               ├── vocab.txt
│               └── tokenizer.json
│
├── notebooks/                    # Notebooks para exploração de dados e experimentação
│   ├── EDA.ipynb                 # Análise exploratória dos dados
│   └── preprocessing.ipynb       # Notebooks para pré-processamento dos dados
│
├── config/                       # Arquivos de configuração do projeto
│   ├── scraping_config.json      # URLs, headers, parâmetros de scraping
│   └── llm_config.json           # Configurações para treinamento do LLM
│
├── tests/                        # Testes unitários e de integração
│   ├── test_scraper.py           # Testes para o scraper
│   ├── test_parser.py            # Testes para o parser
│   └── test_preprocessing.py     # Testes para pré-processamento
│
└── scripts/                      # Scripts auxiliares
    ├── run_scraper.sh            # Script shell para iniciar o scraping
    ├── preprocess_data.sh        # Script shell para pré-processamento dos dados
    └── train_model.sh            # Script shell para iniciar o treinamento do LLM

```
