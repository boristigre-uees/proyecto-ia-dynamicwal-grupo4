from pydantic import BaseModel

class PriceRequest(BaseModel):
    category: str
    base_price: float
    elasticity: float = -1.3

class PriceResponse(BaseModel):
    optimal_price: float
    uplift_percent: float
    message: str