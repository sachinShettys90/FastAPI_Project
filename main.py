from fastapi import FastAPI

app = FastAPI()  # defining the object


@app.get("/")  # using decorator routing the / , with get method
def hello():
    return {"message": "hello world"}


@app.get('/about')
def about():
    return {"message": "Campusx is an education platform where you can learn api "}


@app.get('/info')
def info():
    return {"message": "this is the url info will be updated in the application"}
