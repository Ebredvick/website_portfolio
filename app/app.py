import json
from datetime import datetime

import httpx
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates/")

def get_api_key():
    with open('./secrets/api_key.txt') as f:
        api_key = f.read()
    return api_key

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

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("home.html", 
                                      {"request": request}) 
