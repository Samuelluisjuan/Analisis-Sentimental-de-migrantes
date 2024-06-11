import pandas as pd
import tweepy 

# Configuración de la API de Twitter (asegúrate de tener tus propias claves)
# Estas claves se obtienen al crear una aplicación en el portal de desarrolladores de Twitter
api_key = "TU_API_KEY"
api_secret_key = "TU_API_SECRET_KEY"
access_token = "TU_ACCESS_TOKEN"
access_token_secret = "TU_ACCESS_TOKEN_SECRET"

# Autenticación con la API de Twitter
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Léxico de palabras clave refinado y ampliado
# Este léxico contiene palabras y frases comunes en tweets sobre migrantes,
# incluyendo términos relacionados con estatus migratorio, emociones, condiciones del viaje, y más.
lexicon = [
    "asilo", "refugio", "inmigrante", "migrante", "exiliado", "desplazado", 
    "documentos", "visa", "deportación", "regularización", "residencia", 
    "permiso", "solicitud de asilo", "miedo", "esperanza", "tristeza", "alegría", 
    "desesperación", "frustración", "nostalgia", "alivio", "ansiedad", "angustia", 
    "preocupación", "optimismo", "incertidumbre", "gratitud", "cruce", "frontera", 
    "travesía", "camino", "trayecto", "ruta", "viaje", "desierto", "mar", 
    "caravana", "paso", "coyotes", "rutas peligrosas", "violencia", "persecución", 
    "abuso", "detención", "secuestro", "extorsión", "discriminación", "xenofobia", 
    "racismo", "protección", "inseguridad", "amenazas", "peligro", "familia", 
    "hijos", "padres", "reunificación", "separación", "reencuentro", "amigo", 
    "compañero", "comunidad", "apoyo", "seres queridos", "solidaridad", 
    "redes de apoyo", "albergue", "refugio", "comida", "salud", "educación", 
    "trabajo", "empleo", "asistencia", "ayuda", "recursos", "apoyo humanitario", 
    "servicios médicos", "atención psicológica", "México", "Estados Unidos", 
    "Guatemala", "Honduras", "El Salvador", "Tijuana", "Tapachula", "Chiapas", 
    "frontera norte", "frontera sur", "albergues en México", "rutas migratorias", 
    "estaciones migratorias", "buscando una vida mejor", "huyendo de la violencia", 
    "cruzar la frontera", "en busca de asilo", "esperando la respuesta", 
    "temor a la deportación", "esperanza de un futuro mejor"
]

# Función para buscar tweets usando el léxico
# Esta función toma el léxico y busca tweets que contengan cualquiera de las palabras o frases del léxico.
# Puede especificarse el número máximo de tweets a buscar por palabra clave.
def search_tweets(lexicon, num_tweets=100):
    tweets = []
    for word in lexicon:
        for tweet in tweepy.Cursor(api.search_tweets, q=word, lang="es", tweet_mode="extended").items(num_tweets):
            tweets.append(tweet.full_text)
    return tweets

# Buscar tweets
# Llamar a la función search_tweets con el léxico y especificar cuántos tweets buscar por palabra clave
tweets = search_tweets(lexicon, num_tweets=50)

# Mostrar algunos ejemplos de tweets encontrados
# Imprimir los primeros 10 tweets encontrados para revisión
for i, tweet in enumerate(tweets[:10]):
    print(f"{i+1}. {tweet}\n")
    

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