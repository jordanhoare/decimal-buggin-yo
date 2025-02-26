import decimal
from fastapi import FastAPI
from typing import Dict, Any


app = FastAPI()


def perform_calculation(**kwargs):
    return (kwargs['a'] * 1000) / ((30 * kwargs['b']) / 100)

@app.post("/")
async def calculate(request: Dict[str, Any]):

    kwargs = {}
    for key, value in request.items():
        if isinstance(value, (int, float)):
            kwargs[key] = decimal.Decimal(str(value))
        elif isinstance(value, str):
            kwargs[key] = decimal.Decimal(value)
        else:
            kwargs[key] = value

    result = perform_calculation(**kwargs)

    return {"result": result}
