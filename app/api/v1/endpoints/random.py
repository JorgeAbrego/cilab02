from fastapi import APIRouter
import random
from app.core.logger import setup_logger

logger = setup_logger("v1")

router = APIRouter()


@router.get("/int/",
            response_model=int,
            tags=["random"])
def generate_integer():
    logger.info("Generating random integer")
    return random.randint(0, 100)


@router.get("/float/",
            response_model=float,
            tags=["random"])
def generate_float():
    logger.info("Generating random float")
    return random.uniform(0, 100)
