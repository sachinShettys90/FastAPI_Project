from fastapi import FastAPI, Path, HTTPException
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


@app.get('/patient/{patient_id}')
# import Path and use it for description "Path parameters"
def view_patient(patient_id: str = Path(..., description="ID of the patient in the DB", example="P003")):
    # load all the data
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    # HTTP Exceptions
    raise HTTPException(status_code=404, detail="Patient not found")
