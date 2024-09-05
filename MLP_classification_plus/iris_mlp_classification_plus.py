import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data  # Características
y = iris.target  # Classes

# Divide em treino (70%) e teste (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Inicializa os classificadores
classifiers = {
    "KNN": KNeighborsClassifier(),
    "C4.5 (Decision Tree)": DecisionTreeClassifier(random_state=42),
    "SVM": SVC(),
    "MLP": MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)
}

# Treina e avalia cada classificador
accuracies = {}
for name, clf in classifiers.items():
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracies[name] = accuracy_score(y_test, y_pred)

# Salva os resultados em um arquivo .txt
with open("classification_analysis.txt", "w") as f:
    f.write("Comparacao de Algoritmos para Classificacao do Iris Dataset\n\n")
    for name, acc in accuracies.items():
        f.write(f"{name}: Acuracia = {acc * 100:.2f}%\n")

# Exibe a acurácia de cada modelo
for name, acc in accuracies.items():
    print(f"{name}: Acuracia = {acc * 100:.2f}%")
