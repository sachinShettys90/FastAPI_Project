from fastapi import FastAPI, Path, Query, HTTPException
import json

app = FastAPI()


def load_data():
    with open('patient.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


@app.get('/')
def about():
    return {'messgae': "A fully functional API to manage Patients record"}


@app.get('/view')
def view():
    data = load_data()
    return data


@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description="Enter the Patient id , will search in Datbase", example="P001")):
    data = load_data()
    if patient_id not in data:
        return HTTPException(status_code=400, detail="Patient not found")
    return data[patient_id]


@app.get('/sort')
def sort_data(sort_by: str = Query(..., description="Enter the sort_by details, height, weight, bmi"),
              order: str = Query('asc', description="Order by asc or desc")):
    data = load_data()
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid field selected. Choose from: {valid_fields}"
        )

    if order not in ['asc', 'desc']:
        raise HTTPException(
            status_code=400,
            detail="Invalid order selected. Use 'asc' or 'desc'."
        )

    sorted_data = sorted(
        data.values(),
        key=lambda patient: patient.get(sort_by, 0),
        reverse=(order == 'desc')
    )

    return sorted_data
