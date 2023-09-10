import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    load_dotenv()
    ctx = dict(request=request, secret=os.getenv("SECRET"))
    return templates.TemplateResponse("index.html", ctx)
