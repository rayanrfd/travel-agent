from geopy.geocoders import Nominatim

def get_lat_long(search_query: str) -> tuple:
    geolocator = Nominatim(user_agent="my-geolocator-app")
    location = geolocator.geocode(search_query)
    if location:
        return (location.latitude, location.longitude)
    return (None, None)

get_lat_long_tool = [{
    "type": "function",
    "function": {
        "name": "get_lat_long",
        "description": "Get latitude and longitude for a given location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "Name of the location to get latitude and longitude for."
                }
            },
            "required": [
                "location"
            ],
            "additionalProperties": False
        },
        "strict": True
    }
}]

if __name__ == "__main__":
    # Example usage
    lat, lon = get_lat_long("Eiffel Tower, Paris")
    print(f"Latitude: {lat}, Longitude: {lon}")
