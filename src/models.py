from pydantic import BaseModel

# Classe para validar os dados que chegam na API
class inputValidation(BaseModel):

    #Variaveis Numericas
    tenure: int
    MonthlyCharges: float
    TotalCharges: float

    #Variaveis Categoricas 
    gender:str
    Partner:str
    Contract:str
    PaymentMethod:str
    InternetService:str

    #Variaveis para gerar o "Engajamento
    PhoneService:str
    OnlineSecurity:str
    OnlineBackup:str
    DeviceProtection:str
    TechSupport:str
    StreamingTV:str
    StreamingMovies:str