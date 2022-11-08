import pytest

from caenhv import CaenHV


def test_caen_no_connection():
    with pytest.raises(Exception):
        # no ports available
        caen = CaenHV(port=None, connect=False)

    with pytest.raises(Exception):
        # no ports available or cannot connect
        caen = CaenHV(connect=True)
