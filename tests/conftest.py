import pytest


@pytest.fixture(params=[1, 2, 3, 4, 5])
def station_id(request):
    return request.param
