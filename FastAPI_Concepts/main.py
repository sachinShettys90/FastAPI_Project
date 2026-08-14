
from fastapi import FastAPI, Path, HTTPException, Query
import json
from pydantic import BaseModel, Field, computed_field
from typing import TypedDict, Literal, Optional, List, Dict, Annotated
from fastapi.responses import JSONResponse

app = FastAPI()  # defining the object

# define the pydantic


class Patient(BaseModel):
    id: Annotated[str, Field(..., description="Patient's id", example="P001")]
    name: Annotated[str, Field(..., description="Patient's name")]
    city: Annotated[str, Field(..., description="Patient's city")]
    age: Annotated[int, Field(..., description="Patient's age", gt=0, lt=110)]
    gender: Annotated[Literal['male', 'female'],
                      Field(..., description="Patient's gender")]
    height: Annotated[float, Field(..., description="Patient's height")]
    weight: Annotated[float, Field(..., description="Patient's weight")]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "normal"
        else:
            return "Obese"


def load_data():
    with open('patient.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data


def save_data(data):  # this will save the incoming data into the json
    with open('patient.json', 'w') as f:
        json.dump(data, f)


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


# Queryparameters
# /patients?city=Delhi&sort_by=age

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="sort on the basis of height, weight or bmi"), order: str = Query('asc', description="sort in asc or desc order")):
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400, detail=f'Invalid field select from {valid_fields}')

    if order not in ['asc', 'desc']:
        raise HTTPException(
            status_code=400, detail=f'Invalid order select betweem asc and desc')

    data = load_data()
    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(
        sort_by, 0), reverse=sort_order)

    return sorted_data


@app.post('/create')
def create_patient(patient: Patient):
    # 1.load existing data,#2.check if patient already exists or not, #3.new patient add to the data base
    # 1.load data
    data = load_data()
    # 2 check if patient already exists or not
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")
    # 3:new patient add to the data base
    # patient is pydantic object, data is json so use dump to add it to dictionary
    data[patient.id] = patient.model_dump(exclude='id')

    # 4 save into the json file
    save_data(data)

    # 5 return the response once the data updated
    return JSONResponse(status_code=201, content={'message': 'Patient created successfully'})
