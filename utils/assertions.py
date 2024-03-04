class Assertions:

    @staticmethod
    def check_success_status(response):
        assert response.status_code == 200


