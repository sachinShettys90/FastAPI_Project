from pydantic import BaseModel, Field, EmailStr, field_validator
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

    @field_validator('email')                      # decorator
    @classmethod                                 # field_validator is a class method
    def email_validator(cls, value):
        valid_domain = ['hdfc.com', 'icic.com']

        # value=>abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domain:
            raise ValueError('not a valid domain')

        return value


def update_database(patient: PatientDetails):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print("updated data")


PatientInfo = {'name': "Suresh", 'email': 'abc@hdfc.com', 'weight': 78, 'age': 27,
               'married': True, 'allergies': ["pollen"], 'contact_details': {'mobile': '7019228968'}}

P1 = PatientDetails(**PatientInfo)

update_database(P1)
