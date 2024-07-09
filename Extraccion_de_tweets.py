import pandas as pd
import tweepy
import time

# Configuración de la API de Twitter (asegúrate de tener tus propias claves)
api_key = "t1TmTGZfCfebvaseP7Wz4yUP3"
api_secret_key = "KNZ6KfPRvGzQsEQ5JF4JRF91orVCx8rasCbTBlQjhPYDBIaxBl"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAHX5ugEAAAAAO%2B6Tbx1WdlxdeOjz3rPiE%2BuZTaQ%3DibH5C0VfuLxMs8mGfULfzVR6SsRZH0zHeVEunNnHkGYnE9F1H3"

# Autenticación con la API de Twitter
client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

# Léxico de palabras clave refinado y ampliado
lexicon_optimizado = [
    "asilo", "refugio", "inmigrante", "deportación", "residencia", "permiso",
    "miedo", "esperanza", "tristeza", "alegría", "frustración", "alivio", "ansiedad", "gratitud",
    "cruce", "frontera", "travesía", "ruta", "caravana", "coyotes", "rutas peligrosas",
    "violencia", "detención", "extorsión", "discriminación", "inseguridad", "peligro",
    "familia", "hijos", "separación", "comunidad", "apoyo", "solidaridad",
    "albergue", "comida", "salud", "educación", "trabajo", "ayuda", "recursos",
    "México", "Estados Unidos", "Guatemala", "Tijuana", "Tapachula", "frontera norte", "frontera sur",
    "buscando una vida mejor", "huyendo de la violencia", "cruzar la frontera", "en busca de asilo"
]

# Función para buscar tweets usando el léxico
def search_tweets(lexicon, num_tweets_per_keyword=15):
    tweets_data = []
    for word in lexicon:
        query = f"{word} lang:es -is:retweet"
        for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, tweet_fields=['created_at', 'text', 'author_id'], max_results=num_tweets_per_keyword).flatten(limit=num_tweets_per_keyword):
            tweets_data.append({
                'keyword': word,
                'created_at': tweet.created_at,
                'user_id': tweet.author_id,
                'text': tweet.text
            })
        print(f"Extracted {num_tweets_per_keyword} tweets for keyword: {word}")
        time.sleep(900)  # Esperar 15 minutos (900 segundos) antes de la siguiente búsqueda
    return tweets_data

# Buscar tweets
tweets_data = search_tweets(lexicon_optimizado, num_tweets_per_keyword=15)

# Convertir los datos a un DataFrame de pandas
df_tweets = pd.DataFrame(tweets_data)

# Guardar los tweets en un archivo CSV
df_tweets.to_csv('tweets_migracion.csv', index=False, encoding='utf-8-sig')

# Mostrar algunos ejemplos de tweets encontrados
print(df_tweets.head(10))
    

    # 1. Incorporar Términos Contextuales y Coloquiales: 
    # Los migrantes pueden usar términos y jerga específicos que son relevantes en su contexto. Incluir palabras coloquiales y frases comunes en el habla de los migrantes puede ayudar a mejorar la precisión del algoritmo.

    #2. Análisis de Frecuencia de Palabras en Tweets Reales: 
        # Analiza un conjunto representativo de tweets sobre migrantes para identificar términos que se utilizan con frecuencia y que podrían no estar en el léxico original. Esto puede hacerse mediante un análisis exploratorio de datos.

    #3. Feedback y Ajustes Iterativos:
        # Implementa un ciclo de feedback donde el algoritmo se ajuste y mejore continuamente basado en los resultados obtenidos. Revisa manualmente los tweets clasificados para refinar el léxico y mejorar la precisión.

    #4. Considerar Variaciones Lingüísticas y Regionales:
        # Incluye variaciones de palabras y frases que pueden ser utilizadas en diferentes regiones y dialectos.

    #5. Palabras y Frases Negativas/Positivas:
        # Asegúrate de incluir tanto palabras con connotaciones positivas como negativas para capturar la gama completa de percepciones y emociones.

#Refinamiento del Léxico
# Aquí hay un léxico refinado y ampliado:

#1. Palabras relacionadas con el estatus migratorio:

    #Asilo, refugio, inmigrante, migrante, exiliado, desplazado, documentos, visa, deportación, regularización, residencia, permisos, solicitud de asilo.
        # 2. Palabras relacionadas con emociones y sentimientos:

    #Miedo, esperanza, tristeza, alegría, desesperación, frustración, nostalgia, alivio, ansiedad, angustia, preocupación, optimismo, incertidumbre, gratitud.
        # 3. Palabras relacionadas con el viaje y tránsito:

    #Cruce, frontera, travesía, camino, trayecto, ruta, viaje, desierto, mar, caravana, paso, frontera, coyotes, rutas peligrosas.
        # 4. Palabras relacionadas con condiciones y experiencias:

    #Violencia, persecución, abuso, detención, secuestro, extorsión, discriminación, xenofobia, racismo, protección, inseguridad, amenazas, peligro.
        # 5. Palabras relacionadas con la familia y relaciones personales:

    #Familia, hijos, padres, reunificación, separación, reencuentro, amigo, compañero, comunidad, apoyo, seres queridos, solidaridad, redes de apoyo.
        # 6. Palabras relacionadas con servicios y necesidades:

    #Albergue, refugio, comida, salud, educación, trabajo, empleo, asistencia, ayuda, recursos, apoyo humanitario, servicios médicos, atención psicológica.
        # 7. Palabras relacionadas con lugares y destinos:

    #México, Estados Unidos, Guatemala, Honduras, El Salvador, Tijuana, Tapachula, Chiapas, frontera norte, frontera sur, albergues en México, rutas migratorias, estaciones migratorias.
        # 8. Palabras y frases contextuales y coloquiales:

    #Frases comunes: "buscando una vida mejor", "huyendo de la violencia", "cruzar la frontera", "en busca de asilo", "esperando la respuesta", "temor a la deportación", "esperanza de un futuro mejor".