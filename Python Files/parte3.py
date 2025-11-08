#Importar bibliotecas

import pandas as pd
#Cargar archivos

df0_orders = pd.read_csv('CSV Files/olist_orders_dataset.csv')
df0_orders_items = pd.read_csv('CSV Files/olist_order_items_dataset.csv')

# Unir orders con orders_items

df0 = pd.merge(
    left = df0_orders,  #Dataframe principal
    right=df0_orders_items,  #Dataframe que se quiere agregar 
    on = 'order_id',  # La columna clave que comparten
    how = 'left')   #EL tipo de union

df0.info()
#Se eliminan todas las columnas que no seran utilizadas
df1 = df0.drop(columns = ['customer_id','order_status','order_approved_at','order_delivered_carrier_date','order_estimated_delivery_date','order_item_id','product_id','seller_id'])

df1.info()

#Formato de fecha

#Definir la lista de columnas que tienen una marca de tiempo
columnas_convertir = ["order_purchase_timestamp","order_delivered_customer_date","shipping_limit_date",]

#Iterar y aplicar la conversion directamente al dataframe
for col in columnas_convertir:
    df1[col]=pd.to_datetime(df1[col])

df1.info()
 
""" Calcula GMV mensual """

#Crea una columna cn el valor total por item
df1["valor_total_item"] = df1["price"] + df1["freight_value"]

#Calcular el GMV total de la orden y lo asigna a todas las filas de esa orden
df1["GMV_orden"]= df1.groupby('order_id')['valor_total_item'].transform('sum')
#Se utiliza 'transform' para repetir el total de la orden en cada fila del item


df1['Año_Mes_Compra'] = df1['order_purchase_timestamp'].dt.strftime('%Y-%m')

#Crea el dataframe de ordenes unicas(df2)

df2 = df1[['order_id','Año_Mes_Compra','GMV_orden']].drop_duplicates(subset=['order_id'])

#Eliminar filas cuyo valor de GMV sea cero
df2 = df2[df2['GMV_orden']>0]

#Agrupar el GMV por la columna de tiempo y sumar el total
gmv_mensual = df2.groupby('Año_Mes_Compra')['GMV_orden'].sum().reset_index()

#Renombrar la columna del resultado final
gmv_mensual = gmv_mensual.rename(columns={'GMV_orden': 'GMV_Mensual_Total'})

#Mostrar resultados

print("GMV Total Mensual",gmv_mensual.head(10),sep="\n")


