class Route:
    def __init__(self, route_id, vendor_id, pickup_datetime, drop_off_datetime,
                 passenger_count, pickup_longitude, pickup_latitude,
                 drop_off_longitude, drop_off_latitude, store_and_fwd_flag):
        self.route_id = route_id
        self.vendor_id = vendor_id
        self.pickup_datetime = pickup_datetime
        self.drop_off_datetime = drop_off_datetime
        self.passenger_count = passenger_count
        self.pickup_longitude = pickup_longitude
        self.pickup_latitude = pickup_latitude
        self.drop_off_longitude = drop_off_longitude
        self.drop_off_latitude = drop_off_latitude
        self.store_and_fwd_flag = store_and_fwd_flag

    def __eq__(self, o: object) -> bool:
        return self.__class__ == o.__class__ and self.route_id == o.route_id

    def __ne__(self, o: object) -> bool:
        return self.__class__ != o.__class__ or self.route_id != o.route_id

    def __hash__(self) -> int:
        return hash(self.route_id)

    def __str__(self) -> str:
        return 'route id: ' + str(self.route_id)

