import requests

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
       'moeda': moeda
   }
   return dados_preco

if __name__ == "__main__":
    data_json = get_bitcoin_price()
    dados_preco = trasnform_data(data_json)
    print(dados_preco)