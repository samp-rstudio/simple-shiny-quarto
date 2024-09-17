# hello.py
import os

from shiny import ui, App
from htmltools import HTML
from starlette.applications import Starlette
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles

frontend = ui.page_fluid(
    "Hello Shiny Python with Quarto",
    HTML("<p><a href='/reports/report.html' id='quarto_report'>A generated report</a></p>")
)

def server(input, output, session):
    return True

os.makedirs("reports", exist_ok=True)
cmd = f"quarto render report.qmd -o report.html --to html"
os.system(cmd)
# copy file to reports directory
os.system(f"cp report.html reports/")

my_app = App(frontend, server)
your_app = App(frontend, server)

app_routes = [
    Mount('/reports', app=StaticFiles(directory='./reports', html=True)),
    Mount('/', app=my_app)
]

app = Starlette(routes=app_routes)
