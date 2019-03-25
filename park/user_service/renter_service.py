from .common_service import CommonService
from park.models import User

class RenterService(CommonService):

    renter = None

    def __init__(self, renter):
        self.renter = renter

    def mark_park_position(self):
        pass

    def charge(self):
        pass