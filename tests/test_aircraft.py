
from src.aircraft import Aircraft, aircraft_list_from_opensky


def test_aircraft_compare_by_altitude():
    low = Aircraft("x", "c", 100.0, 1000.0)
    high = Aircraft("y", "c", 200.0, 9000.0)
    assert low < high
    assert high > low


def test_from_opensky_state() -> None:
    row = ["abc123", "UAL123 ", "United States", None, None, None, None, 10500.0, False, 250.0]
    plane = Aircraft.from_opensky_state(row)
    assert plane is not None
    assert plane.callsign == "UAL123"
    assert plane.baro_altitude == 10500.0


def test_aircraft_list_from_opensky() -> None:
    payload = {"states": [None, ["abc123", "UAL123 ", "United States", None, None, None, None, 10500.0, False, 250.0]]}
    planes = aircraft_list_from_opensky(payload)
    assert len(planes) == 1
    assert planes[0].country == "United States"
