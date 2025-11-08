# BIAnalyst

Olist es una plataforma que ofrece soluciones para la gestión y crecimiento de negocios en línea.

El dataset utilizado en este proyecto Brazilian E-Commerce Public Dataset by Olist 
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce?select=olist_customers_dataset.csv 
## Power BI
-Modelado de datos

-GMV (ingresos brutos) por mes
Pasos:
1. Abrir power query
2. Selecconar la tabla orders y validar que la columna order_purchase_timestamp sea tipo fecha (cambiarlo si es texto)
3. Ir a Agregar columna → Columna personalizada y usar esta formula: Date.ToText([order_purchase_timestamp], "yyyy-MM") para creaar una nueva colmna en la tabla
4. Se renombra la nueva columna como Year_month
5. Ir a Inicio → Combinar consultas → Combinar consultas como nuevas
6. Seleccionar orders como tabla principal, order_payments como tabla secundaria, relacion order_id en ambas, tipo de combinacion interna y despues Aceptar
7. Se expande la columna combinada para incluir solo payment_value y se renombra la nueva tabla como orders_payments


-Nº de órdenes por mes.
Contar cuantas ordenes (order_id) se realizaron en cada mes usando la columna Year_month que se genero

-Tiempo promedio de entrega 
Pasos:
1. Selecciona la tabla orders y verificar que las columnas (order_purchase_timestamp, order_delivered_customer_date) esten en formato Fecha
2. Ir a Agregar columna → Columna personalizada y escribir esta formula: Duration.Days([order_delivered_customer_date] - [order_purchase_timestamp])
3. Validar que la nueva columna este en formato de Numero entero y renombrarla a "dias_entrega"


-Ordenes canceladas por mes
Pasos:
1. En PowerQuery seleccionar la tabla ooders
2. Ir a Agregar ccolumna → Columna personalizada y escribir esta formula: if [order_status] = "canceled" then 1 else 0
3. Renombrar la columna como esta_cancelada y verificar que este en tipo de dato entero
4. Commbinar el resultado  con order_payments como tabla secundaria, relacion order_id, tipo de combinacion interna y aceptar
5. Expandir solo payment_value y renombrar la tabla combinada como items_with_category_and_payment
6. Verificar que pdocut_category_name sea tipo texto y payment_value sea tipo decimal


-Categorías por GMV y su contribución 
Pasos:
1. Ir a Combinar consultas → Combinar como nuevas
2. Seleccionar order_item como tabla principal, products como secundaria,   relacion product_id , tipo de combinacion interna y aceptar
3. Expande solo "product_category_name"


### SQL
- Herrammientas utilizadas: PostgreSQL , pgAdmin

### Python
-Herramientas utilizadas: Spyder IDE , Python 3.13 ( Pandas)
