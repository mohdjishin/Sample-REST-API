from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def hello():
    return {"Hello":"World"}

@app.post('/')
def helo_post():
    return {"success": "POSTED!"}


@app.get('/something')
def something():
    return {"Data":"Something"}