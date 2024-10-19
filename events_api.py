
import requests

from models import ApiResponse

BASE_URL = "https://images.parkrun.com/events.json"

def get_endpoint() -> ApiResponse:
    response = requests.get(BASE_URL)
    response.raise_for_status()
    response = response.json()
    return response

if __name__ == "__main__":
    get_endpoint()



