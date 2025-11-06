#Importar bibliotecas

import pandas as pd
from datetime import datetime
#Cargar archivos

df0_orders = pd.read_csv('CSV Files/olist_orders_dataset.csv')
df0_orders_items = pd.read_csv('CSV Files/olist_order_items_dataset.csv')

#Analisis exploratorio df0_orders
print("----- ORDERS -----\n")
print(df0_orders.columns)
print(df0_orders.info())
print(df0_orders.shape)
#Analisis exploratorio df0_orders_items
print("----- ORDERS ITEMS-----\n")
print(df0_orders_items.columns)
print(df0_orders_items.info())
print(df0_orders_items.shape)


#Formato de fecha para Order Items
df0_orders_items['shipping_limit_date'] = pd.to_datetime(df0_orders_items['shipping_limit_date'])
df0_orders_items['Año_Mes_Envio'] = df0_orders_items['shipping_limit_date'].dt.strftime('%Y-%m')

df0_orders_items['Año_Envio'] =df0_orders_items['shipping_limit_date'].dt.year
df0_orders_items['Mes_Envio'] =df0_orders_items['shipping_limit_date'].dt.month

#Calcular GMV oir orden y mes

df0_orders_items['GMV'] = 0

for i in df0_orders_items.columns:
    print(i)


