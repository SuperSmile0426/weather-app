from pydantic import BaseModel

class Location(BaseModel):  # serializer
    name: str
    latitude: float
    longitude: float

    class Config:
        orm_mode = True


class LocationsWithWeatherCondition(Location):
    current_weather_condition: object

class City(BaseModel):
    name: str
