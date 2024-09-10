# GreenLeaf - Dashboard de uso energético
![image](https://github.com/user-attachments/assets/5771cb20-24de-49c8-ad14-df97237f8b65)

## Descrição

Este projeto é uma aplicação web interativa desenvolvida com [Streamlit](https://streamlit.io/) e [Python](https://www.python.org/) para analisar o consumo de energia de dispositivos em pequenas e médias empresas. A aplicação permite o upload de dados de consumo energético e visualiza gráficos históricos.

## Funcionalidades

- **Upload de Dados:** Permite o upload de arquivos CSV contendo dados de consumo de energia.
- **Visualização de Dados:** Exibe gráficos interativos mostrando o consumo de energia ao longo do tempo.

## Pré-requisitos

Certifique-se de ter o Python 3.8 ou superior instalado. Você também precisará instalar as seguintes bibliotecas:

- Streamlit
- Pandas
- NumPy

Você pode instalar essas dependências usando o seguinte comando:

```bash
pip install streamlit pandas numpy  
```

## Como Executar o Projeto

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/galavernag/greenleaf-usage-dashboard.git
   cd greenleaf-usage-dashboard
   ```

2. **Gerar Dados Fictícios:**
   
   Execute o script `generate-dummy-resume.py` para criar um arquivo CSV com dados fictícios para teste:

   ```bash
   python generate-dummy-resume.py
   ```

3. **Executar a Aplicação:**
   
   Inicie a aplicação Streamlit com o seguinte comando:

   ```bash
   streamlit run app.py
   ```

   A aplicação será executada em `http://localhost:8501`.

## Estrutura do Projeto

- `app.py`: Código principal da aplicação Streamlit.
- `generate_data.py`: Script para gerar dados fictícios em formato CSV.
- `dados_consumo_energia.csv`: Arquivo de dados de exemplo gerado pelo script `generate_data.py`.

## Exemplos de Dados

O arquivo `dados_consumo_energia.csv` contém colunas com as seguintes informações:

- **Data:** Data do registro no formato ISO (YYYY-MM-DD).
- **Dispositivo:** Nome do dispositivo (e.g., Ar-condicionado, Lâmpadas).
- **Consumo (kWh):** Quantidade de energia consumida em quilowatt-hora.
- **Custo (R$):** Custo associado ao consumo de energia em reais.

## Contribuição

Sinta-se à vontade para contribuir com melhorias e correções. Para isso, faça um fork do repositório, crie uma branch para sua feature ou correção, e envie um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
