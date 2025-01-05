import requests

class Oracle:
    def __init__(self, service_url):
        self.service_url = service_url

    def get_data(self, query):
        response = requests.get(f"{self.service_url}/{query}")
        if response.status_code == 200:
            return response.json()
        else:
           raise Exception("Failed to fetch data from oracle service")

    def __repr__(self):
        return f"Oracle(service_url='{self.service_url}')"
