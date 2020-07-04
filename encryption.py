from cryptography.fernet import Fernet 
import os 
import json

class Encryption(Fernet): 

    def __init__(self): 

        self.magic = open("magic.key", "rb").read()
        super().__init__(self.magic)


    def update_file(self, file_name): 

        if file_name.split(".", )[1] == "json": 

            with open(file_name) as file1: 

                with open(f"{file_name.split('.')[0]}.encrypted", "wb") as file2: 

                    file2.write(self.encrypt(file1.read().encode()))

                
    def mod_decrypt(self, file_name): 

        with open(file_name, "rb") as file1:

            return json.loads(self.decrypt(file1.read()).decode())


    def mod_encrypt(self, file_name): 

        with open(file_name, "rb") as file1: 

            return self.encrypt(file1.read())
    


obj = Encryption()
