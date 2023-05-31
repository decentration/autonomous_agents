import requests

class APICommunication:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_instance_data(self, instance_id):
        response = requests.get(f"{self.base_url}/api/instances/{instance_id}")
        return response.json()

    def get_conversation_history(self, instance_id):
        response = requests.get(f"{self.base_url}/api/conversations/{instance_id}")
        return response.json()
