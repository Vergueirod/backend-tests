import asyncio
import httpx
from fastapi import FastAPI

app = FastAPI()

@app.get("/buscar-cep/{cep}") # endpoint
async def get_cep(cep: str):
    url = f"https://cdn.apicep.com/file/apicep/{cep}.json"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()