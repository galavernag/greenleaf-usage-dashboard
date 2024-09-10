import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime 
from io import StringIO

sidebar = st.sidebar

sidebar.title('🌱 GreenLeaf - Dashboard de Consumo')
uploaded_consume = sidebar.file_uploader('Envie seu relatório de consumo', "csv", accept_multiple_files=False)

if uploaded_consume is not None:
  dataframe = pd.read_csv(uploaded_consume)
  dataframe['Data'] = pd.to_datetime(dataframe['Data'])
  
  show_dataframe = st.checkbox('Visualizar planilha', value=False)
  
  if show_dataframe is True:
    st.dataframe(dataframe, use_container_width=True)

  chart_data = pd.DataFrame(
    {
      "Tempo (mês)": dataframe['Data'],
      "Consumo (kWh)": dataframe['Consumo (kWh)'],
    }
  )
  
  st.line_chart(chart_data, y='Consumo (kWh)', x='Tempo (mês)')
  