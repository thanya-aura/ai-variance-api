from fastapi import FastAPI, UploadFile, File, HTTPException
from agents.standard.standard_agent import analyze_standard_variance
from agents.plus.plus_agent import analyze_plus_variance
from agents.premium.premium_agent import analyze_premium_variance

app = FastAPI()

@app.post("/analyze")
async def analyze(file: UploadFile = File(...), agent: str = "standard"):
    if not file.filename.endswith((".xlsx", ".csv")):
        raise HTTPException(status_code=400, detail="❌ Only .xlsx or .csv files are supported.")
    content = await file.read()
    if agent == "standard":
        return analyze_standard_variance(content)
    elif agent == "plus":
        return analyze_plus_variance(content)
    elif agent == "premium":
        return analyze_premium_variance(content)
    else:
        raise HTTPException(status_code=400, detail="❌ Unknown agent type.")
