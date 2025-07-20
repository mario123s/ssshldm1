import requests

# La dirección y puerto del servidor proxy que comprarías
proxy_a_usar = {
   "http": "http://181.209.88.130:8080",
   "https": "https://181.209.88.130:8080",
}

# La página de destino
url_del_concierto = "https://www.paginadeventa.com"

# La petición a la página se hace A TRAVÉS del proxy
try:
    respuesta = requests.get(url_del_concierto, proxies=proxy_a_usar, timeout=5)
    print("Conexión a través del proxy exitosa.")
except:
    print("No se pudo conectar al proxy.")