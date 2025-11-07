# Desafio Técnico: Otimizando Algoritmos de Classificação para Previsão de Evasão (Churn)

## Solução Implementada

# Este notebook contém a solução completa para o Desafio Técnico, seguindo as 7 etapas
# da metodologia de projetos de Ciência de Dados, conforme abordado no eBook. O algoritmo
# escolhido para a classificação é o Random Forest Classifier, e a métrica priorizada na
# otimização é o Recall.

### Bibliotecas Necessárias

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import recall_score, precision_score, accuracy_score, f1_score, confusion_matrix
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib 
import warnings
warnings.filterwarnings('ignore')

### 1. Definição do Problema/Objetivos (Observatório de Dados)

# Objetivo: O problema de **Churn** refere-se à evasão ou cancelamento de serviços por parte dos clientes
# de uma empresa de telecomunicações. O objetivo principal deste projeto é desenvolver um modelo de
# Machine Learning que consiga **identificar proativamente** clientes com alta probabilidade de Churn.
# A meta é permitir que a equipe de retenção intervenha com ofertas ou soluções, **minimizando a perda de
# receita** e maximizando o valor de vida útil do cliente (LTV).

# ---

### 2. Coleta e Entendimento dos Dados (Bases Alvos)

# --- AÇÃO: Carregar a Base de Dados ---
# ATENÇÃO: Substitua 'seu_arquivo_churn.csv' pelo nome do seu arquivo de dados Telco Churn.
try:
    df = pd.read_csv('seu_arquivo_churn.csv')
    print(f"Dados carregados com sucesso. Linhas: {df.shape[0]}, Colunas: {df.shape[1]}")
except FileNotFoundError:
    print("ERRO: Arquivo 'seu_arquivo_churn.csv' não encontrado. Simulação de DataFrame para lógica do código.")
    # Estrutura simulada para fins de demonstração da lógica. Substitua pelos seus dados reais!
    data = {
        'gender': ['Female', 'Male', 'Male', 'Female', 'Male'],
        'SeniorCitizen': [0, 1, 0, 0, 1],
        'Partner': ['Yes', 'No', 'No', 'No', 'Yes'],
        'Dependents': ['No', 'No', 'No', 'No', 'No'],
        'tenure': [1, 34, 2, 45, 10],
        'PhoneService': ['No', 'Yes', 'Yes', 'No', 'Yes'],
        'MultipleLines': ['No phone service', 'No', 'No', 'No phone service', 'Yes'],
        'InternetService': ['DSL', 'DSL', 'Fiber optic', 'DSL', 'Fiber optic'],
        'Contract': ['Month-to-month', 'One year', 'Month-to-month', 'One year', 'Month-to-month'],
        'MonthlyCharges': [29.85, 56.95, 80.00, 42.30, 100.00],
        'TotalCharges': [29.85, 1889.5, 160.00, 1840.75, 1000.00],
        'Churn': ['No', 'No', 'Yes', 'No', 'Yes'] 
    }
    df = pd.DataFrame(data)

# Tratamento de Nulos e Erros (Comum em TotalCharges)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(inplace=True)

# Definição das variáveis preditoras (X) e alvo (y)
X = df.drop('Churn', axis=1)
y = df['Churn'].map({'Yes': 1, 'No': 0}) 

# Divisão Treino/Teste (Estratificada)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
print(f"Shape de Treino: {X_train.shape}, Shape de Teste: {X_test.shape}")


# ---

### 3. Tratamento/Preparação dos Dados (Pré-Processamento)

# **Justificativa Algorítmica:** O **One-Hot Encoding** é usado para transformar variáveis categóricas
# em colunas binárias, evitando que o modelo interprete categorias como tendo uma ordem. O **StandardScaler**
# é aplicado às colunas numéricas para equalizar as suas escalas, impedindo que features com grandes
# magnitudes (ex: 'TotalCharges') dominem o treinamento.

# Identificação das colunas
categorical_features = X.select_dtypes(include=['object']).columns
numerical_features = X.select_dtypes(include=['int64', 'float64']).columns

# Criação do Pré-Processador (Pipeline de Transformação)
preprocessor = ColumnTransformer(
    transformers=[
        # 1. One-Hot Encoding: Para variáveis categóricas
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_features),
        # 2. Standard Scaler: Para variáveis numéricas
        ('scaler', StandardScaler(), numerical_features)
    ],
    remainder='passthrough'
)

# Aplicação do pré-processamento
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

print("Pré-processamento aplicado com sucesso.")

# ---

### 4. Análise Exploratória (Mineração)

# Análise Simples da Proporção de Churn
churn_rate = y.mean() * 100
print(f"\nTaxa de Churn na base de dados (1 - Evasão): {churn_rate:.2f}%")

# Análise de uma Feature
print("\nContagem de Clientes por Tipo de Contrato:")
print(df['Contract'].value_counts())

# ---

### 5. Modelagem do Algoritmo (Mineração)

# **Justificativa Algorítmica:** O **Random Forest Classifier** foi escolhido por ser um algoritmo *ensemble*
# (baseado em múltiplas árvores de decisão). Isso garante alta precisão e robustez, pois o resultado final
# é o voto majoritário de centenas de árvores, o que o torna menos propenso ao *overfitting*.

# Inicialização e Treinamento do Modelo Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced') 

# Treinamento
model.fit(X_train_processed, y_train)

# Previsões
y_pred = model.predict(X_test_processed)

# ---

### 6. Análise dos Resultados e Otimização do Modelo (tuning)

#### Avaliação das Métricas (Teste)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\n--- Resultados do Modelo (Teste) ---")
print(f"Acurácia: {accuracy:.4f}")
print(f"Precisão: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")
print("\nMatriz de Confusão (Real vs Previsto):\n", confusion_matrix(y_test, y_pred))

#### a) Métrica Lógica: Priorização do Recall

# **Priorizamos o Recall.** No problema de Churn, o objetivo é a retenção. O maior custo de negócio
# é um cliente em risco (positivo real) ser classificado como não-risco (**Falso Negativo - FN**).
# Um alto *Recall* garante que a equipe de retenção receba a maior quantidade possível de
# clientes de alto risco para intervenção, minimizando a perda de clientes.

#### b) Otimização (Tuning): Validação Cruzada (Cross-Validation)

# **Lógica Algorítmica:** A **Validação Cruzada (K-Fold)** divide o conjunto de treinamento em `K` fatias.
# O modelo é treinado `K` vezes, sendo que a cada vez uma fatia diferente é usada para validação
# e as `K-1` restantes para treinamento. A performance final é a média dos `K` resultados.
# Isso torna a avaliação mais **robusta**, pois o desempenho do modelo não depende de uma única
# divisão aleatória de treino/teste, e ajuda a mitigar o *overfitting*.

# Ação: Implementar Cross-Validation
cv = KFold(n_splits=5, shuffle=True, random_state=42) # 5 Folds
recall_scores = cross_val_score(model, X_train_processed, y_train, cv=cv, scoring='recall')

print("\n--- Otimização com Cross-Validation (5 Folds) ---")
print(f"Scores de Recall por Fold: {recall_scores}")
print(f"Recall Médio CV (Otimizado): {recall_scores.mean():.4f}")

# Salvamento do modelo e pré-processador para a próxima etapa (Deploy)
joblib.dump(preprocessor, 'churn_preprocessor.pkl')
joblib.dump(model, 'churn_model.pkl')


# ---

### 7. Deploy (Simulado)

# **Justificativa Prática:** A função simula o ambiente de produção. É crucial que ela aplique
# **exatamente as mesmas transformações** (encodings e escalonamento) que o modelo viu durante
# o treinamento (usando `loaded_preprocessor.transform`), garantindo que os dados de entrada
# estejam no formato correto para a previsão.

def prever_novo_cliente(dados_cliente: dict):
    """
    Recebe um dicionário com as features de um novo cliente, aplica o pré-processamento
    e retorna a probabilidade de Churn e a decisão final.
    """
    # 1. Carregar o modelo e o pré-processador
    try:
        loaded_model = joblib.load('churn_model.pkl')
        loaded_preprocessor = joblib.load('churn_preprocessor.pkl')
    except FileNotFoundError:
        return {"ERRO": "Modelo ou pré-processador não encontrados. Execute a etapa 6 primeiro."}

    # 2. Converter o dicionário em DataFrame (formato esperado pelo pré-processador)
    new_client_df = pd.DataFrame([dados_cliente])

    # 3. Aplicar o Pré-Processamento (transformação)
    processed_client = loaded_preprocessor.transform(new_client_df)

    # 4. Previsão
    probability_churn = loaded_model.predict_proba(processed_client)[:, 1][0]
    decision = loaded_model.predict(processed_client
