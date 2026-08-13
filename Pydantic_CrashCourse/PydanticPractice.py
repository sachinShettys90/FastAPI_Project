from pydantic import BaseModel
from typing import Annotated, TypedDict, Optional


class Patient_details(BaseModel):
    name: str
    age: int
    weight: Optional[float] = None


def UpdateDetails(patient: Patient_details):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print("data updated")


Data = {'name': 'Suresh', 'age': 56}

PydanticData = Patient_details(**Data)
UpdateDetails(PydanticData)
