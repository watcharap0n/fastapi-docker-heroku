from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def first_page():
    return 'Hello FastAPI'
