''' GET MEETHOD
Here we are creating new end point using get method where we can 
1.view the patients data using /view
2.view the patient using specific id using /patient/{patient_id} Eg: /patient/P001
3.We can sort the data using sort function /sort --- where we can sortby(height,weight,bni) and with order(asc,desc)'''


from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()  # defining the object


def load_data():
    with open('patient.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data


@app.get("/")  # using decorator routing the / , with get method
def hello():
    return {"message": "Patient Management system API"}


@app.get('/about')
def about():
    return {"message": "A fully functional API to manage your patient records"}


@app.get('/view')
def view():
    data = load_data()

    return data


@app.get('/patient/{patient_id}')
# import Path and use it for description "Path parameters"
def view_patient(patient_id: str = Path(..., description="ID of the patient in the DB", example="P003")):
    # load all the data
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    # HTTP Exceptions
    raise HTTPException(status_code=404, detail="Patient not found")


# Queryparameters
# /patients?city=Delhi&sort_by=age

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="sort on the basis of height, weight or bmi"), order: str = Query('asc', description="sort in asc or desc order")):
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400, detail=f'Invalid field select from {valid_fields}')

    if order not in ['asc', 'desc']:
        raise HTTPException(
            status_code=400, detail=f'Invalid order select betweem asc and desc')

    data = load_data()
    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(
        sort_by, 0), reverse=sort_order)

    return sorted_data
