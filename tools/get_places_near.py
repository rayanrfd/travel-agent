import overpy
from typing import List

def get_places_near(place_types: List[str], lat: float, lon: float, radius: int = 1000):
    """
    Get places near a given latitude and longitude with specified place types.

    Args:
        place_types (List[str]): A list of place types to search for (e.g., ["restaurant", "cafe"]).
        lat (float): The latitude of the location to search around.
        lon (float): The longitude of the location to search around.
        radius (int, optional): The radius (in meters) to search within. Defaults to 1000.

    Returns:
        None: Prints the names and coordinates of the places found.
    """
    api = overpy.Overpass()

    query = f"""
    node
    [amenity{'~' + '"' + '|'.join(place_types) + '"' if len(place_types) > 1 else '=' + place_types[0]}]
    (around:{radius},{lat},{lon});
    out;
    """
    print(f"Query: {query}")  # Debugging line to see the query being sent

    result = api.query(query)

    for node in result.nodes:
        name = node.tags.get("name", "Unnamed")
     
    return {{
        "name": name,
        "latitude": node.lat,
        "longitude": node.lon
        } for node in result.nodes if node.tags.get("name")
}


if __name__ == "__main__":
    # Example usage
    places = get_places_near(["restaurant", "cafe"], 48.8566, 2.3522, 1000)
    for place in places:
        print(f"Place: {place['name']}, Latitude: {place['latitude']}, Longitude: {place['longitude']}")
