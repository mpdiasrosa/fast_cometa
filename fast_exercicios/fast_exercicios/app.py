from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/', response_class=HTMLResponse)
def read_root():
    return """
    <html>
      <head>
        <title> Hello </title>
      </head>
      <body>
        <h1> Olar Mundo </h1>
      </body>
    </html>"""