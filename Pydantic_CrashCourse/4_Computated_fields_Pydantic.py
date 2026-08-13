# Computated fields in pydantic ,where we can add the computated field , which can calculate the value using the existing values Eg: calculating the bmi using height and weight

from pydantic import BaseModel, Field, EmailStr, computed_field
from typing import TypedDict, Annotated, List, Dict


class Patient_Pydantic(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property                    # we have to use the property decorator in computed field
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi


def update_patientDatabase(patient: Patient_Pydantic):
    print(patient.name)
    print(patient.weight)
    print(patient.bmi)
    print("Updated data base")


Patient_info = {'name': "Suresh", 'email': 'abc@hdfc.com', 'weight': '78', 'age': '70', 'height': 1.7,
                'married': True, 'allergies': ["pollen"], 'contact_details': {'mobile': '7019228968', 'emergency': "89516762666"}}
P1 = Patient_Pydantic(**Patient_info)
update_patientDatabase(P1)
