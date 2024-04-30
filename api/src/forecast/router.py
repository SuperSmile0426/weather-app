import src.models as models
import requests
from src.database import SessionLocal
from fastapi import APIRouter, HTTPException, status

router = APIRouter()

db = SessionLocal()

def fetch_forecast(latitude, longitude):
    api_url = (
        "https://api.open-meteo.com/v1/forecast?latitude="
        + str(latitude)
        + "&longitude="
        + str(longitude)
        + "&forecast_days="
        + str(7)
        + "&daily=temperature_2m_max,temperature_2m_min,weather_code"
    )
    weather_data = requests.get(api_url).json()

    return weather_data

@router.get("/{location_name}", response_model=object, status_code=200)
def get_forecast(location_name: str):
    location = db.query(models.Location).filter(models.Location.name == location_name).first()
    if location is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Location Not Found")

    response = fetch_forecast(location.latitude, location.longitude)

    return response