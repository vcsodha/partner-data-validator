from __future__ import annotations
import io
import pandas as pd
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from app.models import PartnerRow
from app.validator import validate_dataframe

app = FastAPI(title="Partner Data Validator")

@app.post("/validate")
async def validate(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        return JSONResponse(status_code=400, content={"error": "CSV only"})
    df = pd.read_csv(io.BytesIO(await file.read()))
    return validate_dataframe(df, PartnerRow)
