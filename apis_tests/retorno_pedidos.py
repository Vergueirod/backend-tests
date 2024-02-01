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


@app.get("/pedidos-last")
def get_pedidos_last():
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
    
    
@app.get("/pedidos-list")
def get_pedidos_list():
    dados_pedido = parse_pedido()
    pedidos = dados_pedido['retorno']['pedidos']
    lista_pedidos = []

    for pedido in pedidos:
        info_pedido = pedido['pedido']
        lista_pedidos.append({
            "Numero do pedido": info_pedido['numero'],
            "Total de Venda": info_pedido['totalvenda']
        })

    return lista_pedidos


@app.get("/pedidos-items")
def get_pedidos_items():
    dados_pedido = parse_pedido()
    pedidos = dados_pedido['retorno']['pedidos']
    item_list = []
    
    for i in pedidos:
        itens = i['pedido']['itens']
        for j in itens:
            item = j['item']

            item_list.append({
                "Código": item['codigo'],
                "Descrição": item['descricao'],
                "Quantidade": item['quantidade'],
                "Valor": item['valorunidade'],
                "Peso": item['pesoBruto'],
            })
    
    return item_list
    