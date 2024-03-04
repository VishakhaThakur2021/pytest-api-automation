import requests
from config.config import AppConfig


class APIRequests:
    @staticmethod
    def send_compliance_request(station_id ,command , payload=None):
        url = f"{AppConfig.BASE_URL}/v1/tests/{station_id}"
        test_request = {"command": command, "payload": payload}

        try:
            response = requests.post(url, json=test_request)
            return response
        except Exception as e:
            print(f"Error communicating with station {station_id}: {str(e)}")
            return None

    @staticmethod
    def get_version(station_id):
        return APIRequests.send_compliance_request(station_id, 'getVersion')

    @staticmethod
    def get_interval(station_id):
        return APIRequests.send_compliance_request(station_id, 'getInterval')

    @staticmethod
    def set_values(station_id, n):
        return APIRequests.send_compliance_request(station_id, 'setValues', payload=n)