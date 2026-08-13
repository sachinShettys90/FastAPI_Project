from pydantic import BaseModel
from typing import TypedDict, Annotated, List, Dict

# suppose if we add address to the Patient_Pydantic , we can't fetch if we define it in one single type
# so we will create a saparate pydantic class for the Address with city satate pin as values
# while defining the address in the patient_pydantic , assign address:Address class


class Address(BaseModel):
    city: str
    state: str
    pin: int


class Patient_Pydantic(BaseModel):
    name: str
    age: int
    address: Address


PatientAddress = {'city': "Bangalore", 'state': 'Karnataka', 'pin': '232234'}

# Addresss class we are unpacking and defining the object Address1
Address1 = Address(**PatientAddress)

patient_info = {'name': 'Suresh', 'age': 89, 'address': Address1}

# Patient_Pydantic class, we are unpacking and defining the object Patient1

Patient1 = Patient_Pydantic(**patient_info)

print(Patient1)
# name='Suresh' age=89 address=Address(city='Bangalore', state='Karnataka', pin=232234)

print(Patient1.name)
# Suresh

print(Patient1.address.state)
# Karnataka


# Uses
# Better organization: for related data like address, vitals, insurance
# Readability Easier: for developers and API consumenrs to understand
# Reuseability : Use vitals in multiple models( eg: patient, Medicalrecord)
