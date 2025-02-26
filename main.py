import decimal
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Dict, Any

# Set decimal precision to 25 digits
decimal.getcontext().prec = 25

app = FastAPI()

# Calculation function with precise decimal literals
def perform_calculation(**kwargs):
    return (kwargs['a'] * decimal.Decimal("1000")) / ((decimal.Decimal("30") * kwargs['b']) / decimal.Decimal("100"))

# Endpoint with manual JSON response
@app.post("/")
async def calculate(request: Dict[str, Any]):
    # Process request values
    kwargs = {}
    for key, value in request.items():
        if isinstance(value, (int, float)):
            kwargs[key] = decimal.Decimal(str(value))
        elif isinstance(value, str):
            kwargs[key] = decimal.Decimal(value)
        else:
            kwargs[key] = value
    
    # Calculate result
    result = perform_calculation(**kwargs)
    
    # Extract mantissa and exponent for scientific notation
    # This preserves full precision while still being a "number" format
    result_str = format(result, '.25g')
    
    return JSONResponse(content={
        "result": result_str,  # Scientific notation as string
        "decimal_str": str(result),  # Full decimal string
        "approximate_float": float(str(result))  # Approximate float value
    })
