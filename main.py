from fastapi import FastAPI

app = FastAPI()



@app.get('/')
def abc():
    return {'data': {'name': 'Sreekanth'}}

@app.get('/about')
def about():
    return {'data': {'page': 'about'}}