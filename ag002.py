"""
Guilherme Muniz de Oliveira Reis - 127 - GES
Raissa Beatriz Carlucio - 1825 - GEC
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.metrics import classification_report

from utils import Utils

# Lendo o arquivo:
df = pd.read_csv('palmerpenguins.csv')

# 3 --------------------
mapping = {
    'island': {'Biscoe': 0, 'Dream': 1, 'Torgersen': 2},
    'sex': {'FEMALE': 0, 'MALE': 1},
    'species': {'Adelie': 0, 'Chinstrap': 1, 'Gentoo': 2}
}

# Converter os valores de acordo com o mapeamento
df.replace(mapping, inplace=True)
print(df)
print()

# 4 --------------
df = df.reindex(columns=['island', 'sex', 'culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g', 'species'])
print(df)
print()

# 5 ------------
X = df.drop(columns=['species']) 
y = df['species']  

# Separando os dados em conjuntos de treinamento e teste (80% para treinamento e 20% para teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Mostrando o tamanho dos conjuntos de treinamento e teste
print("Tamanho do conjunto de treinamento:", len(X_train))
print("Tamanho do conjunto de teste:", len(X_test))

# 6 - Decision Tree Classifier
model = DecisionTreeClassifier()

# 7 -----------
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# 8 ------------
# Avaliar a precisão do modelo
accuracy = metrics.accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print(classification_report(y_test, y_pred))

# 9 ------------
flag = True
while True:
    print("\nDeseja entrar com um novo penguim (1 - Sim, 2 - Não): \n")
    ch = int(input())
    
    if ch == 1:
        Utils.new_penguin(model, mapping)
    else:
        break