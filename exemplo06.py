import requests
from tinydb import TinyDB
from datetime import datetime
import time


# extrair o preço do bitcoin
def get_bitcoin_price():
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    return response.json()

def trasnform_data(data_json):
   valor = data_json['data']['amount']
   criptomoeda = data_json['data']['currency']
   moeda = data_json['data']['base']
   dados_preco = {
       'valor': valor,
       'criptomoeda': criptomoeda,
       'moeda': moeda,
       'date': datetime.now().isoformat()
   }
   return dados_preco

def save_data(data):
    db = TinyDB('db.json')
    db.insert(data)
    print("Dados salvos no banco de dados.")

if __name__ == "__main__":
    while True:
        data_json = get_bitcoin_price()
        dados_preco = trasnform_data(data_json)
        save_data(dados_preco)
        time.sleep(5)