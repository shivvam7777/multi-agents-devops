from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from services import user_api

app = FastAPI()

# Include API router (pure backend endpoints)
app.include_router(user_api.router)

# Jinja2 templates setup
templates = Jinja2Templates(directory="templates")

# UI route
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Form route (separate from API)
@app.post("/form-users")
async def create_user_form(request: Request, username: str = Form(...)):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "message": f"User '{username}' created successfully!"}
    )
