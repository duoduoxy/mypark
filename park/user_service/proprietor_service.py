from .common_service import CommonService
from park.models import User

class PropritorService(CommonService):

    propritor = None

    def __init__(self, properitor):
        self.propritor = properitor

    def bind_park_position(self):
        pass

    def charge(self):
        pass

    def publish_comment(self):
        pass