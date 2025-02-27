from decimal import Decimal, getcontext
from fastapi import FastAPI
from pydantic import BaseModel


getcontext().prec = 50  # "just in case": set high precision for any float/decimal values calculations
LONG_DECIMAL = Decimal("3.14159265358979323846264338327950288419716939937510")


class DefaultModel(BaseModel):
    value: Decimal


app = FastAPI()


@app.get("/default")
def direct_decimal():
    """Default behavior of Python's standard json module behaviour converts to float and loses precision"""
    return {"value": LONG_DECIMAL}


@app.get("/decimal", response_model=DefaultModel)
def default_behavior():
    """Using a model with direct Decimal encoder - still loses precision"""
    return DefaultModel(value=LONG_DECIMAL)
