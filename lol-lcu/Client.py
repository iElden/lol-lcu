from .Connector import Connector
from .RawRequester import RawRequester

class Client:
    def __init__(self):
        self.connector = Connector()
        self.raw_requester = RawRequester(self.connector.url, self.connector.username, self.connector.password, {"Accept": "application/json"})

    @property
    def is_connected(self):
        return self.connector.connected

