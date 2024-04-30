import requests
from src.database import SessionLocal
import src.models as models
from fastapi import APIRouter, HTTPException, status

from src.locations.schemas import Location, LocationsWithWeatherCondition, City
from src.doc import hard_data, fields_to_select

router = APIRouter()


db = SessionLocal()


def fetch_current(latitude, longitude):
    api_url = (
        "https://api.open-meteo.com/v1/forecast?latitude="
        + str(latitude)
        + "&longitude="
        + str(longitude)
        + "&current=temperature_2m,rain,weather_code"
    )
    weather_data = requests.get(api_url).json()

    return weather_data


@router.get("/", response_model=list[LocationsWithWeatherCondition], status_code=200)
def get_all_locations():
    locations = db.query(models.Location).all()
    locationsWithWeatherCondition = []
    for location in locations:
        current_weather_condition = fetch_current(location.latitude, location.longitude)
        locationsWithWeatherCondition.append(LocationsWithWeatherCondition(
            name=location.name,
            latitude=location.latitude,
            longitude=location.longitude,
            current_weather_condition=current_weather_condition,
        ))

    return locationsWithWeatherCondition


@router.post("/", response_model=Location, status_code=status.HTTP_201_CREATED)
def create_location(location: City):
    found_location = None
    for hard_location in hard_data:
        print(hard_location[fields_to_select[0]])
        if hard_location[fields_to_select[0]] == location.name:
            found_location = hard_location
            break

    if found_location is None:
        raise HTTPException(status_code=400, detail="Provide detail with longitude and latitude")
    
    db_location = db.query(models.Location).filter(models.Location.name == found_location[fields_to_select[0]]).first()

    if db_location is not None:
        raise HTTPException(status_code=400, detail="Location already exists")

    new_location = models.Location(
        name=found_location[fields_to_select[0]],
        latitude=found_location[fields_to_select[1]],
        longitude=found_location[fields_to_select[2]],
    )

    db.add(new_location)
    db.commit()

    return new_location


@router.delete("/{city}")
def delete_item(city: str):
    location_to_delete = db.query(models.Location).filter(models.Location.name == city).first()

    if location_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Location Not Found")

    db.delete(location_to_delete)
    db.commit()

    return location_to_delete