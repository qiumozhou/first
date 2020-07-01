#-*-coding:utf-8-*-
import uuid


def gen_token():
    random_uuid = str(uuid.uuid4()).replace('-', '')
    return random_uuid


class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__

def dict_to_object(dictObj):
    if not isinstance(dictObj, dict):
        return dictObj
    inst = Dict()
    for k, v in dictObj.items():
        inst[k] = dict_to_object(v)

