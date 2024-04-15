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
def read_root():
    return RedirectResponse("/home")

@app.get("/home", response_class=HTMLResponse)
def read_home(request: Request):
    return templates.TemplateResponse("home.html", 
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

@app.get("/about", response_class=HTMLResponse)
async def read_about(request: Request):
    return templates.TemplateResponse("about.html", 
                                      { "request": request,
                                        "title": "My Portfolio", 
                                       "github_url": "https://github.com/Ebredvick", 
                                       "linkedin_url": "https://www.linkedin.com/in/ethan-bredvick-967b52123"}) 

@app.get("/portfolio", response_class=HTMLResponse)
async def read_portfolio(request: Request):
    return templates.TemplateResponse("portfolio.html", 
                                      { "request": request,
                                        "title": "My Portfolio", 
                                       "github_url": "https://github.com/Ebredvick", 
                                       "linkedin_url": "https://www.linkedin.com/in/ethan-bredvick-967b52123"}) 

@app.get("/contacts", response_class=HTMLResponse)
async def read_contacts(request: Request):
    return templates.TemplateResponse("contacts.html", 
                                      { "request": request,
                                        "title": "My Portfolio", 
                                       "github_url": "https://github.com/Ebredvick", 
                                       "linkedin_url": "https://www.linkedin.com/in/ethan-bredvick-967b52123"}) 

@app.get("/blog", response_class=HTMLResponse)
async def read_blog(request: Request):
    return templates.TemplateResponse("blog.html", 
                                      { "request": request,
                                        "title": "My Portfolio", 
                                       "github_url": "https://github.com/Ebredvick", 
                                       "linkedin_url": "https://www.linkedin.com/in/ethan-bredvick-967b52123"}) 