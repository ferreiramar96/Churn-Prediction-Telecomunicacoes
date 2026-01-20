# --- TESTE DA API (Simulando entrada em Português) ---
dados_api = {
    "gender": "Feminino",
    "Partner": "Sim",
    "tenure": 1,
    "MonthlyCharges": 29.85,
    "TotalCharges": 29.85,
    "Contract": "Month-to-month", # Se vier traduzido tipo "Mensal", precisa mapear também
    "PaymentMethod": "Electronic check",
    "InternetService": "DSL",
    "PhoneService": "Não",
    "OnlineSecurity": "Não",
    "OnlineBackup": "Sim",
    "DeviceProtection": "Não",
    "TechSupport": "Não",
    "StreamingTV": "Não",
    "StreamingMovies": "Não"
}

entrada = pd.DataFrame([dados_api])
pred = pipeline.predict(entrada)
prob = pipeline.predict_proba(entrada)

print(f"Predição: {'Churn' if pred[0] == 1 else 'Fica'}")
print(f"Confiança: {prob[0][1]*100:.2f}%")