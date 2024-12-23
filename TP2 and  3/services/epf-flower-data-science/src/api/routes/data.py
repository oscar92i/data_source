import os
from fastapi import APIRouter
from src.schemas.message import MessageResponse
from kaggle.api.kaggle_api_extended import KaggleApi
from fastapi.responses import JSONResponse

router = APIRouter()

DATA_DIR = "src/data"
iris_route = "https://www.kaggle.com/datasets/uciml/iris"

# Iris dataset download route
@router.post("/data/download", name="Download Iris Dataset")
def download_iris_dataset() -> JSONResponse:
    """
    Downloads the Iris dataset from Kaggle and saves it to the src/data folder.
    """
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    dataset_name = "uciml/iris"
    dataset_path = os.path.join(DATA_DIR, "iris")

    try:
        # Initialize and  authenticate Kaggle API
        api = KaggleApi()
        api.authenticate()

        # Download dataset
        api.dataset_download_files(dataset_name, path=dataset_path, unzip=True)
        return JSONResponse(content={"message": f"Dataset downloaded successfully to {dataset_path}"})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)