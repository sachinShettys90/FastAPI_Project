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
