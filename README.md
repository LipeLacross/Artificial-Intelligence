## 🌐 [English Version of README](README_EN.md)

# Artificial-Intelligence
# Projeto de Classificação e Algoritmos de Busca

Este projeto contém duas partes principais: a classificação de dados usando algoritmos de machine learning e a implementação de vários algoritmos de busca em grafos ponderados. Ele inclui um exemplo prático de uso de uma rede neural MLP para classificação e algoritmos de busca clássicos aplicados a um grafo representando cidades da Romênia.

## 🔨 Funcionalidades do Projeto

### Classificação com MLP e Comparação de Algoritmos
- **`iris_mlp_classification.py`**: Implementa um classificador MLP para o dataset Iris e salva a acurácia em um arquivo `accuracy_report.txt`.
- **`iris_mlp_classification_plus.py`**: Compara diferentes algoritmos de classificação (KNN, Decision Tree, SVM, MLP) no dataset Iris e salva a análise em `classification_analysis.txt`.

### Algoritmos de Busca em Grafos
- **`best_first_search.py`**: Implementa a busca Best-First Search.
- **`bidirectional_search.py`**: Implementa a busca Bidirectional Search.
- **`breadth_first_search.py`**: Implementa a busca em Largura (BFS).
- **`depth_first_search.py`**: Implementa a busca em Profundidade (DFS).
- **`uniform_cost_search.py`**: Implementa a busca Uniform Cost Search.

### Exemplo Visual do Projeto

- **`grafo_romenia_com_pesos.py`**: Define um grafo ponderado representando cidades da Romênia e inclui métodos para imprimir e visualizar o grafo.
  ![image](https://github.com/user-attachments/assets/ddb13a7a-5f98-4d26-9b61-3d1f37f55463)

## ✔️ Técnicas e Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada.
- **Scikit-Learn**: Biblioteca para machine learning, usada para o classificador MLP e outros algoritmos.
- **NetworkX**: Biblioteca para manipulação e visualização de grafos.
- **Matplotlib**: Biblioteca para visualização gráfica.

## 📁 Estrutura do Projeto

- **`mlp_classification/`**
    - `accuracy_report.txt`: Arquivo de saída com a acurácia do classificador MLP.
    - `iris_mlp_classification.py`: Código para classificação do dataset Iris usando MLP.

- **`mlp_classification_plus/`**
    - `classification_analysis.txt`: Arquivo de saída com a comparação dos classificadores.
    - `iris_mlp_classification_plus.py`: Código para comparar diferentes algoritmos de classificação no dataset Iris.

- **`search_algorithms/`**
    - `atividade_ygor_best_first_search.py`: Implementação da busca Best-First Search.
    - `atividade_ygor_bidirectional_search.py`: Implementação da busca Bidirectional Search.
    - `atividade_ygor_breadth_first_search.py`: Implementação da busca em Largura (BFS).
    - `atividade_ygor_depth_first_search.py`: Implementação da busca em Profundidade (DFS).
    - `atividade_ygor_uniform_cost_search.py`: Implementação da busca Uniform Cost Search.
    - `grafo_romenia_com_pesos.py`: Define e visualiza o grafo ponderado das cidades da Romênia.

- **`README.md`**: Documento de documentação do projeto.

## 🛠️ Abrir e Rodar o Projeto

Para rodar os scripts, siga os passos abaixo:

1. **Certifique-se de que o Python está instalado**:
    - Verifique se o Python está instalado com:
      ```bash
      python --version
      ```
    - Se não estiver instalado, baixe e instale a versão recomendada do [Python](https://www.python.org/).

2. **Instale as dependências**:
    - Instale as bibliotecas necessárias com:
      ```bash
      pip install -r requirements.txt
      ```

3. **Execute os Scripts**:
    - Para executar os scripts de classificação, use:
      ```bash
      python mlp_classification/iris_mlp_classification.py
      python mlp_classification_plus/iris_mlp_classification_plus.py
      ```
    - Para executar os scripts de busca, use:
      ```bash
      python search_algorithms/atividade_ygor_best_first_search.py
      python search_algorithms/atividade_ygor_bidirectional_search.py
      python search_algorithms/atividade_ygor_breadth_first_search.py
      python search_algorithms/atividade_ygor_depth_first_search.py
      python search_algorithms/atividade_ygor_uniform_cost_search.py
      ```

## 🌐 Deploy

O projeto pode ser implantado em um servidor ou ambiente de desenvolvimento que suporte Python. Não há instruções específicas de deploy neste momento, mas os scripts devem funcionar em qualquer ambiente Python configurado corretamente.

