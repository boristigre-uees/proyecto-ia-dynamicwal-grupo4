from fastapi import APIRouter
from api.schemas.schemas import PriceRequest, PriceResponse
import sys
import os

# Path para importar QLearning
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.models.qlearning_pricing import QLearningPricer

router = APIRouter()

@router.post("/optimize-price", response_model=PriceResponse)
def optimize_price(request: PriceRequest):
    pricer = QLearningPricer(base_price=request.base_price, elasticity=request.elasticity)
    pricer.train(episodes=500)
    
    optimal_price = pricer.get_optimal_price(1.0)
    uplift = ((optimal_price - request.base_price) / request.base_price) * 100
    
    message = f"Subir precio {uplift:.1f}%" if uplift > 0 else f"Bajar precio {abs(uplift):.1f}%"
    
    return PriceResponse(
        optimal_price=optimal_price,
        uplift_percent=uplift,
        message=message
    )