# Pydantic Crash Course

This folder contains short practice scripts demonstrating Pydantic (v2) features, validations, and common errors encountered while learning.

## Contents
- `1_Pydantic_Basics_Practice.py` — basic model examples, Field/Annotated usage, and a small runner.
- (Add more files here as you create them.)

## Purpose
Give hands-on examples of Pydantic model declarations, validation, and how FastAPI/OpenAPI interacts with Pydantic models.

## Prerequisites
- Python 3.10+
- A virtual environment is recommended.
- Install Pydantic v2 and (optionally) FastAPI for integration examples:

```powershell
python -m venv myenv
.\myenv\Scripts\Activate.ps1
pip install -U pip
pip install pydantic
```

If you plan to use the FastAPI examples in the repo, also:

```powershell
pip install fastapi uvicorn
```

## How to run the exercises
- From the repository root (recommended):

```powershell
python Pydantic_CrashCourse\1_Pydantic_Basics_Practice.py
```

- Or change into the folder and run:

```powershell
cd Pydantic_CrashCourse
python 1_Pydantic_Basics_Practice.py
```

## Common Pydantic v2 notes and gotchas

- Fields must be declared using annotations. Wrong:

```python
diagnosis = Annotated[str, Field(...)]  # NOT a field — no ':' annotation
```

Correct:

```python
diagnosis: Annotated[str, Field(...)]
# or
diagnosis: str = Field(...)
```

- Use `Annotated` when you want to attach `Field(...)` metadata (examples, descriptions, constraints).
- Use proper Python types in annotations (e.g., `age: int`, not `age: str`). Wrong types break OpenAPI generation.
- Pydantic v2 returns model dumps via `model_dump()` (replaces v1's `dict()`), and validation APIs changed.
- `computed_field` decorator can be used to add read-only computed properties included in model output.

## Example: Fixing "non-annotated attribute" error

Error message:

```
PydanticUserError: A non-annotated attribute was detected: `diagnosis = typing.Annotated[str, FieldInfo(...)]`. All model fields require a type annotation; if `diagnosis` is not meant to be a field, you may be able to resolve this error by annotating it as a `ClassVar` or updating `model_config['ignored_types']`.
```

Cause: You used `=` instead of `:`. Fix by adding a type annotation with `:` as shown above.

## Example snippets

- Creating a minimal model:

```python
from pydantic import BaseModel, Field
from typing import Annotated

class Patient(BaseModel):
    id: Annotated[str, Field(..., description="Patient id", example="P001")]
    name: str
    age: int = Field(gt=0, lt=150)

p = Patient(id='P001', name='Alice', age=30)
print(p.model_dump())
```

## Troubleshooting
- If you see OpenAPI generation errors in FastAPI, inspect your Pydantic model annotations for:
  - incorrect types (e.g., using `str` where `int` is expected)
  - wrong metadata types for `example(s)` (OpenAPI expects lists/dicts in some places)

- If you accidentally committed your virtual environment, ensure your repository `.gitignore` lists the venv folder and remove it from git tracking:

```bash
git rm -r --cached myenv
git commit -m "Remove venv"
git push
```

## References
- Pydantic v2 docs: https://pydantic.dev/
- FastAPI docs (models & OpenAPI): https://fastapi.tiangolo.com/

If you want, I can expand this README with per-file explanations, expected outputs, or add quick unit-tests for each exercise.
