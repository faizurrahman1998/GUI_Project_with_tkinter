from cryptography.fernet import Fernet 
import os 
import json

class Encryption(Fernet): 

    def __init__(self): 

        self.magic = open("magic.key", "rb").read()
        super().__init__(self.magic)

    def update_user(self):
        pass

    def mod_decrypt(self, file_name): 

        with open(file_name, "rb") as file1:

            return json.loads(self.decrypt(file1.read()).decode())


    def mod_encrypt(self, file_name): 

        with open(file_name, "rb") as file1: 

            return self.encrypt(file1.read())


obj = Encryption()

# with open("database.encrypted", "wb") as file1: 

#     file1.write(obj.mod_encrypt("database.json"))