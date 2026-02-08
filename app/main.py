from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

import scripts.parse_quotes as parse_quotes
import app.database as db 

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

class QuoteRequest(BaseModel):
    quote: str

@app.get("/", response_class=HTMLResponse)
async def index():
    with open('app/templates/index.html', encoding='utf-8') as f:
        return f.read()


@app.get("/quote") 
async def get_quote():
    import random 
    quote = random.choice(db.load_quotes())
    return {"quote": quote}


@app.post("/add_quote")
async def add_quote(data: QuoteRequest):
    if len(data.quote.strip()) == 0:
        raise HTTPException(status_code=400, detail="Цитата не может быть пустой")
    
    db.save_quote(data.quote.strip())
    return {"message": "Цитата добавлена успешно", "quote":data.quote}

