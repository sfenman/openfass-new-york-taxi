import unittest
from handler import is_in_quarter

class HandlerTest(unittest.TestCase):

    QUARTER_ONE = {
        "minLon": 40.0000000000000,
        "maxLon": 42.0000000000000,
        "minLat": -72.0000000000000,
        "maxLat": -70.0000000000000,
    }
    
    def test_given_smaller_lon_than_minimun_should_return_false(self):
        route = {'pickup_longitude': 39.0000000000000, 'pickup_latitude': -71.0000000000000}
        self.assertFalse(is_in_quarter(self.QUARTER_ONE, route))
        

        
if __name__ == '__main__':
    unittest.main()