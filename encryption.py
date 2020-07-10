from cryptography.fernet import Fernet 
import pymongo
import os 
import json

class Encryption(Fernet): 

    def __init__(self): 

        self.magic = open("magic.key", "rb").read()
        super().__init__(self.magic)


class Connection(pymongo.MongoClient):

    def __init__(self, connection_URI):
        super().__init__(connection_URI)


