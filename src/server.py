from fastapi import FastAPI
from models import URL, ShortURL
from database import create_url_record, get_url_record
from code_generator import generate_random_code

app = FastAPI()
prefix = "http://127.0.0.1:8000"


@app.post("/", response_model=ShortURL)
async def shorten_url(url: URL):
    code = generate_random_code()
    while get_url_record(code):
        print("Code already exists, generating again...")
        code = generate_random_code()
    short_url = prefix + "/" + code
    create_url_record(code, url.long_url)
    response = ShortURL(short_url=short_url)
    return response
