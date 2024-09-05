## 🌐 [Versão em Português do README](README.md)

# Artificial-Intelligence
# Classification and Search Algorithms Project

This project contains two main parts: data classification using machine learning algorithms and the implementation of various search algorithms on weighted graphs. It includes a practical example of using an MLP neural network for classification and classic search algorithms applied to a graph representing cities in Romania.

## 🔨 Project Features

### Classification with MLP and Algorithm Comparison
- **`iris_mlp_classification.py`**: Implements an MLP classifier for the Iris dataset and saves the accuracy to a file `accuracy_report.txt`.
- **`iris_mlp_classification_plus.py`**: Compares different classification algorithms (KNN, Decision Tree, SVM, MLP) on the Iris dataset and saves the analysis to `classification_analysis.txt`.

### Graph Search Algorithms
- **`best_first_search.py`**: Implements the Best-First Search algorithm.
- **`bidirectional_search.py`**: Implements the Bidirectional Search algorithm.
- **`breadth_first_search.py`**: Implements the Breadth-First Search (BFS) algorithm.
- **`depth_first_search.py`**: Implements the Depth-First Search (DFS) algorithm.
- **`uniform_cost_search.py`**: Implements the Uniform Cost Search algorithm.

### Visual Example of the Project

- **`grafo_romenia_com_pesos.py`**: Defines a weighted graph representing cities in Romania and includes methods to print and visualize the graph.
  ![image](https://github.com/user-attachments/assets/ddb13a7a-5f98-4d26-9b61-3d1f37f55463)

## ✔️ Techniques and Technologies Used

- **Python**: Programming language used.
- **Scikit-Learn**: Library for machine learning, used for the MLP classifier and other algorithms.
- **NetworkX**: Library for graph manipulation and visualization.
- **Matplotlib**: Library for graphical visualization.

## 📁 Project Structure

- **`mlp_classification/`**
    - `accuracy_report.txt`: Output file with the MLP classifier's accuracy.
    - `iris_mlp_classification.py`: Code for classifying the Iris dataset using MLP.

- **`mlp_classification_plus/`**
    - `classification_analysis.txt`: Output file with the comparison of classifiers.
    - `iris_mlp_classification_plus.py`: Code for comparing different classification algorithms on the Iris dataset.

- **`search_algorithms/`**
    - `atividade_ygor_best_first_search.py`: Implementation of the Best-First Search algorithm.
    - `atividade_ygor_bidirectional_search.py`: Implementation of the Bidirectional Search algorithm.
    - `atividade_ygor_breadth_first_search.py`: Implementation of the Breadth-First Search (BFS) algorithm.
    - `atividade_ygor_depth_first_search.py`: Implementation of the Depth-First Search (DFS) algorithm.
    - `atividade_ygor_uniform_cost_search.py`: Implementation of the Uniform Cost Search algorithm.
    - `grafo_romenia_com_pesos.py`: Defines and visualizes the weighted graph of Romanian cities.

- **`README.md`**: Documentation file of the project.

## 🛠️ Running the Project

To run the scripts, follow the steps below:

1. **Make sure Python is installed**:
    - Check if Python is installed with:
      ```bash
      python --version
      ```
    - If not installed, download and install the recommended version from [Python](https://www.python.org/).

2. **Install the dependencies**:
    - Install the required libraries with:
      ```bash
      pip install -r requirements.txt
      ```

3. **Run the Scripts**:
    - To execute the classification scripts, use:
      ```bash
      python mlp_classification/iris_mlp_classification.py
      python mlp_classification_plus/iris_mlp_classification_plus.py
      ```
    - To execute the search algorithms scripts, use:
      ```bash
      python search_algorithms/atividade_ygor_best_first_search.py
      python search_algorithms/atividade_ygor_bidirectional_search.py
      python search_algorithms/atividade_ygor_breadth_first_search.py
      python search_algorithms/atividade_ygor_depth_first_search.py
      python search_algorithms/atividade_ygor_uniform_cost_search.py
      ```

## 🌐 Deploy

The project can be deployed on any server or development environment that supports Python. There are no specific deployment instructions at this time, but the scripts should work in any properly configured Python environment.
