from src.database import Base
from sqlalchemy import Column, Float, Integer, String


class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    latitude = Column(Float)
    longitude = Column(Float)

    def __repr__(self):
        return f"<Item name={self.name} latitude={self.latitude} longitude={self.longitude}>"
