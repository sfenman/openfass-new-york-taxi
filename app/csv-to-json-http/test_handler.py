import unittest
from handler import convert_datatipes
from datetime import datetime
class HandlerTest(unittest.TestCase):

    ROUTE = {
        "id": "id3004672",
        "vendor_id": "1",
        "pickup_datetime": "2016-06-30 23:59:58",
        "passenger_count": "1",
        "pickup_longitude": "-73.9881286621094",
        "pickup_latitude": "40.7320289611816",
        "drop_off_longitude": "-73.9901733398438",
        "drop_off_latitude": "40.7566795349121",
        "store_and_fwd_flag": "N"
    }
    
    def test_given_valid_route_IT_should_succeed(self):
        result = convert_datatipes([self.ROUTE])
        self.assertEqual(1, result[0]['vendor_id'])
        self.assertEqual(datetime(2016, 6, 30, 23, 59, 58), result[0]['pickup_datetime'])
        self.assertEqual(-73.9881286621094, result[0]['pickup_longitude'])
        
if __name__ == '__main__':
    unittest.main()