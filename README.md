[![author](https://img.shields.io/badge/author-felipeferreira-red.svg)](https://www.linkedin.com/in/felipeferreiratids/) [![](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-365/) [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/ferreiramar96/Data_Science)

<p align="center">
  <img src="https://raw.githubusercontent.com/ferreiramar96/Churn-Prediction-Telecomunicacoes/main/notebook/Churn_Prediction_Capa.jpeg" alt="imagem maneira relacionada ao projeto"height=470px >
</p>

## Churn Prediction - Empresa de Telecomunicações
Nesse projeto realizei uma análise sobre os dados de uma empresa de Telecomunicações que oferece vários serviços diferentes. E algo que ocorre muito em empresas de assinatura normalmente é o Churn, que nada mais é que a taxa de cancelamento da assinatura de um cliente, e para a empresa é muito mais barato manter um cliente do que buscar um novo. Então nosso objetivo é criar um modelo de Machine Learning para conseguir detectar se um cliente tende a dar churn ou não, e a partir desta previsão a empresa decide o que deve ser feito para conter este cliente, para este problema será um algoritmo de classificação. A seguir alguns pontos do projeto:
* Análise exploratória para entender os dados
* Algumas visualizações a partir de insights
* Preparação dos dados para aplicar um modelo de IA
* Comparação de vários algoritmos de Machine Learning
* Técnicas avaçadas de Machine Learning
* Avaliação dos resultados e conclusão

Ao longo de todo o projeto, cada célula de código está explicada para uma fácil compreensão, acompanhado de um belo storytelling. Vocês também encontrarão algumas análises estatísticas, boxplots, histogramas, balanceamento de classes, padronização de algumas variáveis, seleção de features, feature engineering, codificação de variáveis e muitos modelos de machine learning.

Neste projeto foi utilizado: Storytelling, Estatística, Machine Learning e a linguagem de programação Python.

## 🛠️ API do Modelo
A inteligência do projeto está exposta através de uma API robusta desenvolvida com **FastAPI**. Esta API é responsável por receber os dados brutos dos clientes, aplicar o pré-processamento e as transformações necessárias em tempo real, e consultar o modelo de Machine Learning (carregado via `joblib`) para retornar a probabilidade de churn.
**Tecnologias utilizadas:** Python, FastAPI, Pandas e Scikit-learn.

## 🖥️ Front-end

<p align="center">
  <img src="https://raw.githubusercontent.com/ferreiramar96/Churn-Prediction-Telecomunicacoes/refs/heads/deploy/notebook/front-end.png" alt="imagem maneira relacionada ao projeto"height=470px >
</p>

Para facilitar a interação com o modelo, foi desenvolvida uma interface dinâmica utilizando **Streamlit**.
- **Coleta de Dados:** O front-end organiza a entrada de informações demográficas, serviços contratados e custos mensais.
- **Conversão de Câmbio:** Como o modelo foi treinado com faturamento em dólares (USD), a aplicação integra a **AwesomeAPI** para buscar a cotação atual do câmbio. Isso permite que o usuário insira valores em Reais (R$), que são convertidos automaticamente antes do processamento pela IA, garantindo a integridade da predição.

## 🚀 Deploy
O projeto foi containerizado e publicado para garantir escalabilidade e facilidade de acesso:
- **Docker:** Utilização de contêineres para isolar a API e o Front-end, assegurando consistência entre os ambientes de desenvolvimento e produção.
- **Render:** Deploy realizado na plataforma Render, utilizando o fluxo de integração contínua para hospedar a solução completa na nuvem.

**Link da aplicação:** [Predição de Churn](https://churn-prediction-telecomunicacoes-vds8.onrender.com/)


[Link para o projeto completo](https://bit.ly/443L5J5)

**Links para me acharem:**
* [Artigo desse projeto no Linkedin](https://www.linkedin.com/posts/felipeferreiratids_datascience-cienciadedados-machinelearning-activity-7096951640322142209-WszZ?utm_source=share&utm_medium=member_desktop)
* [LinkedIn](https://www.linkedin.com/in/felipeferreiratids/)
* [Instagram](https://www.instagram.com/ferreiramar96/)
* [Portfólio Completo](https://github.com/ferreiramar96/Data_Science)

