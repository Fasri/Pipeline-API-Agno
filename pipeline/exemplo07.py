import requests
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
import time
from dotenv import load_dotenv
import os

load_dotenv()


# Configuração do banco de dados PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL")

# Criação da conexão com o banco de dados
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)



# Definição do modelo de dados
class Preco(Base):
    __tablename__ = 'precos'
    id = Column(Integer, primary_key=True)
    valor = Column(Float)
    criptomoeda = Column(String(10))
    moeda = Column(String(10))
    timedata = Column(DateTime)

# Criação da tabela no banco de dados
Base.metadata.create_all(engine)

# extrair o preço do bitcoin
def get_bitcoin_price():
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    return response.json()

def trasnform_data(data_json):
   valor = float(data_json['data']['amount'])
   criptomoeda = data_json['data']['currency']
   moeda = data_json['data']['base']
   dados_preco = Preco(
       valor= valor,
       criptomoeda= criptomoeda,
       moeda= moeda,
       timedata= datetime.now()
    )
   return dados_preco

def save_data(data):
    with Session() as session:
        session.add(data)
        session.commit()        
    print("Dados salvos no banco de dados.")

if __name__ == "__main__":
    while True:
        data_json = get_bitcoin_price()
        dados_preco = trasnform_data(data_json)
        print("Dados transformados:")

        save_data(dados_preco)
        print("Aguardando 5 segundos para a próxima coleta...")
        time.sleep(5)