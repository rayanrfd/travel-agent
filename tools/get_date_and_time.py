from datetime import datetime
import pytz

def get_date_and_time(departure_tz: str, destination_tz: str) -> dict:
    """Get current date and time for a given departure and destination time zone."""
    # User time zone
    user_tz = pytz.timezone(departure_tz)
    user_time = datetime.now(user_tz)

    # Destination time zone
    destination_tz = pytz.timezone(destination_tz)
    destination_time = datetime.now(destination_tz)

    return {
        "user_time": user_time.isoformat(),
        "destination_time": destination_time.isoformat()
    }



get_date_and_time_tool = [{
    "type": "function",
    "function": {
        "name": "get_date_and_time",
        "description": "Get current date and time for a given departure and destination time zone.",
        "parameters": {
            "type": "object",
            "properties": {
                "departure_tz": {
                    "type": "string",
                    "description": "Departure time zone e.g. Europe/Paris"
                },
                "destination_tz": {
                    "type": "string",
                    "description": "Destination time zone e.g. America/New_York"
                }
            },
            "required": [
                "departure_tz",
                "destination_tz"
            ],
            "additionalProperties": False
        },
        "strict": True
    }
}]


