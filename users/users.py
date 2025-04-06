import json
import os

class User:
    def __init__(self, first_name: str, last_name: str, 
                 username: str, user_id: int, lang_code: str, ip: str):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.username: str = username
        self.user_id: int = user_id
        self.lang_code: str = lang_code
        self.ip: str = ip
        self.write_to_file()


    def write_to_file(self):
        with open(f'users/configs/{self.user_id}.json', 'w+') as f:
            f.write(json.dumps(self.__dict__))


    @classmethod
    def create_from_file(cls, user_id: int):
        with open(f'users/configs/{user_id}.json', 'r') as f:
            data = json.load(f)
            first_name = data['first_name']
            last_name = data['last_name']
            username = data['username']
            user_id = data['user_id']
            lang_code = data['lang_code']
            ip = data['ip']
            return User(first_name, last_name, username, user_id, lang_code, ip)
        
    @classmethod 
    def check_if_user_existss(cls, user_id: int) -> bool:
        file_name = f'{user_id}.json'
        folder = 'users/configs'
        return file_name in os.listdir(folder)