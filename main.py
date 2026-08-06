from fastapi import FastAPI
import json

app = FastAPI()  # defining the object


def load_data():
    with open('patient.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data


@app.get("/")  # using decorator routing the / , with get method
def hello():
    return {"message": "Patient Management system API"}


@app.get('/about')
def about():
    return {"message": "A fully functional API to manage your patient records"}


@app.get('/view')
def view():
    data = load_data()

    return data
