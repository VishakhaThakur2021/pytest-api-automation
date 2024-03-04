import allure
import pytest
from api.compliance_station_api_requests import APIRequests
from utils.assertions import Assertions
from utils.responsebody import ExampleResponseBody

@allure.feature("get version for compliance station ")
@pytest.mark.regression
def test_get_version_compliance(station_id):
    response = APIRequests.get_version(station_id)
    Assertions.check_success_status(response)
    assert float(response.json()["result"]) > 1.6


@allure.feature("get interval for compliance station ")
@pytest.mark.regression
def test_get_interval_compliance(station_id):
    response = APIRequests.get_interval(station_id)
    Assertions.check_success_status(response)
    assert 1 <= int(response.json()["result"]) <= 60


@allure.feature("set values for compliance station ")
@pytest.mark.regression
@pytest.mark.parametrize("command, payload, expected_response", [
    ('setValues', 5, ExampleResponseBody.SET_VALUES_OK_RESPONSE),
    ('setValues', 15, ExampleResponseBody.SET_VALUES_FAILED_RESPONSE)
])
def test_set_values_compliance(station_id, command,payload, expected_response):
    response = APIRequests.set_values(station_id, payload)
    Assertions.check_success_status(response)
    assert response.json()["result"] == expected_response
