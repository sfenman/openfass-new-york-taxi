import unittest
from handler import is_more_than_one_km

class HandlerTest(unittest.TestCase):

    QUARTER_ONE = {
        "pickup_longitude": 00.0000000000000,
        "pickup_latitude": 00.000000000000,
        "drop_off_longitude": 00.0100000000000,
        "drop_off_latitude": 00.0000000000000,
    }
    
    def test_given_smaller_lon_than_minimun_should_return_false(self):
        self.assertTrue(is_more_than_one_km(self.QUARTER_ONE))

        
if __name__ == '__main__':
    unittest.main()