import json

import httpx
from fastapi import FastAPI

app = FastAPI()

def get_api_key():
    with open('./secrets/api_key.txt') as f:
        api_key = f.read()
    return api_key

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/github/{user}/repos")
async def get_github_repos(user: str):
    api_key = get_api_key() 
    async with httpx.AsyncClient() as client:
        headers = {
            'Authorization': f'{api_key}', 
            'Accept': 'application/vnd.github.v3+json'
            }
        print(headers)
        response = await client.get(f"https://api.github.com/users/{user}/repos", 
                                    headers=headers)
    return response.json()

