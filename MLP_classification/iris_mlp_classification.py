from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

# Carrega os dados
iris = load_iris()
X = iris.data  # Características
y = iris.target  # Classes

# Divide em treino e teste (70% treino, 30% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Cria o MLP com 10 neurônios
mlp = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)

# Treina o modelo
mlp.fit(X_train, y_train)

# Faz previsões
y_pred = mlp.predict(X_test)

# Calcula a acurácia
accuracy = accuracy_score(y_test, y_pred)

# Cria um arquivo .txt com a acurácia
with open("accuracy_report.txt", "w") as f:
    f.write(f"Acuracia: {accuracy * 100:.2f}%\n")

# Exibe a acurácia
print(f"Acurácia: {accuracy * 100:.2f}%")
