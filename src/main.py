from models import inputValidation
from fastapi import FastAPI
import pandas as pd
import joblib
import os
import __main__

# Função necessária para reconstruir o pipeline salvo pelo joblib
def transformacoes_api(df):
    df = df.copy()

    mapa = {'Yes': 1, 'No': 0} 
    servicos = ['PhoneService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV','StreamingMovies']
    
    for col in servicos:
        if col in df.columns:
            df[f"{col}_temp"] = df[col].map(mapa).fillna(0)

    df["Engajamento"] = df[[f"{c}_temp" for c in servicos if f"{c}_temp" in df.columns]].sum(axis=1)
    df["InteracaoCharges"] = (pd.to_numeric(df["MonthlyCharges"]) * pd.to_numeric(df["TotalCharges"]))

    cols_to_drop = [f"{c}_temp" for c in servicos if f"{c}_temp" in df.columns]
    return df.drop(columns=cols_to_drop)

# Necessário porque o modelo (função transformacoes_api) foi salvo no Notebook (onde a função fica no __main__)
__main__.transformacoes_api = transformacoes_api

# Carregando o modelo e pegando o caminho do modelo
path_model = os.path.join(os.path.dirname(__file__), "..", "models", "churn_pipeline.joblib")
model = joblib.load(path_model)

app = FastAPI()

# Endpoint para verificar se a API está funcionando
@app.get("/health")
def health():
    return {"status":"ok"}

# Endpoint para fazer previsões
@app.post("/predict")
def predict(data: inputValidation):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict_proba(df)
    return {"prediction": prediction[0][1]}