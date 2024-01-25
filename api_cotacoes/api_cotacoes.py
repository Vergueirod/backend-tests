from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/cotacao") #endpoint
async def get_cotacao():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()