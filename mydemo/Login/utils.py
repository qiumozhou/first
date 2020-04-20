#-*-coding:utf-8-*-
import uuid
def generate_token():
    random_uuid=str(uuid.uuid4()).replace('-','')
    return random_uuid
