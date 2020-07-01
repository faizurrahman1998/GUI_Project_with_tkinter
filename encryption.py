from cryptography.fernet import Fernet 
import os 
import json

class Encryption(Fernet): 

    def __init__(self): 

        self.magic = open("magic.key", "rb").read()
        super().__init__(self.magic)

    def update_user(self):

        pass 

    def mod_decrypt(self): 

        with open("credentials.encrypted", "rb"):
            pass