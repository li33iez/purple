from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

# Serve CSS, JS, images from /static
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve homepage (index.html) at root
@app.get("/")
def home():
    index_path = Path("static") / "index.html"
    return FileResponse(index_path)
