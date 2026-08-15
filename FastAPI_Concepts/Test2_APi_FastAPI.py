from fastapi import FastAPI, Path, Query, HTTPException
from fastapi.responses import JSONResponse
from pydantic import Field, BaseModel, computed_field
from typing import TypedDict, Annotated, Dict, List, Literal, Optional
import json
app = FastAPI()


def load_data():
    with open('patient.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def save_data(data):
    with open('patient.json', 'w') as f:
        json.dump(data, f)


class Patient(BaseModel):
    id: Annotated[str,
                  Field(..., description="ID of the patient", example='P001')]
    name: Annotated[str, Field(..., description="Patient's name",
                               max_length=30, title="Patient's Name")]
    city: Optional[str] = Field(default=None, description="Patient's city")
    age: Annotated[int, Field(..., description="patients age", gt=0, lt=100)]
    gender: Annotated[Literal['male', 'female'],
                      Field(..., description="Patient's gender")]
    height: Annotated[float,
                      Field(..., description="Patient's height", gt=0, lt=3)]
    weight: Annotated[float,
                      Field(..., description="Patient's weight", gt=0, lt=300)]

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


@app.post('/create')
def create_patient(patient: Patient):
    data = load_data()
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exist")

    data[patient.id] = patient.model_dump(exclude=['id'])

    save_data(data)

    return JSONResponse(status_code=200, content={'message': "Patients  details added successfully"})
