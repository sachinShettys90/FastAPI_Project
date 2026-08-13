from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, TypedDict, Annotated, Optional, Dict

''' We can perform
 1.type validation(str,int,float,EmailStr)

 2.data validation using Pydantic(List[str], Dict[str,str] .... this will make sure that data type for the input should be of the same type mentioned in the Pydantic)

 3.Custom data validation (use Field to define the custom values): where we can define the custom range, Eg: age:int=Field(gt=0,lt=200)
 Using Field we can add the CustomData validation by adding the contraints and also we can add the description as metadata , to add the title and description as meta data , use Annotated

 '''


class Patient(BaseModel):
    # Custom validation of max length, we are adding the meta data using Annotated(title,description,examples)
    name: Annotated[str, Field(..., max_length=20, title="Name of the patient",
                               description="Give the name of the patient in less than 50 characters", examples=['Nitesh', 'Amit'])]

    diagnosis: Annotated[str,
                         Field(default=None, description="write the patient diagnosis", max_length=25)]

    # custom validation of age, and also we can add the meta data with description
    age: int = Field(
        gt=0, lt=150, description="Age should be between 0 and 150")

    weight: float = Field(gt=0)
    website: Optional[AnyUrl] = None
    email: EmailStr  # IF the proper email format is not given , it will throw an error

    # we can give default values for this aswell, if no inputs for married , default=False
    married: bool = False

    # don't use normal list , cause we can't do two validation with list and string
    # for Optional field we have to give default value 'None'
    allergies: Optional[List[str]] = None

    contactDetails: Dict[str, str]


def Insert_patientRecord(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.contactDetails)
    print(patient.diagnosis)
    print("Data inserted")


Patient_info = {'name': "Suresh", 'age': 35, 'diagnosis': "Nothing", 'email': 'suresh@apple.com', 'weight': 45,
                'married': True, 'allergies': ['pollen', 'dust'], 'contactDetails': {'mobile': '72304932432'}}

Patient1 = Patient(**Patient_info)

Insert_patientRecord(Patient1)
