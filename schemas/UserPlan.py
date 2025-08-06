from pydantic import BaseModel

class TravelPlan(BaseModel):
    origin_place: str
    origin_country: str
    destination_place: str
    destination_country: str
    start_date: str
    end_date: str
