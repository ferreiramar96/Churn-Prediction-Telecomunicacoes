import requests

dados_api = {
  "tenure": 21,
  "MonthlyCharges":59.95,
  "TotalCharges": 1455,
  "gender": "Female",
  "Partner": "No",
  "Contract": "Month-to-month",
  "PaymentMethod": "Electronic check",
  "InternetService": "Fiber optic",
  "PhoneService": "Yes",
  "OnlineSecurity": "No",
  "OnlineBackup": "No",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "No"
}

response = requests.post("http://localhost:8000/predict", json=dados_api)
data = response.json()

print(f"Existe {data['prediction'] * 100:.2f}% de chance de churn")