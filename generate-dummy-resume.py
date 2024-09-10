import pandas as pd
import numpy as np
import datetime

# Configurações
np.random.seed(0)
num_rows = 1000
start_date = datetime.date(2024, 1, 1)
end_date = datetime.date(2024, 2, 1)

# Geração de datas
date_range = pd.date_range(start=start_date, end=end_date, freq='D')
date_samples = np.random.choice(date_range, size=num_rows)

# Converta as datas para o formato ISO
date_samples_iso = [np.datetime64(date) for date in date_samples]

# Dispositivos
devices = ['Ar-condicionado', 'Lâmpadas', 'Computador', 'Geladeira', 'TV', 'Secadora']
device_samples = np.random.choice(devices, size=num_rows)

# Consumo e custo
consumo_samples = np.random.uniform(1, 20, size=num_rows).round(2)
custo_samples = (consumo_samples * np.random.uniform(2, 5, size=num_rows)).round(2)

# Criação do DataFrame
df = pd.DataFrame({
    'Data': date_samples_iso,
    'Dispositivo': device_samples,
    'Consumo (kWh)': consumo_samples,
    'Custo (R$)': custo_samples
})

# Salvamento do arquivo CSV
df.to_csv('dados_consumo_energia.csv', index=False)
