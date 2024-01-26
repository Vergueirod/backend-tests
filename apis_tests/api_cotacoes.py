import asyncio
import httpx
from fastapi import FastAPI

app = FastAPI()

@app.get("/cotacao") #endpoint
async def get_cotacao():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        par_moeda = data["USDBRL"]["name"]
        valor_dolar_hoje = data["USDBRL"]["bid"]
        return par_moeda, valor_dolar_hoje 

# testes de calculos: Depois passarei isso para um banco de dados, quando fizer o design dele.
salary_month = 1000
supermarket_month = 400
dif = salary_month - supermarket_month 
    
# real:
print("Relatorio mensal: ")
print(f"Receita mensal: R$ {salary_month} ")
print(f"Gastos totais: R$ {supermarket_month} ")
print(f"Quanto ainda tenho disponivel: R$ {dif} ")    
    
# dolar:
async def main():
    par_moeda, valor_dolar_hoje = await get_cotacao()
    
    print("Monthly report: ")
    print(f"Monthly income: $ {salary_month / float(valor_dolar_hoje):.2f} ")
    print(f"Total spending: $ {supermarket_month / float(valor_dolar_hoje):.2f} ")
    print(f"How much do I still have available: $ {dif / float(valor_dolar_hoje):.2f} ")
    
if __name__ == "__main__":
    asyncio.run(main())