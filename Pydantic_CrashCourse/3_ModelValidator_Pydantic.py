from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator
from typing import TypedDict, Annotated, List, Dict

'''
Field validator : By using this we can do our custom data validation for the fields and also we can apply the transformation for the given field Eg:If the name should be small , we can apply the transformation to change the input to small

Note:Use the fieldvalidator in the decorator
'''


class PatientDetails(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    # model validation : we can validate  with two conditions with age>60 should have contact details
    # since the emergency contact is provided , it will not give any validation error
    # mode = after , means it will validate after Pydantic validation

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError(
                'Patients older than 60 must have emergency contact')
        return model


def update_database(patient: PatientDetails):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print("updated data")


PatientInfo = {'name': "Suresh", 'email': 'abc@hdfc.com', 'weight': '78', 'age': '70',
               'married': True, 'allergies': ["pollen"], 'contact_details': {'mobile': '7019228968', 'emergency': "89516762666"}}

# apply pydantic to the PatientInfo---Validation will happen after Pydantic
P1 = PatientDetails(**PatientInfo)

update_database(P1)  # Add the details to the database
