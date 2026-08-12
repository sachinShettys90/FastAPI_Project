from pydantic import BaseModel


class Patient(BaseModel):
    name: str
    age: int


def Insert_patientRecord(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Data inserted")


Patient_info = {'name': "Suresh", 'age': 34}

Patient1 = Patient(**Patient_info)

Insert_patientRecord(Patient1)
