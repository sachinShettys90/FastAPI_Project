''' POST MEETHOD
Here we are creating new end point using Post method where we can 
1.create the patient using /create : 
2.save_data()  is used to save the data into the database when we create in server
3.And also we are using computed_field to calculate the bmi,verdict from the input data fields 

NOTE: we used Pydantic to validate the type of the given input patient data '''


from fastapi import FastAPI, Path, HTTPException
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


class Patient_Update(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[str], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0, lt=3)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]


def load_data():
    with open('patient.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data


def save_data(data):  # this will save the incoming data into the json
    with open('patient.json', 'w') as f:
        json.dump(data, f)


@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: Patient_Update):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')

    existing_patient_info = data[patient_id]

    # Only pull fields the client actually sent
    updated_fields = patient_update.model_dump(exclude_unset=True)

    # Merge the changes into the existing record
    existing_patient_info.update(updated_fields)

    # Rebuild a full Patient object so bmi/verdict recompute correctly
    # if height or weight changed. Patient requires 'id', so add it back in.
    existing_patient_info['id'] = patient_id
    patient_pydantic_obj = Patient(**existing_patient_info)

    # Convert back to dict for storage, dropping id since it's the dict key
    data[patient_id] = patient_pydantic_obj.model_dump(exclude=['id'])

    save_data(data)

    return JSONResponse(status_code=200, content={'message': 'Patient updated successfully'})
