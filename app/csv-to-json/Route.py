

class Route:
    def __init__(self, id: int, vendor_id: int, pickup_datetime, passenger_count,
                 pickup_longitude, pickup_latitude, drop_off_longitude,
                 drop_off_latitude, store_and_fwd_flag
                 ):
        self.id = id
        self.vendor_id = vendor_id
        self.pickup_datetime = pickup_datetime
        self.passenger_count = passenger_count
        self.pickup_longitude = pickup_longitude
        self.pickup_latitude = pickup_latitude
        self.drop_off_longitude = drop_off_longitude
        self.drop_off_latitude = drop_off_latitude
        self.store_and_fwd_flag = store_and_fwd_flag

    # def get_id(self):
    #     return self.__id
    #
    # def get_vendor_id(self):
    #     return self.__vendor_id

    # def get_pickup_datetime(self):
    #     return self.__pickup_datetime
    #
    # def get_passenger_count(self):
    #     return self.__passenger_count
    #
    # def get_pickup_longitude(self):
    #     return self.__pickup_longitude
    #
    # def get_pickup_latitude(self):
    #     return self.__pickup_latitude
    #
    # def get_drop_off_longitude(self):
    #     return self.__drop_off_longitude
    #
    # def get_drop_off_latitude(self):
    #     return self.__drop_off_latitude
    #
    # def get_store_and_fwd_flag(self):
    #     return self.__store_and_fwd_flag


