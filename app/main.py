import json
from datetime import datetime

import httpx
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates/")

skills_dict = {
    'Development Arsenal': [
        {'name': 'Android Development', 'credential_link': 'https://credential-link-for-android.dev'},
        {'name': 'Amazon Web Services', 'credential_link': 'https://credential-link-for-aws.dev'},
        # Add more skills as needed
    ],
    'Programming Languages': [
        {'name': 'Python', 'credential_link': 'https://credential-link-for-python.dev'},
        {'name': 'Java', 'credential_link': 'https://credential-link-for-java.dev'},
        # Add more skills as needed
    ],
    'DevOps Tools': [
        {'name': 'Docker', 'credential_link': 'https://credential-link-for-docker.dev'},
        {'name': 'Kubernetes', 'credential_link': 'https://credential-link-for-kubernetes.dev'},
        # Add more skills as needed
    ],
    'Frontend Technologies': [
        {'name': 'React', 'credential_link': 'https://credential-link-for-react.dev'},
        {'name': 'Vue.js', 'credential_link': 'https://credential-link-for-vuejs.dev'},
        # Add more skills as needed
    ]
    # Add more categories as needed
}


def get_api_key():
    with open('./secrets/api_key.txt') as f:
        api_key = f.read()
    return api_key

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", 
                                      {"request": request, 
                                       "title": "My Portfolio", 
                                       "github_url": "https://github.com/Ebredvick", 
                                       "linkedin_url": "https://www.linkedin.com/in/ethan-bredvick-967b52123",
                                       "skills_dict": skills_dict})

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