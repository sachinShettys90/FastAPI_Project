# FastAPI Example Project

A minimal FastAPI app with instructions to run and development notes.

## Contents
- `main.py` — FastAPI application entrypoint
- `myenv/` — Python virtual environment (ignored by git)

## Prerequisites
- Python 3.10+ installed
- (Optional) Git

## Setup
1. Create and activate a virtual environment:

```powershell
python -m venv myenv
.\myenv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

If `requirements.txt` is not present, install manually:

```powershell
pip install fastapi uvicorn
```

## Run (development)
Start the app with Uvicorn and autoreload:

```powershell
uvicorn main:app --reload
```

Open http://127.0.0.1:8000 in your browser. Interactive docs at http://127.0.0.1:8000/docs

## Git
- Virtual environment folders are ignored via `.gitignore`. If you accidentally committed your env, remove it from the repo:

```bash
git rm -r --cached myenv
git commit -m "Remove virtualenv from repo"
git push
```

## Notes
- Keep `myenv/` listed in `.gitignore` to avoid large and platform-specific files in the repo.
- Consider adding `requirements.txt` via `pip freeze > requirements.txt` before sharing the project.

## API Usage Notes

### Query Parameters
Use query parameters for optional filters or pagination. Example endpoint in `main.py`:

```python
@app.get('/patients')
def list_patients(city: str | None = None, limit: int = 10):
	# city is a query param (optional), limit is a query param with default
	...
```

Call it like: `GET /patients?city=Mumbai&limit=5`

### Path Parameters
Use path parameters for identifying a specific resource. Example:

```python
@app.get('/patients/{patient_id}')
def get_patient(patient_id: str):
	# patient_id comes from the URL path
	...
```

Call it like: `GET /patients/P001`

### HTTP Exceptions
When an error condition occurs (missing resource, invalid input), raise `HTTPException` to return a proper status code and message:

```python
from fastapi import HTTPException

if not found:
	raise HTTPException(status_code=404, detail='Patient not found')

# For server-side errors related to data files, you can return 500:
raise HTTPException(status_code=500, detail='patient.json contains invalid JSON')
```

FastAPI will render the JSON error response and the HTTP status code accordingly.
