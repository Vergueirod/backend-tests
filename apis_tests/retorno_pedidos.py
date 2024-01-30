import json
from fastapi import FastAPI

app = FastAPI()

def carregar_dados_json():
    with open('../teste_pedidos_response.json', 'r') as arquivo:
        dados_json = json.load(arquivo)
    return dados_json

@app.get("/all-pedido")
def obter_peedido():
    dados_pedido = carregar_dados_json()
    return dados_pedido