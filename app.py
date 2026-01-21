from fastapi import FastAPI
from pydantic import BaseModel
from logic import razure_decision_engine

app = FastAPI(title="RaZure Decision Engine")

class DecisionInput(BaseModel):
    energy: int
    money_stress: int
    clarity: int
    weight_note: str | None = None

@app.post("/decision")
def get_decision(data: DecisionInput):
    result = razure_decision_engine(
        energy=data.energy,
        money_stress=data.money_stress,
        clarity=data.clarity,
        weight_note=data.weight_note
    )
    return result