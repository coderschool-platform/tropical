from dotenv import load_dotenv
import os
import requests

load_dotenv()

from constants.api_paths import GET_ALL_COURSES


class LWClient:
    """
    Class for getting data from LearnWorlds API.

    Connection to LW API is established using a proxy through CS Platform.
    """

    def __init__(self) -> None:
        self.base_url = os.getenv("BASE_URL")
        PLATFORM_APP_TOKEN = os.getenv("PLATFORM_APP_TOKEN")

        self.headers = {
            "app-token": PLATFORM_APP_TOKEN,
        }

    def build_api_path(self, path: str) -> str:
        """
        Build API path from base_url and path.
        """
        return f"{self.base_url}{path}"

    def get(self, path, params) -> any:
        """
        GET request to LW API through CS Platform proxy.
        """
        response = requests.get(
            self.base_url, params={"path": path, **params}, headers=self.headers
        )
        return response.json()

    def get_all_courses(self) -> list:
        """
        Get all courses from LW API.
        """
        return self.get(GET_ALL_COURSES, {})


if __name__ == "__main__":
    # Test API connection
    client = LWClient()
    print(client.get_all_courses())
