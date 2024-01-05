from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import markdown

templates = Jinja2Templates(directory="templates")
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def show_resume(request: Request):
    with open("RESUME.md", "r") as f:
        markdown_string = f.read()

    html_string = markdown.markdown(markdown_string)

    return templates.TemplateResponse("resume.html", {"request": request, "resume_body": html_string})


@app.get("/other", response_class=HTMLResponse)
def show_resume(request: Request):
    with open("OTHER.md", "r") as f:
        markdown_string = f.read()

    html_string = markdown.markdown(markdown_string)

    return templates.TemplateResponse("resume.html", {"request": request, "resume_body": html_string})
