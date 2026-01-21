import streamlit as st
import requests
import os

# Configuração da página
st.set_page_config(page_title="Predição de Churn - Telecom", page_icon="📊", layout="wide")

# Função para buscar cotação do dólar (AwesomeAPI)
@st.cache_data(ttl=3600)
def get_dolar_quote():
    try:
        response = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
        if response.status_code == 200:
            return float(response.json()["USDBRL"]["bid"])
        return 5.30
    except Exception:
        return 5.30

# Mapeamento de traduções (Português para Inglês (Como o modelo foi treinado))
mapping = {
    "Gênero": {"Feminino": "Female", "Masculino": "Male"},
    "Sim/Não": {"Sim": "Yes", "Não": "No"},
    "Serviços": {"Sim": "Yes", "Não": "No", "Sem serviço de internet": "No internet service"},
    "Internet": {"DSL": "DSL", "Fibra ótica": "Fiber optic", "Não": "No"},
    "Contrato": {"Mês a mês": "Month-to-month", "Um ano": "One year", "Dois anos": "Two year"},
    "Pagamento": {
        "Cheque eletrônico": "Electronic check",
        "Cheque enviado": "Mailed check",
        "Transferência bancária": "Bank transfer (automatic)",
        "Cartão de crédito": "Credit card (automatic)"
    }
}

# URL da API do nosso modelo
api_url = os.getenv("API_URL", "http://localhost:8000/predict")

# Cabeçalho Principal com Cotação no canto superior direito
header_col1, header_col2 = st.columns([4, 1])

with header_col1:
    st.title("📊 Predição de Churn de Clientes")

with header_col2:
    dolar_atual = get_dolar_quote()
    st.metric(
        label="Câmbio (USD/BRL)", 
        value=f"R$ {dolar_atual:.2f}",
        help="Este valor é utilizado para converter os preços inseridos em Reais para Dólares antes do envio à API. Isso é necessário porque o modelo de IA foi treinado originalmente com dados de uma empresa americana (em dólar)."
    )

st.markdown("""
Esta aplicação utiliza um modelo de Machine Learning para prever a probabilidade de um cliente cancelar os serviços (Churn) de uma empresa de telecomunicações.
Preencha todos os dados abaixo para obter a análise.
""")

st.divider()

# Organizando o formulário em colunas
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Informações Pessoais")
    gender = st.selectbox("Gênero", ["Selecione...", "Feminino", "Masculino"], index=0)
    partner = st.selectbox("Possui Parceiro(a)?", ["Selecione...", "Sim", "Não"], index=0)
    tenure = st.number_input("Meses de Contrato (Tenure)", min_value=0, max_value=100, value=0)

with col2:
    st.subheader("Serviços Contratados")
    internet_service = st.selectbox("Serviço de Internet", ["Selecione...", "DSL", "Fibra ótica", "Não"], index=0)
    contract = st.selectbox("Tipo de Contrato", ["Selecione...", "Mês a mês", "Um ano", "Dois anos"], index=0)
    payment_method = st.selectbox("Método de Pagamento", ["Selecione...", "Cheque eletrônico", "Cheque enviado", "Transferência bancária", "Cartão de crédito"], index=0)
    phone_service = st.selectbox("Serviço de Telefonia", ["Selecione...", "Sim", "Não"], index=0)

with col3:
    st.subheader("Custos (R$)")
    monthly_charges = st.number_input("Valor Mensal (R$)", min_value=0.0, value=0.0)
    total_charges = st.number_input("Custo Total Acumulado (R$)", min_value=0.0, value=0.0)

st.divider()

st.subheader("Serviços Adicionais")
c1, c2, c3, c4 = st.columns(4)
with c1:
    online_security = st.selectbox("Segurança Online", ["Selecione...", "Sim", "Não", "Sem serviço de internet"], index=0)
with c2:
    online_backup = st.selectbox("Backup Online", ["Selecione...", "Sim", "Não", "Sem serviço de internet"], index=0)
with c3:
    device_protection = st.selectbox("Proteção de Dispositivo", ["Selecione...", "Sim", "Não", "Sem serviço de internet"], index=0)
with c4:
    tech_support = st.selectbox("Suporte Técnico", ["Selecione...", "Sim", "Não", "Sem serviço de internet"], index=0)

c5, c6 = st.columns(2)
with c5:
    streaming_tv = st.selectbox("Streaming TV", ["Selecione...", "Sim", "Não", "Sem serviço de internet"], index=0)
with c6:
    streaming_movies = st.selectbox("Streaming Movies", ["Selecione...", "Sim", "Não", "Sem serviço de internet"], index=0)

# Verificação de campos preenchidos
campos_obrigatorios = [gender, partner, internet_service, contract, payment_method, phone_service, online_security, online_backup, device_protection, tech_support, streaming_tv, streaming_movies]

todos_preenchidos = all(campo != "Selecione..." for campo in campos_obrigatorios) and monthly_charges > 0 and total_charges > 0

if not todos_preenchidos:
    st.warning("⚠️ A predição não será tão boa pois ainda há campos não preenchidos ou valores zerados.")

# Botão de Predição
if st.button("🚀 Calcular Probabilidade de Churn", use_container_width=True):
    if not todos_preenchidos:
        st.error("Por favor, preencha todos os campos antes de realizar a predição.")
    else:
        # Preparando os dados para API
        payload = {
            "tenure": int(tenure),
            "MonthlyCharges": float(monthly_charges) / dolar_atual,
            "TotalCharges": float(total_charges) / dolar_atual,
            "gender": mapping["Gênero"][gender],
            "Partner": mapping["Sim/Não"][partner],
            "Contract": mapping["Contrato"][contract],
            "PaymentMethod": mapping["Pagamento"][payment_method],
            "InternetService": mapping["Internet"][internet_service],
            "PhoneService": mapping["Sim/Não"][phone_service],
            "OnlineSecurity": mapping["Serviços"][online_security],
            "OnlineBackup": mapping["Serviços"][online_backup],
            "DeviceProtection": mapping["Serviços"][device_protection],
            "TechSupport": mapping["Serviços"][tech_support],
            "StreamingTV": mapping["Serviços"][streaming_tv],
            "StreamingMovies": mapping["Serviços"][streaming_movies]
        }

        try:
            with st.spinner('Consultando o cérebro da IA...'):
                response = requests.post(api_url, json=payload)
                
                if response.status_code == 200:
                    result = response.json()
                    probabilidade = result["prediction"]
                    
                    # Exibição do resultado
                    st.divider()
                    st.subheader("Resultado da Análise")
                    
                    if probabilidade > 0.6:
                        st.error(f"⚠️ **Risco Alto de Churn!** Probabilidade: {probabilidade:.2%}")
                    elif probabilidade > 0.3:
                        st.warning(f"🟡 **Risco Moderado.** Probabilidade: {probabilidade:.2%}")
                    else:
                        st.success(f"✅ **Baixo Risco.** Probabilidade: {probabilidade:.2%}")
                    
                    st.progress(probabilidade)
                else:
                    st.error(f"Erro na API: {response.status_code} - {response.text}")
                    
        except Exception as e:
            st.error(f"Erro ao conectar com a API: {e}")