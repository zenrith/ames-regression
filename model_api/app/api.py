import json
from pathlib import Path
from typing import Any

import pandas as pd
from ames_model import __version__ as model_version
from ames_model.predict import make_prediction
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from loguru import logger

from app.config import settings
from app.schemas.health import Health
from app.schemas.predict import MultipleHouseDataInputs, PredictionResults

with open(Path(__file__).resolve().parent / "VERSION") as version_file:
    version = version_file.read().strip()

api_router = APIRouter()


@api_router.get("/health", response_model=Health, status_code=200)
def health() -> dict:
    """Root get"""
    health = Health(
        name=settings.PROJECT_NAME, api_version=version, model_version=model_version
    )
    return health.model_dump()


@api_router.post("/predict", response_model=PredictionResults, status_code=200)
async def predict(input_data: MultipleHouseDataInputs) -> Any:
    """
    Make house price predictions with the Ames regression model
    """

    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))

    # Advanced: You can improve performance of your API by rewriting the
    # `make prediction` function to be async and using await here.
    logger.info(f"Making prediction on inputs: {input_data.inputs}")
    results = make_prediction(input_df)

    if results["errors"] is not None:
        logger.warning(f"Prediction validation error: {results.get('errors')}")
        raise HTTPException(status_code=400, detail=json.loads(results["errors"]))

    logger.info(f"Prediction results: {results.get('predictions')}")

    return results
