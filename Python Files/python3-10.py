"""
Dado reviews.csv, calcula la proporción de reseñas positivas (review_score ≥ 4) por mes.
"""
import pandas as pd

df0_reviews = pd.read_csv('CSV Files/olist_order_reviews_dataset.csv')
df0_reviews.info()

# Convertir la columna de creación de la reseña a datetime
df0_reviews['review_creation_date'] = pd.to_datetime(df0_reviews['review_creation_date'])


# Extraer el Año y Mes de la creación de la reseña
df0_reviews['Año_Mes_Review'] = df0_reviews['review_creation_date'].dt.strftime('%Y-%m')


# Clasificar la reseña como positiva (1) si la puntuación es 4 o 5, y 0 en caso contrario.
df0_reviews['es_positiva'] = df0_reviews['review_score'].apply(lambda x: 1 if x >= 4 else 0)

# Agrupar por mes y calcular el número total de reseñas y el número de reseñas positivas
resumen_mensual = df0_reviews.groupby('Año_Mes_Review').agg(
    Total_Reviews=('review_id', 'count'),
    Total_Positivas=('es_positiva', 'sum')
).reset_index()

# Calcular la proporción: (Total de Positivas / Total de Reseñas)
resumen_mensual['Proporcion_Positiva'] = (
    resumen_mensual['Total_Positivas'] / resumen_mensual['Total_Reviews']
)

print("Proporción de Reseñas Positivas por Mes:", resumen_mensual.head(10), sep="\n")