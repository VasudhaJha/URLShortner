from fastapi import FastAPI, Request, Response, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from models import URL, ShortURL
from database import create_url_record, get_url_record
from code_generator import generate_random_code

app = FastAPI()
prefix = "http://127.0.0.1:8000"

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/", response_model=ShortURL, status_code=status.HTTP_201_CREATED)
async def shorten_url(url: URL):
    code = generate_random_code()
    while get_url_record(code):
        print("Code already exists, generating again...")
        code = generate_random_code()
    short_url = prefix + "/" + code
    create_url_record(code, url.long_url)
    response = ShortURL(short_url=short_url)
    return response


@app.get("/{url_code}", status_code=status.HTTP_302_FOUND)
async def redirect(url_code, response: Response):
    url_record = get_url_record(code=url_code)
    if url_record:
        response.headers['Location'] = url_record['long_url']
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
