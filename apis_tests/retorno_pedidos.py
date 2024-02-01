import json
from fastapi import FastAPI

app = FastAPI()

def carregar_dados_json():
    with open('../teste_pedidos_response.json', 'r') as arquivo:
        dados_json = json.load(arquivo)
    return dados_json

@app.get("/all-pedido")
def parse_pedido():
    dados_pedido = carregar_dados_json()
    return dados_pedido

@app.get("/pedidos")
def get_pedidos():
    dados_pedido = parse_pedido()
    pedidos = dados_pedido['retorno']['pedidos']
    
    if pedidos:
        info_pedido = pedidos[-1]['pedido']
        
        return {
            "Numero do pedido": info_pedido['numero'],
            "Total de Venda": info_pedido['totalvenda']
        }
    else:
        return {"mensagem": "Nenhum pedido encontrado."}