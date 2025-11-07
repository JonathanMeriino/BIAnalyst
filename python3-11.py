"""Con payments.csv, calcula la distribución de payment_type y el ticket promedio por método de pago."""


import pandas as pd 

df0_payments = pd.read_csv("CSV Files/olist_order_payments_dataset.csv")

df0_payments.info()

#Contar la frecuencia de cada metodo de pago

conteo_pagos = df0_payments['payment_type'].value_counts()

# calcular el total de transacciones
total_transacciones = conteo_pagos.sum()

#Calcular la proporcion de cada metodo de pago
distribucion_pagos = (conteo_pagos/total_transacciones)*100

"""Ticket promedio por metodo de pago"""

# Agrupar por 'payment_type' y calcular el valor promedio del pago
ticket_promedio = df0_payments.groupby('payment_type')['payment_value'].mean().reset_index()

# Renombrar la columna del resultado
ticket_promedio = ticket_promedio.rename(columns={'payment_value': 'Ticket_Promedio'})

# Redondear a dos decimales para formato de moneda
ticket_promedio['Ticket_Promedio'] = ticket_promedio['Ticket_Promedio'].round(2)

print("\n💰 Ticket Promedio por Método de Pago:")
print(ticket_promedio)