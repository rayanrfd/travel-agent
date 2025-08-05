from pydantic import BaseModel

class TravelPlan(BaseModel):
    origin: str
    destination: str
    start_date: str
    end_date: str
