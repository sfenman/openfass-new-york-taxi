from marshmallow import Schema, fields, post_load
from Route import *


class RouteSchema(Schema):
    id = fields.Str()
    vendor_id = fields.Str()
    pickup_datetime = fields.Str()
    passenger_count = fields.Str()
    pickup_longitude = fields.Str()
    pickup_latitude = fields.Str()
    drop_off_longitude = fields.Str()
    drop_off_latitude = fields.Str()
    store_and_fwd_flag = fields.Str()

    @post_load
    def create_route(self, data, **kwargs):
        return Route(**data)

